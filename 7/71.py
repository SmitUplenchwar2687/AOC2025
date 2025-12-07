file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = list(arr[i])


def tachyon(matrix):
    count = 0
    vis = set()
    for j in range(len(matrix[0])):
        if matrix[0][j] == "S":
            vis.add(j)
    for i in range(0, len(matrix), 2):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^" and j in vis:
                count += 1
                vis.remove(j)
                vis.add(j-1)
                vis.add(j+1)

    return count


print(tachyon(arr))