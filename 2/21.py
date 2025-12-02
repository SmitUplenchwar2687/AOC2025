file = open("input.txt").read()

arr = file.split(",")

for i in range(len(arr)):
    arr[i] = arr[i].split("-")
    arr[i][0] = int(arr[i][0])
    arr[i][1] = int(arr[i][1])

def check(num):
    s = str(num)
    if len(s)%2 == 1:
        return False
    l, r = 0, len(s)//2
    while(r < len(s) and s[l] == s[r]):
        l += 1
        r += 1
    if r == len(s):
        return True
    return False

def invalidIDs(ranges):
    sum = 0
    for i in range(len(ranges)):
        for num in range(ranges[i][0], ranges[i][1]+1):
            if check(num):
                sum += num
    return sum

print(invalidIDs(arr))
            





        

    


    



