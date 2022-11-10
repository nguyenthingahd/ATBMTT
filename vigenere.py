def generatekey(string, key):
  key = list(key)
  if(len(string)==len(key)):
    return key
  else:
    for i in range (len(string)-len(key)):
      key.append(key[i % len(key)])
  return ("".join(key))

def encrypt(string, key):
  cipher_text = []
  for i in range (len(string)):
    x = (ord(string[i])+ord(key[i]))%26
    x += ord("A")
    cipher_text.append(chr(x))
  return("" . join(cipher_text))

def decrypt(cipher_text, key):
  result = []
  for i in range(len(cipher_text)):
    x = (ord(cipher_text[i]) - ord(key[i])+26)%26
    x+=ord("A")
    result.append(chr(x))
  return("".join(result))

string = "HELLOWORLD"
k = "HOME"
key = generatekey(string, k)
print(key)
cipher_text = encrypt(string, key)
print ("Ma hoa: ", cipher_text)
print ("Giai ma : ", decrypt(cipher_text, key))


