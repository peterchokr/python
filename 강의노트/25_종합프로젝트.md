# 25장 종합 프로젝트

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장에서는 지금까지 배운 모든 내용을 활용하여 실전 프로젝트를 완성합니다. CSV 파일 처리, 데이터 분석, 시각화, GUI 프로그래밍을 결합하여 완성도 있는 애플리케이션을 제작할 수 있게 됩니다.

---

## 1️⃣ **프로젝트 개요**

### **지금까지 배운 내용 총정리**

```
Part 1 (Week 01-12)
├─ 변수, 자료형, 연산자
├─ 조건문, 반복문
├─ 함수
└─ 리스트, 튜플

Part 2 (Week 14-25)
├─ 딕셔너리, 파일 입출력
├─ 예외 처리, 모듈
├─ 클래스 (기초, 상속, 고급)
├─ GUI 프로그래밍 (tkinter)
├─ CSV 파일과 데이터 분석
├─ Matplotlib 시각화
└─ 웹 스크래핑
```

### **종합 프로젝트 주제**

이번 장에서는 3가지 종합 프로젝트를 진행합니다:

1. **학생 성적 관리 시스템** (기초)
2. **가계부 프로그램** (중급)
3. **날씨 데이터 분석 대시보드** (고급)

---

## 2️⃣ **프로젝트 1: 학생 성적 관리 시스템**

**난이도**: ⭐⭐☆☆☆ (기초)

**사용 기술**: 클래스, 파일 입출력, CSV, 예외 처리

### **프로젝트 요구사항**

**기능:**

1. 학생 추가 (이름, 학번, 과목별 점수)
2. 성적 조회 (개인별, 전체)
3. 평균 계산 (개인, 과목별, 전체)
4. 등급 부여 (A/B/C/D/F)
5. 데이터 저장 (CSV 파일)
6. 데이터 불러오기

### **프로젝트 구조**

```
student_manager/
├─ main.py              # 메인 프로그램
├─ student.py           # Student 클래스
├─ manager.py           # StudentManager 클래스
└─ students.csv         # 데이터 파일
```

### **1단계: Student 클래스**

**student.py:**

```python
class Student:
    """학생 클래스"""
  
    def __init__(self, name, student_id, korean, english, math):
        self.name = name
        self.student_id = student_id
        self.korean = korean
        self.english = english
        self.math = math
  
    def get_average(self):
        """평균 계산"""
        return (self.korean + self.english + self.math) / 3
  
    def get_grade(self):
        """등급 계산"""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
  
    def get_total(self):
        """총점"""
        return self.korean + self.english + self.math
  
    def __str__(self):
        return f"{self.name}({self.student_id}) - 평균: {self.get_average():.1f}, 등급: {self.get_grade()}"
```

### **2단계: StudentManager 클래스**

**manager.py:**

