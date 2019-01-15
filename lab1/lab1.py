import math    
import binascii
import copy
num = input("Input = ")
IPtable = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

text_split =list(num)
num_blocks = math.ceil(len(text_split)/8)
text_block = [[]for i in range(num_blocks)]
for i in range(num_blocks+1):
    for j in range(8):
        if len(text_split) > 0:
            text_block[i].append(text_split.pop(0))
        else:
            break

samp = text_block.copy()

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

for i in range(len(text_block)):
    for j in range(len(text_block[i])):
        samp[i][j] = text_to_bits(text_block[i][j])

print("Bits of each characters in input - ",samp)

def concat_bits(s):
    bits = ''
    for i in range(len(s)):
        bits += s[i]
    return (bits).ljust(64,'0')

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
# print(final_code)

full_final = ''
for i in range(len(final_code)):
    join_final = ''
    for j in range(len(final_code[i])):
        join_final += final_code[i][j]
    full_final += join_final

print("After Initial Permutation = ",full_final)
#####################################################################33

num1 = full_final
FPtable = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41,  9, 49, 17, 57, 25]

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
print("After Final Permutation Bits = ",full_final)
print("After Final Permutation Text = ",text_from_bits(full_text),"\n",end= "")