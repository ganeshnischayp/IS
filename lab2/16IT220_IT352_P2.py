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
                   21, 13, 5, 28, 20, 12, 4]

permut_choice_2 = [14, 17, 11, 24, 1, 5,
                   3, 28, 15, 6, 21, 10,
                   23, 19, 12,  4, 26, 8,
                   16, 7, 27, 20, 13, 2,
                   41, 52, 31, 37, 47, 55,
                   30, 40, 51, 45, 33, 48,
                   44, 49, 39, 56, 34, 53,
                   46, 42, 50, 36, 29, 32]

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


if len(imp_list) >= to_extract:
    choice = input("1. Left bits \n2. Right bit selection ")
    if choice == '1':
        inp_8_char = imp_list[:to_extract]
        for i in range(len(inp_8_char)):
            inp_8_char[i] = text_to_bits(inp_8_char[i])
        bit_64_arr = convert_to_single_bits(inp_8_char)
        bit_56_arr = []
        for i in range(56):
            bit_56_arr.append(bit_64_arr[permut_choice_1[i]-1])
        left_half = bit_56_arr[:28]
        right_half = bit_56_arr[28:]

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
                print(l+1,join_single_bits(key1))
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

                print(l+1,join_single_bits(key1))
                left_half = convert_to_single_bits(left_half1)
                right_half = convert_to_single_bits(right_half1)
    else:
        inp_8_char = imp_list[-to_extract:]
        for i in range(len(inp_8_char)):
            inp_8_char[i] = text_to_bits(inp_8_char[i])
        bit_64_arr = convert_to_single_bits(inp_8_char)
        bit_56_arr = []
        for i in range(56):
            bit_56_arr.append(bit_64_arr[permut_choice_1[i]-1])

        left_half = bit_56_arr[:28]
        right_half = bit_56_arr[28:]

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
                print(l+1,join_single_bits(key1))
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

                print(l+1,join_single_bits(key1))
                left_half = convert_to_single_bits(left_half1)
                right_half = convert_to_single_bits(right_half1)

else:
    print("Enter key of bigger length")
    exit