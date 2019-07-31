
# Square root of an integer
# Given an integer x, find square root of it. If x is not
# a perfect square, then return floor of sqrroot of x)

# Examples :

# Input: x = 4
# Output: 2

# Input: x = 11
# Output: 3

# Solution

# A Simple Solution to find floor of square root is to try
# all numbers starting from 1. For every tried number i,
# if i*i is smaller than x, then increment i. We stop when i*i
# becomes more than or equal to x. Below is the implementation of above idea.


def floorSqrt(num):
    # Base Condition
    if num == 0 or num == 1:
        return num
    # Starting from 1 try all numbers
    # till the sqrt is less than num
    i = 1
    result = 1
    while(result<=num):
        i = i+1
        result = i*i
    return i-1
num = 11
sol = floorSqrt(num)
print("Floor Sqrt of {} is {}".format(num,sol))