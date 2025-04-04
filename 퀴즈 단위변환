from tkinter import *
root = Tk()
root.geometry("600x400")

def change() :
    if var1.get() == 1:
        l1["text"] = f"{float(e1.get()) * 1000}g"
    if var2.get() == 1:
        l1["text"] = f"{float(e1.get()) * 2.204623}lb"

Label(root, text="단위변환").pack()

f1 = Frame(root)
Label(f1, text="입력").pack(side="left")
e1 = Entry(f1)
e1.pack(side="left")
Label(f1, text="kg").pack(side="left")

f1.pack()

var1 = IntVar()
var2 = IntVar()

f2 = Frame(root)
c1 = Checkbutton(f2, text="그램", variable=var1, command=change)
c1.pack(side="left")
c2 = Checkbutton(f2, text="파운드", variable=var2, command=change)
c2.pack(side="left")

f2.pack()

l1 = Label(root, text="원하는 단위를 선택하세요")
l1.pack()

root.mainloop()
