import time
from threading import Thread
step_i=0

MAX_THREAD = 4

def printMatrix(m):
    print("The result is:\n")
    for i in range(len(m)):
        for j in range (len(m[i])):
            print(m[i][j],end=' ')
        print()
    print()

def multiply(x,y):
    start = time.time()
    print("\n-------Multithreaded Multiplication--------\n")
    result = [[0 for i in range(len(y[0]))] for j in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    printMatrix(result)
    end = time.time()
    print("The time of execution of multithreaded multiplication is :",(end-start) * 10**3, "ms")

def multiplyMT():
    global step_i, result
    i = step_i
    step_i = step_i + 1
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] = result[i][j] + X[i][k] * Y[k][j]
    
X = [[3,7,3,6],
    [9,2,0,3],
    [0,2,1,7],
    [2,2,7,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1],
    [11,2,5,6]]

result = [[0 for i in range(len(Y[0]))] for j in range(len(X))]
thread = list(range(MAX_THREAD))

start = time.time()
for i in range(MAX_THREAD):
    thread[i] = Thread(target=multiplyMT)
    thread[i].start()

for i in range(MAX_THREAD):
    thread[i].join()

print("-------Normal Multiplication--------\n")
printMatrix(result)
end = time.time()

print("The time of execution of normal multiplication is :",(end-start) * 10**3, "ms")
multiply(X,Y)