import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

file = open("input.txt").read()

arr = file.split("\n")

for i in range(len(arr)):
    arr[i] = arr[i].split(" ")
    arr[i][0] = arr[i][0][1:len(arr[i][0])-1]
    temp = []
    for j in range(len(arr[i][0])):
        if arr[i][0][j] == ".":
            temp.append(0)
        else:
            temp.append(1)
    arr[i][0] = temp

    for j in range(1, len(arr[i])-1):
        arr[i][j] = arr[i][j][1:len(arr[i][j])-1]
        arr[i][j] = arr[i][j].split(",")
        for k in range(len(arr[i][j])):
            arr[i][j][k] = int(arr[i][j][k])
    
    arr[i][-1] = arr[i][-1][1:len(arr[i][-1])-1]
    arr[i][-1] = arr[i][-1].split(",")
    for j in range(len(arr[i][-1])):
        arr[i][-1][j] = int(arr[i][-1][j]) 
    
    arr[i] = arr[i][1:]

def minimize_variable_sum(Aeq, beq):
    Aeq = np.array(Aeq, dtype=float)
    beq = np.array(beq, dtype=float)
    n = Aeq.shape[1]
    c = np.ones(n)
    constraints = LinearConstraint(Aeq, beq, beq)
    bounds = Bounds(lb=np.zeros(n), ub=np.full(n, np.inf))
    integrality = np.ones(n) 
    result = milp(
        c=c,
        constraints=constraints,
        bounds=bounds,
        integrality=integrality
    )
    if result.success:
        return int(round(result.fun)) 
    else:
        return None 


def indicator_lights(arr):
    count = 0
    for k in range(len(arr)):
        target = arr[k][-1]
        buttons = arr[k][:-1]
        n = len(buttons)
        m = len(target)
        mat = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                for button in buttons[j]:
                    if button == i:
                        mat[i][j] = 1
                        break
        min_sum  = minimize_variable_sum(mat, target)
        count += min_sum

    return count


print(indicator_lights(arr))

             