```python
import csv
from student import Student

class StudentManager:
    """학생 관리 클래스"""
  
    def __init__(self, filename='students.csv'):
        self.filename = filename
        self.students = []
        self.load_data()
  
    def add_student(self, name, student_id, korean, english, math):
        """학생 추가"""
        # 중복 확인
        for student in self.students:
            if student.student_id == student_id:
                print(f"❌ 학번 {student_id}는 이미 존재합니다.")
                return False
    
        student = Student(name, student_id, korean, english, math)
        self.students.append(student)
        print(f"✓ {name} 학생이 추가되었습니다.")
        return True
  
    def find_student(self, student_id):
        """학생 찾기"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
  
    def show_all_students(self):
        """전체 학생 조회"""
        if not self.students:
            print("등록된 학생이 없습니다.")
            return
    
        print("\n" + "=" * 80)
        print("전체 학생 성적표")
        print("=" * 80)
        print(f"{'이름':^8} {'학번':^10} {'국어':^6} {'영어':^6} {'수학':^6} {'평균':^8} {'등급':^4}")
        print("-" * 80)
    
        for student in self.students:
            print(f"{student.name:^8} {student.student_id:^10} "
                  f"{student.korean:^6} {student.english:^6} {student.math:^6} "
                  f"{student.get_average():^8.1f} {student.get_grade():^4}")
    
        print("=" * 80)
        print(f"총 {len(self.students)}명")
  
    def get_subject_average(self):
        """과목별 평균"""
        if not self.students:
            return None
    
        korean_avg = sum(s.korean for s in self.students) / len(self.students)
        english_avg = sum(s.english for s in self.students) / len(self.students)
        math_avg = sum(s.math for s in self.students) / len(self.students)
    
        return {
            '국어': korean_avg,
            '영어': english_avg,
            '수학': math_avg
        }
  
    def save_data(self):
        """데이터 저장"""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8-sig') as file:
                fieldnames = ['이름', '학번', '국어', '영어', '수학']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
            
                writer.writeheader()
                for student in self.students:
                    writer.writerow({
                        '이름': student.name,
                        '학번': student.student_id,
                        '국어': student.korean,
                        '영어': student.english,
                        '수학': student.math
                    })
            print(f"✓ 데이터가 {self.filename}에 저장되었습니다.")
            return True
        except Exception as e:
            print(f"❌ 저장 오류: {e}")
            return False
  
    def load_data(self):
        """데이터 불러오기"""
        try:
            with open(self.filename, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row['이름'],
                        row['학번'],
                        int(row['국어']),
                        int(row['영어']),
                        int(row['수학'])
                    )
                    self.students.append(student)
            print(f"✓ {len(self.students)}명의 데이터를 불러왔습니다.")
        except FileNotFoundError:
            print("데이터 파일이 없습니다. 새로 시작합니다.")
        except Exception as e:
            print(f"❌ 불러오기 오류: {e}")
```

### **3단계: 메인 프로그램**

**main.py:**

```python
from manager import StudentManager

def print_menu():
    """메뉴 출력"""
    print("\n" + "=" * 50)
    print("📚 학생 성적 관리 시스템")
    print("=" * 50)
    print("1. 학생 추가")
    print("2. 학생 조회")
    print("3. 전체 학생 조회")
    print("4. 과목별 평균")
    print("5. 데이터 저장")
    print("0. 종료")
    print("=" * 50)

def main():
    """메인 함수"""
    manager = StudentManager()
  
    while True:
        print_menu()
        choice = input("선택: ")
    
        if choice == '1':
            # 학생 추가
            print("\n[학생 추가]")
            name = input("이름: ")
            student_id = input("학번: ")
        
            try:
                korean = int(input("국어 점수: "))
                english = int(input("영어 점수: "))
                math = int(input("수학 점수: "))
            
                if not (0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100):
                    print("❌ 점수는 0-100 사이여야 합니다.")
                    continue
            
                manager.add_student(name, student_id, korean, english, math)
            except ValueError:
                print("❌ 올바른 숫자를 입력하세요.")
    
        elif choice == '2':
            # 학생 조회
            print("\n[학생 조회]")
            student_id = input("학번: ")
            student = manager.find_student(student_id)
        
            if student:
                print("\n" + "=" * 50)
                print(f"이름: {student.name}")
                print(f"학번: {student.student_id}")
                print(f"국어: {student.korean}점")
                print(f"영어: {student.english}점")
                print(f"수학: {student.math}점")
                print(f"평균: {student.get_average():.1f}점")
                print(f"등급: {student.get_grade()}")
                print("=" * 50)
            else:
                print(f"❌ 학번 {student_id}를 찾을 수 없습니다.")
    
        elif choice == '3':
            # 전체 학생 조회
            manager.show_all_students()
    
        elif choice == '4':
            # 과목별 평균
            averages = manager.get_subject_average()
            if averages:
                print("\n" + "=" * 50)
                print("과목별 평균")
                print("=" * 50)
                for subject, avg in averages.items():
                    print(f"{subject}: {avg:.1f}점")
                print("=" * 50)
            else:
                print("❌ 등록된 학생이 없습니다.")
    
        elif choice == '5':
            # 데이터 저장
            manager.save_data()
    
        elif choice == '0':
            # 종료
            save = input("종료 전에 저장하시겠습니까? (y/n): ")
            if save.lower() == 'y':
                manager.save_data()
            print("프로그램을 종료합니다.")
            break
    
        else:
            print("❌ 올바른 번호를 선택하세요.")

if __name__ == "__main__":
    main()
```

---

## 3️⃣ **프로젝트 2: 가계부 프로그램 (GUI)**

