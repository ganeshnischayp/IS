
def b_s_a(N,M,e,r,block_size):
    # r_inv = r_inverse(r,N)
    
    count = 0
    flag = 0
    while count < 3:
        count += 1
        r_inv = r_inverse(r,N)
        if r_inv != -1:
            flag = 1
            break
        else:
            if count==3:
                break
            r = int(input("Enter r: "))

    if flag == 0:
        print("r inverse dosent exist")
        exit()
    
    # print(r_inv)
    phi_n = (p-1)*(q-1)
    array = [M[i:i+block_size] for i in range(0, len(M), block_size)]
    
    # print(array)
    with open('Program5-Output-Bsignature-S5.txt', 'w') as output_file:
        for i in range(len(array)):
            hex_con=""
            for j in range(len(array[i])):
                hex_con = hex_con + to_hexa(array[i][j])

        # print(hex_con)
        
            dec_blck = to_decimal(hex_con)

        # print(dec_blck)
        # print(str(dec_blck))
            decieve_text = attacker(int(dec_blck),int(N),int(r),int(e))
            user_sends   = user(int(decieve_text),int(phi_n),int(e))
            # signature = get_signature(int(user_sends),int(r_inv),int(N))
            plaintext    = plaint(int(user_sends),int(r_inv),int(N))
            # print(plaintext)
            decode_tohex = dec_to_hexa(int(plaintext))

            if(len(decode_tohex)%2!=0):
                decode_tohex='0'+decode_tohex

            hex_array = [decode_tohex[i:i+2] for i in range(0, len(decode_tohex), 2)]
            print(hex_array)
            final_ans=''
            
            # for k in range(len(hex_array)):
            #     final_ans = final_ans + to_decimal_to_char(hex_array[k])
            # print(final_ans)
            
            print("Block " + str(array[i]) +" Plain text INT:  "+str(plaintext) +" HEX PLAINTEXT : "+str(decode_tohex))
            # output_file.write("Block " + str(array[i]) +"  Sign Int :  "+str(signature) +"   Signature :  " +final_ans+"\n")

def attacker(M,N,r,e):
    text=M*(r**e)%N
    return text

def user(d_t,phi_N,e):
    d=int(modinv(e,phi_N))
    # print(d)
    if(d==-1):
        print("D doesnt exist")
        exit()
    user_sends = (d_t**d)%N
    return user_sends

def plaint(u_s,r_inv,N):
    p = (u_s*r_inv)%N
    return p
    
def dec_to_hexa(num):
    return hex(num).split('x')[-1]

def to_hexa(chara):
    return format(ord(chara), "x")

def to_decimal(h):
    return  int(h,16)
     

def to_decimal_to_char(h):
    ascii = int(h,16)
    # print(ascii)
    return chr(ascii)

def r_inverse(r,N):
    r_inv = modinv(r,N)
    return r_inv

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
        print("Inverse doesnt exist")
        # raise Exception('modular inverse does not exist')
    else:
        return x % m


# def get_signature(t,r_i,N):
#     sig = (t*r_i)%N
#     return sig

p = int(input('Enter the p value:'))
q = int(input('Enter the q value:'))
# change M format 
M = input('Enter plaintext :')
e = int(input('Enter e Value :'))
r = int(input('Enter r value :'))
N=p*q
# determine block size
x=8
while(N>(2**x)):
    if(N>(2**(x+8))):
        x=x+8
    else:
        break
block_size=x/8
b_s_a(N,M,e,r,int(block_size))
