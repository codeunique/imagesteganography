
import numpy as np



# Function to convert a string to its binary representation
def strToBinary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8)) 

def binToString(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def addZeros(strr, n): 
    for i in range(n): 
        strr = "0" + strr 
    return strr 
  
# Function to return the XOR 
# of the given strrings 
def getXOR(a, b): 
  
    # Lengths of the given strrings 
    aLen = len(a) 
    bLen = len(b) 
  
    # Make both the strrings of equal lengths asd
    # by inserting 0s in the beginning 
    if (aLen > bLen): 
        b = addZeros(b, aLen - bLen) 
    elif (bLen > aLen): 
        a = addZeros(a, bLen - aLen) 
  
    # Updated length 
    lenn = max(aLen, bLen); 
  
    # To store the resultant XOR 
    res = "" 
    for i in range(lenn): 
        if (a[i] == b[i]): 
            res += "0"
        else: 
            res += "1"
  
    return res 