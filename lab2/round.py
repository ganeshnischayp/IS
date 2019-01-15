import copy

imp = input("Enter key to generate: ")
imp_list = list(imp)
to_extract = 8

permut_choice_1 = [57, 49, 41, 33, 25, 17, 9,
                        1, 58, 50, 42, 34, 26, 18,
                         10, 2, 59, 51, 43, 35, 27,
                         19, 11, 3, 60, 52, 44, 36,
                         63, 55, 47, 39, 31, 23, 15,
                         7, 62, 54, 46, 38, 30, 22,
                         14, 6, 61, 53, 45, 37, 29,
                         21, 13, 5, 28, 20, 12, 4 ]

permut_choice_2 = [          14, 17, 11, 24, 1, 5,
                             3, 28, 15, 6, 21, 10,
                             23, 19, 12,  4, 26, 8,
                             16, 7, 27, 20, 13, 2,
                             41, 52, 31, 37, 47, 55,
                             30, 40, 51, 45, 33, 48,
                             44, 49, 39, 56, 34, 53,
                             46, 42, 50, 36, 29, 32 ]
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def join_single_bits(arr):
    string = ''
    for i in range(len(arr)):
        string += arr[i]
    return string

def one_bit_shift(var):
    var1 = list(var)
    for i in range(len(var1)):
        if i == len(var1)-1:
            break
        var1[i] = var1[i+1]
    var1[len(var1)-1] = '0'
    return join_single_bits(var1)

def two_bit_shift(var):
    var1 = list(var)
    for i in range(len(var1)):
        if i == len(var1)-1:
            break
        var1[i] = var1[i+1]
    var1[len(var1)-1] = '0'
    for i in range(len(var1)):
        if i == len(var1)-1:
            break
        var1[i] = var1[i+1]
    var1[len(var1)-1] = '0'
    return join_single_bits(var1)


def convert_to_single_bits(arr):
    split_list = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            split_list.append(arr[i][j])
    # k = 0
    # for i in range(len(split_list)):
    #     if(i%8) == 0:
    #         split_list.pop(i-k)
    #         # print(i)
    #         k = k + 1

    return split_list




if len(imp_list) >= to_extract:
    choice = input("1. Left bits \n2. Right bit selection ")
    if choice == '1':
        inp_8_char = imp_list[:to_extract]
        # print(inp_8_char)
        for i in range(len(inp_8_char)):
            inp_8_char[i] = text_to_bits(inp_8_char[i])
        # print(inp_8_char)
        bit_64_arr = convert_to_single_bits(inp_8_char)
        # print(bit_64_arr)


        for i in range(len(bit_64_arr)):
            if ((i+1)%8) == 0:
                continue
            else:
                bit_64_arr[permut_choice_1.index(i+1)] = bit_64_arr[i]
        
        k = 0
        for i in range(len(bit_64_arr)):
            if(i%8) == 0:
                bit_64_arr.pop(i-k)
                # print(i)
                k = k + 1
        # print(len(bit_64_arr))


            
        # for i in range(16):
        left_half = bit_64_arr[:28]
        right_half = bit_64_arr[28:]

        # if i == 1 and i == 2 and i == 9 and i == 16:
        left_half = join_single_bits(left_half)
        left_half1 = one_bit_shift(left_half)

        right_half = join_single_bits(right_half)
        right_half1 = one_bit_shift(right_half)

        left_half1 = convert_to_single_bits(left_half1)
        right_half1 = convert_to_single_bits(right_half1)

        key = right_half1 + right_half1
        key1 = key.copy()
        # print(key1)


        for i in range(len(key1)):
            if i == 8 or i == 17 or i == 21 or i == 24 or i == 34 or i == 37 or i == 42 or i == 53:
                continue
            else:
                key1[permut_choice_2.index(i+1)] = key1[i]
        # print(key1)

        kk = 0
        for i in range(len(key1)):
            if i == 8 or i == 17 or i == 21 or i == 24 or i == 34 or i == 37 or i == 42 or i == 53:
                key1.pop(i-k)
                # print(i)
                k = k + 1
        # print(join_single_bits(key1))






        # else:
        #     pass















    else:
        inp_8_char = imp_list[-7:]
        print(inp_8_char)





    
else:
    print("Enter key of bigger length") 
    exit
# print(len(imp_list))