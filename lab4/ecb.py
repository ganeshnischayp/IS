import P1,P2,P3
import math

input_text = input("Enter text for ecb : ")
input_key = input("Enter key for ecb : ")
keys = P2.round_keys_generate(8,list(input_key))

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
# print(*keys)
# input_text = list(input_text)

if len(input_text) >= 8 and len(input_text) <= 40:
    num_blocks = math.ceil(len(input_text)/8)
    text_blocks = []
    for i in range(num_blocks):
        n = i*8
        text_blocks.append(input_text[n:n+8].ljust(8," "))

    for i in range(len(text_blocks)):
        out_initial_permut = P1.initial_permutation(text_blocks[i])
        # print(out_initial_permut)
        output_des_rounds = P3.output_only_des(out_initial_permut,keys)
        # print(output_des_rounds)
        print("block ",i+1)
        for k in range(len(output_des_rounds)-1):
            print(output_des_rounds[k])
        out_final_permut = P1.final_permut(output_des_rounds[15])
        print((out_final_permut))
        print('\n\n\n')


else:
    exit