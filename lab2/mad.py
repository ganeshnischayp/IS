def ascii_to_binary(asci_num):
	asci_bits = []
	rem = 0
	while(asci_num > 0):
		rem = asci_num % 2
		asci_bits.append(rem)
		asci_num = asci_num // 2
	asci_bits = list(reversed(asci_bits))
	asci_length = len(asci_bits)
	asci_length2 = 8 - asci_length
	if asci_length == 0:
		return asci_bits
	else:
		i = 0
		for i in range(asci_length2):
			asci_bits.insert(0,0)
		return asci_bits
def get_ascii(operation_text):
	ascii_array = []
	for i in range(len(operation_text)):
		ascii_array.append(ord(operation_text[i]))
	return ascii_array
def left_rotate_one_bit(bits_rotate_array):
	bits_rotate_array.append(bits_rotate_array.pop(0))
	return bits_rotate_array
def left_rotate_two_bits(bits_rotate_array):
	bits_rotate_array.append(bits_rotate_array.pop(0))
	bits_rotate_array.append(bits_rotate_array.pop(0))
	return bits_rotate_array
operation_text = ''
plain_key = input("Enter the Key:")
plain_key = plain_key.replace(" ","")
if len(plain_key) < 8:
	print("Please enter more than 8 characters")
else:
	print("Enter:-")
	print("1 - This is for choosing first 8 characters")
	print("2 - This is for choosing last 8 characters")	
	choice = int(input("Enter choice:"))
	if choice != 1 and choice != 2:
		print("Please enter 1 or 2")
	else:
		if choice == 1:
			operation_text = plain_key[:8]
		if choice == 2:
			operation_text = plain_key[-8:]
		ascii_values = []
		bits = []
		ascii_values = get_ascii(operation_text)	
		pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]		
		for i in range(len(ascii_values)):
			bits.append(ascii_to_binary(ascii_values[i]))
		bits_array = []
		i = 0
		j = 0
		for i in range(len(bits)):
			for j in range(len(bits[i])):
				bits_array.append(bits[i][j])
		#print(*bits_array,sep="")
		pc1_array = []
		for i in range(len(pc1)):
			pc1_array.append(bits_array[pc1[i]-1])
		#print(*pc1_array,sep=" ")
		pc2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
		i = 0
		pc1_first_half = []
		pc1_second_half = []
		pc1_first_half = pc1_array[:28]
		pc1_second_half = pc1_array[28:]
		#print(pc1_second_half)
		print()
		with open('result.txt', 'a') as f:
			f.write(plain_key+"\n")
			f.write("choice:"+str(choice)+"\n")
			for i in range(16):
				if i == 0 or i == 1 or i == 8 or i == 15:
					pc1_first_half = left_rotate_one_bit(pc1_first_half)
					pc1_second_half = left_rotate_one_bit(pc1_second_half)
				else:
					pc1_first_half = left_rotate_two_bits(pc1_first_half)
					pc1_second_half = left_rotate_two_bits(pc1_second_half)
				#print(*pc1_second_half,sep="")
				key = []
				key = pc1_first_half + pc1_second_half
				round_key = []
				l = 0
				for l in range(len(pc2)):
					round_key.append(key[pc2[l]-1])
				print(" Round",i+1,":- ",*round_key,sep="")
				for item in round_key:
					f.write(str(item))
				f.write("\n")
			f.write("\n")	
			f.close()