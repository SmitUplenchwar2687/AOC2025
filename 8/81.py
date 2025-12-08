import math
from collections import Counter

file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = arr[i].split(",")
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])

def circuit(matrix):
    m = len(matrix)
    dist = []
    for i in range(1, m):
        for j in range(i):
            temp = math.sqrt((matrix[i][0] - matrix[j][0])**2 + (matrix[i][1] - matrix[j][1])**2 + (matrix[i][2] - matrix[j][2])**2)
            dist.append([temp, j, i])
    dist.sort(key = lambda x: x[0])
    parent = [i for i in range(m)]
    for i in range(1000):
        u,v = dist[i][1], dist[i][2]
        if parent[u] == parent[v]:
            continue
        old = parent[v]
        new = parent[u]

        for j in range(len(parent)):
            if parent[j] == old:
                parent[j] = new


    c = Counter(parent)
    top3 = c.most_common(3)
    res = 1
    for i in range(len(top3)):
        res *= top3[i][1]
    return res
    

print(circuit(arr))
