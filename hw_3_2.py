import argparse

def from_roman_numerals(args):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    try:
        for i, c in enumerate((args.n)):

            if (i + 1) == len(args.n) or roman_numerals[c] >= roman_numerals[args.n[i + 1]]:
                result += roman_numerals[c]

            else:
                result -= roman_numerals[c]

        return result
    except:
        raise ValueError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=str)
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
