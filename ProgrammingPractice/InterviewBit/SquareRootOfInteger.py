# Implement int sqrt(int x).
# Compute and return the square root of x.
# If x is not a perfect square, return floor(sqrt(x))

# Example
# Input : 11
# Output : 3

def sqrt(self, A):
        if A ==0:
            return 0
        start,end = 1,A
        #return (start,end)
        while (start <= end):
            mid = int((start + end)/2)
            if mid*mid == A:
                return mid
            elif mid*mid > A:
                end = mid-1
            else:
                start = mid+1
        if mid*mid < A:
            return mid
        else:
            return mid-1
