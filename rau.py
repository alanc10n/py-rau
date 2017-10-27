import argparse
from redis import StrictRedis
from rau.commands import Command

def delete(args, command):
    """ Execute the delete command """
    command.delete(args.pattern)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', default='localhost', help='Host')
    parser.add_argument('-p', '--port', default=6379, type=int, help='Port')
    subparsers = parser.add_subparsers(help='Commands')
    del_parser = subparsers.add_parser('delete',
                                        help='Delete key(s)')
    del_parser.add_argument('pattern', type=str, help='Key pattern')
    del_parser.set_defaults(func=delete)

    args = parser.parse_args()
    print args
    return args

def main():
    args = parse_args()
    redis = StrictRedis(host=args.host, port=args.port)
    command = Command(redis)
    args.func(args, command)

if __name__ == '__main__':
    main()
