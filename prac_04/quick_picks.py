"""
Quick Picks - CP1404 - Michael Richards
"""

import random

def main():
    done_input = False
    while not done_input:
        try:
            NUMBER_OF_ROWS = int(input("How many quick picks? "))
            done_input = True
        except ValueError:
            print("Please enter a valid integer.")
    for i in range(NUMBER_OF_ROWS):
        row = []
        while len(row) < 6:
            RAND_NUMBER = random.randint(1,45)
            if RAND_NUMBER not in row:
                row.append(RAND_NUMBER)
        for number in row:
            print("{:>2}".format(number),end=' ')
        print()

main()
