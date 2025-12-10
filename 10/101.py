file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = arr[i].split(" ")
    arr[i][0] = arr[i][0][1:len(arr[i][0])-1]
    temp = []
    for j in range(len(arr[i][0])):
        if arr[i][0][j] == ".":
            temp.append(0)
        else:
            temp.append(1)
    arr[i][0] = temp

    for j in range(1, len(arr[i])-1):
        arr[i][j] = arr[i][j][1:len(arr[i][j])-1]
        arr[i][j] = arr[i][j].split(",")
        for k in range(len(arr[i][j])):
            arr[i][j][k] = int(arr[i][j][k])
    
    arr[i].pop()

def indicator_lights(arr):
    count = 0
    for i in range(len(arr)):
        target = arr[i][0]
        buttons = arr[i][1:]
        n = len(buttons)
        currmin = n
        sets = [i for i in range(n)]
        comb = []
        for mask in range(1 << n):
            subset = []
            for j in range(n):
                if mask & (1 << j):
                    subset.append(sets[j])
            comb.append(subset)
        
        for subs in comb:
            start = [0] * len(target)
            for j in subs:
                for k in buttons[j]:
                    if start[k] == 1:
                        start[k] = 0
                    else:
                        start[k] = 1
            if start == target:
                currmin = min(currmin, len(subs))

        count += currmin

    return count
    

print(indicator_lights(arr))

             