import tkinter as tk

def calculate_or_clear():
    if button01["text"] == "계산하기":
        radius = float(entry01.get())
        area = 3.14159 * radius ** 2
        label03.config(text=f"결과 : {area:.2f}")
        button01.config(text="초기화")
    else:
        entry01.delete(0, tk.END)
        label03.config(text="결과")
        button01.config(text="계산하기")

c = tk.Tk()
c.title("원관련 계산기")
c.geometry("500x400")

label01 = tk.Label(c, text="원의 면적 계산", font=("맑은 고딕", 20), fg="blue", bg="yellow")
label01.pack()

label02 = tk.Label(c, text="반지름을 입력하세요", font=("맑은 고딕", 16), fg="black", bg="lightgray")
label02.pack()

entry01 = tk.Entry(c, font=("맑은 고딕", 16), width=5)
entry01.pack()

button01 = tk.Button(c, text="계산하기", font=("맑은 고딕", 16), command=calculate_or_clear)
button01.pack()

label03 = tk.Label(c, text="결과", font=("맑은 고딕", 16))
label03.pack()

c.mainloop()
