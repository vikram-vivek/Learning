# The following code is supposed to rotate the array A by B positions.


class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        for i in xrange(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret
