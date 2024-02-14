strList = ['chris', 'bob', 'ban', 'kim', 'taylor']

strList.sort(key=lambda x: (len(x), x))
print(strList)