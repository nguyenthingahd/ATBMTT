keyMatrix = [[0]*3 for i in range (3)]
clearTextVector = [[0] for i in range (3)]
cipherMatrix = [[0] for i in range (3)]

alphabet = a = list(map(chr, range(ord("a"), ord("z") + 1)))
print(alphabet)

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = alphabet.index(key[k])
            k+=1
def encryptHill(messageVector):
    for i in range(3):
        for j in range (1):
            cipherMatrix[i][j]=0
            for x in range (3):
                cipherMatrix[i][j] += (keyMatrix[i][x]*messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] %26
def hillCipher(message, key):
    getKeyMatrix(key)
    for i in range(3):
        clearTextVector[i][0] = alphabet.index(message[i])
    encryptHill(clearTextVector)
    cipherText = []
    for i in range(3):
        cipherText.append(alphabet[cipherMatrix[i][0]])
    print("".join(cipherText))

import numpy as np
from egcd import egcd

def inv_matrix(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det,26)[1]%26
    invMatrix = det_inv*np.round(det*np.linalg.inv(matrix)).astype(int)%26
    return invMatrix
def decrypt_Hill(message, key):
    getKeyMatrix(key)
    invKey = inv_matrix(np.array(keyMatrix))

    for i in range(3):
        cipherMatrix[i][0] = alphabet.index(message[i])
    
    cipherMatrix1 = np.array(cipherMatrix)

    for i in range(3):
        for j in range(1):
                clearTextVector[i][j] = 0
                for x in range(3):
                        clearTextVector[i][j] += (invKey[i][x] *
                                        cipherMatrix1[x][j])
                clearTextVector[i][j] = clearTextVector[i][j] % 26

    ClearText = []
    for i in range(3):
        ClearText.append(alphabet[clearTextVector[i][0]])
 
    print("".join(ClearText))
message = "act"
key = "gybnqkurp"
print("Ma hoa: ")
hillCipher(message, key)
print("Giai ma: ")
decrypt_Hill("poh", key)