**난이도**: ⭐⭐⭐☆☆ (중급)

**사용 기술**: tkinter, CSV, Matplotlib, 클래스

### **프로젝트 요구사항**

**기능:**

1. 수입/지출 입력
2. 거래 내역 조회
3. 카테고리별 통계
4. 월별 분석
5. 그래프 시각화 (원 그래프, 막대 그래프)
6. CSV 저장/불러오기

### **프로젝트 구조**

```
budget_app/
├─ main.py              # GUI 메인
├─ transaction.py       # Transaction 클래스
├─ budget_manager.py    # BudgetManager 클래스
└─ transactions.csv     # 데이터 파일
```

### **1단계: Transaction 클래스**

**transaction.py:**

```python
from datetime import datetime

class Transaction:
    """거래 내역 클래스"""
  
    def __init__(self, date, category, amount, transaction_type, memo=''):
        self.date = date
        self.category = category
        self.amount = amount
        self.type = transaction_type  # 'income' or 'expense'
        self.memo = memo
  
    def __str__(self):
        type_str = '수입' if self.type == 'income' else '지출'
        return f"{self.date} | {type_str} | {self.category} | {self.amount:,}원 | {self.memo}"
```

### **2단계: BudgetManager 클래스**

**budget_manager.py:**

```python
import csv
from transaction import Transaction
from datetime import datetime

class BudgetManager:
    """가계부 관리 클래스"""
  
    def __init__(self, filename='transactions.csv'):
        self.filename = filename
        self.transactions = []
        self.load_data()
  
    def add_transaction(self, date, category, amount, transaction_type, memo=''):
        """거래 추가"""
        transaction = Transaction(date, category, amount, transaction_type, memo)
        self.transactions.append(transaction)
        return True
  
    def get_transactions_by_month(self, year, month):
        """월별 거래 내역"""
        result = []
        for t in self.transactions:
            t_date = datetime.strptime(t.date, '%Y-%m-%d')
            if t_date.year == year and t_date.month == month:
                result.append(t)
        return result
  
    def get_balance(self):
        """잔액 계산"""
        income = sum(t.amount for t in self.transactions if t.type == 'income')
        expense = sum(t.amount for t in self.transactions if t.type == 'expense')
        return income - expense
  
    def get_category_summary(self, transaction_type):
        """카테고리별 합계"""
        summary = {}
        for t in self.transactions:
            if t.type == transaction_type:
                if t.category in summary:
                    summary[t.category] += t.amount
                else:
                    summary[t.category] = t.amount
        return summary
  
    def save_data(self):
        """데이터 저장"""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8-sig') as file:
                fieldnames = ['날짜', '카테고리', '금액', '유형', '메모']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
            
                writer.writeheader()
                for t in self.transactions:
                    writer.writerow({
                        '날짜': t.date,
                        '카테고리': t.category,
                        '금액': t.amount,
                        '유형': t.type,
                        '메모': t.memo
                    })
            return True
        except Exception as e:
            print(f"저장 오류: {e}")
            return False
  
    def load_data(self):
        """데이터 불러오기"""
        try:
            with open(self.filename, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transaction = Transaction(
                        row['날짜'],
                        row['카테고리'],
                        int(row['금액']),
                        row['유형'],
                        row.get('메모', '')
                    )
                    self.transactions.append(transaction)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"불러오기 오류: {e}")
```

### **3단계: GUI 메인 프로그램**

**main.py:**

