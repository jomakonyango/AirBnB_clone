#!/usr/bin/python3
"""
This module provides a simple example of a Python script that is compliant
with the PEP 8 style guide.
"""

import sys
import os


def calculate_sum(numbers):
    """Calculate and return the sum of a list of numbers."""
    return sum(numbers)


def main():
    """Main function that processes input and prints the sum of numbers."""
    if len(sys.argv) > 1:
        try:
            # Convert arguments to a list of numbers
            numbers = [float(arg) for arg in sys.argv[1:]]
            result = calculate_sum(numbers)
            print(f"The sum of the numbers is: {result}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please ensure all inputs are numbers.")
    else:
        print("Usage: python3 script.py num1 num2 ... numN")


if __name__ == '__main__':
    main()
