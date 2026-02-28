# 21장 GUI 프로그래밍 2 (고급)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 tkinter의 고급 위젯들을 활용할 수 있습니다. 체크박스, 라디오 버튼, 스크롤바, 메시지 박스 등을 사용하여 더욱 완성도 높은 GUI 애플리케이션을 제작할 수 있습니다.

---

## 1️⃣ **Checkbutton - 체크박스**

여러 개를 동시에 선택할 수 있는 체크박스입니다.

### **왜 체크박스를 사용할까?**

설문조사나 옵션 선택처럼 **여러 개를 동시에 선택**할 때 사용합니다.

```
예시: 좋아하는 과일 선택 (여러 개 가능)
☑ 사과
☐ 바나나
☑ 딸기
```

### **기본 체크박스**

```python
import tkinter as tk

def show_choice():
    """선택한 항목 표시"""
    choices = []
    if var1.get():
        choices.append("사과")
    if var2.get():
        choices.append("바나나")
    if var3.get():
        choices.append("딸기")
  
    if choices:
        result_label.config(text=f"선택: {', '.join(choices)}")
    else:
        result_label.config(text="선택 없음")

# 윈도우 생성
window = tk.Tk()
window.title("체크박스 예제")
window.geometry("300x250")

# 제목
tk.Label(window, text="좋아하는 과일을 선택하세요", font=("맑은 고딕", 12, "bold")).pack(pady=10)

# 체크박스 변수 (선택 여부 저장)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# 체크박스 생성
tk.Checkbutton(window, text="사과", variable=var1, font=("맑은 고딕", 11)).pack(anchor="w", padx=50)
tk.Checkbutton(window, text="바나나", variable=var2, font=("맑은 고딕", 11)).pack(anchor="w", padx=50)
tk.Checkbutton(window, text="딸기", variable=var3, font=("맑은 고딕", 11)).pack(anchor="w", padx=50)

# 확인 버튼
tk.Button(window, text="확인", command=show_choice, bg="lightblue").pack(pady=10)

# 결과 표시
result_label = tk.Label(window, text="", font=("맑은 고딕", 11), fg="blue")
result_label.pack(pady=10)

window.mainloop()
```

**핵심 포인트:**

- `IntVar()`: 체크 상태를 저장하는 변수 (0=해제, 1=선택)
- `variable`: 체크박스와 변수 연결
- `get()`: 선택 여부 확인 (True/False 또는 1/0)

---

## 2️⃣ **Radiobutton - 라디오 버튼**

여러 개 중 **하나만** 선택할 수 있는 버튼입니다.

### **왜 라디오 버튼을 사용할까?**

성별, 학년처럼 **하나만 선택**해야 할 때 사용합니다.

```
예시: 성별 선택 (하나만 가능)
◉ 남자
◯ 여자
```

### **기본 라디오 버튼**

```python
import tkinter as tk

def show_choice():
    """선택한 항목 표시"""
    choice = var.get()
    result_label.config(text=f"선택: {choice}")

# 윈도우 생성
window = tk.Tk()
window.title("라디오 버튼 예제")
window.geometry("300x250")

# 제목
tk.Label(window, text="좋아하는 색을 선택하세요", font=("맑은 고딕", 12, "bold")).pack(pady=10)

# 라디오 버튼 변수 (하나의 변수를 공유!)
var = tk.StringVar()
var.set("빨강")  # 기본 선택

# 라디오 버튼 생성 (같은 variable 사용)
tk.Radiobutton(window, text="빨강", variable=var, value="빨강", font=("맑은 고딕", 11)).pack(anchor="w", padx=50)
tk.Radiobutton(window, text="파랑", variable=var, value="파랑", font=("맑은 고딕", 11)).pack(anchor="w", padx=50)
tk.Radiobutton(window, text="초록", variable=var, value="초록", font=("맑은 고딕", 11)).pack(anchor="w", padx=50)

# 확인 버튼
tk.Button(window, text="확인", command=show_choice, bg="lightgreen").pack(pady=10)

# 결과 표시
result_label = tk.Label(window, text="선택: 빨강", font=("맑은 고딕", 11), fg="blue")
result_label.pack(pady=10)

window.mainloop()
```

