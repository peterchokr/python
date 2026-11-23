import tkinter as tk
import math

c = tk.Tk()
c.title("원 계산")
c.geometry("500x400")
c.configure(bg="#39c5bb")
#---------------------------------
def calc():
    try:
        r = float(entry01.get())
        label03.config(text=f"면적 : {math.pi * r ** 2:.2f}")
        button01.config(text="지우기", command=clear)
    except ValueError:
        label03.config(text="숫자를 입력하세요")
#---------------------------------
def clear():
    entry01.delete(0, tk.END)
    label03.config(text="0")
    button01.config(text="계산", command=calc)
#---------------------------------
label01 = tk.Label(
    c,
    text="원의 면적계산",
    font=("맑은 고딕", 28, "bold"),
    fg="black",
    bg="#39c5bb"
)
label01.pack(pady=(40, 20))
#---------------------------------
label02 = tk.Label(
    c,
    text="반지름 입력",
    font=("맑은 고딕", 16),
    fg="black",
    bg="#39c5bb"
)
label02.pack(pady=5)
#---------------------------------
entry01 = tk.Entry(
    c,
    width=10,
    font=("맑은 고딕", 16),
    justify="center"
)
entry01.pack(pady=5)
#---------------------------------
button01 = tk.Button(
    c,
    text="계산",
    font=("맑은 고딕", 16),
    fg="#39c5bb",
    bg="white",
    width=8,
    command=calc
)
button01.pack(pady=15)
#---------------------------------
label03 = tk.Label(
    c,
    text="0",
    font=("맑은 고딕", 16),
    fg="black",
    bg="#39c5bb"
)
label03.pack(pady=5)
#---------------------------------
c.mainloop()
