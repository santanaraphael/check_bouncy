# check_bouncy

This script checks for if a number is bouncy, that is neither increasing nor decreasing.  

The check_bouncy function does this job and returns whether the number is bouncy or not.  

The bouncy_number function checks for every integer until the desired number and returns the amount of bouncy numbers in that range.  
  
Finally, the challenge function will loop over the integer numbers until a given percentage is achieved, then it will return the final number as the answer to the challenge.

## What is a Bouncy Number?

If a number is neither an increasing number (each digit from the left to the right is greater than or equal to the previous one) or decreasing (the opposite), it is a bouncy number.
The first bouncing number is 101. 

## Getting Started

First off, this project uses Python 3.5.2, but using a newer version will probably be fine. 

### Prerequisites

There are no third-party packages needed for this project.

## Running the tests

The tests are designed under the unittest standard module. There will be a single TestCase for the whole script, with a test method testing each function.

### Using the command-line
Simply run:

```
python -m unittest test_check_bouncy.py
```

### Using an IDE

Some IDEs feature testing. In general, you just have to run the test_check_bouncy.py file in your IDE and it will print the test results on the screen. 

## Using the script

### Solving the Challenge

To solve the challenge, just run the check_bouncy.py file, either on an IDE or the command-line. The script will loop over the positive integers until the target ratio is achieved.  
The script will also print out each iteration on the screen to help the user visualize the convergence of the program.

Without any arguments, the script will look for a default ratio of 99% or 0.99 in decimal. 

### Use another target ratio

To use another target ratio, you just need to give the script the ratio as the second command-line argument, like in:

```
python check_bouncy.py 0.9
```

In the above example, the script will run the challenge algorithm with the target ratio of 90%. 

## Challenge results

The least number for which the proportion of bouncy numbers to the whole sample is 99% is **1587000**.