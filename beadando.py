import numpy as np

list=[]; lists=[]; list25=[]
for i in range(1,101):
    list.append(i)

np.random.shuffle(list)
lists.append(list)
for i in range(0,25):
    list25.append(list[i])

def matrix():
    x=[0,1,2,3,4]; x1=[0,1,2,3,4]; x2=[0,1,2,3,4]; x3=[0,1,2,3,4]; x4=[0,1,2,3,4]
    for i in range(0,5):
        for j in range(0,5):
            x[i]=list25[i]
            x1[i]=list25[i+5]
            x2[i]=list25[i+10]
            x3[i]=list25[i+15]
            x4[i]=list25[i+20]
    matrix=np.array([[x],[x1],[x2],[x3],[x4]])

    sor=[0,0,0,0,0]; oszlop=[0,0,0,0,0]; max=[0,0,0,0,0]

    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][0][j]>max[0]:
                max[0]=matrix[i][0][j]
                sor[0]=i
                oszlop[0]=j
            if matrix[i][0][j]>max[1] and matrix[i][0][j]<max[0]:
                sor[1]=i
                oszlop[1]=j
                max[1]=matrix[i][0][j]
            if matrix[i][0][j]>max[2] and matrix[i][0][j]<max[1]:
                sor[2]=i
                oszlop[2]=j
                max[2]=matrix[i][0][j]
            if matrix[i][0][j]>max[3] and matrix[i][0][j]<max[2]:
                sor[3]=i
                oszlop[3]=j
                max[3]=matrix[i][0][j]
            if matrix[i][0][j]>max[4] and matrix[i][0][j]<max[3]:
                sor[4]=i
                oszlop[4]=j
                max[4]=matrix[i][0][j]
    return matrix,max[0]+max[1]+max[2]+max[3]+max[4]
print(matrix())



