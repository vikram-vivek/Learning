"""
Given an array a[1..N]. For each element at position i (1 <= i <= N). Where

L(i) is defined as closest index j such that j < i and a[j] > a[i]. If no such j exists then L(i) = 0.
R(i) is defined as closest index k such that k > i and a[k] > a[i]. If no such k exists then R(i) = 0.
"""

# Below solution is not optimized
# This can be improved by using Stack and finding the Left and Right of each element in the beginning.

class Solution:
    # @param A : list of integers
    # @return an integer
    def rmax(self,el,X,idx):
        for i in xrange(len(X)):
            if X[i]>el:
                return i+idx+1
        return 0
    def lmax(self,el,X,idx):
        X.reverse()
        for i in xrange(len(X)):
            if X[i]>el:
                return idx-1-i
        return 0
    def maxSpecialProduct(self, A):
        l = len(A)
        maxprod = 0
        for i in xrange(1,l-1):
            right = self.rmax(A[i],A[i+1:],i)
            left = self.lmax(A[i],A[:i],i)
            product = left*right
            maxprod = max(maxprod,product)
        return (maxprod)%1000000007
