file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = arr[i].split(",")
    arr[i][0],arr[i][1]  = int(arr[i][1]), int(arr[i][0])

def largest_rect(mat):
    vis = set()
    res = 0
    mat.sort()
    indexrow = {}
    indexcol = {}
    for i in range(0, len(mat), 2):
        l = min(mat[i][1], mat[i+1][1])
        r = max(mat[i][1], mat[i+1][1])
        for j in range(l, r+1):
            if j in indexcol:
                if len(indexcol[j]) == 1:
                    indexcol[j].append(mat[i][0])
                indexcol[j][0], indexcol[j][1] = min(indexcol[j][0], indexcol[j][1], mat[i][0]), max(indexcol[j][0], indexcol[j][1], mat[i][0])
            else:
                indexcol[j] = [mat[i][0]]

    mat.sort(key = lambda x : [x[1],x[0]])
    for i in range(0, len(mat), 2):
        l = min(mat[i][0], mat[i+1][0])
        r = max(mat[i][0], mat[i+1][0])
        for j in range(l, r+1):
            if j in indexrow:
                if len(indexrow[j]) == 1:
                    indexrow[j].append(mat[i][1])
                indexrow[j][0], indexrow[j][1] = min(indexrow[j][0], indexrow[j][1], mat[i][1]), max(indexrow[j][0], indexrow[j][1], mat[i][1])
            else:
                indexrow[j] = [mat[i][1]]
            

    for i in range(len(mat)):
        for j in range(i):
            flag = True
            if indexrow[mat[i][0]][0] <= min(mat[i][1], mat[j][1]) and indexrow[mat[i][0]][1] >= max(mat[i][1], mat[j][1]):
                for k in range(min(mat[i][1], mat[j][1]), max(mat[i][1], mat[j][1])+1):
                    if indexcol[k][0] > mat[i][0] or indexcol[k][1] < mat[i][0]:
                        flag = False
                        break
            else:
                flag = False

            if flag and indexrow[mat[j][0]][0] <= min(mat[i][1], mat[j][1]) and indexrow[mat[j][0]][1] >= max(mat[i][1], mat[j][1]):
                for k in range(min(mat[i][1], mat[j][1]), max(mat[i][1], mat[j][1])+1):
                    if indexcol[k][0] > mat[j][0] or indexcol[k][1] < mat[j][0]:
                        flag = False
                        break
            else:
                flag = False

            if flag and indexcol[mat[i][1]][0] <= min(mat[i][0], mat[j][0]) and indexcol[mat[i][1]][1] >= max(mat[i][0], mat[j][0]):
                 for k in range(min(mat[i][0], mat[j][0]), max(mat[i][0], mat[j][0])+1):
                    if indexrow[k][0] > mat[i][1] or indexrow[k][1] < mat[i][1]:
                        flag = False
                        break
            else:
                flag = False

            if flag and indexcol[mat[j][1]][0] <= min(mat[i][0], mat[j][0]) and indexcol[mat[j][1]][1] >= max(mat[i][0], mat[j][0]):
                 for k in range(min(mat[i][0], mat[j][0]), max(mat[i][0], mat[j][0])+1):
                    if indexrow[k][0] > mat[j][1] or indexrow[k][1] < mat[j][1]:
                        flag = False
                        break
            else:
                flag = False

            if flag:
                res = max(res, (abs(mat[i][0]-mat[j][0])+1) * (abs(mat[i][1]-mat[j][1])+1))

    
    
    return res


print(largest_rect(arr))