#Resevior Sampling
Used to sample large unknown populations. Each new item added has a 1/count chance of being selected

def __init__(self, nums):
    self.nums = nums
def pick(self, target):
    res = None
    count = 0
    for i, x in enumerate(self.nums):
        if x == target:
            count += 1
            chance = random.randint(1, count)
            if chance == 1:
                res = i
    return res