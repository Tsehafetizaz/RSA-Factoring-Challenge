#!/usr/bin/env python3
import sys
import math
import time


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_prime_factors(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            q = number // i
            if is_prime(q):
                return i, q
    return number, 1


def factorize_file(filename):
    with open(filename, 'r') as file:
        number = int(file.readline().strip())
        start_time = time.time()
        p, q = find_prime_factors(number)
        if p and q:
            print(f"{number}={p}*{q}")
        else:
            print(f"No prime factors found for {number}")

        if time.time() - start_time > 5:
            print("Execution took longer than 5 seconds.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    factorize_file(sys.argv[1])
