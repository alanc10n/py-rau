from redis import StrictRedis


class Command:
    """ Commands to run against the specified redis instance """
    def __init__(self, redis_obj=None):
        if redis_obj is None:
            self.redis = StrictRedis()
        else:
            self.redis = redis_obj

    def delete(self, key_pattern):
        """ Delete keys matching the specified pattern """
        print("Deleting %s" % key_pattern)
        for key in self.redis.scan_iter(key_pattern):
            print("Found key: %s" % key)
            self.redis.delete(key)
