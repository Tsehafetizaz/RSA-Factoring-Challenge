#!/usr/bin/python3
import sys


def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
        return 1, n


def main(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = file.readlines()
            for number in numbers:
                num = int(number.strip())
                p, q = factorize(num)
                print(f"{num}={p}*{q}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        main(sys.argv[1])
