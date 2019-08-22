#A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.
#Assumptions in the Egg Dropping Puzzle:
#The two eggs are identical.
#If an egg does not break by dropping from a certain floor, it will not break dropping from any floor below that.
#If an egg breaks by dropping on a certain floor, it will break dropping from any floor above that.
#An egg may break by dropping on the 1st floor.
#An egg may not break by dropping even on the 100th floor.

#https://code.oursky.com/famous-egg-dropping-puzzle-in-combinatorics/

#https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
import sys 

# Function to get minimum number of trials 
# needed in worst case with n eggs and k floors 
def eggDrop(n, k): 

	# If there are no floors, then no trials 
	# needed. OR if there is one floor, one 
	# trial needed. 
	if (k == 1 or k == 0): 
		return k 

	# We need k trials for one egg 
	# and k floors 
	if (n == 1): 
		return k 

	min = sys.maxsize 

	# Consider all droppings from 1st 
	# floor to kth floor and return 
	# the minimum of these values plus 1. 
	for x in range(1, k + 1): 

		res = max(eggDrop(n - 1, x - 1), 
				eggDrop(n, k - x)) 
		if (res < min): 
			min = res 

	return min + 1

# Driver Code 
if __name__ == "__main__": 

	n = 2
	k = 10
	print("Minimum number of trials in worst case with", 
		n, "eggs and", k, "floors is", eggDrop(n, k)) 

# This code is contributed by ita_c 


#Dynamic Programming Solution

# A Dynamic Programming based Python Program for the Egg Dropping Puzzle 
INT_MAX = 32767

# Function to get minimum number of trials needed in worst 
# case with n eggs and k floors 
def eggDrop(n, k): 
	# A 2D table where entery eggFloor[i][j] will represent minimum 
	# number of trials needed for i eggs and j floors. 
	eggFloor = [[0 for x in range(k+1)] for x in range(n+1)] 

	# We need one trial for one floor and0 trials for 0 floors 
	for i in range(1, n+1): 
		eggFloor[i][1] = 1
		eggFloor[i][0] = 0

	# We always need j trials for one egg and j floors. 
	for j in range(1, k+1): 
		eggFloor[1][j] = j 

	# Fill rest of the entries in table using optimal substructure 
	# property 
	for i in range(2, n+1): 
		for j in range(2, k+1): 
			eggFloor[i][j] = INT_MAX 
			for x in range(1, j+1): 
				res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
				if res < eggFloor[i][j]: 
					eggFloor[i][j] = res 

	# eggFloor[n][k] holds the result 
	return eggFloor[n][k] 

# Driver program to test to pront printDups 
n = 2
k = 36
print("Minimum number of trials in worst case with" + str(n) + "eggs and "
	+ str(k) + " floors is " + str(eggDrop(n, k))) 

# This code is contributed by Bhavya Jain 
