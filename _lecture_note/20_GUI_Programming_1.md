# 20장 GUI 프로그래밍 1 (tkinter 기초)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 tkinter를 사용하여 윈도우 프로그램을 만들 수 있습니다. 버튼, 텍스트 상자, 레이블 등을 배치하고, 클릭 이벤트를 처리하여 사용자와 상호작용하는 GUI 애플리케이션을 제작할 수 있습니다.

---

## 1️⃣ **GUI란 무엇인가?**

지금까지 우리는 터미널(검은 화면)에서 텍스트로만 프로그램을 만들었습니다. 하지만 우리가 일상적으로 사용하는 프로그램들은 어떤가요? 버튼, 메뉴, 텍스트 상자가 있는 윈도우 프로그램입니다!

### **CLI vs GUI**

```
CLI (Command Line Interface)     GUI (Graphical User Interface)
터미널, 명령어 입력               윈도우, 마우스 클릭

┌─────────────────────┐         ┌─────────────────────┐
│ $ python calc.py    │         │  계산기        [_][□][X]│
│ 숫자1: 10          │         ├─────────────────────┤
│ 숫자2: 20          │         │                     │
│ 결과: 30           │         │  결과: 30           │
│                     │         │                     │
│                     │         │  [7][8][9][+]      │
│                     │         │  [4][5][6][-]      │
│                     │         │  [1][2][3][×]      │
└─────────────────────┘         └─────────────────────┘
```

**GUI의 장점:**

- ✅ 직관적이고 사용하기 쉬움
- ✅ 마우스로 클릭만 하면 됨
- ✅ 시각적으로 보기 좋음
- ✅ 일반 사용자도 쉽게 사용 가능

### **tkinter란?**

**tkinter**는 파이썬에 기본으로 포함된 GUI 라이브러리입니다. 별도 설치 없이 바로 사용할 수 있습니다!

```python
import tkinter  # 이미 설치되어 있음!
```

---

## 2️⃣ **첫 번째 윈도우 만들기**

가장 간단한 윈도우부터 만들어봅시다.

### **기본 윈도우**

```python
import tkinter as tk

# 윈도우 생성
window = tk.Tk()
window.title("내 첫 프로그램")  # 제목 설정
window.geometry("400x300")      # 크기 설정 (가로x세로)

# 윈도우 실행 (이 줄이 있어야 창이 뜸!)
window.mainloop()
```

**실행하면:**

- 가로 400픽셀, 세로 300픽셀 크기의 윈도우가 나타남
- 제목 표시줄에 "내 첫 프로그램"이 표시됨

### **코드 설명**

```python
import tkinter as tk          # tkinter를 tk라는 짧은 이름으로

window = tk.Tk()              # 윈도우 생성
window.title("제목")          # 윈도우 제목
window.geometry("가로x세로")   # 윈도우 크기

window.mainloop()             # 윈도우 실행 (항상 마지막!)
```

💡 **중요**: `mainloop()`는 항상 코드의 **마지막**에 있어야 합니다!

---

## 3️⃣ **Label - 텍스트 표시하기**

윈도우에 글자를 표시하려면 Label을 사용합니다.

### **기본 Label**

```python
import tkinter as tk

window = tk.Tk()
window.title("Label 예제")
window.geometry("400x300")

# Label 생성
label = tk.Label(window, text="안녕하세요!")
label.pack()  # 화면에 배치

window.mainloop()
```

### **Label 꾸미기**

```python
import tkinter as tk

window = tk.Tk()
window.title("예쁜 Label")
window.geometry("400x300")

# 다양한 옵션
label1 = tk.Label(
    window,
    text="큰 글씨",
    font=("맑은 고딕", 20),      # 폰트, 크기
    fg="blue",                   # 글자 색 (foreground)
    bg="yellow"                  # 배경 색 (background)
)
label1.pack()

label2 = tk.Label(
    window,
    text="두꺼운 글씨",
    font=("맑은 고딕", 15, "bold")  # bold = 굵게
)
label2.pack()

window.mainloop()
```

**주요 옵션:**

- `text`: 표시할 글자
- `font`: 글꼴 (폰트이름, 크기, 스타일)
- `fg`: 글자 색 (foreground)
- `bg`: 배경 색 (background)
- `width`, `height`: 크기

---

