import random

X = [random.randint(0,1) for i in range(6)]
Y = [random.randint(0,1) for i in range(8)]
Z = [random.randint(0,1) for i in range(9)]

print ("X = ", X)
print ("Y = ", Y)
print ("Z = ", Z)

def maj (x,y,z):
    if (x==y==0 or y==z==0 or z==x==0):
        return 0
    return 1

def quay_X(X):
    t = X[2]^X[4]^X[5]
    new_X = [t]
    
    for i in range (0, len(X)-1):
        new_X.append(X[i])
    return new_X
def quay_Y(Y):
    t = Y[6]^Y[7]
    new_Y = [t]
    for i in range (0, len(Y)-1):
        new_Y.append(Y[i])
    return new_Y
def quay_Z(Z):
    t = Z[2]^Z[7]^Z[8]
    new_Z = [t]
    for i in range (0, len(Z)-1):
        new_Z.append(Z[i])
    return new_Z
        
P = '1000101010011010'
C = ''

for i in range(len(P)):
    m = maj(X[1], Y[3], Z[3])
    if X[1]==m:
        x = quay_X
    if Y[3]==m:
        y = quay_Y
    if Z[3]==m:
        z = quay_Z
    s = X[5]^Y[7]^Z[8]
    t = int (P[i]) ^ s
    C+=str(t)	

print("P = ", P)
print("C = ", C)



