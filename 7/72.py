file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = list(arr[i])


def quantom_tachyon(matrix):
    count = 0
    vis = set()
    arr = [[0,0] for i in range(len(matrix[0]))]
    for j in range(len(matrix[0])):
        if matrix[0][j] == "S":
            arr[j][0] = 1
            arr[j][1] = 1
    for i in range(0, len(matrix), 2):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^" and arr[j][0]==1:
                arr[j][0] = 0
                arr[j-1][0] = 1
                arr[j-1][1] += arr[j][1]
                arr[j+1][0] = 1
                arr[j+1][1] += arr[j][1]
                arr[j][1] = 0
    for i in range(len(arr)):
        count += arr[i][1]
    return count


print(quantom_tachyon(arr))