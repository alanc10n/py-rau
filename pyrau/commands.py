import humanfriendly
from redis import StrictRedis
from six.moves import range
from tabulate import tabulate

class Command:
    """ Commands to run against the specified redis instance """
    def __init__(self, redis_obj=None):
        if redis_obj is None:
            self.redis = StrictRedis()
        else:
            self.redis = redis_obj

    def _get_obj_details(self, obj):
        """ Given debug data, extract values of interest """
        return obj['serializedlength']

    def delete(self, key_pattern):
        """ Delete keys matching the specified pattern """
        for key in self.redis.scan_iter(key_pattern):
            print("Deleting key: %s" % key)
            self.redis.delete(key)

    def get_details(self, key_list):
        """ Get debug info for specified keys """
        pipe = self.redis.pipeline()
        details = []

        strides = range(0, len(key_list), self.batch_size)
        for i in strides:
            for j in key_list[i: i + self.batch_size]:
                pipe.debug_object(j)
            batch_dets = pipe.execute()
            details.extend(map(self._get_obj_details, batch_dets))

        return zip(key_list, details)

    def keys(self, key_pattern, details=False, sort_by_size=False):
        """ List keys matching pattern, optionally with details like size """
        key_list = list(self.redis.scan_iter(key_pattern))

        if details:
            detailed_result = self.get_details(key_list)
            if sort_by_size:
                detailed_result = sorted(detailed_result, key=lambda x: x[1], reverse=True)

            result = []
            for r in detailed_result:
                #result.append('%s : %s' % (r[0],
                #              humanfriendly.format_size(r[1])))
                result.append((r[0].decode(), humanfriendly.format_size(r[1])))
            headers = ['Name', 'Size']
        else:
            result = [(x.decode(),) for x in key_list]
            headers = ['Name',]

        print(tabulate(result, headers=headers))
        #for value in result:
        #   print(value)

