#Python Extended

#Lambda
Can be used with (list).sort(), sorted(), min(), max(), (heapq).nlargest,nsmallest(), map()

# a=3,b=8,target=10
min((b,a), key=lambda x: abs(target - x)) # 8
>>> ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
>>> print(sorted(ids)) # Lexicographic sort
['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
>>> sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
>>> print(sorted_ids)
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']
trans = lambda x: list(al[i] for i in x) # apple, a->0..
print(trans(words[0])) # [0, 15, 15, 11, 4]
Lambda can sort by 1st, 2nd element in tuple

sorted([('abc', 121),('bbb',23),('abc', 148),('bbb', 24)], key=lambda x: (x[0],x[1]))
# [('abc', 121), ('abc', 148), ('bbb', 23), ('bbb', 24)]

##Zip
Combine two dicts or lists

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
list(zip(s1, s2)) # [(1, 'a'), (2, 'c'), (3, 'b')]
Traverse in Parallel

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
  print(f'Letter: {l}') # a,b,c
  print(f'Number: {n}') # 0,1,2
Empty in one list is ignored

letters = ['a', 'b', 'c']
numbers = []
for l, n in zip(letters, numbers):
  print(f'Letter: {l}') #
  print(f'Number: {n}') #
Compare characters of alternating words

for a, b in zip(words, words[1:]):
    for c1, c2 in zip(a,b):
        print("c1 ", c1, end=" ")
        print("c2 ", c2, end=" ")
Passing in * unpacks a list or other iterable, making each of its elements a separate argument.

a = [[1,2],[3,4]]
test = zip(*a)
print(test) # (1, 3) (2, 4)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
test = zip(*matrix)
print(*test) # (1, 4, 7) (2, 5, 8) (3, 6, 9)
Useful when rotating a matrix

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[:] = zip(*matrix[::-1]) # [[7,4,1],[8,5,2],[9,6,3]]
Iterate through chars in a list of strs

strs = ["cir","car","caa"]
for i, l in enumerate(zip(*strs)):
    print(l)
    # ('c', 'c', 'c')
    # ('i', 'a', 'a')
    # ('r', 'r', 'a')
	
Iter
Creates iterator from container object such as list, tuple, dictionary and set

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) # apple
print(next(myit)) # banana
Map
map(func, *iterables)

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets)) # ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers)) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
A1 = [1, 4, 9]
''.join(map(str, A1))
Filter
filter(func, iterable)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75 = list(filter(lambda x: x>75, scores)) # [90, 76, 88, 81]
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores)) # [90, 76, 88, 81]
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes)) # ['madam', 'anutforajaroftuna']
Get degrees == 0 from list

stk = list(filter(lambda x: degree[x]==0, degree.keys()))
Reduce
reduce(func, iterable[, initial]) where initial is optional

numbers = [3, 4, 6, 9, 34, 12]
result = reduce(lambda x, y: x+y, numbers) # 68
result = reduce(lambda x, y: x+y, numbers, 10) #78
itertools
itertools.accumulate(iterable[, func]) –> accumulate object

import itertools
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
list(itertools.accumulate(data)) # [3, 7, 13, 15, 16, 25, 25, 32, 37, 45]
list(accumulate(data, max))  # [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
cashflows = [1000, -90, -90, -90, -90]  # Amortize a 5% loan of 1000 with 4 annual payments of 90
list(itertools.accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)) [1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]
for k,v in groupby("aabbbc")    # group by common letter
    print(k)                    # a,b,c
    print(list(v))              # [a,a],[b,b,b],[c,c]