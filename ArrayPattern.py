#Array Pattern

Shift Array Right
Arrays can be shifted right by reversing the whole string, and then reversing 0,k-1 and k,len(str)
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(self, nums: List[int], k: int) -> None:
    def reverse(l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    if len(nums) <= 1: return
    k = k % len(nums)
    reverse(0, len(nums)-1, nums)
    reverse(0, k-1, nums)
    reverse(k, len(nums)-1, nums)
	
Continuous Subarrays with Sum k
The total number of continuous subarrays with sum k can be found by hashing the continuous sum per value and adding the count of continuous sum - k
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
	
def subarraySum(self, nums: List[int], k: int) -> int:
    mp = {0: 1}
    rtn, total = 0, 0
    for n in nums:
        total += n
        rtn += mp.get(total - k, 0)
        mp[total] = mp.get(total, 0) + 1
    return rtn
	
Events
Events pattern can be applied when to many interval problems such as 'Find employee free time between meetings' and 'find peak population' when individual start/ends are irrelavent and sum start/end times are more important

def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    events = []
    for e in schedule:
        for m in e:
            events.append((m.start, 1))
            events.append((m.end, -1))
    events.sort()
    itv = []
    prev = None
    bal = 0
    for t, c in events:
        if bal == 0 and prev is not None and t != prev:
            itv.append(Interval(prev, t))
        bal += c
        prev = t
    return itv
	
Merge Meetings
Merging a new meeting into a list
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
	
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    bisect.insort(intervals, newInterval)
    merged = [intervals[0]]
    for i in intervals:
        ms, me = merged[-1]
        s, e = i
        if me >= s:
            merged[-1] = (ms, max(me, e))
        else:
            merged.append(i)
    return merged
	
Kadane
local_maxiumum[i] = max(A[i], A[i] + local_maximum[i-1]) Explanation Determine max subarray sum
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
	
# input: [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums) # max([-2,1,-2,4,3,5,6,1,5]) = 6
	
Max Profit Stock
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Infinite Transactions, base formula

def maxProfit(self, prices: List[int]) -> int:
    t0, t1 = 0, float('-inf')
    for p in prices:
        t0old = t0
        t0 = max(t0, t1 + p)
        t1 = max(t1, t0old - p)
    return t0

Single Transaction, t0 (k-1) = 0

def maxProfit(self, prices: List[int]) -> int:
    t0, t1 = 0, float('-inf')
    for p in prices:
        t0 = max(t0, t1 + p)
        t1 = max(t1, - p)
    return t0

K Transactions

t0 = [0] * (k+1)
t1 = [float(-inf)] * (k+1)
for p in prices:
    for i in range(k, 0, -1):
        t0[i] = max(t0[i], t1[i] + p)
        t1[i] = max(t1[i], t0[i-1] - p)
return t0[k]