**핵심 포인트:**

- 모든 라디오 버튼이 **같은 variable** 공유
- `value`: 각 버튼의 값
- `set()`: 기본 선택 설정

### **체크박스 vs 라디오 버튼**

```
Checkbutton (여러 개 선택)      Radiobutton (하나만 선택)
☑ 사과                         ◉ 빨강
☑ 바나나                       ◯ 파랑
☐ 딸기                         ◯ 초록

각자 다른 변수                  같은 변수 공유
var1, var2, var3              var
```

---

## 3️⃣ **Text - 여러 줄 입력**

Entry는 한 줄만 입력할 수 있지만, Text는 **여러 줄** 입력이 가능합니다.

### **기본 Text 위젯**

```python
import tkinter as tk

def show_text():
    """입력된 내용 표시"""
    content = text.get("1.0", tk.END)  # 전체 내용 가져오기
    print(content)

def clear_text():
    """내용 지우기"""
    text.delete("1.0", tk.END)

# 윈도우 생성
window = tk.Tk()
window.title("메모장")
window.geometry("400x300")

# 제목
tk.Label(window, text="메모장", font=("맑은 고딕", 14, "bold")).pack(pady=10)

# Text 위젯
text = tk.Text(window, width=40, height=10, font=("맑은 고딕", 11))
text.pack(pady=10)

# 버튼 프레임
button_frame = tk.Frame(window)
button_frame.pack()

tk.Button(button_frame, text="출력", command=show_text, width=10).pack(side="left", padx=5)
tk.Button(button_frame, text="지우기", command=clear_text, width=10).pack(side="left", padx=5)

window.mainloop()
```

**Text 주요 메서드:**

- `get("1.0", tk.END)`: 전체 내용 가져오기
- `delete("1.0", tk.END)`: 전체 내용 삭제
- `insert("1.0", "텍스트")`: 맨 앞에 텍스트 삽입

💡 **"1.0"의 의미**: 1번째 줄, 0번째 문자 (첫 위치)

---

## 4️⃣ **Scrollbar - 스크롤바**

내용이 많을 때 스크롤할 수 있게 만듭니다.

### **Text와 Scrollbar 연결**

```python
import tkinter as tk

window = tk.Tk()
window.title("스크롤바 예제")
window.geometry("400x300")

# Frame 생성
frame = tk.Frame(window)
frame.pack(pady=10)

# Scrollbar 생성
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Text 생성 (Scrollbar와 연결)
text = tk.Text(frame, width=40, height=15, yscrollcommand=scrollbar.set)
text.pack(side="left")

# Scrollbar와 Text 연결
scrollbar.config(command=text.yview)

# 샘플 텍스트 추가
for i in range(1, 51):
    text.insert(tk.END, f"{i}번째 줄입니다.\n")

window.mainloop()
```

**연결 방법:**

1. Text 생성 시: `yscrollcommand=scrollbar.set`
2. Scrollbar 설정: `scrollbar.config(command=text.yview)`

---

## 5️⃣ **messagebox - 메시지 박스**

사용자에게 알림, 확인, 오류 메시지를 보여줍니다.

### **주요 메시지 박스**

