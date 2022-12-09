#Parenthesis
Count can be used if simple case, otherwise stack. Basic Calculator is an extension of this algo

def isValid(self, s) -> bool:
  cnt = 0
  for c in s:
    if c == '(':
      cnt += 1
    elif c == ')':
      cnt -= 1
      if cnt < 0:
        return False
  return cnt == 0
  
Stack can be used if more complex

def isValid(self, s: str) -> bool:
  stk = []
  mp = {")":"(", "}":"{", "]":"["}
    for c in s:
      if c in mp.values():
        stk.append(c)
      elif c in mp.keys():
        test = stk.pop() if stk else '#'
        if mp[c] != test:
          return False
  return len(stk) == 0
  
Or must store parenthesis index for further modification

def minRemoveToMakeValid(self, s: str) -> str:
  rtn = list(s)
  stk = []
  for i, c in enumerate(s):
    if c == '(':
      stk.append(i)
    elif c == ')':
      if len(stk) > 0:
        stk.pop()
      else:
        rtn[i] = ''
  while stk:
    rtn[stk.pop()] = ''
  return "".join(rtn)
  
Basic Calculator
A calculator can be simulated with stack

class Solution:
    def calculate(self, s: str) -> int:
        s += '$'
        def helper(stk, i):
            sign = '+'
            num = 0
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                elif c.isdigit():
                    num = num * 10 + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stk.append(num)
                    if sign == '-':
                        stk.append(-num)
                    if sign == '*':
                        stk.append(stk.pop() * num)
                    if sign == '/':
                        stk.append(int(stk.pop() / num))
                    i += 1
                    num = 0
                    if c == ')':
                        return sum(stk), i
                    sign = c
            return sum(stk)
        return helper([],0)
		
Reverse Polish
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        while tokens:
            c = tokens.pop(0)
            if c not in '+-/*':
                stk.append(int(c))
            else:
                a = stk.pop()
                b = stk.pop()
                if c == '+':
                    stk.append(a + b)
                if c == '-':
                    stk.append(b-a)
                if c == '*':
                    stk.append(a * b)
                if c == '/':
                    stk.append(int(b / a))
        return stk[0]