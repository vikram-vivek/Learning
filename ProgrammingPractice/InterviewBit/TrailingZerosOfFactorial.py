# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Logic - To count the nuumber of 5 contributed by each number

  def trailingZeroes(self, A):
        count=0
        n=5
        while(A/n>=1):
            count = count + int(A/n)
            n=5*n
        return count