```python
import tkinter as tk
from tkinter import messagebox

def show_info():
    """정보 메시지"""
    messagebox.showinfo("알림", "저장되었습니다!")

def show_warning():
    """경고 메시지"""
    messagebox.showwarning("경고", "주의하세요!")

def show_error():
    """오류 메시지"""
    messagebox.showerror("오류", "파일을 찾을 수 없습니다!")

def ask_question():
    """질문 (예/아니오)"""
    result = messagebox.askyesno("확인", "정말 삭제하시겠습니까?")
    if result:
        messagebox.showinfo("결과", "삭제되었습니다")
    else:
        messagebox.showinfo("결과", "취소되었습니다")

def ask_okcancel():
    """확인/취소"""
    result = messagebox.askokcancel("확인", "계속하시겠습니까?")
    print(f"결과: {result}")

# 윈도우 생성
window = tk.Tk()
window.title("메시지 박스 예제")
window.geometry("300x300")

tk.Label(window, text="메시지 박스 테스트", font=("맑은 고딕", 14, "bold")).pack(pady=20)

tk.Button(window, text="정보", command=show_info, width=15, bg="lightblue").pack(pady=5)
tk.Button(window, text="경고", command=show_warning, width=15, bg="yellow").pack(pady=5)
tk.Button(window, text="오류", command=show_error, width=15, bg="lightcoral").pack(pady=5)
tk.Button(window, text="질문 (예/아니오)", command=ask_question, width=15, bg="lightgreen").pack(pady=5)
tk.Button(window, text="확인/취소", command=ask_okcancel, width=15, bg="lightgray").pack(pady=5)

window.mainloop()
```

**주요 messagebox:**

- `showinfo()`: 정보 (ℹ️)
- `showwarning()`: 경고 (⚠️)
- `showerror()`: 오류 (❌)
- `askyesno()`: 예/아니오 질문 (True/False 반환)
- `askokcancel()`: 확인/취소 (True/False 반환)

---

## 6️⃣ **Scale - 슬라이더**

마우스로 드래그하여 값을 선택하는 슬라이더입니다.

### **기본 Scale**

```python
import tkinter as tk

def show_value(value):
    """슬라이더 값 표시"""
    label.config(text=f"현재 값: {value}")

window = tk.Tk()
window.title("슬라이더 예제")
window.geometry("400x200")

tk.Label(window, text="음량 조절", font=("맑은 고딕", 14, "bold")).pack(pady=20)

# Scale 생성
scale = tk.Scale(
    window,
    from_=0,          # 최솟값
    to=100,           # 최댓값
    orient="horizontal",  # 가로 방향
    length=300,       # 길이
    command=show_value  # 값 변경시 호출할 함수
)
scale.set(50)  # 초기값
scale.pack(pady=10)

# 결과 표시
label = tk.Label(window, text="현재 값: 50", font=("맑은 고딕", 12))
label.pack(pady=10)

window.mainloop()
```

**Scale 주요 옵션:**

- `from_`: 최솟값
- `to`: 최댓값
- `orient`: "horizontal"(가로) 또는 "vertical"(세로)
- `command`: 값 변경시 호출할 함수

---

## 7️⃣ **실전 예제: 설문조사 프로그램**

지금까지 배운 위젯들을 활용한 설문조사 프로그램입니다.

