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
    last_connection = None
    c = Counter(parent)
    i = -1
    while(len(c) > 1):
        i += 1
        u,v = dist[i][1], dist[i][2]
        if parent[u] == parent[v]:
            continue
        old = parent[v]
        new = parent[u]

        for j in range(len(parent)):
            if parent[j] == old:
                parent[j] = new
        last_connection = [u,v]
        c = Counter(parent)
        
    res = matrix[last_connection[0]][0] * matrix[last_connection[1]][0] 
    return res
    

print(circuit(arr))
