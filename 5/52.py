file = open("input.txt").read()

ranges, ids = file.split("\n\n", 2)

ranges = ranges.split("\n")
for i in range(len(ranges)):
    ranges[i] = ranges[i].split("-")
    ranges[i][0] = int(ranges[i][0])
    ranges[i][1] = int(ranges[i][1])

def fresh(ranges):
    ranges.sort(key = lambda x : [x[0],x[1]])
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    count = 0
    for i in range(len(merged)):
        curr = merged[i][1] - merged[i][0] + 1
        count += curr
    return count

print(fresh(ranges))
