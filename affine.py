# Ma hoa
alphabet = list(map(chr, range(ord("A"), ord("Z")+1)))
text = input("Nhap: ").upper()
def encrypt(text, a, b, alphabet):
   E = ''
   for char in text:
      x = alphabet.index(char)
      e = (a*x+b) %26
      c = alphabet[e]
      E +=c
   return E
print (encrypt(text, 5,3, alphabet))

# Giai ma x = a^-1 *(y-b)mod 26
def a_nghich_dao(a):
   for i in range(1,26):
      if (a*i)%26 == 1:
         return i
def affineCiper(text, a, b, alphabet):
   result = ''
   for char in text: 
      y = alphabet.index(char)
      a_nd = a_nghich_dao(a)
      x = a_nd*(y-b)%26
      c = alphabet[x]
      result += c
   return result
print(affineCiper("MXGGV", 5, 3, alphabet))