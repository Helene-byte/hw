import argparse
def calculate(n):
    if n>=0:
        return n*n
    elif n<0:
        return abs(n)
    elif n==0:
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    print(calculate(args.n))


if __name__ == '__main__':
    main()
