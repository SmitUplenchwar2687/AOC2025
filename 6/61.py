file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = arr[i].split(" ")
    temp = []
    for j in range(len(arr[i])):
        if arr[i][j].isdigit(): 
            temp.append(int(arr[i][j]))
        if arr[i][j] == "+" or arr[i][j] == "*":
            temp.append(arr[i][j])
    arr[i] = temp

def worksheet(mat):
    m = len(mat)
    n = len(mat[0])
    res = 0
    for j in range(n):
        if mat[-1][j] == "+":
            curr = 0
            flag = True
        else:
            curr = 1
            flag = False
        for i in range(m-1):
            if flag:
                curr += mat[i][j]
            else:
                curr *= mat[i][j]
        res += curr
    
    return res


print(worksheet(arr))