## 4️⃣ **Button - 버튼 만들기**

버튼을 클릭하면 함수가 실행되게 만들 수 있습니다!

### **기본 Button**

```python
import tkinter as tk

def button_click():
    """버튼 클릭시 실행될 함수"""
    print("버튼이 클릭되었습니다!")

window = tk.Tk()
window.title("Button 예제")
window.geometry("400x300")

# 버튼 생성
button = tk.Button(
    window,
    text="클릭하세요",
    command=button_click  # 클릭시 실행할 함수
)
button.pack()

window.mainloop()
```

버튼을 클릭하면 터미널에 "버튼이 클릭되었습니다!"가 출력됩니다.

### **Label과 함께 사용**

```python
import tkinter as tk

def change_text():
    """버튼 클릭시 Label 내용 변경"""
    label.config(text="버튼을 눌렀습니다!")

window = tk.Tk()
window.title("상호작용 예제")
window.geometry("400x300")

# Label 생성
label = tk.Label(window, text="안녕하세요", font=("맑은 고딕", 15))
label.pack(pady=20)  # pady = 위아래 여백

# Button 생성
button = tk.Button(
    window,
    text="클릭",
    command=change_text,
    font=("맑은 고딕", 12),
    bg="lightblue"
)
button.pack()

window.mainloop()
```

---

## 5️⃣ **Entry - 입력 받기**

사용자로부터 텍스트를 입력받을 수 있습니다.

### **기본 Entry**

```python
import tkinter as tk

def show_input():
    """입력된 내용을 Label에 표시"""
    text = entry.get()  # Entry에서 텍스트 가져오기
    label.config(text=f"입력: {text}")

window = tk.Tk()
window.title("입력 예제")
window.geometry("400x300")

# 안내 Label
info_label = tk.Label(window, text="이름을 입력하세요:")
info_label.pack(pady=10)

# Entry (입력 상자)
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# 버튼
button = tk.Button(window, text="확인", command=show_input)
button.pack(pady=10)

# 결과 Label
label = tk.Label(window, text="", font=("맑은 고딕", 12))
label.pack(pady=10)

window.mainloop()
```

**Entry 주요 메서드:**

- `get()`: 입력된 텍스트 가져오기
- `delete(0, tk.END)`: 내용 지우기
- `insert(0, "텍스트")`: 텍스트 넣기

---

## 6️⃣ **pack() - 레이아웃 배치**

위젯을 화면에 배치하는 방법입니다.

### **pack() 기본**

```python
import tkinter as tk

window = tk.Tk()
window.title("pack 예제")
window.geometry("400x300")

# 위에서 아래로 차례대로 배치
tk.Label(window, text="첫 번째", bg="red").pack()
tk.Label(window, text="두 번째", bg="green").pack()
tk.Label(window, text="세 번째", bg="blue").pack()

window.mainloop()
```

### **pack() 옵션**

```python
import tkinter as tk

window = tk.Tk()
window.title("pack 옵션")
window.geometry("400x300")

# side: 배치 방향
tk.Label(window, text="왼쪽", bg="red").pack(side="left")
tk.Label(window, text="오른쪽", bg="green").pack(side="right")

# pady, padx: 여백
tk.Label(window, text="여백 있음", bg="yellow").pack(pady=20, padx=20)

# fill: 채우기
tk.Label(window, text="가로로 채움", bg="lightblue").pack(fill="x")

window.mainloop()
```

**pack() 주요 옵션:**

- `side`: "top"(위), "bottom"(아래), "left"(왼쪽), "right"(오른쪽)
- `pady`: 위아래 여백
- `padx`: 좌우 여백
- `fill`: "x"(가로 채움), "y"(세로 채움), "both"(양쪽 채움)

---

## 7️⃣ **실전 예제: 간단한 계산기**

지금까지 배운 것으로 계산기를 만들어봅시다!

