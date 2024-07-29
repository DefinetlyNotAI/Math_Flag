def is_decimal(n):
    # A decimal has a non-integer part
    return isinstance(n, float)


def is_pair(n):
    # Check if n is divisible by 2
    return n % 2 == 0


def is_dozen(n):
    # Check if n is divisible by 12
    return n % 12 == 0


def is_stack(n):
    # Check if n is divisible by 64
    return n % 64 == 0


def is_sequential(n):
    # Check if the number is the first element of a sequence where the next element differs by 0, 1, 2, ..., 9
    for diff in range(10):  # Iterate through possible differences
        potential_next = n + diff
        if potential_next <= n:  # Ensure the potential next number is greater than the current number
            continue
        # Check if the potential next number is valid and fits the criteria
        if potential_next % 2 != 0 and potential_next % 3 != 0:
            return True
    return False


def is_repetitive(n):
    # Convert the number to string and check for repeated characters
    return len(set(str(n))) < len(str(n))


def is_factorable(n):
    # A number is factorable if it can be expressed as a product of two smaller integers
    return any(n % i == 0 for i in range(1, int(n ** 0.5) + 1)) and n > 1


def is_composite(n):
    # A composite number is a positive integer that has at least one divisor other than 1 and itself
    return n > 1 and any(n % i == 0 for i in range(2, n))


def is_prime(n):
    # A prime number is greater than 1 and has no divisors other than 1 and itself
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def is_even(n):
    # Check if n is divisible by 2
    return n % 2 == 0


def is_odd(n):
    # Check if n is not divisible by 2
    return n % 2 != 0


def is_palindromic(n):
    # A number is palindromic if it reads the same backward as forward
    return str(n) == str(n)[::-1]


def is_negative(n):
    # Check if n is less than 0
    return n < 0
