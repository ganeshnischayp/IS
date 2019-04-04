# command to build .exe
# gpn@gpnpc:~/Documents/6th-Sem/IS/lab6$ pyinstaller --onefile tinker.py

from tkinter import *
import math
import binascii
import copy
IPtable = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]



def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def concat_bits(s):
    bits = ''
    for i in range(len(s)):
        bits += s[i]
    return (bits).ljust(64,'0')


def initial_permutation(num):
    text_split =list(num)
    text_split1 =list(num)

    num_blocks = math.ceil(len(text_split)/8)
    text_block = [[]for i in range(num_blocks)]
    for i in range(num_blocks+1):
        for j in range(8):
            if len(text_split) > 0:
                text_block[i].append(text_split.pop(0))
            else:
                break

    samp = text_block.copy()

    for i in range(len(text_block)):
        for j in range(len(text_block[i])):
            samp[i][j] = text_to_bits(text_block[i][j])
    final_code = [[]for i in range(len(text_block))]
    for i in range(len(text_block)):
        list_concat_64 = list(concat_bits(samp[i]))
        onlyListConcat = list_concat_64.copy()
        useful_array = [None for i in range(64)]
        for j in range(len(list_concat_64)):
            useful_array[IPtable.index(j+1)] = onlyListConcat[j]
        copy_list_concat_64 = useful_array.copy()
        for k in range(8):
            var = ''
            for l in range(8):
                var += copy_list_concat_64.pop(0)
            final_code[i].append(var)
    full_final = ''
    for i in range(len(final_code)):
        join_final = ''
        for j in range(len(final_code[i])):
            join_final += final_code[i][j]
        full_final += join_final


    return full_final

##################DECODING PART########################################

FPtable = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41,  9, 49, 17, 57, 25]

