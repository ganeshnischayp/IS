# command to build .exe
# gpn@gpnpc:~/Documents/6th-Sem/IS/lab6$ pyinstaller --onefile tinker.py

from tkinter import *
import P1
import P2
import P3
import math

root = Tk()
root.title("DES Algorithm")
# root.geometry("400x350")


l1 = Label(root, text="Message")
l1.grid(row=0, column=0)

l2 = Label(root, text="KEY/N")
l2.grid(row=1, column=0)

l3 = Label(root, text="e ")
l3.grid(row=2, column=0)

l4 = Label(root, text="DES output")
l4.grid(row=3, column=0)

msg_text = StringVar()
e1 = Entry(root, textvariable=msg_text)
e1.grid(row=0, column=1)

key_text = StringVar()
e2 = Entry(root, textvariable=key_text)
e2.grid(row=1, column=1)

e_text = StringVar()
e3 = Entry(root, textvariable=e_text)
e3.grid(row=2, column=1)


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

list_box = Text(master=root, height=6, width=30)
list_box.grid(row=3, column=1, rowspan=6, columnspan=1)


sb1 = Scrollbar(root)
sb1.grid(row=3, column=2, rowspan=6)

list_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_box.yview)


def clear_text():
    e2.delete(0, 'end')
    e1.delete(0, 'end')
    e3.delete(0, 'end')
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

    C1 = encrypt(((e),(N)),(message))
    while True:
        C2 = encrypt((e,N),C1)
        append_arr.append(C2)
        if C2 == message:
            break
        C1 = C2
    # print(append_arr)
    # print("The plain text is: ",append_arr[-2])
    list_box.insert(END, append_arr[-2])



b1 = Button(root, text="DES Encrypt", width=12, command=function2)
b1.grid(row=0, column=3)

b2 = Button(root, text="Cyclic", width=12,command=function3)
b2.grid(row=1, column=3)

b3 = Button(root, text="Clear", width=12, command=clear_text)
b3.grid(row=3, column=3)


root.mainloop()
