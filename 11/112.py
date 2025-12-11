file = open("input.txt").read()

arr = file.split("\n")

cables = {}

for i in range(len(arr)):
    arr[i] = arr[i].split(":")
    arr[i][1] = arr[i][1].split(" ")[1:]
    cables[arr[i][0]] = arr[i][1]

memo = {}
def recurse(curr, dac, fft):
    key = (curr, dac, fft)
    if key in memo:
        return memo[key]
    
    if curr == "out" and dac and fft:
        memo[key] = 1
        return 1
    
    if curr == "out":
        memo[key] = 0
        return 0
    
    count = 0
    for cab in cables[curr]:
        if cab == "dac":
            count += recurse(cab, True, fft)
        elif cab == "fft":
            count += recurse(cab, dac, True)
        else:
            count += recurse(cab, dac, fft)
        
    memo[key] = count
    return count


print(recurse("svr", False, False))