def final_permut(full_final):
    num1 = full_final
    num_split =list(num1)
    sam = num_split
    num_blocks = int(len(num_split)//64)
    bits_arr_64 = [[]for i in range(num_blocks)]
    for i in range(num_blocks):
        for j in range(64):
            bits_arr_64[i].append(sam.pop(0))

    new_copy_bits_arr_64 = bits_arr_64.copy()
    useful_array = [[None for i in range(64)]for i in range(num_blocks)]

    for i in range(len(bits_arr_64)):
        for j in range(len(bits_arr_64[i])):
            useful_array[i][FPtable.index(j+1)] = new_copy_bits_arr_64[i][j]
    full_text = ''
    for i in range(len(useful_array)):
        var = ''
        for j in range(len(useful_array[i])):
            var += useful_array[i][j]
        full_text += var
    return full_text

permut_choice_1 = [57, 49, 41, 33, 25, 17, 9,
                   1, 58, 50, 42, 34, 26, 18,
                   10, 2, 59, 51, 43, 35, 27,
                   19, 11, 3, 60, 52, 44, 36,
                   63, 55, 47, 39, 31, 23, 15,
                   7, 62, 54, 46, 38, 30, 22,
                   14, 6, 61, 53, 45, 37, 29,
                   21, 13, 5, 28, 20, 12, 4]

permut_choice_2 = [14, 17, 11, 24, 1, 5,
                   3, 28, 15, 6, 21, 10,
                   23, 19, 12,  4, 26, 8,
                   16, 7, 27, 20, 13, 2,
                   41, 52, 31, 37, 47, 55,
                   30, 40, 51, 45, 33, 48,
                   44, 49, 39, 56, 34, 53,
                   46, 42, 50, 36, 29, 32]



def join_single_bits(arr):
    string = ''
    for i in range(len(arr)):
        string += arr[i]
    return string

def one_bit_shift(var):
    var1 = list(var)
    ele0 = var1.pop(0)
    var1.append(ele0)
    return join_single_bits(var1)


def two_bit_shift(var):
    var1 = list(var)
    ele0 = var1.pop(0)
    ele1 = var1.pop(0)
    var1.append(ele0)
    var1.append(ele1)
    return join_single_bits(var1)


def convert_to_single_bits(arr):
    split_list = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            split_list.append(arr[i][j])
    return split_list



def round_keys_generate(to_extract,imp_list):
    if len(imp_list) >= to_extract:
        inp_8_char = imp_list[:to_extract]
        for i in range(len(inp_8_char)):
            inp_8_char[i] = text_to_bits(inp_8_char[i])
        bit_64_arr = convert_to_single_bits(inp_8_char)
        bit_56_arr = []
        for i in range(56):
            bit_56_arr.append(bit_64_arr[permut_choice_1[i]-1])
        # print(bit_56_arr)
        left_half = bit_56_arr[:28]
        right_half = bit_56_arr[28:]
        round_keys_output = []
        for l in range(16):
            if l == 0 or l == 1 or l == 8 or l == 15:
                left_half = join_single_bits(left_half)
                left_half1 = one_bit_shift(left_half)

                right_half = join_single_bits(right_half)
                right_half1 = one_bit_shift(right_half)

                left_half1 = convert_to_single_bits(left_half1)
                right_half1 = convert_to_single_bits(right_half1)

                key = left_half1 + right_half1

                key1 = []
                for i in range(48):
                    key1.append(key[permut_choice_2[i]-1])
                round_keys_output.append(join_single_bits(key1))
                # print("Round - ", l+1,join_single_bits(key1))
                left_half = convert_to_single_bits(left_half1)
                right_half = convert_to_single_bits(right_half1)

            else:
                left_half = join_single_bits(left_half)
                left_half1 = two_bit_shift(left_half)

                right_half = join_single_bits(right_half)
                right_half1 = two_bit_shift(right_half)

                left_half1 = convert_to_single_bits(left_half1)
                right_half1 = convert_to_single_bits(right_half1)

                key = left_half1 + right_half1

                key1 = []
                for i in range(48):
                    key1.append(key[permut_choice_2[i]-1])
                round_keys_output.append(join_single_bits(key1))
                # print("Round - ",l+1,join_single_bits(key1))
                left_half = convert_to_single_bits(left_half1)
                right_half = convert_to_single_bits(right_half1)

    else:
        print("Enter key of bigger length")
        exit
    
    return round_keys_output


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def decimalToBinary(n):
    return bin(n).replace("0b", "").zfill(48)


def decimalToBinary_4(n):
    return bin(n).replace("0b", "").zfill(4)


def decimalToBinary_32(n):
    return bin(n).replace("0b", "").zfill(32)


# def convert_to_single_bits(arr):
#     split_list = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             split_list.append(arr[i][j])
#     return split_list


# def join_single_bits(arr):
#     string = ''
#     for i in range(len(arr)):
#         string += arr[i]
#     return string


def convert_to_6_bit(var):
    bit_6_join = []
    for i in range(48):
        if i % 6 == 0:
            bit_6_join.append(var[i:i+6])
    return bit_6_join


expansion_permurt = [32, 1, 2, 3, 4, 5,
                     4, 5, 6, 7, 8, 9,
                     8, 9, 10, 11, 12, 13,
                     12, 13, 14, 15, 16, 17,
                     16, 17, 18, 19, 20, 21,
                     20, 21, 22, 23, 24, 25,
                     24, 25, 26, 27, 28, 29,
                     28, 29, 30, 31, 32, 1]
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

perm_after_s_box = [16, 7, 20, 21, 29, 12, 28, 17,
                    1, 15, 23, 26, 5, 18, 31, 10,
                    2, 8, 24, 14, 32, 27, 3, 9,
                    19, 13, 30, 6, 22, 11, 4, 25]


def S_box_out(arr):
    s_box_out_32 = []
    for i in range(8):
        a = arr[i][0]
        b = arr[i][5]
        row = binaryToDecimal(int(a+b))
        col = binaryToDecimal(int(arr[i][1:-1]))
        s_box_out_32.append(decimalToBinary_4(S_BOX[i][row][col]))
    return s_box_out_32

def output_only_des(IP_out,round_keys):
    output_each_round = []
    for l in range(16):
        IP_out_single_bit = convert_to_single_bits(IP_out)

        left_32 = IP_out_single_bit[:32]
        right_32 = IP_out_single_bit[32:]

        out_exp_permut = []

        for i in range(48):
            out_exp_permut.append(right_32[expansion_permurt[i]-1])

        xor_out = (binaryToDecimal(int(join_single_bits(out_exp_permut)))
                ^ binaryToDecimal(int(round_keys[l])))
        xor_out = decimalToBinary(xor_out)

        bit_6_join = convert_to_6_bit(xor_out)
        bit_4_join = S_box_out(bit_6_join)
        bit_4_join_single = ''
        for i in range(8):
            bit_4_join_single += bit_4_join[i]
        bit_4_join_split = convert_to_single_bits(bit_4_join_single)

        permut_after_sbox = []
        for i in range(32):
            permut_after_sbox.append(bit_4_join_split[perm_after_s_box[i]-1])

        # print(binaryToDecimal(int(join_single_bits(permut_after_sbox))))

        # print(binaryToDecimal(int(join_single_bits(left_32))))

        xor_out_with_left32 = binaryToDecimal(int(join_single_bits(
            permut_after_sbox))) ^ binaryToDecimal(int(join_single_bits(left_32)))

        xor_out_with_left32 = decimalToBinary_32(xor_out_with_left32)
        # print(xor_out_with_left32)
        last_right_join = (join_single_bits(right_32))

        output_each_round.append(xor_out_with_left32 + last_right_join)
        
        round_output = last_right_join + xor_out_with_left32
        IP_out = round_output
    return output_each_round

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

def blind_signature_attack(p,q,m,e,r):
    n = p * q
    factors = factors_func(n)
    phi_of_n = (p-1)*(q-1)
    d = modInverse(e,phi_of_n)

    if d == -1:
        return "d dosent exist"

    r_inverse = modInverse(r,n)

    if r_inverse == -1:
        return "r inverse dosent exist"



    block_size = (math.floor(math.log(n)/math.log(2))+1) // 8

    block_size = int(block_size)
    num_blocks =len(m) /  (block_size)
    num_blocks = int(num_blocks)

    arr = [m[i:i+block_size] for i in range(0,len(m),block_size)]
    return_string = ''
    for k in range(len(arr)):
        hexa_caoncat = ''
        for j in arr[k]:
            ascii = ord(j)
            hexa_caoncat += (hex(ascii).replace('0x',''))
        in_dec = int(hexa_caoncat,16)

        sends_to_sign = (in_dec * (r ** e)) % n
        sends_signed = (sends_to_sign ** d) % n
        attacker_recieved = (sends_signed * r_inverse) % n

        attacker_recieved_in_hex = hex(attacker_recieved).replace('0x','')

        if len(attacker_recieved_in_hex)%2 != 0:
            attacker_recieved_in_hex = '0' + attacker_recieved_in_hex


        final_hex_arr = [attacker_recieved_in_hex[i:i+2] for i in range(0,len(attacker_recieved_in_hex),2)]
        

        final_ans = ''
        for i in range(len(final_hex_arr)):
            in_int = int(final_hex_arr[i],16)
            in_chr = chr(in_int)

            final_ans += chr(int(final_hex_arr[i],16))
        
        checking = (attacker_recieved ** e) % n 
        # print(" Checking ",checking,)
        # print("Block ",arr[k], " Signature : ",attacker_recieved, "Hexadecimal = ",attacker_recieved_in_hex," Split Hexa = ",final_hex_arr, "Human  = ",final_ans)
        return_string += ("Block "+ str(arr[k]) + " Signature : " + str(attacker_recieved))
        return_string += '\n'
    
    return return_string


# def modInverse(a, m) : 
#     a = a % m; 
#     for x in range(1, m) : 
#         if ((a * x) % m == 1) : 
#             return x 
#     return -1

# def factors_func(n):
#     factors = []
#     i=1
#     while(i<=n):
#         k=0
#         if(n%i==0):
#             j=1
#             while(j<=i):
#                 if(i%j==0):
#                     k=k+1
#                 j=j+1
#             if(k==2):
#                 factors.append(i)
#         i=i+1
#     return factors


def chosen_cipher_text(p,q,m,e,r):
    n = p * q

    factors = factors_func(n)
    phi_of_n = (factors[0]-1)*(factors[1]-1)
    d = modInverse(e,phi_of_n)

    if d == -1:
        return "d dosent exist"

    r_inverse = modInverse(r,n)

    if r_inverse == -1:
        return "r inverse dosent exist"

    block_size = (math.floor(math.log(n)/math.log(2))+1) // 8

    block_size = int(block_size)
    num_blocks =len(m) /  (block_size)
    num_blocks = int(num_blocks)

    arr = [m[i:i+block_size] for i in range(0,len(m),block_size)]


    cipher_arr = []
    for l in range(len(arr)):
        hexa_caoncat = ''
        for ll in arr[l]:
            val = ord(ll)
            hexa_caoncat += (hex(val).replace('0x',''))
        in_dec = int(hexa_caoncat,16)
        cipher_arr.append(in_dec)

    vapas_string = ''
    cipher_string = ''

    return_string = ''

    for k in range(len(arr)):
        hexa_caoncat = ''
        for j in arr[k]:
            ascii = ord(j)
            hexa_caoncat += (hex(ascii).replace('0x',''))
        in_dec = int(hexa_caoncat,16)

        sends_to_sign = (in_dec * (r ** e)) % n
        sends_signed = (sends_to_sign ** d) % n
        attacker_recieved = (sends_signed * r_inverse) % n

        attacker_recieved_in_hex = hex(attacker_recieved).replace('0x','')

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


        final_ans = ''
        for i in range(len(final_hex_arr)):
            in_int = int(final_hex_arr[i],16)
            in_chr = chr(in_int)
            final_ans += chr(int(final_hex_arr[i],16))
        
        checking = (attacker_recieved ** e) % n 
        text =  (attacker_recieved ** e) % n
        txt1 = hex(text)[2:]
        msg = bytes.fromhex(txt1).decode('utf-8')
    
        vapas_string += msg
        cipher_string += cch_join


        return_string += ("Block "+ str(arr[k]) + " Signature : " + str(attacker_recieved))
        return_string += '\n'

    return return_string


        

root = Tk()
root.title("DES Algorithm")
# root.geometry("400x350")


l1 = Label(root, text="Message")
l1.grid(row=0, column=0)

l2 = Label(root, text="KEY/N")
l2.grid(row=1, column=0)

l3 = Label(root, text="e ")
l3.grid(row=2, column=0)

l5 = Label(root, text="p ")
l5.grid(row=3, column=0)

l6 = Label(root, text="q ")
l6.grid(row=4, column=0)

l6 = Label(root, text="r ")
l6.grid(row=5, column=0)

l4 = Label(root, text="DES output")
l4.grid(row=6, column=0)

msg_text = StringVar()
e1 = Entry(root, textvariable=msg_text)
e1.grid(row=0, column=1)

key_text = StringVar()
e2 = Entry(root, textvariable=key_text)
e2.grid(row=1, column=1)

e_text = StringVar()
e3 = Entry(root, textvariable=e_text)
e3.grid(row=2, column=1)

p_text = StringVar()
e4 = Entry(root, textvariable=p_text)
e4.grid(row=3, column=1)

q_text = StringVar()
e5 = Entry(root, textvariable=q_text)
e5.grid(row=4, column=1)

r_text = StringVar()
e6 = Entry(root, textvariable=r_text)
e6.grid(row=5, column=1)


def getMsg():
    return str(msg_text.get())


def getKey():
    return str(key_text.get())


def getMsg_int():
    return int(msg_text.get())


def getKey_int():
    return int(key_text.get())


def getE_int():
    return int(e_text.get())

def getP_int():
    return int(p_text.get())

def getQ_int():
    return int(q_text.get())

def getR_int():
    return int(r_text.get())




list_box = Text(master=root, height=6, width=30)
list_box.grid(row=6, column=1, rowspan=6, columnspan=1)


sb1 = Scrollbar(root)
sb1.grid(row=4, column=2, rowspan=6)

list_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_box.yview)


