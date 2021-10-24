import argparse
import sys
import math
import operator

parser = argparse.ArgumentParser()
parser.add_argument("z", help="math/operator method")
parser.add_argument("x", type=int, help="1st oprerand")
parser.add_argument("y", type=int, help="2nd operand")

# parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
try:
    print(getattr(operator,args.z)(args.x,args.y))
except:
    e = sys.exc_info()[0]
    print(NotImplementedError, e)

