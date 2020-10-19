def nfind(p,q):  #to find n
    return p*q

def phyOfn(p,q):       #to find phy of n
    return (p-1)*(q-1)

def gcd(a,b):       #to find gcd of two numbers
    lim = min(a,b)
    gcdval=0
    
    for i in range(1,lim+1):
        if(a%i == 0 and b%i == 0 ):
            gcdval = i
        
    return gcdval

def efind(phy):     #to find e
    eval = 0
    for i in range(2,phy):
        if (gcd(i,phy) == 1):
            eval = i

    return eval


def dfind(phy,e):   #to find d
    if (e > phy):
        return 0
    
    i = 0
    while(1):
        if ((i*e) % phy == 1):
            return i
        i = i + 1

    return 0


def encryptRSA(m,e,n):  #encryption
    crypto = (pow(m,e)) % n
    return crypto


def decryptRSA(crypto,d,n): #decryption
    decrypt = (pow(crypto,d)) % n
    return decrypt


#--main code begins--

p = int(input("\n Enter value of P : ")) 
q = int(input("\n Enter value of Q : ")) 

n = nfind(p,q)      # value of n 
phy = phyOfn(p,q)   # value of phy of n
e = efind(phy)      # value of e

public_key = [e,n]  # public key

d = dfind(phy,e)    # value of d

private_key = [d,n] # private key

message = list(input("\n Enter your message to be encrypted : "))
print("\n Your message is : ", ''.join(message))

ascii_lst =[ord(i) for i in message]
#print(ascii_lst)

encrypted_value = []

for m in ascii_lst:
    en = encryptRSA(m,e,n)      # encrypt value
    encrypted_value.append(en)
    
print("\n Encrypted value : ", encrypted_value)

decrypted_value = []

for c in encrypted_value:
    de = decryptRSA(c,d,n)      # decrypt value
    decrypted_value.append(chr(de))
    

print("\n Decrypted value : ", ''.join(decrypted_value),"\n")

