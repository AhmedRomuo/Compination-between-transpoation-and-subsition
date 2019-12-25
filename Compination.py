from tkinter import *

x_window = Tk()
output_text = StringVar()
check_space = IntVar()
txt_plain_text = Entry(x_window, width=35, font=10)


ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
matrix = [[0] * 5 for i in range(5)]


def make_matrix():
    x = 0

    for row in range(5):
        for column in range(5):
            if x == 25:
                break
            else:
                matrix[row][column] = ls[x]
                x += 1

    print(matrix)


def encryption(plain_txt):
    temp_txt = ""

    for item in range(len(plain_txt)):
        if plain_txt[item] != ' ':
            for row in range(5):
                for column in range(5):
                    if plain_txt[item] == matrix[row][column]:
                        temp_txt += ls[row] + ls[column]
                    elif plain_txt[item] == 'z':
                        temp_txt += 'db'

    # print test
    print(temp_txt, len(temp_txt))

    temp_txt_left = ""
    temp_txt_right = ""
    for item in range(len(temp_txt)):
        if item >= int(len(temp_txt) / 2):
            temp_txt_right += temp_txt[item]
        else:
            temp_txt_left += temp_txt[item]

    # print test
    print(temp_txt_left, len(temp_txt_left))
    print(temp_txt_right, len(temp_txt_right))

    temp_txt = ""
    for item in range(len(temp_txt_right)):
        temp_txt += matrix[ls.index(temp_txt_left[item])][ls.index(temp_txt_right[item])]

    print(temp_txt, len(temp_txt))
    output_text.set("Cipher text : " + temp_txt)


def decryption(cipher_txt):
    temp_txt = ""

    temp_txt_left = ""
    temp_txt_right = ""

    for item in range(len(cipher_txt)):
        for row in range(5):
            for column in range(5):
                if cipher_txt[item] == matrix[row][column]:
                    temp_txt_left += ls[row]
                    temp_txt_right += ls[column]
                elif cipher_txt[item] == 'z':
                    temp_txt_left += 'd'
                    temp_txt_right += 'b'

    temp_txt = temp_txt_left + temp_txt_right
    # print test
    print(temp_txt, len(temp_txt))

    plain_text = ""
    item = 0
    while item < len(temp_txt):
        plain_text += matrix[ls.index(temp_txt[item])][ls.index(temp_txt[item + 1])]
        item += 2

    print(plain_text)
    output_text.set("Cipher text : " + plain_text)


def click_btn1():
    encryption(str(txt_plain_text.get()).lower())


def click_btn2():
    decryption(str(txt_plain_text.get()).lower())


def main():
    make_matrix()

    # frame window
    x_window.configure(background="black")
    x_window.title("Combination transposition & substitution ")
    x_window.geometry("500x300")

    # labels
    lbl_txt1 = Label(x_window, text="Text : ", padx=5, pady=5, bg="black", fg="white")
    lbl_txt2 = Label(x_window, textvariable=output_text, padx=5, pady=5, font=10, bg="black", fg="white")
    lbl_txt1.place(x=10, y=10)

    # text
    txt_plain_text.focus()
    txt_plain_text.place(x=60, y=15)

    # Button and check button
    btn_encrypt = Button(x_window, text="Encrypt", padx=5, pady=5, command=click_btn1, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")
    btn_decrypt = Button(x_window, text="Decrypt", padx=5, pady=5, command=click_btn2, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")

    btn_encrypt.place(x=100, y=110)
    btn_decrypt.place(x=250, y=110)

    lbl_txt2.place(x=60, y=160)
    x_window.mainloop()


if __name__ == '__main__':main()