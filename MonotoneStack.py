#Monotone Stack 
#https://leetcode.com/discuss/study-guide/2347639/a-comprehensive-guide-and-template-for-monotonic-stack-based-problems

#https://leetcode.com/problems/daily-temperatures/solutions/1364519/monotonic-stack-python-easiest-explanation-with-code/

Main idea is, we take a stack, and do a linear scan through the given array. As a matter of initialisation, (index of) first element gets added to the stack. Now, we compare the next element with top of the stack. "Is it any bigger?" if it is, the you pop the top, from stack (which was an index), and difference of current index of temperatures array and index obtained from popping the stack, gives you the "number of days". You add that to your result array, and repeat this same process for entire length in the array. Cool, Right?

    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0]*n
        stack = deque() #a double ended queue that we are going to use as a stack
        
        i = 0
        while i<n:
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i) 
                i+=1
                continue
            
            t = stack.pop()
            result[t] = i-t
        
        return result

