Combination Sum
Sum with Duplicates allowed

CODE

 def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans
		
Combination Sum II
Sum with Duplicates not allowed


CODE

def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(i+1, end, tmp, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack(0, len(candidates), [], target)
        return ans
		
SUBSETS

Possible subsets of given array without duplicate

CODE

 def subsets(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans
		
Subsets II

Possible subsets of given array with duplicate

CODE

 def subsetsWithDup(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        nums.sort()
        backtrack(0, len(nums), [])
        return ans
		
Permutations

CODE

def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans

Permutations II

def permuteUnique(self, nums):
        def backtrack(tmp, size):
            if len(tmp) == size:
                ans.append(tmp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False
        ans = []
        visited = [False] * len(nums)
        nums.sort()
        backtrack([], len(nums))
        return ans
        
        
Palindrome Partitioning

CODE

def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans