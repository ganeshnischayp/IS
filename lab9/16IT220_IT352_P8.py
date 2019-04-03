import pcapkit

def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 

def encrypt(pk, plaintext):
    key, n = pk
    cipher = power(plaintext,key, n)
    return cipher

extraction = pcapkit.extract(fin='55.pcap',nofile=True,engine='dpkt')
# print(extraction.frame)

st = extraction.frame[4]['Raw'].info.packet.__str__()[2:-1]
print(st)

cipher = int(st)
N = int(input("Enter N: "))
e = int(input("Enter e:" ))
append_arr = []

C1 = encrypt((e,N),cipher)
while True:
    C2 = encrypt((e,N),C1)
    append_arr.append(C2)
    if C2 == cipher:
        break
    C1 = C2

# print("\n".join(map(str,append_arr)))
# print("\n")
# print("Intermediate results: ")

# file1 = open("16IT220_Intermediate_results_P5_S5.txt","x") 
# file1.write("\n".join(map(str,append_arr))) 
# print(*append_arr,sep="\t")

print("\n")
print("The plain text is: ",append_arr[-2])

print("\n")
print("Checking: ")
check = encrypt((e,N),append_arr[-2])
print("Original Cipher: ",check)
print("\n")