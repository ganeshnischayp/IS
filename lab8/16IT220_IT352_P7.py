import math
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return -1

def factors_func(n):
    factors = []
    i=1
    while(i<=n):
        k=0
        if(n%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                factors.append(i)
        i=i+1
    return factors
p = int(input("enter p: "))
q = int(input("enter q: "))
m = (input("Enter M: "))

# n = int(input("Enter N: "))
n = p * q
e = int(input("Enter e: "))


factors = factors_func(n)
# print("factors of N = ",*factors)
phi_of_n = (factors[0]-1)*(factors[1]-1)
# phi_of_n = (p-1)*(q-1)
d = modInverse(e,phi_of_n)

if d == -1:
    print("d dosent exist: ")
    exit()

print("Private key ",d)

r = int(input("Enter r: "))
count = 0
flag = 0
while count < 3:
    count += 1
    r_inverse = modInverse(r,n)
    if r_inverse != -1:
        flag = 1
        break
    else:
        if count == 3:
            break
        r = int(input("Enter r: "))

if flag == 0:
    print("r inverse dosent exist")
    exit()



print("r_inverse ",r_inverse)

block_size = (math.floor(math.log(n)/math.log(2))+1) // 8

block_size = int(block_size)
print(int(block_size))
num_blocks =len(m) /  (block_size)
num_blocks = int(num_blocks)

arr = [m[i:i+block_size] for i in range(0,len(m),block_size)]
print(arr)


cipher_arr = []
for l in range(len(arr)):
    hexa_caoncat = ''
    for ll in arr[l]:
        val = ord(ll)
        hexa_caoncat += (hex(val).replace('0x',''))
    in_dec = int(hexa_caoncat,16)
    cipher_arr.append(in_dec)
    print(cipher_arr)

vapas_string = ''
cipher_string = ''


for k in range(len(arr)):
    hexa_caoncat = ''
    for j in arr[k]:
        ascii = ord(j)
        hexa_caoncat += (hex(ascii).replace('0x',''))
    # print(hexa_caoncat)
    in_dec = int(hexa_caoncat,16)
    # print(in_dec)//////////////////////////////

    sends_to_sign = (in_dec * (r ** e)) % n
    sends_signed = (sends_to_sign ** d) % n
    attacker_recieved = (sends_signed * r_inverse) % n

    attacker_recieved_in_hex = hex(attacker_recieved).replace('0x','')
    # print(attacker_recieved_in_hex)

    if len(attacker_recieved_in_hex)%2 != 0:
        attacker_recieved_in_hex = '0' + attacker_recieved_in_hex


    final_hex_arr = [attacker_recieved_in_hex[i:i+2] for i in range(0,len(attacker_recieved_in_hex),2)]
        
    final_char_arr = []
    cch = []
    for kkk in (final_hex_arr):
        cch.append(chr(int(kkk,16)))

    cch_join = ''
    for ll in cch:
        cch_join += ll

        



    # print(final_hex_arr)
    #  = int(attacker_recieved_in_hex,16)

    final_ans = ''
    for i in range(len(final_hex_arr)):
        in_int = int(final_hex_arr[i],16)
        in_chr = chr(in_int)
        # print(final_hex_arr[i],int(final_hex_arr[i],16),chr(int(final_hex_arr[i],16)))

        # print(in_int,str(in_chr))
        final_ans += chr(int(final_hex_arr[i],16))
    
    checking = (attacker_recieved ** e) % n 
    # print(" Checking ",checking,)
    text =  (attacker_recieved ** e) % n
    txt1 = hex(text)[2:]
    msg = bytes.fromhex(txt1).decode('utf-8')
   
    # print("Block ",arr[k], " Attacker Received : ",attacker_recieved, "Hexadecimal = ",attacker_recieved_in_hex," Split Hexa = ",final_hex_arr, "Human  = ",final_ans)
    vapas_string += msg
    cipher_string += cch_join


    print("Block ",arr[k]," AttackerReceived : ",attacker_recieved,"Hexadecimal = ",attacker_recieved_in_hex," Split Hexa = ",final_hex_arr," cipher string: ",cch_join, "cipher = ",msg)
    

    # print(msg)
print("Final Plain text: ",cipher_string)
print("cipher msg obtained: ",vapas_string)


