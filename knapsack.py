def hardKnapsack(m,b,n):    #Function to find General Knapsack Series
    return (m*b) % n

def encryptKnapsack(msg_lst, hard_lst): #Function to encrypt
    sum =0
    for i,j in zip(msg_lst,hard_lst):
        sum = sum + (int(i)*j)
        
    return sum

def inverse(m,n):   #Function to find inverse of m
    inv = 0
    while(1):
        if ((m*inv) % n == 1):
            return inv

        inv = inv + 1

def decryptKnapsack(c,inv,n): #Function to decrypt the encrypted value
    de = (inv * c) % n
    bin = ['0' for i in range(len(b))]
    lst = subset_sum(b, de)

    for i in lst[-1]:
        bin[b.index(i)] = '1'

    return bin

def subset_sum(numbers, target, partial=[]): #Returns list of numbers who's sum is equal to de
    s = sum(partial)

    if s == target:                              
        result_list1.append(partial)
        
    if s >= target:
        return result_list1                                    

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])
    
    return result_list1 

def BinaryToDecimal(binary):   #Function to convert binaryto decimal
    string = int(binary, 2)   
    return string

#---------------Main Code----------------

b = [3, 5, 11, 20, 41]  # super-increaseing series
n = 85                  # modulus
m = 44                  # multiplier

message = list(input("\n Enter your message to be encrypted : ").replace(" ","")) #input message
#print("\n Your message is : ",''.join(message))

res = ''.join(format(ord(i), 'b') for i in message) #binary string of input message

add_str =''
if(len(res) % len(b) != 0):
    add_str = "0" * (len(b) - len(res) % len(b))
    res = add_str + res
    
print("\n Binary string of your message : ",res)

res_list = list(list(res[i:i+len(b)]) for i in range(0, len(res), len(b))) #binary list of elements of length len(b)

#-------------------GKS--------------------
gks =[]

for i in b:
    gks.append(hardKnapsack(m,i,n))     # generates general knapsack series/hard knapsack series & stores in gks

#----------------Encryption----------------
encrypted_lst =[]

for j in res_list:
    encrypted_lst.append(encryptKnapsack(j,gks))   # generates list of encrypted values 

print("\n Encrypted value list : ",encrypted_lst)

#----------------decryption-----------------

minv = inverse(m,n) # Obtains the inverse of m

decrypted_lst = []
result_list1 =[]
for c in encrypted_lst:
    decrypted_lst.append(''.join(decryptKnapsack(c,minv,n))) # generates list of binary values of decrypted message

debin_str = ''.join(decrypted_lst)
print("\n Decrypted value in binary : ",debin_str)

#covert decrypted binary value back to string
str_data =''
for i in range(len(add_str), len(debin_str), 7): 
    bin_temp = str(debin_str[i:i + 7])
    decimal_data = BinaryToDecimal(bin_temp) 
    str_data = str_data + chr(decimal_data)  

print("\n Decrypted String value is : ",str_data)