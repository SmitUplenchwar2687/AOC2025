file = open("input.txt").read()

arr = file.split("\n")


operations = arr.pop()
temp = []
for i in range(len(operations)):
    if operations[i] == "+" or operations[i] == "*":
        temp.append(operations[i])
operations = temp.copy()



divisions = []

for j in range(len(arr[0])):
    flag = True
    for i in range(len(arr)):
        if arr[i][j] != " ":
            flag = False
            break
    if flag:
        divisions.append(j)

index = 0
prev = 0
matrix = []
for index in range(len(divisions) + 1):
    if index < len(divisions):
        maxlen = divisions[index]
    else:
        maxlen = len(arr[0])
    nums = []
    for j in range(maxlen-1, prev-1, -1):
        temp = ""
        for i in range(len(arr)):
            if arr[i][j].isdigit():
                temp += arr[i][j]
        if temp.isdigit():
            nums.append(int(temp))
    
    matrix.append(nums)
    if index < len(divisions):
        prev = divisions[index]

res = 0



for i in range(len(matrix)):
    if operations[i] == "+":
        flag = True
        curr = 0
    else:
        flag = False
        curr = 1
    for j in range(len(matrix[i])):
        if flag:
            curr += matrix[i][j]
        else:
            curr *= matrix[i][j]
    res += curr



print(res)

