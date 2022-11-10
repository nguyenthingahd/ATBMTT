list_text = ["A" ,	"B",	"C",	"D",	"E",	"F",	"G",	"H",	
            "I",	"J",	"K",	"L", "M",	"N",	"O",	"P",	"Q",	
            "R",	"S",	"T",	"U",	"V",	"W",	"X",	"Y",	"Z"]
 # mã hóa 

def Encrypt(string ,key):
    List_Index_String = list()
    List_Index_Key = list()
    
    ## Lấy ra index từ list_text , xem xem index của HELLO trong list_text
    for i in string : 
        index_string = list_text.index(i)
        List_Index_String.append(index_string)
      
    ## Lấy ra index từ list_text , xem xem index của XMCKL trong list_text
    for j in key : 
        index_key = list_text.index(j)
        List_Index_Key.append(index_key)
            
    ## Trings + Key % 26 -> ra 
    List_Index_Encrypt = list()
    for index in range(0,len(key)):
        Xor = (List_Index_String[index]  + List_Index_Key[index] ) % 26 
        List_Index_Encrypt.append(Xor)
    
    C = ""
    for index in List_Index_Encrypt:
        C += list_text[index]
    
    return C 

Ma_hoa = Encrypt("HELLO","XMCKL")
print("Ma Hoa : " + Ma_hoa)

def Decrypt(string ,key):

    List_Index_String = list()
    List_Index_Key = list()
    
    ## Lấy ra index từ list_text , xem xem index của EQNVZ trong list_text
    for i in string : 
        index_string = list_text.index(i)
        List_Index_String.append(index_string)
        
        
    ## Lấy ra index từ list_text , xem xem index của XMCKL trong list_text
    for j in key : 
        index_key = list_text.index(j)
        List_Index_Key.append(index_key)
        
        
    List_Index_Decrypt = list()
    for index in range(0,len(key)):
        Xor = (List_Index_String[index]  - List_Index_Key[index] ) % 26 
        List_Index_Decrypt.append(Xor)
        
        
    
    M = ""
    for index in List_Index_Decrypt:
        M += list_text[index]
        
    
    return M
        
        
Giai_ma = Decrypt("EQNVZ","XMCKL")
print("Giai ma : " + Giai_ma)