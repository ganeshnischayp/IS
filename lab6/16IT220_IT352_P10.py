# command to build .exe
# gpn@gpnpc:~/Documents/6th-Sem/IS/lab6$ pyinstaller --onefile tinker.py

from tkinter import *
import math
import P1
import P2
import P3
import P4
import P5
import binascii
import copy
       

root = Tk()
root.title("GUI IS")
# root.geometry("500x800")
#16IT220_IT352_P10_S1

l1 = Label(root, text="Message")
l1.grid(row=0, column=0)

l2 = Label(root, text="KEY/N")
l2.grid(row=1, column=0)

l3 = Label(root, text="e ")
l3.grid(row=2, column=0)

l5 = Label(root, text="p ")
l5.grid(row=3, column=0)

l6 = Label(root, text="q ")
l6.grid(row=4, column=0)

l6 = Label(root, text="r ")
l6.grid(row=5, column=0)

l4 = Label(root, text="Output")
l4.grid(row=6, column=0)

msg_text = StringVar()
e1 = Entry(root, textvariable=msg_text)
e1.grid(row=0, column=1)

key_text = StringVar()
e2 = Entry(root, textvariable=key_text)
e2.grid(row=1, column=1)

e_text = StringVar()
e3 = Entry(root, textvariable=e_text)
e3.grid(row=2, column=1)

p_text = StringVar()
e4 = Entry(root, textvariable=p_text)
e4.grid(row=3, column=1)

q_text = StringVar()
e5 = Entry(root, textvariable=q_text)
e5.grid(row=4, column=1)

r_text = StringVar()
e6 = Entry(root, textvariable=r_text)
e6.grid(row=5, column=1)


def getMsg():
    return str(msg_text.get())


def getKey():
    return str(key_text.get())


def getMsg_int():
    return int(msg_text.get())


def getKey_int():
    return int(key_text.get())


def getE_int():
    return int(e_text.get())

def getP_int():
    return int(p_text.get())

def getQ_int():
    return int(q_text.get())

def getR_int():
    return int(r_text.get())




list_box = Text(master=root, height=6, width=30)
list_box.grid(row=6, column=1, rowspan=6, columnspan=1)


sb1 = Scrollbar(root)
sb1.grid(row=4, column=2, rowspan=6)

list_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_box.yview)


def clear_text():
    e2.delete(0, 'end')
    e1.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    
    list_box.delete('1.0', END)

def clear_text_OUTPUT():
    list_box.delete('1.0', END)




def function2():

    message = getMsg()
    out_initial_permut = P1.initial_permutation((message))

    input_key = getKey()

    keys = P2.round_keys_generate(8, list(input_key))

    output_des_rounds = P3.output_only_des(out_initial_permut, (keys))

    out_final_permut = P1.final_permut(output_des_rounds[15])

    list_box.insert(END, out_final_permut)


def encrypt(pk, plaintext):
    key, n = pk
    cipher = ((plaintext) ** key) % n
    return cipher


def function3():

    message = int(getMsg_int())
    N = int(getKey_int())
    e = int(getE_int())
    # print(type(message),type(N),type(e))

    append_arr = []

    C1 = encrypt(((e), (N)), (message))
    while True:
        C2 = encrypt((e, N), C1)
        append_arr.append(C2)
        if C2 == message:
            break
        C1 = C2

    list_box.insert(END, append_arr[-2])


def function4():
    message = (getMsg())
    p = int(getP_int())
    q = int(getQ_int())
    r = int(getR_int())
    e = int(getE_int())

    answer = P4.blind_signature_attack(p,q,message,e,r)
    list_box.insert(END, answer)

def function5():
    message = (getMsg())
    p = int(getP_int())
    q = int(getQ_int())
    r = int(getR_int())
    e = int(getE_int())

    answer = P5.chosen_cipher_text(p,q,message,e,r)
    list_box.insert(END, answer)




b1 = Button(root, text="DES Encrypt", width=12, command=function2)
b1.grid(row=0, column=3)

b2 = Button(root, text="Cyclic", width=12, command=function3)
b2.grid(row=1, column=3)

b4 = Button(root, text="BSA", width=12, command=function4)
b4.grid(row=2, column=3)

b5 = Button(root, text="CSA", width=12, command=function5)
b5.grid(row=3, column=3)

b3 = Button(root, text="Clear", width=12, command=clear_text)
b3.grid(row=5, column=3)
b6 = Button(root, text="Clear Answer", width=12, command=clear_text_OUTPUT)
b6.grid(row=6, column=3)




root.mainloop()
