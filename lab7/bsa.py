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

m = int(input("Enter M: "))
e = int(input("Enter e: "))
n = int(input("Enter N "))
r = int(input("Enter r: "))

factors = factors_func(n)
print("factors of N = ",*factors)
phi_of_n = (factors[0]-1)*(factors[1]-1)
d = modInverse(e,phi_of_n)
print("private key = ",d)
r_inverse = modInverse(r,n)
print("r inverse wrt mod(N)",r_inverse)

# fucker attacker
sends_to_sign = (m * (r ** e)) % n

# noob bob
sends_signed = (sends_to_sign ** d) % n

# fucker attacker receives
attacker_recieved = (sends_signed * r_inverse) % n

print("Blind signature attack: ",attacker_recieved)
