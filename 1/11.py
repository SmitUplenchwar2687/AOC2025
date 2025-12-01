file = open("input.txt").read()

arr = file.split("\n")

def password(nums):
    count = 0
    curr = 50
    for num in nums:
        if num[0] == "R":
            sign = 1
        else:
            sign = -1

        curr = (curr + (sign * int(num[1:]))) % 100
        if curr == 0:
            count += 1
        
    return count

print(password(arr))