def clear_text():
    e2.delete(0, 'end')
    e1.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    
    list_box.delete('1.0', END)

def clear_text_OUTPUT():
    list_box.delete('1.0', END)




def function2():

    message = getMsg()
    out_initial_permut = initial_permutation((message))

    input_key = getKey()

    keys = round_keys_generate(8, list(input_key))

    output_des_rounds = output_only_des(out_initial_permut, (keys))

    out_final_permut = final_permut(output_des_rounds[15])

    list_box.insert(END, out_final_permut)


def encrypt(pk, plaintext):
    key, n = pk
    cipher = ((plaintext) ** key) % n
    return cipher


def function3():

    message = int(getMsg_int())
    N = int(getKey_int())
    e = int(getE_int())
    # print(type(message),type(N),type(e))

    append_arr = []

    C1 = encrypt(((e), (N)), (message))
    while True:
        C2 = encrypt((e, N), C1)
        append_arr.append(C2)
        if C2 == message:
            break
        C1 = C2

    list_box.insert(END, append_arr[-2])


def function4():
    message = (getMsg())
    p = int(getP_int())
    q = int(getQ_int())
    r = int(getR_int())
    e = int(getE_int())

    answer = blind_signature_attack(p,q,message,e,r)
    list_box.insert(END, answer)

def function5():
    message = (getMsg())
    p = int(getP_int())
    q = int(getQ_int())
    r = int(getR_int())
    e = int(getE_int())

    answer = chosen_cipher_text(p,q,message,e,r)
    list_box.insert(END, answer)




b1 = Button(root, text="DES Encrypt", width=12, command=function2)
b1.grid(row=0, column=3)

b2 = Button(root, text="Cyclic", width=12, command=function3)
b2.grid(row=1, column=3)

b4 = Button(root, text="BSA", width=12, command=function4)
b4.grid(row=2, column=3)

b5 = Button(root, text="CSA", width=12, command=function5)
b5.grid(row=3, column=3)

b3 = Button(root, text="Clear", width=12, command=clear_text)
b3.grid(row=5, column=3)
b6 = Button(root, text="Clear Answer", width=12, command=clear_text_OUTPUT)
b6.grid(row=6, column=3)




root.mainloop()
