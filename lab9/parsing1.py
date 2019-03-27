import pcapkit

def encrypt(pk, plaintext):
    key, n = pk
    cipher = ((plaintext) ** key) % n 
    return cipher

extraction=pcapkit.extract(fin='sai.pcap',nofile=True,engine='dpkt')
# print(extraction.frame)

st = extraction.frame[356]['Raw'].info.packet.__str__()[2:-1]
print(st)

cipher = st
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

print("\n".join(map(str,append_arr)))
# print("\n")
# print("Intermediate results: ")

# file1 = open("16IT220_Intermediate_results_P5_S5.txt","x") 
# file1.write("\n".join(map(str,append_arr))) 
# print(*append_arr,sep="\t")

print("\n")
print("The plain text is: ",append_arr[-2])
