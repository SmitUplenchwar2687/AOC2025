file = open("input.txt").read()

arr = file.split("\n")

cables = {}

for i in range(len(arr)):
    arr[i] = arr[i].split(":")
    arr[i][1] = arr[i][1].split(" ")[1:]
    cables[arr[i][0]] = arr[i][1]

def recurse(cables, vis, curr):
    if curr == "out":
        return 1
    
    if len(vis) == len(cables):
        return 0
    
    count = 0
    for cab in cables[curr]:
        if cab not in vis:
            vis.add(cab)
            count += recurse(cables, vis, cab)
            vis.remove(cab)
    
    return count


def server(cables):
    count = 0
    vis = set()
    vis.add("you")
    count = recurse(cables, vis, "you")
    return count

print(server(cables))
