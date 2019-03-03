def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

plaintext = input("Enter Cipher text: ")
# N = int(input("Enter N: "))
# public_key = int(input("Enter public key: "))

plaintext_ord = [ord(i) for i in plaintext]
print(plaintext_ord)

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [((char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


text1 = []
append_arr = [plaintext_ord]

text1 = encrypt((3,143),plaintext_ord)
append_arr.append(text1)

GPN = append_arr[0]

while True:

    text2 = encrypt((3,143),GPN)

    append_arr.append(text2)

    if text2 == append_arr[0]:
        break
    GPN = text2
    
# print(append_arr)
for i in append_arr:
    for j in range(len(i)):
        print(chr(i[j]),end= '')
    print('\n')


# plaintext_real = (append_arr[len(append_arr)-1])
# print("Plain text is: ")
# for i in range(len(plaintext_real)):
#     print(chr(plaintext_real[i]),end= '')


# print('\n')
# print("Checking: ")
# checking = encrypt((3,143),plaintext_real)
# for i in checking:
#     print(chr(i),end= '')
# print('\n')