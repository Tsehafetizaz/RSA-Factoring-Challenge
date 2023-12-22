#!/usr/bin/env python3
import sys
import math
import time


def find_factors(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return i, number // i
    return number, 1


def factorize_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            start_time = time.time()
            p, q = find_factors(number)
            print(f"{number}={p}*{q}")
            if time.time() - start_time > 5:
                break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    factorize_file(sys.argv[1])
