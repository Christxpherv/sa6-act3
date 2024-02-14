from functools import reduce

x = 124
numbers = []
for i in str(x):
    numbers.append(int(i))

numberSum = reduce(lambda x, y: x + y, numbers)
print(numberSum)