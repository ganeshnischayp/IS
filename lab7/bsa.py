import math
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

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

n = p * q
e = int(input("Enter e: "))
factors = factors_func(n)
# print("factors of N = ",*factors)
# phi_of_n = (factors[0]-1)*(factors[1]-1)
phi_of_n = (p-1)*(q-1)
d = modInverse(e,phi_of_n)
print(d)
r = int(input("Enter r: "))
r_inverse = modInverse(r,n)
print(r_inverse)
block_size = (math.floor(math.log(n)/math.log(2))+1) // 8

block_size = int(block_size)
print(int(block_size))
num_blocks =len(m) /  (block_size)
num_blocks = int(num_blocks)

arr = [m[i:i+block_size] for i in range(0,len(m),block_size)]
print(arr)

for k in range(len(arr)):
    hexa_caoncat = ''
    for j in arr[k]:
        ascii = ord(j)
        hexa_caoncat += (hex(ascii).replace('0x',''))
    # print(hexa_caoncat)
    in_dec = int(hexa_caoncat,16)


    sends_to_sign = (in_dec * (r ** e)) % n
    sends_signed = (sends_to_sign ** d) % n
    attacker_recieved = (sends_signed * r_inverse) % n

    attacker_recieved_in_hex = hex(attacker_recieved).replace('0x','')
    # print(attacker_recieved_in_hex)

    final_hex_arr = [attacker_recieved_in_hex[i:i+2] for i in range(0,len(attacker_recieved_in_hex),block_size)]
    # print(final_hex_arr)
    #  = int(attacker_recieved_in_hex,16)

    final_ans = ''
    for i in range(len(final_hex_arr)):
        in_int = int(final_hex_arr[i],16)
        in_chr = chr(in_int)
        # print(final_hex_arr[i],int(final_hex_arr[i],16),chr(int(final_hex_arr[i],16)))

        # print(in_int,str(in_chr))
        final_ans += chr(int(final_hex_arr[i],16))

    print("Block ",arr[k]," Signature : ",attacker_recieved, "Hexadecimal = ",attacker_recieved_in_hex," Split Hexa = ",final_hex_arr, "Human  = ",final_ans)