```python
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from budget_manager import BudgetManager

class BudgetApp:
    def __init__(self, window):
        self.window = window
        self.window.title("💰 가계부")
        self.window.geometry("800x600")
    
        self.manager = BudgetManager()
    
        # 한글 폰트 설정
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
    
        self.create_widgets()
        self.update_display()
  
    def create_widgets(self):
        """위젯 생성"""
        # 상단: 요약 정보
        summary_frame = tk.Frame(self.window, bg='lightblue', height=100)
        summary_frame.pack(fill='x', padx=10, pady=10)
    
        self.balance_label = tk.Label(
            summary_frame,
            text="잔액: 0원",
            font=('맑은 고딕', 18, 'bold'),
            bg='lightblue'
        )
        self.balance_label.pack(pady=20)
    
        # 중앙: 입력 프레임
        input_frame = tk.LabelFrame(self.window, text="거래 입력", padx=10, pady=10)
        input_frame.pack(fill='x', padx=10, pady=10)
    
        # 날짜
        tk.Label(input_frame, text="날짜:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame, width=15)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
    
        # 카테고리
        tk.Label(input_frame, text="카테고리:").grid(row=0, column=2, sticky='e', padx=5, pady=5)
        self.category_var = tk.StringVar()
        categories = ['급여', '식비', '교통비', '문화생활', '쇼핑', '기타']
        self.category_combo = ttk.Combobox(input_frame, textvariable=self.category_var, values=categories, width=12)
        self.category_combo.grid(row=0, column=3, padx=5, pady=5)
    
        # 금액
        tk.Label(input_frame, text="금액:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.amount_entry = tk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)
    
        # 유형
        tk.Label(input_frame, text="유형:").grid(row=1, column=2, sticky='e', padx=5, pady=5)
        self.type_var = tk.StringVar(value='expense')
    
        type_frame = tk.Frame(input_frame)
        type_frame.grid(row=1, column=3, padx=5, pady=5)
        tk.Radiobutton(type_frame, text="수입", variable=self.type_var, value='income').pack(side='left')
        tk.Radiobutton(type_frame, text="지출", variable=self.type_var, value='expense').pack(side='left')
    
        # 메모
        tk.Label(input_frame, text="메모:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.memo_entry = tk.Entry(input_frame, width=50)
        self.memo_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky='w')
    
        # 버튼
        button_frame = tk.Frame(input_frame)
        button_frame.grid(row=3, column=0, columnspan=4, pady=10)
    
        tk.Button(button_frame, text="추가", command=self.add_transaction, width=10, bg='lightgreen').pack(side='left', padx=5)
        tk.Button(button_frame, text="저장", command=self.save_data, width=10, bg='lightblue').pack(side='left', padx=5)
        tk.Button(button_frame, text="통계", command=self.show_statistics, width=10, bg='lightyellow').pack(side='left', padx=5)
    
        # 하단: 거래 내역 리스트
        list_frame = tk.LabelFrame(self.window, text="최근 거래 내역")
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
        # 스크롤바
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
    
        self.transaction_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, font=('맑은 고딕', 10))
        self.transaction_listbox.pack(fill='both', expand=True)
        scrollbar.config(command=self.transaction_listbox.yview)
  
    def add_transaction(self):
        """거래 추가"""
        try:
            date = self.date_entry.get()
            category = self.category_var.get()
            amount = int(self.amount_entry.get())
            transaction_type = self.type_var.get()
            memo = self.memo_entry.get()
        
            if not category:
                messagebox.showwarning("경고", "카테고리를 선택하세요!")
                return
        
            self.manager.add_transaction(date, category, amount, transaction_type, memo)
        
            # 입력 필드 초기화
            self.amount_entry.delete(0, tk.END)
            self.memo_entry.delete(0, tk.END)
        
            self.update_display()
            messagebox.showinfo("성공", "거래가 추가되었습니다!")
        
        except ValueError:
            messagebox.showerror("오류", "금액은 숫자로 입력하세요!")
  
    def update_display(self):
        """화면 업데이트"""
        # 잔액 업데이트
        balance = self.manager.get_balance()
        self.balance_label.config(text=f"잔액: {balance:,}원")
    
        # 거래 내역 업데이트
        self.transaction_listbox.delete(0, tk.END)
        for t in reversed(self.manager.transactions[-10:]):  # 최근 10개
            self.transaction_listbox.insert(tk.END, str(t))
  
    def save_data(self):
        """데이터 저장"""
        if self.manager.save_data():
            messagebox.showinfo("성공", "데이터가 저장되었습니다!")
  
    def show_statistics(self):
        """통계 창"""
        stats_window = tk.Toplevel(self.window)
        stats_window.title("📊 통계")
        stats_window.geometry("800x600")
    
        # 지출 카테고리별 원 그래프
        expense_summary = self.manager.get_category_summary('expense')
    
        if expense_summary:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
            # 지출 원 그래프
            categories = list(expense_summary.keys())
            amounts = list(expense_summary.values())
        
            ax1.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
            ax1.set_title('카테고리별 지출')
        
            # 지출 막대 그래프
            ax2.bar(categories, amounts, color='lightcoral')
            ax2.set_title('카테고리별 지출 금액')
            ax2.set_ylabel('금액 (원)')
            plt.xticks(rotation=45)
        
            plt.tight_layout()
        
            canvas = FigureCanvasTkAgg(fig, stats_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
        else:
            tk.Label(stats_window, text="거래 내역이 없습니다.", font=('맑은 고딕', 14)).pack(pady=50)

# 프로그램 실행
if __name__ == "__main__":
    window = tk.Tk()
    app = BudgetApp(window)
    window.mainloop()
```

