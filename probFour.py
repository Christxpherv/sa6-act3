listOne = [1, 5, 6, 7]
listTwo = [1, 10, 6, 3]

intersection = list(filter(lambda x: x in listOne, listTwo))
print(intersection)