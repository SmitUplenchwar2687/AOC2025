file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    temp = []
    for num in arr[i]:
        temp.append(int(num))
    arr[i] = temp

def joltage(banks):
    res = 0
    for bank in banks:
        curr1 = bank[0]
        index = 0
        for i in range(len(bank)):
            if bank[i] > curr1:
                curr1 = bank[i]
                index = i
        curr2 = 0
        if index == len(bank) - 1:
            for i in range(len(bank)-1):
                if bank[i] > curr2:
                    curr2 = bank[i]
            res += curr2*10 + curr1
        else:
            for i in range(index+1, len(bank)):
                if bank[i] > curr2:
                    curr2 = bank[i]
            res += curr1*10 + curr2

    return res

print(joltage(arr))