---

## 4️⃣ **프로젝트 3: 날씨 데이터 분석 대시보드**

**난이도**: ⭐⭐⭐⭐☆ (고급)

**사용 기술**: 웹 스크래핑, CSV, Matplotlib, tkinter, 데이터 분석

### **프로젝트 요구사항**

**기능:**

1. HTML 파일에서 날씨 데이터 수집
2. CSV로 저장
3. 데이터 분석 (평균, 최대, 최소)
4. GUI 대시보드
5. 그래프 시각화 (기온, 강수량, 습도)
6. 월별/주별 통계

### **실습용 HTML 파일**

**weather_data.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>날씨 데이터</title>
</head>
<body>
    <h1>2024년 1월 날씨</h1>
  
    <div class="weather">
        <p class="date">2024-01-01</p>
        <p class="temp">최고: 5°C, 최저: -2°C</p>
        <p class="rain">강수량: 0mm</p>
        <p class="humidity">습도: 45%</p>
    </div>
  
    <div class="weather">
        <p class="date">2024-01-02</p>
        <p class="temp">최고: 3°C, 최저: -4°C</p>
        <p class="rain">강수량: 5mm</p>
        <p class="humidity">습도: 60%</p>
    </div>
  
    <!-- 더 많은 날씨 데이터... -->