```python
import tkinter as tk

def calculate():
    """계산 실행"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"결과: {result}", fg="blue")
    except ValueError:
        result_label.config(text="숫자를 입력하세요!", fg="red")

def clear():
    """입력 지우기"""
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="")

# 윈도우 생성
window = tk.Tk()
window.title("🔢 간단 계산기")
window.geometry("400x300")
window.config(bg="lightgray")

# 제목
title = tk.Label(
    window,
    text="덧셈 계산기",
    font=("맑은 고딕", 20, "bold"),
    bg="lightgray"
)
title.pack(pady=20)

# 첫 번째 숫자
label1 = tk.Label(window, text="첫 번째 숫자:", bg="lightgray")
label1.pack()
entry1 = tk.Entry(window, width=20, font=("맑은 고딕", 12))
entry1.pack(pady=5)

# 두 번째 숫자
label2 = tk.Label(window, text="두 번째 숫자:", bg="lightgray")
label2.pack()
entry2 = tk.Entry(window, width=20, font=("맑은 고딕", 12))
entry2.pack(pady=5)

# 버튼들
button_frame = tk.Frame(window, bg="lightgray")
button_frame.pack(pady=15)

calc_button = tk.Button(
    button_frame,
    text="계산",
    command=calculate,
    width=10,
    bg="lightgreen"
)
calc_button.pack(side="left", padx=5)

clear_button = tk.Button(
    button_frame,
    text="지우기",
    command=clear,
    width=10,
    bg="lightcoral"
)
clear_button.pack(side="left", padx=5)

# 결과 표시
result_label = tk.Label(
    window,
    text="",
    font=("맑은 고딕", 15, "bold"),
    bg="lightgray"
)
result_label.pack(pady=10)

window.mainloop()
```

---

## 8️⃣ **실전 예제: 할 일 목록**

입력과 리스트를 활용한 할 일 관리 프로그램입니다.

```python
import tkinter as tk

def add_task():
    """할 일 추가"""
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        status_label.config(text="할 일을 입력하세요!", fg="red")

def delete_task():
    """선택한 할 일 삭제"""
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        status_label.config(text="삭제 완료", fg="green")
    except IndexError:
        status_label.config(text="삭제할 항목을 선택하세요!", fg="red")

def clear_all():
    """전체 삭제"""
    listbox.delete(0, tk.END)
    status_label.config(text="전체 삭제 완료", fg="green")

# 윈도우 생성
window = tk.Tk()
window.title("📝 할 일 목록")
window.geometry("400x500")
window.config(bg="white")

# 제목
title = tk.Label(
    window,
    text="오늘의 할 일",
    font=("맑은 고딕", 20, "bold"),
    bg="white"
)
title.pack(pady=20)

# 입력 영역
entry_frame = tk.Frame(window, bg="white")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=25, font=("맑은 고딕", 12))
entry.pack(side="left", padx=5)

add_button = tk.Button(
    entry_frame,
    text="추가",
    command=add_task,
    bg="lightblue",
    width=8
)
add_button.pack(side="left")

# 리스트 영역
listbox = tk.Listbox(
    window,
    width=40,
    height=12,
    font=("맑은 고딕", 11)
)
listbox.pack(pady=10)

# 버튼 영역
button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=10)

delete_button = tk.Button(
    button_frame,
    text="삭제",
    command=delete_task,
    bg="lightcoral",
    width=10
)
delete_button.pack(side="left", padx=5)

clear_button = tk.Button(
    button_frame,
    text="전체 삭제",
    command=clear_all,
    bg="lightgray",
    width=10
)
clear_button.pack(side="left", padx=5)

# 상태 표시
status_label = tk.Label(
    window,
    text="",
    font=("맑은 고딕", 10),
    bg="white"
)
status_label.pack(pady=5)

window.mainloop()
```

---

## 9️⃣ **grid() - 표 형태 배치**

`grid()`를 사용하면 위젯을 표처럼 배치할 수 있습니다.

### **기본 grid**

```python
import tkinter as tk

window = tk.Tk()
window.title("grid 예제")
window.geometry("300x200")

# row=행, column=열
tk.Label(window, text="이름:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Entry(window).grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="나이:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Entry(window).grid(row=1, column=1, padx=5, pady=5)

tk.Label(window, text="이메일:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Entry(window).grid(row=2, column=1, padx=5, pady=5)

tk.Button(window, text="확인").grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
```

**grid() 주요 옵션:**

- `row`: 행 번호 (0부터 시작)
- `column`: 열 번호 (0부터 시작)
- `sticky`: 정렬 ("n"북, "s"남, "e"동, "w"서)
- `columnspan`: 여러 열 차지
- `rowspan`: 여러 행 차지

---

## 🔟 **실전 예제: 로그인 화면**

