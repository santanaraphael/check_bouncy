# check_bouncy

This script checks for if a number is bouncy, that is neither increasing nor decreasing.  
The check_bouncy function does this job and returns wether the number is bouncy or not.  
The bouncy_number function checks for every integer until the desired number and returns the amount of bouncy numbers in that range.  
Finally, the challenge function will loop over the integer numbers until a given percentage is achieved, then it will return the final number as the answer to the challenge.

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
