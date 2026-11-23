import tkinter as tk

c = tk.Tk()
c.title("원 관련 계산")
c.geometry("500x400")

def find_area():
    if label03['text'] == "0":
        if entry01.get() != "":
            r = float(entry01.get())
            area = round(r * r * 3.14, 2)
            label03.config(text=str(area))
            button01.config(text="초기화")
    else:
        entry01.delete(0, tk.END)
        label03.config(text="0")
        button01.config(text="계산하기")


label01 = tk.Label(c, text="원의 면적 계산")
label01.pack()

label02 = tk.Label(c, text="반지름 입력")
label02.pack()

entry01 = tk.Entry(c, width=5)
entry01.pack()

button01 = tk.Button(c, text="계산하기", command=find_area)
button01.pack()

label03 = tk.Label(c, text="0")
label03.pack()



c.mainloop()
