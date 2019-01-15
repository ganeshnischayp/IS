import math    
import binascii
import sys
import copy



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
print("After Final Permutation = ",text_from_bits(full_text),end= "")
print("\n")





