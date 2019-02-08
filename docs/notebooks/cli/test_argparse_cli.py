
import argparse,sys

def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description = "command line test")
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args(argv)
    print(args.accumulate(args.integers))
    

if __name__ == '__main__':
    main(sys.argv[1:])
