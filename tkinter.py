from tkinter import *
root = Tk()  # 윈도우를 생성
root.geometry("600x600")

def test() :
    msg = ""
    total = 0
    if e2.get() != "" :
        msg = msg + "아메리카노 "  + e2.get() + "잔"
        total = total + (1000 * int(e2.get()))
    if e3.get() != "" :
        msg = msg + "라떼 "  + e3.get() + "잔"
        total = total + (2000 * int(e3.get()))
    if e4.get() != "" :
        msg = msg + "맥주 "  + e4.get() + "잔"
        total = total + (3000 * int(e4.get()))
    l2["text"] = "주문한 메뉴 : " +  msg + ", 총 금액 : " + str(total)

l1 = Label(root, text="심심카페")
l1.pack()

f1 = Frame(root)
l2 = Label(f1, text="아메리카노(1000원)  ")
l2.pack(side=LEFT)
e2 = Entry(f1)
e2.pack(side=LEFT)
f1.pack()

f2 = Frame(root)
l3 = Label(f2, text="라떼(2000원)  ")
l3.pack(side=LEFT)
e3 = Entry(f2)
e3.pack(side=LEFT)
f2.pack()

f3 = Frame(root)
l4 = Label(f3, text="맥주(3000원)  ")
l4.pack(side=LEFT)
e4 = Entry(f3)
e4.pack(side=LEFT)
f3.pack()

b1 = Button(root, text="주문하기", command=test)
b1.pack()

l2 = Label(root, text="메뉴를 선택하세요")
l2.pack()



root.mainloop()