</body>
</html>
```

### **종합 프로그램**

**weather_dashboard.py:**

```python
import tkinter as tk
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup
import csv
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class WeatherDashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("🌤️ 날씨 분석 대시보드")
        self.window.geometry("1000x700")
    
        self.weather_data = []
    
        # 한글 폰트 설정
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
    
        self.create_widgets()
  
    def create_widgets(self):
        """위젯 생성"""
        # 상단: 제어 버튼
        control_frame = tk.Frame(self.window)
        control_frame.pack(fill='x', padx=10, pady=10)
    
        tk.Button(control_frame, text="데이터 수집", command=self.scrape_data, width=12, bg='lightblue').pack(side='left', padx=5)
        tk.Button(control_frame, text="통계 보기", command=self.show_statistics, width=12, bg='lightgreen').pack(side='left', padx=5)
        tk.Button(control_frame, text="그래프", command=self.show_graphs, width=12, bg='lightyellow').pack(side='left', padx=5)
    
        # 중앙: 통계 요약
        self.stats_frame = tk.LabelFrame(self.window, text="📊 통계 요약", font=('맑은 고딕', 12, 'bold'))
        self.stats_frame.pack(fill='x', padx=10, pady=10)
    
        self.stats_text = tk.Text(self.stats_frame, height=8, font=('맑은 고딕', 10))
        self.stats_text.pack(fill='x', padx=10, pady=10)
    
        # 하단: 그래프 영역
        self.graph_frame = tk.Frame(self.window)
        self.graph_frame.pack(fill='both', expand=True, padx=10, pady=10)
  
    def scrape_data(self):
        """HTML에서 날씨 데이터 수집"""
        try:
            with open('weather_data.html', 'r', encoding='utf-8') as file:
                html = file.read()
        
            soup = BeautifulSoup(html, 'html.parser')
            weather_items = soup.find_all('div', class_='weather')
        
            self.weather_data = []
        
            for item in weather_items:
                date = item.find('p', class_='date').text
                temp_text = item.find('p', class_='temp').text
                rain_text = item.find('p', class_='rain').text
                humidity_text = item.find('p', class_='humidity').text
            
                # 숫자 추출
                temps = re.findall(r'-?\d+', temp_text)
                max_temp = int(temps[0])
                min_temp = int(temps[1])
            
                rain = int(re.findall(r'\d+', rain_text)[0])
                humidity = int(re.findall(r'\d+', humidity_text)[0])
            
                self.weather_data.append({
                    '날짜': date,
                    '최고기온': max_temp,
                    '최저기온': min_temp,
                    '강수량': rain,
                    '습도': humidity
                })
        
            # CSV 저장
            self.save_to_csv()
        
            messagebox.showinfo("성공", f"{len(self.weather_data)}개의 데이터를 수집했습니다!")
            self.show_statistics()
        
        except FileNotFoundError:
            messagebox.showerror("오류", "weather_data.html 파일이 없습니다!")
        except Exception as e:
            messagebox.showerror("오류", f"데이터 수집 오류: {e}")
  
    def save_to_csv(self):
        """CSV로 저장"""
        with open('weather_collected.csv', 'w', newline='', encoding='utf-8-sig') as file:
            fieldnames = ['날짜', '최고기온', '최저기온', '강수량', '습도']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
        
            writer.writeheader()
            writer.writerows(self.weather_data)
  
    def show_statistics(self):
        """통계 표시"""
        if not self.weather_data:
            messagebox.showwarning("경고", "데이터를 먼저 수집하세요!")
            return
    
        # 통계 계산
        max_temps = [d['최고기온'] for d in self.weather_data]
        min_temps = [d['최저기온'] for d in self.weather_data]
        rains = [d['강수량'] for d in self.weather_data]
        humidities = [d['습도'] for d in self.weather_data]
    
        avg_max_temp = sum(max_temps) / len(max_temps)
        avg_min_temp = sum(min_temps) / len(min_temps)
        total_rain = sum(rains)
        avg_humidity = sum(humidities) / len(humidities)
    
        # 텍스트 업데이트
        self.stats_text.delete('1.0', tk.END)
    
        stats_info = f"""
데이터 기간: {self.weather_data[0]['날짜']} ~ {self.weather_data[-1]['날짜']}
총 데이터 수: {len(self.weather_data)}일

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 기온
  평균 최고기온: {avg_max_temp:.1f}°C
  평균 최저기온: {avg_min_temp:.1f}°C
  최고 기록: {max(max_temps)}°C
  최저 기록: {min(min_temps)}°C

💧 강수량
  총 강수량: {total_rain}mm
  평균 강수량: {total_rain / len(rains):.1f}mm

💨 습도
  평균 습도: {avg_humidity:.1f}%
  최고 습도: {max(humidities)}%
  최저 습도: {min(humidities)}%
        """
    
        self.stats_text.insert('1.0', stats_info)
  
    def show_graphs(self):
        """그래프 표시"""
        if not self.weather_data:
            messagebox.showwarning("경고", "데이터를 먼저 수집하세요!")
            return
    
        # 기존 그래프 제거
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
    
        # 데이터 추출
        dates = [d['날짜'].split('-')[2] for d in self.weather_data]  # 일자만
        max_temps = [d['최고기온'] for d in self.weather_data]
        min_temps = [d['최저기온'] for d in self.weather_data]
        rains = [d['강수량'] for d in self.weather_data]
        humidities = [d['습도'] for d in self.weather_data]
    
        # 그래프 생성
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    
        # 1. 기온 그래프
        ax1.plot(dates, max_temps, marker='o', label='최고기온', color='red')
        ax1.plot(dates, min_temps, marker='o', label='최저기온', color='blue')
        ax1.set_title('일별 기온 변화')
        ax1.set_xlabel('일')
        ax1.set_ylabel('온도 (°C)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
    
        # 2. 강수량 막대 그래프
        ax2.bar(dates, rains, color='skyblue')
        ax2.set_title('일별 강수량')
        ax2.set_xlabel('일')
        ax2.set_ylabel('강수량 (mm)')
        ax2.grid(axis='y', alpha=0.3)
    
        # 3. 습도 그래프
        ax3.plot(dates, humidities, marker='s', color='green', linewidth=2)
        ax3.set_title('일별 습도')
        ax3.set_xlabel('일')
        ax3.set_ylabel('습도 (%)')
        ax3.grid(True, alpha=0.3)
    
        # 4. 기온 분포 히스토그램
        all_temps = max_temps + min_temps
        ax4.hist(all_temps, bins=10, color='lightcoral', edgecolor='black')
        ax4.set_title('기온 분포')
        ax4.set_xlabel('온도 (°C)')
        ax4.set_ylabel('빈도')
        ax4.grid(axis='y', alpha=0.3)
    
        plt.tight_layout()
    
        # 캔버스에 표시
        canvas = FigureCanvasTkAgg(fig, self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

# 프로그램 실행
if __name__ == "__main__":
    window = tk.Tk()
    app = WeatherDashboard(window)
    window.mainloop()
```

---

## 5️⃣ **프로젝트 발전 방향**

### **추가 기능 아이디어**

**프로젝트 1 (성적 관리) 확장:**

- 성적 추이 그래프
- 학생별 성적 변화 추적
- 석차 계산
- GUI 버전 제작

**프로젝트 2 (가계부) 확장:**

- 월별/연도별 비교
- 예산 설정 및 알림
- 반복 거래 자동 입력
- 영수증 사진 저장

**프로젝트 3 (날씨 대시보드) 확장:**

- 실시간 웹사이트 스크래핑
- 지역별 비교
- 일기예보 정확도 분석
- 날씨 알림 기능

---

## 📝 **프로젝트 체크리스트**

### **코드 품질**

- [ ] 클래스 구조 적절히 사용
- [ ] 함수/메서드 이름이 명확함
- [ ] 주석이 충분함
- [ ] 예외 처리가 되어 있음

### **기능**

- [ ] 모든 필수 기능 구현
- [ ] 사용자 입력 검증
- [ ] 데이터 저장/불러오기
- [ ] 오류 메시지 친절함

### **사용성**

- [ ] UI가 직관적임
- [ ] 버튼/메뉴가 논리적으로 배치
- [ ] 안내 메시지가 명확함
- [ ] 종료 시 데이터 저장 확인

---

## 💡 **최종 과제**

### **나만의 프로젝트 만들기**

위 3개 프로젝트를 참고하여 자신만의 프로젝트를 기획하고 구현하세요!

**프로젝트 주제 예시:**

1. 도서 관리 시스템
2. 운동 기록 앱
3. 단어장 프로그램
4. 할 일 관리 앱
5. 쇼핑몰 상품 가격 비교
6. 영화 추천 시스템
7. 식단 관리 프로그램
8. 주식 포트폴리오 관리
9. 블로그 게시글 분석
10. 음악 재생 목록 관리

**프로젝트 기획서 작성:**

```
1. 프로젝트 제목
2. 목적 (왜 만드는가?)
3. 주요 기능 (최소 5개)
4. 사용 기술 (클래스, GUI, CSV, 시각화 등)
5. 데이터 구조 (어떤 데이터를 다룰 것인가?)
6. 화면 설계 (간단한 스케치)
7. 개발 일정
```

---

## 🎓 **마무리**

축하합니다! 25장에 걸친 파이썬 프로그래밍 여정을 완주했습니다! 🎉

### **여러분이 배운 것들**

```
기초 → 중급 → 고급
  ↓      ↓      ↓
변수   클래스   프로젝트
조건문  파일    시각화
반복문  예외    GUI
함수   모듈    스크래핑
```

### **다음 단계**

**계속 성장하기:**

1. 매일 코딩하기 (30분이라도)
2. 오픈소스 프로젝트 기여
3. 코딩 문제 사이트 활용 (백준, 프로그래머스)
4. 개인 프로젝트 GitHub에 공유
5. 새로운 라이브러리 학습 (Django, Flask, Pandas 등)

**추천 학습 자료:**

- 📚 공식 문서: https://docs.python.org
- 💻 연습 사이트: https://programmers.co.kr
- 🎓 무료 강의: YouTube, Coursera
- 📖 추천 도서: "파이썬 코딩의 기술", "Effective Python"

---

## 🏆 **최종 메시지**

프로그래밍은 **도구**입니다.
여러분이 하고 싶은 일을 실현하는 도구입니다.

지금까지 배운 것들로 충분히 많은 것을 만들 수 있습니다.
두려워하지 말고 도전하세요!

> "The only way to learn a new programming language is by writing programs in it."
>
> - Dennis Ritchie

**Happy Coding! 🚀**

---

수고했습니다.  
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
