#Monotonic Queue

#https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solutions/204290/Monotonic-Queue-Summary/

LC 85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Idea: convert 2D matrix to 1D height array. The task becomes LC84. Largest Rectangle in Histogram which is essentially "finding the index of the nearest previous value smaller than itself".

        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        dp = [0] * (M + 1)
        area = 0
            
        for i in range(N):
            for j in range(M):
                # obtain the height based on each row
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            
            s = []
            for j in range(M + 1): # IMPORTANT: note that the last ZERO should pop out all remaining heights
                if not s: s.append(j)
                else:
                    while s and dp[s[-1]] >= dp[j]:
                        x = s.pop()
                        if s: area = max(area, dp[x]*(j - s[-1] - 1))
                        else: area = max(area, dp[x]*j)
                    s.append(j)
            
        return area
		
		
LC862. Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

Key observation: If we accumulate array A to obtain B, then B[l] <= B[r] - K indicates sum(A[l:r]) >= K. Given B[r], the problem is equivalent to finding the nearest previous element B[l] such that B[l] <= B[r] - K.

We maintain a increasing queue here because, given a new B[i], the larger element on the left are inferior than B[i] as a candidate to make some future element B[j] >= B[i] + K (j > i).

One extra optimization learnt from @lee215 is that we can also pop up the element on the left side <= B[i] - K of the increasing queue because, given current element B[i], if a future element B[j] > B[i], then B[j] - K would be within the queue after the removal of such elements <= B[i] - K; Otherwise, if a future element B[j] > B[i] then it never appears in the final results.

        Q = collections.deque([])
        
        B = [0]
        for a in A: B.append(B[-1] + a)
            
        res = float('inf')
        for i, b in enumerate(B):
            if not Q: Q.append(i)
            else:
                while Q and B[Q[-1]] > b: Q.pop()
                while Q and B[Q[0]] <= b - K:
                    res = min(res, i - Q[0])
                    Q.popleft()
                Q.append(i)
        return res if res < float('inf') else -1