file = open("input.txt").read()

ranges, ids = file.split("\n\n", 2)

ranges = ranges.split("\n")
for i in range(len(ranges)):
    ranges[i] = ranges[i].split("-")
    ranges[i][0] = int(ranges[i][0])
    ranges[i][1] = int(ranges[i][1])

ids = ids.split("\n")
for i in range(len(ids)):
    ids[i] = int(ids[i])

def fresh(ranges, ids):
    count = 0
    ranges.sort(key = lambda x : [x[0],x[1]])
    for id in ids:
        for i in range(len(ranges)):
            if id >= ranges[i][0] and id <= ranges[i][1]:
                count += 1
                break
    
    return count 

print(fresh(ranges,ids))
