#!/usr/bin/env python3 
import argparse
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

def fibonnaci_function(n): 
    # Do something
    fibonnaci_list = []
    if n >= 0: 
        fibonnaci_list.append(0)
        
    if n >= 1:
        fibonnaci_list.append(1)
    
    if n > 1:
        i = 2 
        while i < n: 
            fibonnaci_list.append(fibonnaci_list[i-2] + fibonnaci_list[i-1])
            i += 1

    return fibonnaci_list



parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("-c", "--count", type=int, default=1)
args = parser.parse_args()

##python fibonnaci.py fibonacci_100.txt -c 100 

if __name__ == "__main__":
    # Do stuff here
    fibonnaci_list = fibonnaci_function(args.count)
    with open(args.filename,'w') as file:
       for number in fibonnaci_list: 
       	file.write(str(number)+ "\n")