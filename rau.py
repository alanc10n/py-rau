import argparse
from redis import StrictRedis
from rau.commands import Command


def delete(args, command):
    """ Execute the delete command """
    command.delete(args.pattern)


def keys(args, command):
    """ Execute the keys command """
    command.keys(args.pattern, args.details)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', default='localhost', help='Host')
    parser.add_argument('-p', '--port', default=6379, type=int, help='Port')
    parser.add_argument('-b', '--batch_size', default=20,
                        type=int, help='Batch size for pipeline operations')

    subparsers = parser.add_subparsers(help='Commands')
    del_parser = subparsers.add_parser('delete', help='Delete key(s)')
    del_parser.add_argument('pattern', type=str, help='Key pattern')
    del_parser.set_defaults(func=delete)

    key_parser = subparsers.add_parser('keys', help="List keys")
    key_parser.add_argument('-p', '--pattern', help='Key pattern',
                            default=None)
    key_parser.add_argument('-d', '--details',
                            help='Include details for key(s)',
                            action='store_true')
    key_parser.set_defaults(func=keys)

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    redis = StrictRedis(host=args.host, port=args.port)
    command = Command(redis)
    command.batch_size = args.batch_size
    args.func(args, command)


if __name__ == '__main__':
    main()