grid를 활용한 깔끔한 로그인 화면입니다.

```python
import tkinter as tk
from tkinter import messagebox

def login():
    """로그인 처리"""
    username = username_entry.get()
    password = password_entry.get()
  
    if username == "admin" and password == "1234":
        messagebox.showinfo("성공", f"환영합니다, {username}님!")
    else:
        messagebox.showerror("오류", "아이디 또는 비밀번호가 틀렸습니다!")

# 윈도우 생성
window = tk.Tk()
window.title("🔐 로그인")
window.geometry("350x200")
window.config(bg="white")

# 제목
title = tk.Label(
    window,
    text="로그인",
    font=("맑은 고딕", 18, "bold"),
    bg="white"
)
title.grid(row=0, column=0, columnspan=2, pady=20)

# 아이디
tk.Label(window, text="아이디:", bg="white", font=("맑은 고딕", 11)).grid(
    row=1, column=0, sticky="e", padx=10, pady=10
)
username_entry = tk.Entry(window, width=20, font=("맑은 고딕", 11))
username_entry.grid(row=1, column=1, pady=10)

# 비밀번호
tk.Label(window, text="비밀번호:", bg="white", font=("맑은 고딕", 11)).grid(
    row=2, column=0, sticky="e", padx=10, pady=10
)
password_entry = tk.Entry(window, width=20, show="*", font=("맑은 고딕", 11))
password_entry.grid(row=2, column=1, pady=10)

# 로그인 버튼
login_button = tk.Button(
    window,
    text="로그인",
    command=login,
    width=15,
    bg="lightblue",
    font=("맑은 고딕", 11)
)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()
```

---

## 📝 **핵심 개념 정리**

### **기본 구조**

```python
import tkinter as tk

window = tk.Tk()           # 윈도우 생성
window.title("제목")
window.geometry("가로x세로")

# 위젯 추가

window.mainloop()          # 실행 (마지막!)
```

### **주요 위젯**

- `Label`: 텍스트 표시
- `Button`: 버튼 (command로 함수 연결)
- `Entry`: 한 줄 입력
- `Listbox`: 목록

### **레이아웃**

- `pack()`: 순서대로 배치
- `grid()`: 표 형태로 배치

### **이벤트 처리**

```python
def my_function():
    # 실행할 코드
    pass

button = tk.Button(window, command=my_function)
```

---

## 💡 **실습 과제**

### **과제 1: 인사 프로그램**

```python
# 힌트
# 이름 입력 → 버튼 클릭 → "안녕하세요, OOO님!" 표시
```

### **과제 2: 간단한 메모장**

```python
# 힌트
# Text 위젯 사용
# 저장 버튼 → 파일로 저장
# 불러오기 버튼 → 파일에서 읽기
```

---

## ✅ **퀴즈**

### **[초급] 1번**

tkinter를 import하는 방법은?

```python
1. import tk
2. import tkinter
3. import gui
4. import window
```

### **[중급] 2번**

윈도우를 실행하는 메서드는?

```python
1. run()
2. start()
3. mainloop()
4. execute()
```

### **[중급] 3번**

버튼 클릭 시 함수를 연결하는 옵션은?

```python
1. onclick
2. command
3. function
4. event
```

### **[고급] 4번**

Entry에서 입력값을 가져오는 메서드는?

```python
1. value()
2. text()
3. get()
4. read()
```

### **[고급] 5번**

위젯을 표 형태로 배치하는 메서드는?

```python
1. pack()
2. grid()
3. place()
4. table()
```

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
`import tkinter` 또는 `import tkinter as tk`로 사용합니다.

**2번 정답: 3**
`mainloop()` 메서드로 윈도우를 실행합니다.

**3번 정답: 2**
`command` 옵션으로 클릭 시 실행할 함수를 지정합니다.

**4번 정답: 3**
`get()` 메서드로 Entry의 입력값을 가져옵니다.

**5번 정답: 2**
`grid()` 메서드로 표 형태(행, 열)로 배치합니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 GUI 프로그래밍의 고급 기능을 배웁니다. 체크박스, 라디오 버튼, 메뉴 바 등 더 다양한 위젯과 이벤트 처리 방법을 학습하여 완성도 높은 GUI 프로그램을 만들 수 있게 됩니다!

---

수고했습니다.  
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
