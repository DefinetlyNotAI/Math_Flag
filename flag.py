import argparse
import json


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_composite(n):
    return n > 1 and not is_prime(n)


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_palindromic(n):
    return str(n) == str(n)[::-1]


def is_decimal(n):
    if int(n) != n:
        return True
    else:
        return False


def is_pair(n):
    return n == 2


def is_dozen(n):
    return n == 12


def is_stack(n):
    return n == 64


def is_sequential(n):
    str_n = str(n)
    diff = int(str_n[0])
    for i in range(1, len(str_n)):
        if int(str_n[i]) - diff != 1:
            return False
        diff = int(str_n[i])
    return True


def is_repetitive(n):
    str_n = str(n)
    for i in range(len(str_n) // 2):
        if str_n[i] != str_n[-i-1]:
            return False
    return True


def is_factorable(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False


def evaluate_flags(n):
    try:
        n = float(n)
        flags = {
            # Previous flags go here
            "Decimal": is_decimal(n),
            "Pair (2)": is_pair(n),
            "Dozen (12)": is_dozen(n),
            "Stack (64)": is_stack(n),
            "Sequential Numbers": is_sequential(n),
            "Repetitive Numbers": is_repetitive(n),
            "Factorable Numbers": is_factorable(n),
            "Composite Number": is_composite(n),
            "Prime Number": is_prime(n),
            "Even": is_even(n),
            "Odd": is_odd(n),
            "Palindromic Numbers": is_palindromic(n),
        }
        return flags
    except Exception as e:
        return f"Error: {e}"


def main():
    parser = argparse.ArgumentParser(description='Evaluate mathematical flags of a number.')
    parser.add_argument('number', type=str, help='Number to evaluate')
    parser.add_argument('--json', action='store_true', help='Output flags in JSON format')

    args = parser.parse_args()
    flags = evaluate_flags(args.number)

    if args.json:
        print(json.dumps(flags))
    else:
        try:
            for flag, value in flags.items():
                print(f"{flag}: {value}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
