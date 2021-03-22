import matrix
import random
from fractions import Fraction

def cramer(A, B):
    X = [0] * len(A)
    temp = [row[:] for row in A]
    triangleA = A
    detA = matrix.detUpperTriangle(triangleA)
    print("detA: %.2f" % detA)

    for i in range(len(A)):
        T = [row[:] for row in temp]
        for j in range(len(A)):
            T[j][i] = B[j]
        detT = matrix.detUpperTriangle(T)
        X[i] = detT / detA
        print("det %d : %.2f" % (i, detT))

    print("Cramer solutions:")
    for x in X:
        print("%.4f" % x)



def gauss(A, B):
    for i in range(len(A) - 1): # for each column except last
        x = i + 1
        while A[i][i] == 0 and j < len(A):
            matrix.shuffleRows(A, i, x)
            matrix.shuffleRows(B, i, x)
            x += 1
            print("SHUFLLEEEE")
        if x == len(A): 
            continue
        for j in range(i + 1, len(A)): # for each row down 
            rowRatio = A[j][i] / A[i][i]
            B[j] -= rowRatio * B[i]
            for k in range(i, len(A)): # for each element
                A[j][k] -= rowRatio * A[i][k]
    X = B.copy()
    # algorytm podstawiania wstecz
    for i in reversed(range(0, len(A))):
        for j in range(i+1, len(A)):
            X[i] -= A[i][j] * X[j]
        X[i] /= A[i][i]
    print("Gauss solutions:")
    for x in X:
        print("%.4f" % x)


N = int(input("DIM: "))
#A = matrix.randomMatrix(N)
#B = random.sample(range(1,100), N)

A = [[1, 1, 1],
     [0, 2, 5],
     [2, 5, -1]]
B = [6, -4, 27]

# X = [5, 3, -2]


#cramer(A,B)
gauss(A,B)
