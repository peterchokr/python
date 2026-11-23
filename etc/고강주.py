import tkinter as tk


def bas():
    r = float(entry.get())
    area = (3.14 * (r * r))
    label103.config(text=(area))
    button.config(text="초기화", command=asd)


def asd():
    entry.delete(0, tk.END)
    label103.config(text="0")
    button.config(text="계산하기", command=bas)



c = tk.Tk()
c.title("환전")
c.geometry("500x400")

label102 = tk.Label(c, text="돈 계산", font=("맑은 고딕", 15))
label102.pack(pady=10)

label101 = tk.Label(c, text="돈을 입력하세요")
label101.pack(pady=5)

entry = tk.Entry(c, width=10)
entry.pack(pady=5)

button = tk.Button(c, text="계산하기", command=bas)
button.pack(pady=10)

label103 = tk.Label(c, text="0", font=("맑은 고딕", 12))
label103.pack(pady=10)


c.mainloop()
