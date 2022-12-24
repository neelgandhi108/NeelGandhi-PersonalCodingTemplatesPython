#Greedy Algorithms

# Minimum Coin Change Problem

denominations = [1, 5, 10, 25, 50, 100]
# 100kr is ₺1


def return_change(change, denominations):
    to_give_back = [0] * len(denominations)

    # starting with the largest coin, goes through denominations list
    # and also keeps track of the counter, pos.
    for pos, coin in enumerate(reversed(denominations)):
        # while we can still use coin, use it until we can't
        while coin <= change:
            change = change - coin
            to_give_back[pos] += 1
    return to_give_back


print(return_change(267, denominations))
# returns [2, 1, 0, 1, 1, 2]


#Activity Selection Problem 

# You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. Example:

# Example 1 : Consider the following 3 activities sorted
# by finish time.
#      start[]  =  {10, 12, 20};
#      finish[] =  {20, 25, 30};
# A person can perform at most two activities. The 
# maximum set of activities that can be executed 
# is {0, 2} [ These are indexes in start[] and 
# finish[] ]

"""The following implementation assumes that the activities
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

def printMaxActivities(s, f ):
	n = len(f)
	print("The following activities are selected")

	# The first activity is always selected
	i = 0
	print(i)

	# Consider rest of the activities
	for j in range(n):

		# If this activity has start time greater than
		# or equal to the finish time of previously
		# selected activity, then select it
		if s[j] >= f[i]:
			print(j)
			i = j

# Driver program to test above function
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)


# Fractional Knapsack problem

# Given the weights and values of N items, in the form of {value, weight} put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In Fractional Knapsack, we can break items for maximizing the total value of the knapsack

# Note: In the 0-1 Knapsack problem, we are not allowed to break items. We either take the whole item or don’t take it. 

# Input: arr[] = {{60, 10}, {100, 20}, {120, 30}}, W = 50
# Output: 240 
# Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. 
# Hence total price will be 60+100+(2/3)(120) = 240

# Input:  arr[] = {{500, 30}}, W = 10
# Output: 166.667

# Structure for an item which stores weight and
# corresponding value of Item
class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):

	# Sorting Item on basis of ratio
	arr.sort(key=lambda x: (x.value/x.weight), reverse=True)

	# Result(value in Knapsack)
	finalvalue = 0.0

	# Looping through all Items
	for item in arr:

		# If adding Item won't overflow,
		# add it completely
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.value

		# If we can't add current Item,
		# add fractional part of it
		else:
			finalvalue += item.value * W / item.weight
			break
	
	# Returning final value
	return finalvalue


# Driver Code
if __name__ == "__main__":

	W = 50
	arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

	# Function call
	max_val = fractionalKnapsack(W, arr)
	print(max_val)
