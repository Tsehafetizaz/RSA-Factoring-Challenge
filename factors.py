import sys


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if len(sys.argv) != 2:
    print("Usage: python factors.py <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize(n)
            if len(factors) >= 2:
                p = factors[0]
                q = n // p
                print(f"{n}={p}*{q}")

except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    sys.exit(1)

except ValueError:
    print("Invalid input. All lines contain natural numbers greater than 1.")
    sys.exit(1)
