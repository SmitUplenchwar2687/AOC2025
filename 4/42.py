file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = list(arr[i])


def forklift(papers):
    count = 0
    dire = [[0,1],[1,0],[1,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1]]
    change = True
    while(change):
        change = False
        temp = []
        for i in range(len(papers)):
            for j in range(len(papers[i])):
                curr = 0
                if papers[i][j] == '@':
                    for d in dire:
                        r = i + d[0]
                        c = j + d[1]
                        if r >=0 and c >=0 and r<len(papers) and c<len(papers[i]) and papers[r][c] == "@":
                            curr += 1
                            if curr >= 4:
                                break
                    if curr < 4:
                        change = True
                        count += 1
                        temp.append([i,j])
        
        for i in range(len(temp)):
            papers[temp[i][0]][temp[i][1]] = "."

    
    return count


print(forklift(arr))