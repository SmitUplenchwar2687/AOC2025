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

        temp = curr + (sign * int(num[1:]))
        
        if curr!= 0 and temp <= 0:
            count += (abs(temp)//100) + 1

        elif curr == 0 and curr + (sign * int(num[1:])) < 0:
            count += abs(temp)//100

        elif curr + (sign * int(num[1:])) >= 100:
            count += abs(temp)//100

        curr = temp % 100

    return count

print(password(arr))


