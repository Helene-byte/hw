import argparse

def check_formula(user_input):
    if not user_input:
        return (False, None)
    accum = 0
    number = 0
    pending = '0'

    def process(accum, op, number):
        if op == '+':
            return accum + number
        elif op == '-':
            return accum - number
        elif op == '0':
            return number
    for c in user_input:
        if c.isdigit():
            if number is None:
                number = 0
            number = number * 10 + int(c)
        elif c in "+-":
            if number is None:
                return False, None
            accum = process(accum, pending, number)
            pending = c
            number = None
        else:
            return False, None
    return True, process(accum, pending, number)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user_input", type=str, help="expression")
    args = parser.parse_args() # Hint: use methods from argparse module
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
