"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 2 -  Write a program to print following pattern:
(Note :- No of rows of pattern to be accepted as input 
for e.g. given below is pattern for 4 rows):
31  29  27  25  23  21  19
    17  15  13  11   9
         7   5   3
             1
"""

import sys


def pattern(n: int) -> str:
    # Calculates the (n^2)th odd number as each line starts with it.
    val = n**2 * 2 - 1

    # Dynamic indentation based on the largest value in the pyramid.
    indent = len(str(val))

    for i in range(n, 0, -1):
        row = []  # To store the elements of each row.

        for j in range(i * 2 - 1):
            row.append(str(val).rjust(indent))
            val -= 2

        # First string gives proper indentation and the last prints numbers.
        print(
            "".join([" " * indent for i in range((n - i) * 2)])
            + ((" " * indent).join(row))
        )


if __name__ == "__main__":
    try:
        pattern(int(sys.argv[1]))
    except IndexError as e:
        print("Please enter an argument.")
