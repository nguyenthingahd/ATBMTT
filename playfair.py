a = list(map(chr, range(ord("a"), ord("z") + 1)))
a.remove("j")
print (a)

def genKeyTable (word, list):
    key = []
    " convert word to list "
    for i in word :
        if i not in key :
            key.append(i)

    "fill the matrix with key first"
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
            
    "do with alphabet"
    for i in a:
        if i not in temp:
            temp.append(i)

    matrix = []
    while temp != []:
        matrix.append(temp[:5])
        temp = temp[5:]

    return matrix

def follow_rule1 (matrix, a1,a2, b1,b2):
    char1 = ''
    if (a2 == 4):
        char1 = matrix[a1][0]
    else :
        char1 = matrix [a1][a2 + 1]
    
    char2 = ''
    if (b2 == 4):
        char2 = matrix[b1][0]
    else :
        char2 = matrix [b1][b2 + 1]
    
    return char1, char2

def follow_rule2 (matrix, a1,a2, b1,b2):
    char1 = ''
    if (a1== 4):
        char1 = matrix[0][a2]
    else :
        char1 = matrix [a1 + 1][a2]
    
    char2 = ''
    if (b1== 4):
        char2 = matrix[0][b2]
    else :
        char2 = matrix [b1 + 1][b2]
    
    return char1, char2

def follow_rule3 (matrix, a1,a2, b1, b2):
    # char1 = ''
    char1 = matrix[a1][b2]
    char2 = matrix[b1][a2]
    return char1, char2

def search (matrix, element):
    for i in range (5):
        for j in range (5):
            if (matrix[i][j] == element):
                return i, j

# Neu hai ki tu lien tiep giong nhau, them x
# du mot ki tu, them x vao cuoi
def Add_x(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = Add_x(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = Add_x(new_word)
                break
            else:
                new_word = text
        new_word += str("x")
    return new_word

# chia string theo tung cap ki tu
def split(text):
    split_2 = []
    group = 0
    for i in range(2, len(text), 2):
        # print (i)
        # print (text[group:i])
        split_2.append(text[group:i])

        group = i
    split_2.append(text[group:])
    return split_2

def encrypt_PF(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        # lấy vị trí(hàng và cột) của từng chữ trong cặp
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = follow_rule1(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            
        elif ele1_y == ele2_y:
            c1, c2 = follow_rule2(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = follow_rule3(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText
text_Plain = 'thematchisover'
PlainTextList = split(Add_x(text_Plain))
print(PlainTextList[0][1])
print(PlainTextList)

matrix = genKeyTable("home", a)
# print (matrix)
print (encrypt_PF(matrix, PlainTextList))