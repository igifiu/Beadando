import numpy as np

#M=a11*a22*a33+a12*a23*a31+a13*a21*a32-a31*a22*a13-a32*a23*a12
def determinans():
    matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
    m=[0,1,2,3,4,5,6,7,8,9]; a=[0,1,2,3,4,5]; b=[0,1]; c=0
    m[0]=matrix[0][0]; m[1]=matrix[0][1]; m[2]=matrix[0][2]
    m[3]=matrix[1][0]; m[4]=matrix[1][1]; m[5]=matrix[1][2]
    m[6]=matrix[2][0]; m[7]=matrix[2][1]; m[8]=matrix[2][2]
    a[0]+=m[0]*m[4]*m[8]
    a[1]+=m[1]*m[5]*m[6]
    a[2]+=m[2]*m[3]*m[7]
    a[3]+=m[6]*m[4]*m[2]
    a[4]+=m[7]*m[5]*m[0]
    a[5]+=m[8]*m[3]*m[1]
    b[0]+=a[0]+a[1]+a[2]
    b[1]+=a[3]-a[4]-a[5]
    c+=b[0]-b[1]
    return matrix,c
print(determinans())
