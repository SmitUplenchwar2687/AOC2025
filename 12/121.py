with open("input.txt", "r") as file:
    shapes = "".join(next(file) for i in range(30))
    regions = file.read()   


shapes = shapes.split("\n\n")


for i in range(len(shapes)):
    shapes[i] = shapes[i].split("\n")
    shapes[i] = shapes[i][1:]
shapes.pop()

print(shapes)
regions = regions.split("\n")
for i in range(len(regions)):
    regions[i] = regions[i].split(":")
    regions[i][0] = regions[i][0].split("x")
    regions[i][0][0], regions[i][0][1] = int(regions[i][0][0]), int(regions[i][0][1])

    regions[i][1] = regions[i][1][1:]
    regions[i][1] = regions[i][1].split(" ")
    for j in range(len(regions[i][1])):
        regions[i][1][j] = int(regions[i][1][j])
                   

def presents(shapes, regions):
    count = 0
    sumshapes = []
    for i in range(len(shapes)):
        curr = 0
        for l in range(3):
            for j in range(3):
                if shapes[i][l][j] == "#":
                    curr += 1
        sumshapes.append(curr)
                
    for i in range(len(regions)):
        currsum = 0
        for j in range(len(regions[i][1])):
            currsum += regions[i][1][j]*sumshapes[j]

        if regions[i][0][0]*regions[i][0][1] >= currsum:
            count += 1

    return count

print(presents(shapes, regions))

