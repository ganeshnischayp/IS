cipher_text = input("Enter the cipher text:")
i = 0
ans = []
got = True
N = int(input("Enter N value:"))
e = int(input("Enter e value:"))
original_cipher_value = 0
cipher_ans = 0
cipher_value_power = 0
for i in range(len(cipher_text)):
    cipher_value = int(ord(cipher_text[i]))
    original_cipher_value = cipher_value
    while got:
        cipher_value_power = cipher_value ** e
        cipher_ans = cipher_value_power % N
        if cipher_ans == original_cipher_value:
            ans.append(chr(cipher_value))
            print(ans)
            break
        else:
            cipher_value = cipher_ans    
    print("hi")        
print(ans)