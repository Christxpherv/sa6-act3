from functools import reduce

def find_max(arr, func):
    if not arr:
        return None
    else: 
        max = arr[0]
        for i in arr:
            max = func(max, i)
        return max




numbers = [1, 2, 5, 6]
maxFinder = lambda x, y: x if x > y else y
print(find_max(numbers, maxFinder))