```python
import tkinter as tk
from tkinter import messagebox

def submit_survey():
    """설문 제출"""
    # 이름 확인
    name = name_entry.get()
    if not name:
        messagebox.showwarning("경고", "이름을 입력하세요!")
        return
  
    # 성별 확인
    gender = gender_var.get()
  
    # 나이 확인
    age = age_scale.get()
  
    # 취미 확인
    hobbies = []
    if hobby1_var.get():
        hobbies.append("운동")
    if hobby2_var.get():
        hobbies.append("독서")
    if hobby3_var.get():
        hobbies.append("영화")
  
    # 의견 확인
    opinion = opinion_text.get("1.0", tk.END).strip()
  
    # 결과 출력
    result = f"""
설문조사 결과
{'='*30}
이름: {name}
성별: {gender}
나이: {age}세
취미: {', '.join(hobbies) if hobbies else '없음'}

의견:
{opinion if opinion else '없음'}
{'='*30}
    """
  
    messagebox.showinfo("제출 완료", result)

# 윈도우 생성
window = tk.Tk()
window.title("📋 설문조사")
window.geometry("450x600")
window.config(bg="white")

# 제목
tk.Label(
    window,
    text="설문조사",
    font=("맑은 고딕", 18, "bold"),
    bg="white"
).pack(pady=20)

# 1. 이름
tk.Label(window, text="이름:", bg="white", font=("맑은 고딕", 11)).pack(anchor="w", padx=30)
name_entry = tk.Entry(window, width=30, font=("맑은 고딕", 11))
name_entry.pack(anchor="w", padx=30, pady=5)

# 2. 성별 (라디오 버튼)
tk.Label(window, text="성별:", bg="white", font=("맑은 고딕", 11)).pack(anchor="w", padx=30, pady=(15, 5))
gender_var = tk.StringVar(value="남자")

gender_frame = tk.Frame(window, bg="white")
gender_frame.pack(anchor="w", padx=30)
tk.Radiobutton(gender_frame, text="남자", variable=gender_var, value="남자", bg="white").pack(side="left", padx=5)
tk.Radiobutton(gender_frame, text="여자", variable=gender_var, value="여자", bg="white").pack(side="left", padx=5)

# 3. 나이 (슬라이더)
tk.Label(window, text="나이:", bg="white", font=("맑은 고딕", 11)).pack(anchor="w", padx=30, pady=(15, 5))
age_scale = tk.Scale(
    window,
    from_=10,
    to=80,
    orient="horizontal",
    length=350,
    bg="white"
)
age_scale.set(25)
age_scale.pack(anchor="w", padx=30)

# 4. 취미 (체크박스)
tk.Label(window, text="취미 (여러 개 선택 가능):", bg="white", font=("맑은 고딕", 11)).pack(anchor="w", padx=30, pady=(15, 5))

hobby1_var = tk.IntVar()
hobby2_var = tk.IntVar()
hobby3_var = tk.IntVar()

hobby_frame = tk.Frame(window, bg="white")
hobby_frame.pack(anchor="w", padx=30)
tk.Checkbutton(hobby_frame, text="운동", variable=hobby1_var, bg="white").pack(anchor="w")
tk.Checkbutton(hobby_frame, text="독서", variable=hobby2_var, bg="white").pack(anchor="w")
tk.Checkbutton(hobby_frame, text="영화", variable=hobby3_var, bg="white").pack(anchor="w")

# 5. 의견 (Text)
tk.Label(window, text="의견:", bg="white", font=("맑은 고딕", 11)).pack(anchor="w", padx=30, pady=(15, 5))

text_frame = tk.Frame(window)
text_frame.pack(padx=30, pady=5)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

opinion_text = tk.Text(text_frame, width=40, height=5, yscrollcommand=scrollbar.set)
opinion_text.pack(side="left")
scrollbar.config(command=opinion_text.yview)

# 제출 버튼
tk.Button(
    window,
    text="제출",
    command=submit_survey,
    width=15,
    bg="lightblue",
    font=("맑은 고딕", 12, "bold")
).pack(pady=20)

window.mainloop()
```

---

## 8️⃣ **실전 예제: 간단한 계산기 (완성판)**

다양한 위젯을 활용한 계산기입니다.

```python
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("🔢 계산기")
        self.window.geometry("350x450")
        self.window.config(bg="lightgray")
    
        self.result_var = tk.StringVar()
        self.result_var.set("0")
    
        self.create_widgets()
  
    def create_widgets(self):
        """위젯 생성"""
        # 결과 표시
        result_label = tk.Label(
            self.window,
            textvariable=self.result_var,
            font=("맑은 고딕", 24, "bold"),
            bg="white",
            anchor="e",
            padx=10,
            pady=20
        )
        result_label.pack(fill="x", padx=10, pady=10)
    
        # 버튼 프레임
        button_frame = tk.Frame(self.window, bg="lightgray")
        button_frame.pack()
    
        # 버튼 목록
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
    
        # 버튼 생성
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                button = tk.Button(
                    button_frame,
                    text=btn_text,
                    width=6,
                    height=2,
                    font=("맑은 고딕", 14, "bold"),
                    command=lambda x=btn_text: self.on_button_click(x)
                )
            
                # 색상 지정
                if btn_text == '=':
                    button.config(bg="lightblue")
                elif btn_text == 'C':
                    button.config(bg="lightcoral")
                elif btn_text in ['+', '-', '*', '/']:
                    button.config(bg="lightyellow")
                else:
                    button.config(bg="white")
            
                button.grid(row=row_idx, column=col_idx, padx=2, pady=2)
  
    def on_button_click(self, btn_text):
        """버튼 클릭 처리"""
        current = self.result_var.get()
    
        if btn_text == 'C':
            # 지우기
            self.result_var.set("0")
    
        elif btn_text == '=':
            # 계산
            try:
                result = eval(current)
                self.result_var.set(str(result))
            except:
                messagebox.showerror("오류", "잘못된 식입니다!")
                self.result_var.set("0")
    
        else:
            # 숫자나 연산자 추가
            if current == "0":
                self.result_var.set(btn_text)
            else:
                self.result_var.set(current + btn_text)

# 윈도우 생성 및 실행
window = tk.Tk()
calculator = Calculator(window)
window.mainloop()
```

