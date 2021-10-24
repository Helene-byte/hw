import argparse
import sys

def calculate(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="1st oprerand")
    parser.add_argument("z", help="sign")
    parser.add_argument("y", type=int, help="2nd operand")

# parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    try:
        if '+' in args.z:
            return int(args.x+args.y)
        elif '-' in args.z:
            return args.x-args.y
        elif '*' in args.z:
            return args.x*args.y

        elif '/' in args.z:
            try:
                return args.x/args.y
            except:
                e = sys.exc_info()[0]
                print(e)
    except:
        e = sys.exc_info()[0]
        print("2", NotImplementedError, e)
def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()

