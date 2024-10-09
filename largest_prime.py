#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

from fibonnaci import fibonnaci_function
import argparse
import sympy

def is_prime(num): 
    for i in range(2, int(round(num*0.5)) + 1): 
        if num % i == 0:
            return False
    return True

def find_largest_prime(fib_list): 
    fib_list = fib_list[::-1]
    for num in fib_list:
        ##a = is_prime(num)
        a = sympy.isprime(num)
        if a: 
            return num


parser_1 = argparse.ArgumentParser()
parser_1.add_argument("filename", type=str, help="The filename to process")  # Positional argument
parser_1.add_argument("-c", "--count", type=int, default=1)
args = parser_1.parse_args()


##python largest_prime.py myfile.txt -c 50000

if __name__ == "__main__":
    # Do stuff here
    fibonnaci_list = fibonnaci_function(args.count)
    largest_prime = find_largest_prime(fibonnaci_list)
    print(largest_prime) 