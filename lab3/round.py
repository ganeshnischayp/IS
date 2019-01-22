IP_out = '1111111101110100001001011011101000000000111111110000101101011001'

file = open("round_keys.txt", "r")
round_keys = file.readlines()


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


def convert_to_single_bits(arr):
    split_list = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            split_list.append(arr[i][j])
    return split_list


def join_single_bits(arr):
    string = ''
    for i in range(len(arr)):
        string += arr[i]
    return string


def convert_to_6_bit(var):
    bit_6_join = []
    for i in range(48):
        if i % 6 == 0:
            bit_6_join.append(xor_out[i:i+6])
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
    round_output = last_right_join + xor_out_with_left32
    IP_out = round_output
    print(round_output)
