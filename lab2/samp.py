def convert_to_single_bits(arr):
    split_list = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            split_list.append(arr[i][j])
    k = 0
    for i in range(len(split_list)):
        if(i%8) == 0:
            split_list.pop(i-k)
            print(i)
            k = k + 1

    return split_list

def join_single_bits(arr):
    string = ''
    for i in range(len(arr)):
        string += arr[i]
    return string

def one_bit_shift(var):
    var1 = int(var)
    va1 = var1 << 1
    var1 = str(var1)
    return var1.zfill(28)


gpn = 2
sg = 1
for i in range(5):
    aa = gpn
    bb = sg
    gpn = gpn + 2
    sg = gpn + 2
    print(gpn,sg)
    gpn = 0
    sg = 0

arr = ['0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0']
# print(join_single_bits(arr))/
# for i in range(len(convert_to_single_bits(arr))):