import random

def printMatrix(M):
    for i in range(len(M)):
        for j in range(len(M)):
            print("%.2f\t" % M[i][j], end = '')
        print()
    print()

def shuffleRows(M, i, j):
    temp = M[i]
    M[i] = M[j]
    M[j] = temp

def detUpperTriangle(M):
    det = 1
    for i in range(len(M) - 1): # for each column except last
        x = i + 1
        while M[i][i] == 0 and j < len(M):
            shuffleRows(M, i, x)
            det *= -1
            x += 1
            print("SHUFLLEEEE")
        if x == len(M): 
            continue
        for j in range(i + 1, len(M)): # for each row down 
            rowRatio = M[j][i] / M[i][i]
            for k in range(i, len(M)): # for each element
                M[j][k] -= rowRatio * M[i][k]
            
    for i in range(len(M)):
            det *= M[i][i]
    return det
    

def randomMatrix(N = random.randint(2,10)):
    #N = random.randint(2,10)
    M = []
    for i in range(N):
        M.append(random.sample(range(1,100), N))
    return M
