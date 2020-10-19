def Swap(list,a,b): #swap list elements
    list[a],list[b] = list[b], list[a]

def GenerateKS(keystream,length): #generate key stream
    for i in range(0,length):
        keystream.append(keystream[i])

def EightByThree(key,p):  # 8 x 3 bit generation
    keystr =key.copy()
    s = [0, 1, 2, 3, 4, 5, 6, 7]

    if len(key) < len(s): 
        GenerateKS(keystr, len(s)-len(key)) #generate key stream
        #print(keystr)

    j = 0 

    for i in range(0,len(s)):
        j = ((j + s[i] + keystr[i])) % 8
        Swap(s,s.index(s[i]),s.index(s[j]))
        
    res = []
    i = j = 0

    for z in p:
        i = (i + 1) % 8   
        j = (j + s[i]) % 8
        Swap(s,s.index(s[i]),s.index(s[j]))
        t = (s[i] + s[j]) % 8
        ke = s[t]
        #print(ke)
        res.append(ke)

    i=0
    enc =[] 
    
    for x in p: #for encrypting input value
        enc.append(x ^ res[i])
        i = i + 1

    print("\n Encrypted value : " ,enc)

    dec =[]
    i=0

    for y in enc: #for decrypting encrypted value
        dec.append(y ^ res[i])
        i = i + 1

    print("\n Decrypted value : " ,dec)


def EightByEight(key,p):   # 8 x 8 bit generation
    keystr =key.copy()
    s = [ i for i in range(0,256)]

    if len(key) < len(s): 
        GenerateKS(keystr, len(s)-len(key)) #generate key stream
        #print(keystr)

    j = 0

    for i in range(0,len(s)-1):
        j = ((j + s[i] + keystr[i])) % 256
        Swap(s,s.index(s[i]),s.index(s[j]))

    res = []
    i = j = 0

    for z in p:
        i = (i + 1) % 256   
        j = (j + s[i]) % 256
        Swap(s,s.index(s[i]),s.index(s[j]))
        t = (s[i] + s[j]) % 256
        ke = s[t]
        #print(ke)
        res.append(ke)

    i=0
    enc =[] 
    
    for x in p: #for encrypting input value
        enc.append(x ^ res[i])
        i = i + 1

    print("\n Encrypted value : " ,enc)

    dec =[]
    i=0

    for y in enc: #for decrypting encrypted value
        dec.append(y ^ res[i])
        i = i + 1

    print("\n Decrypted value : " ,dec)


cont = "y"

while(cont == "y"):
    #p = [1,2,3,4,5,6,7,8,9,11,22]
    p = list(map(int,input("\n Enter the input numbers(with spaces as a differentiator) : ").strip().split()))[:] 
    
    #k=[1,2,0,9,8,8,5,5,5,5,5,5,4,4,32,4,4]
    k = list(map(int,input("\n Enter the key : ").strip().split()))[:] 

    print("\n Input value is :",p)
    print("\n key is :",k)

    print("\n 1) 8 x 3 bit stream \n 2) 8 x 8 bit stream")

    choice =input(" \n Enter RC4 encryption method :")
    
    if (choice == "1"):
        EightByThree(k,p)
    
    if (choice == "2"):
        EightByEight(k,p)

    cont =input("\n\n do you want to continue?(y/n) : ")

    




