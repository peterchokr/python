from tkinter import *
r = 0
e = ""

root = Tk()
root.title("My Calculator")
display = Entry(root, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7',  '8',  '9',  '/',  'C',
'4',  '5',  '6',  '*',  '<-',
'1',  '2',  '3',  '-',  'R',
'0',  '.',  '=',  '+',  ' ' ]

def click(key):
    global r
    global e
    if   key == "=":
        result = eval(display.get())
        r = result
        e = display.get()
        s = str(result)
        display.insert(END, "=" + s)
    elif key == "C":
        display.delete(0, END)
    elif key == "<-" :
        display.delete(len(display.get())-1, END)
    elif key == "R" :
        display.delete(0, END)
        display.insert(0, e + "=" + str(round(r, 2)))
    else :
        display.insert(END, key)

row_index = 1
col_index = 0
for button_text in button_list:
    Button(root, text=button_text, width=5, command=lambda t=button_text: click(t)).grid(row=row_index, column=col_index)
    col_index += 1
    if   col_index > 4:
        row_index += 1
        col_index = 0
root.mainloop()
