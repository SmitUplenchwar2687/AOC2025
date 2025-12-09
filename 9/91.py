file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = arr[i].split(",")
    arr[i][0] = int(arr[i][0])
    arr[i][1] = int(arr[i][1])


def largest_rect(mat):
    res = 0
    for i in range(len(mat)):
        for j in range(i):
            res = max(res, (abs(mat[i][0]-mat[j][0])+1) * (abs(mat[i][1]-mat[j][1])+1))
    return res

print(largest_rect(arr))