---

## 9️⃣ **Menu - 메뉴 바**

프로그램 상단에 메뉴를 추가할 수 있습니다.

### **기본 메뉴**

```python
import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("새 파일", "새 파일을 만듭니다")

def open_file():
    messagebox.showinfo("열기", "파일을 엽니다")

def save_file():
    messagebox.showinfo("저장", "파일을 저장합니다")

def exit_program():
    if messagebox.askyesno("종료", "정말 종료하시겠습니까?"):
        window.destroy()

def about():
    messagebox.showinfo("정보", "간단한 메모장 v1.0")

# 윈도우 생성
window = tk.Tk()
window.title("메뉴 예제")
window.geometry("400x300")

# 메뉴 바 생성
menubar = tk.Menu(window)
window.config(menu=menubar)

# 파일 메뉴
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="새 파일", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()  # 구분선
file_menu.add_command(label="종료", command=exit_program)

# 도움말 메뉴
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="도움말", menu=help_menu)
help_menu.add_command(label="정보", command=about)

window.mainloop()
```

---

## 📝 **핵심 개념 정리**

### **주요 위젯**

- `Checkbutton`: 여러 개 선택 (각자 변수)
- `Radiobutton`: 하나만 선택 (같은 변수)
- `Text`: 여러 줄 입력
- `Scale`: 슬라이더
- `Scrollbar`: 스크롤

### **messagebox**

```python
from tkinter import messagebox

messagebox.showinfo("제목", "내용")
messagebox.askokcancel("제목", "질문")
```

### **Menu**

```python
menubar = tk.Menu(window)
window.config(menu=menubar)
```

---

## 💡 **실습 과제**

### **과제 1: BMI 계산기**

```python
# 힌트
# 키(cm), 몸무게(kg) 입력
# BMI = 몸무게 / (키/100)^2
# 결과: 저체중/정상/과체중/비만
```

### **과제 2: 색상 선택기**

```python
# 힌트
# Scale 3개 (R, G, B)
# 0-255 범위
# 선택한 색상으로 Label 배경 변경
```

---

## ✅ **퀴즈**

### **[초급] 1번**

여러 개를 선택할 수 있는 위젯은?

### **[중급] 2번**

라디오 버튼들이 공유하는 것은?

### **[고급] 3번**

Text 위젯에서 전체 내용을 가져오는 코드는?

### **[고급] 4번**

예/아니오를 묻는 messagebox는?

### **[고급] 5번**

메뉴 바를 윈도우에 추가하는 코드는?

---

## 🔑 **퀴즈 정답**

**1번**: Checkbutton
**2번**: variable (같은 변수)
**3번**: `text.get("1.0", tk.END)`
**4번**: `messagebox.askyesno()`
**5번**: `window.config(menu=menubar)`

---

## 🎯 **다음 장 예고**

다음 장에서는 CSV 파일과 데이터 분석을 배웁니다. 엑셀 파일을 읽고 쓰며, 데이터를 처리하고 분석하는 방법을 학습합니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
