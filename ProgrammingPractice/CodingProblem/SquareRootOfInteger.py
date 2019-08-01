
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

# A faster solution is Binary Search         
def fastFloorSqrt(x): 
    # Base cases 
    if (x == 0 or x == 1): 
        return x 
    # Do Binary Search for floor(sqrt(x)) 
    start = 1
    end = x    
    while (start <= end): 
        mid = (start + end)//2
        # If x is a perfect square 
        if (mid*mid == x): 
            return mid  
        # Since we need floor, we update  
        # answer when mid*mid is smaller 
        # than x, and move closer to sqrt(x) 
        if (mid * mid < x): 
            start = mid + 1
            ans = mid
        else:  
            # If mid*mid is greater than x 
            end = mid-1 
    return ans

num = 11
sol = fastFloorSqrt(num)
print("Floor Sqrt of {} is {}".format(num,sol))
