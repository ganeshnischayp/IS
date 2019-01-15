INI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FIN = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

text= "NITK"

def permut(block, table):
    return [block[x-1] for x in table]

newtext = text.replace(' ','')
if len(newtext) > 8:
    str_array = [newtext[i:i+8] for i in range(0, len(newtext), 8)]
else:
    str_array = [newtext]

byte_array = []
for string in str_array:
    byte_array.append('0'+'0'.join(format(ord(x), 'b') for x in string))

if len(byte_array[-1]) < 64:
    padding = ''.join('0' for _ in range(64 - len(byte_array[-1])))
    byte_array[-1] = byte_array[-1] + padding

print(byte_array)

encoded_string = []
for block in byte_array:
    encoded_array = permut(block, INI)
    encoded_string.append(''.join(x for x in encoded_array))

print(encoded_string)

enc_str = ''
for block in encoded_string:
    block_parts = [block[i:i+8] for i in range(0, len(block), 8)]
    for character in block_parts:
        enc_str = enc_str + chr(int(character, 2))

print(enc_str)

decoded_string = []
for block in encoded_string:
    decoded_array = permut(block, FIN)
    decoded_string.append(''.join(x for x in decoded_array))

print(decoded_string)

final_str = ''
for block in decoded_string:
    block_parts = [block[i:i+8] for i in range(0, len(block), 8)]
    for character in block_parts:
        final_str = final_str + chr(int(character, 2))

print(final_str)