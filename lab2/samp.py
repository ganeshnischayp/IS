st=input("String: ")              #take input
a=(''.join(format(ord(x), 'b').zfill(8) for x in st))     #entire input converted into binary ('a' is string now)

print("Initial 64-bit key:",a)         #printing the same

new=''                  #consider the new empty string
pc1=[57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4]

for i in range(len(pc1)):
    new+=a[pc1[i]-1]   

print(new)