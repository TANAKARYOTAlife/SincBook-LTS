import hashlib

def Sinc_Hash():
    Sinc_Hash = hashlib.sha3_256(''.encode()).digest()
    print(Sinc_Hash)
    
    Sinc_Hash = hashlib.sha3_256(''.encode()).digest()
    print(Sinc_Hash)

Sinc_Hash()
