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


arr1 = '1111111100000100001111111001011000000000000000001110000100000101'
arr = ['0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0']
print(arr1)
print(two_bit_shift(arr1))
# for i in range(len(convert_to_single_bits(arr))):