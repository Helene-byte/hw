import argparse
import operator
import math
import operator


def calculate(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("operator", help="math/operator method")
    parser.add_argument("operands", type=float, nargs="+", help="oprerands")
    args = parser.parse_args()
    c = getattr(math, args.operator, None) or getattr(operator, args.operator, None)
    if c is None:
        raise NotImplementedError()
    print (c(args.operands[0]) if len(args.operands) == 1 else c(args.operands[0], args.operands[1]))


def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()
