#Convert Base
Typically two steps. A digit modulo step and a integer division step by the next base then reverse the result or use a deque()
Base 10 to 16, or any base by changing '16' and index

def toHex(self, num: int) -> str:
  rtn = []
  index = "0123456789abcdef"
  if num == 0: return '0'
  if num < 0: num += 2 ** 32
  while num > 0:
    digit = num % 16
    rtn.append(index[digit])
    num = num // 16
  return "".join(rtn[::-1])
  
 ##Fast Power

Fast Power, or Exponential by squaring allows calculating squares in logn time (x^n)2 = x^(2n)

def myPow(self, x: float, n: int) -> float:
    if n < 0:
        n *= -1
        x = 1/x
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x
        x *= x
        n = n // 2
    return ans