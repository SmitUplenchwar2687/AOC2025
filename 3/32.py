file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    temp = []
    for num in arr[i]:
        temp.append(int(num))
    arr[i] = temp


def calculate(bank, index,  k, nums = 0):
    if k == 0 or index >= len(bank):
        return nums
    
    curr = 0
    ind = index
    for i in range(index, len(bank)-(k-1)):
        if bank[i] > curr:
            curr = bank[i]
            ind = i
    
    nums = nums*10 + curr
    return calculate(bank, ind+1, k-1, nums)


def joltage(banks):
    res = 0
    for bank in banks:
        res += calculate(bank, 0, 12, 0)
    
    return res


print(joltage(arr))