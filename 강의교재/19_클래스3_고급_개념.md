# 19장 클래스 3 (고급 개념)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 파이썬 클래스의 고급 기능들을 활용할 수 있습니다. 특수 메서드, 프로퍼티, 정적 메서드 등을 사용하여 더욱 파이썬다운 전문적인 객체지향 코드를 작성할 수 있습니다.

---

## 1️⃣ **특수 메서드란?**

파이썬에는 `__`(언더스코어 2개)로 시작하고 끝나는 특별한 메서드들이 있습니다. 이를 **매직 메서드** 또는 **던더 메서드**(dunder methods)라고 부릅니다.

### **왜 특수 메서드가 필요한가?**

일반 함수처럼 객체를 다룰 수 있게 해줍니다.

```python
# 특수 메서드 없이
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

book = Book("파이썬", 20000)
print(book)  # <__main__.Book object at 0x...> (의미 없음!)

# 특수 메서드 사용
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
  
    def __str__(self):
        return f"{self.title} ({self.price:,}원)"

book = Book("파이썬", 20000)
print(book)  # 파이썬 (20,000원) (의미 있음!)
```

### **자주 사용하는 특수 메서드**

```
📋 주요 특수 메서드

초기화 및 표현
├─ __init__()     : 객체 생성시 호출
├─ __str__()      : print() 시 문자열 반환
├─ __repr__()     : 개발자용 문자열 반환
└─ __len__()      : len() 시 길이 반환

비교 연산
├─ __eq__()       : == 연산자
├─ __ne__()       : != 연산자
├─ __lt__()       : < 연산자
├─ __le__()       : <= 연산자
├─ __gt__()       : > 연산자
└─ __ge__()       : >= 연산자

산술 연산
├─ __add__()      : + 연산자
├─ __sub__()      : - 연산자
├─ __mul__()      : * 연산자
└─ __truediv__()  : / 연산자
```

---

## 2️⃣ **__str__과 __repr__**

객체를 문자열로 표현하는 방법을 정의합니다.

### **__str__ - 사용자용 표현**

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
  
    def __str__(self):
        """사용자에게 보여줄 문자열"""
        return f"{self.name} - {self.price:,}원 (재고: {self.stock}개)"

product = Product("노트북", 1500000, 5)
print(product)  # 노트북 - 1,500,000원 (재고: 5개)
```

### **__repr__ - 개발자용 표현**

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
  
    def __str__(self):
        """사용자용"""
        return f"{self.name} - {self.price:,}원"
  
    def __repr__(self):
        """개발자용 (디버깅용)"""
        return f"Product('{self.name}', {self.price}, {self.stock})"

product = Product("마우스", 30000, 10)
print(product)       # 마우스 - 30,000원 (__str__)
print(repr(product)) # Product('마우스', 30000, 10) (__repr__)
```

💡 **팁**: `__str__`이 없으면 `__repr__`이 사용됩니다.

---

## 3️⃣ **비교 연산자 오버로딩**

객체끼리 크기를 비교할 수 있게 만듭니다.

### **기본 예제**

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
  
    def __eq__(self, other):
        """== 연산자"""
        return self.score == other.score
  
    def __lt__(self, other):
        """< 연산자"""
        return self.score < other.score
  
    def __le__(self, other):
        """<= 연산자"""
        return self.score <= other.score
  
    def __str__(self):
        return f"{self.name}({self.score}점)"

# 학생 생성
student1 = Student("김철수", 85)
student2 = Student("박영희", 90)
student3 = Student("이민수", 85)

# 비교 연산
print(student1 == student3)  # True (점수가 같음)
print(student1 < student2)   # True (85 < 90)
print(student1 <= student3)  # True (85 <= 85)

# 정렬도 가능!
students = [student1, student2, student3]
students.sort()  # 점수 순으로 정렬
for s in students:
    print(s)
```

**실행 결과:**

```
True
True
True
김철수(85점)
이민수(85점)
박영희(90점)
```

### **실전 예제: 상품 가격 비교**

```python
class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
  
    def __eq__(self, other):
        """가격이 같은지"""
        return self.price == other.price
  
    def __lt__(self, other):
        """가격이 더 싼지"""
        return self.price < other.price
  
    def __gt__(self, other):
        """가격이 더 비싼지"""
        return self.price > other.price
  
    def __str__(self):
        return f"{self.name} ({self.price:,}원, ⭐{self.rating})"

# 상품 목록
products = [
    Product("무선 마우스", 35000, 4.5),
    Product("기계식 키보드", 120000, 4.8),
    Product("웹캠", 80000, 4.2),
    Product("모니터", 350000, 4.7)
]

print("📦 상품 목록")
for p in products:
    print(f"  {p}")

# 가격순 정렬
products.sort()
print("\n💰 가격순 정렬 (낮은 가격부터)")
for p in products:
    print(f"  {p}")

# 가장 싼 상품과 비싼 상품
cheapest = min(products)
most_expensive = max(products)

print(f"\n가장 저렴: {cheapest}")
print(f"가장 비쌈: {most_expensive}")
```

---

## 4️⃣ **산술 연산자 오버로딩**

객체끼리 더하고 빼는 연산을 정의합니다.

### **기본 예제: 벡터 클래스**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    def __add__(self, other):
        """벡터 덧셈"""
        return Vector(self.x + other.x, self.y + other.y)
  
    def __sub__(self, other):
        """벡터 뺄셈"""
        return Vector(self.x - other.x, self.y - other.y)
  
    def __mul__(self, scalar):
        """스칼라 곱"""
        return Vector(self.x * scalar, self.y * scalar)
  
    def __str__(self):
        return f"({self.x}, {self.y})"

# 벡터 연산
v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2  # __add__ 호출
v4 = v1 - v2  # __sub__ 호출
v5 = v1 * 2   # __mul__ 호출

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"v1 - v2 = {v4}")
print(f"v1 * 2 = {v5}")
```

**실행 결과:**

```
v1 = (3, 4)
v2 = (1, 2)
v1 + v2 = (4, 6)
v1 - v2 = (2, 2)
v1 * 2 = (6, 8)
```

### **실전 예제: 시간 클래스**

```python
class Time:
    """시간 클래스 (시:분)"""
  
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self._normalize()  # 60분 넘으면 시간으로 변환
  
    def _normalize(self):
        """시간 정규화"""
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute = self.minute % 60
        self.hour = self.hour % 24  # 24시간 넘으면 0으로
  
    def __add__(self, other):
        """시간 더하기"""
        return Time(self.hour + other.hour, 
                   self.minute + other.minute)
  
    def __sub__(self, other):
        """시간 빼기"""
        total_minutes1 = self.hour * 60 + self.minute
        total_minutes2 = other.hour * 60 + other.minute
        diff = total_minutes1 - total_minutes2
  
        if diff < 0:
            diff += 24 * 60  # 음수면 다음날로
  
        return Time(diff // 60, diff % 60)
  
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

# 시간 계산
work_start = Time(9, 0)    # 09:00
work_time = Time(8, 30)    # 8시간 30분 근무
lunch_time = Time(1, 0)    # 1시간 점심

work_end = work_start + work_time
print(f"출근: {work_start}")
print(f"근무시간: {work_time}")
print(f"퇴근: {work_end}")

print(f"\n점심시간: {lunch_time}")
actual_work = work_time - lunch_time
print(f"실제 근무: {actual_work}")
```

**실행 결과:**

```
출근: 09:00
근무시간: 08:30
퇴근: 17:30

점심시간: 01:00
실제 근무: 07:30
```

---

## 5️⃣ **프로퍼티 (Property) - 안전한 속성 관리**

프로퍼티는 "겉으로는 변수처럼 보이지만 실제로는 함수"입니다. 왜 이런 게 필요할까요?

### **문제 상황: 잘못된 값이 들어갈 수 있다**

```python
class Person:
    def __init__(self, age):
        self.age = age

person = Person(25)
print(person.age)  # 25

# 누군가 실수로 이상한 값을 넣으면?
person.age = -5      # 음수 나이?!
person.age = 999     # 999살?!
person.age = "스물"  # 문자?!
```

이렇게 변수에 직접 접근하면 이상한 값이 들어갈 수 있습니다. 프로그램이 망가질 수 있죠!

### **해결책: 프로퍼티 사용**

프로퍼티를 사용하면 값을 넣을 때 자동으로 검사할 수 있습니다.

```python
class Person:
    def __init__(self, age):
        self._age = age  # _age는 내부 변수 (숨김)
  
    @property
    def age(self):
        """나이 읽기"""
        return self._age
  
    @age.setter
    def age(self, value):
        """나이 쓰기 - 여기서 검사!"""
        if value < 0:
            print("❌ 나이는 0보다 작을 수 없습니다!")
            return
        if value > 150:
            print("❌ 나이가 너무 많습니다!")
            return
        self._age = value

# 사용
person = Person(25)
print(f"나이: {person.age}")  # 25 (읽기)

person.age = 30              # OK! (쓰기)
print(f"나이: {person.age}")  # 30

person.age = -5              # ❌ 나이는 0보다 작을 수 없습니다!
print(f"나이: {person.age}")  # 30 (변경 안 됨!)

person.age = 999             # ❌ 나이가 너무 많습니다!
print(f"나이: {person.age}")  # 30 (변경 안 됨!)
```

**핵심 포인트:**

- `@property`: "이 함수를 변수처럼 읽을 수 있게 해줘"
- `@age.setter`: "이 함수로 값을 쓸 때 검사해줘"
- 사용하는 사람은 `person.age`처럼 그냥 변수처럼 사용!

### **읽기 전용 속성 만들기**

계산된 값은 읽기만 가능하게 만들 수 있습니다.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    @property
    def area(self):
        """넓이 (읽기만 가능)"""
        return self.width * self.height

# 사용
rect = Rectangle(10, 5)
print(f"가로: {rect.width}")
print(f"세로: {rect.height}")
print(f"넓이: {rect.area}")  # 10 * 5 = 50

# 가로/세로는 변경 가능
rect.width = 20
print(f"새 넓이: {rect.area}")  # 20 * 5 = 100

# rect.area = 200  # 오류! setter가 없어서 쓰기 불가
```

넓이는 가로 × 세로로 자동 계산되므로 직접 바꿀 필요가 없습니다!

### **간단한 실전 예제: 학생 성적**

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score
  
    @property
    def score(self):
        """점수 읽기"""
        return self._score
  
    @score.setter
    def score(self, value):
        """점수 쓰기 (0-100 사이만 허용)"""
        if value < 0:
            print("❌ 점수는 0보다 작을 수 없습니다!")
            return
        if value > 100:
            print("❌ 점수는 100보다 클 수 없습니다!")
            return
        self._score = value
  
    @property
    def grade(self):
        """학점 (읽기 전용, 자동 계산)"""
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"
  
    def show_info(self):
        print(f"{self.name}: {self.score}점 ({self.grade}학점)")

# 학생 생성
student = Student("김철수", 85)
student.show_info()  # 김철수: 85점 (B학점)

# 점수 변경
student.score = 95
student.show_info()  # 김철수: 95점 (A학점)

# 잘못된 점수 입력
student.score = 150  # ❌ 점수는 100보다 클 수 없습니다!
student.show_info()  # 김철수: 95점 (A학점) - 변경 안 됨!
```

**정리:**

- 프로퍼티 = 안전한 변수
- `@property`: 읽기 함수
- `@변수이름.setter`: 쓰기 함수 (검사 가능)
- 자동 계산 값은 읽기 전용으로 만들기

---

## 6️⃣ **정적 메서드 - 클래스의 도구함**

정적 메서드는 클래스 안에 있지만 **객체와 상관없는 독립적인 함수**입니다. 마치 도구 상자에 넣어둔 도구처럼, 필요할 때 꺼내 쓰는 것입니다.

### **왜 정적 메서드를 사용할까?**

관련된 함수들을 클래스 안에 정리해서 모아두면 편리합니다.

```python
# 정적 메서드 없이 (함수가 여기저기 흩어짐)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 정적 메서드 사용 (깔끔하게 정리됨)
class Calculator:
    @staticmethod
    def add(a, b):
        """덧셈"""
        return a + b
  
    @staticmethod
    def subtract(a, b):
        """뺄셈"""
        return a - b

# 객체 생성 없이 바로 사용!
print(Calculator.add(10, 5))       # 15
print(Calculator.subtract(10, 5))  # 5
```

**핵심 포인트:**

- `@staticmethod`: "이 함수는 self가 필요 없어요"
- 객체 생성 안 해도 됨: `클래스이름.함수이름()`
- 유틸리티 함수 모음에 좋음!

### **간단한 예제 1: 문자열 도구**

```python
class StringUtil:
    """문자열 유틸리티"""
  
    @staticmethod
    def reverse(text):
        """문자열 뒤집기"""
        return text[::-1]
  
    @staticmethod
    def count_vowels(text):
        """모음 개수 세기"""
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count
  
    @staticmethod
    def is_palindrome(text):
        """회문 판별 (거꾸로 읽어도 같은 단어)"""
        text = text.replace(" ", "").lower()
        return text == text[::-1]

# 객체 생성 없이 바로 사용
print(StringUtil.reverse("Hello"))           # olleH
print(StringUtil.count_vowels("Python"))     # 1
print(StringUtil.is_palindrome("level"))     # True
print(StringUtil.is_palindrome("python"))    # False
```

### **간단한 예제 2: 계산 도구**

```python
class MathHelper:
    """수학 도구 모음"""
  
    @staticmethod
    def average(numbers):
        """평균 계산"""
        if len(numbers) == 0:
            return 0
        return sum(numbers) / len(numbers)
  
    @staticmethod
    def max_min_diff(numbers):
        """최댓값과 최솟값의 차이"""
        if len(numbers) == 0:
            return 0
        return max(numbers) - min(numbers)
  
    @staticmethod
    def even_count(numbers):
        """짝수 개수"""
        count = 0
        for num in numbers:
            if num % 2 == 0:
                count += 1
        return count

# 사용
scores = [85, 90, 78, 92, 88]

print(f"평균: {MathHelper.average(scores)}")           # 86.6
print(f"점수 차이: {MathHelper.max_min_diff(scores)}")  # 14
print(f"짝수 개수: {MathHelper.even_count(scores)}")    # 4
```

### **언제 사용하나요?**

**정적 메서드 사용:**

- ✅ 계산기 함수 (덧셈, 뺄셈 등)
- ✅ 문자열 처리 함수
- ✅ 날짜 계산 함수
- ✅ 유효성 검사 함수

**일반 메서드 사용:**

- ✅ 객체의 데이터가 필요할 때
- ✅ self.name, self.age 등을 사용할 때

### **클래스 메서드는 언제 쓰나요?**

클래스 변수(모든 객체가 공유하는 변수)를 다룰 때 사용합니다.

```python
class Student:
    # 클래스 변수 (모든 학생이 공유)
    school_name = "영남이공대학교"
    student_count = 0
  
    def __init__(self, name):
        self.name = name
        Student.student_count += 1  # 학생 수 증가
  
    @classmethod
    def get_school_name(cls):
        """학교 이름 (클래스 변수)"""
        return cls.school_name
  
    @classmethod
    def get_student_count(cls):
        """총 학생 수 (클래스 변수)"""
        return cls.student_count
  
    @classmethod
    def set_school_name(cls, name):
        """학교 이름 변경 (클래스 변수)"""
        cls.school_name = name

# 학생 3명 생성
s1 = Student("김철수")
s2 = Student("박영희")
s3 = Student("이민수")

# 클래스 메서드로 전체 정보 확인
print(f"학교: {Student.get_school_name()}")
print(f"총 학생 수: {Student.get_student_count()}명")

# 학교 이름 변경 (모든 학생에게 적용)
Student.set_school_name("다른대학교")
print(f"새 학교: {Student.get_school_name()}")
```

**정리:**

| 종류          | 데코레이터    | 첫 번째 매개변수 | 언제 사용?       |
| ------------- | ------------- | ---------------- | ---------------- |
| 일반 메서드   | 없음          | self             | 객체 데이터 필요 |
| 정적 메서드   | @staticmethod | 없음             | 독립 함수처럼    |
| 클래스 메서드 | @classmethod  | cls              | 클래스 변수 접근 |

**간단히 기억하기:**

- **일반 메서드**: "나(객체)의 데이터 필요해!"
- **정적 메서드**: "나는 혼자서도 일 잘해!"
- **클래스 메서드**: "우리(클래스) 모두의 데이터 필요해!"

---

## 7️⃣ **실전 예제: 도서 관리 시스템**

배운 내용을 활용한 간단한 도서 관리 시스템입니다.

```python
class Book:
    """도서 클래스"""
  
    # 클래스 변수
    total_books = 0
  
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = price
        Book.total_books += 1
  
    # 프로퍼티 (가격 검증)
    @property
    def price(self):
        """가격 읽기"""
        return self._price
  
    @price.setter
    def price(self, value):
        """가격 쓰기 (0 이상만 허용)"""
        if value < 0:
            print("❌ 가격은 0 이상이어야 합니다!")
            return
        self._price = value
  
    # 특수 메서드
    def __str__(self):
        """문자열 표현"""
        return f"{self.title} - {self.author} ({self.price:,}원)"
  
    def __eq__(self, other):
        """가격 비교 (==)"""
        return self.price == other.price
  
    def __lt__(self, other):
        """가격 비교 (<)"""
        return self.price < other.price
  
    # 정적 메서드
    @staticmethod
    def is_valid_price(price):
        """가격 유효성 검사"""
        return 0 <= price <= 100000
  
    # 클래스 메서드
    @classmethod
    def get_total_books(cls):
        """총 도서 수"""
        return cls.total_books

# 도서 목록 생성
print("📚 도서 관리 시스템\n")

books = [
    Book("파이썬 기초", "김철수", 20000),
    Book("자료구조", "박영희", 25000),
    Book("알고리즘", "이민수", 30000)
]

print("등록된 도서:")
for book in books:
    print(f"  {book}")

# 가격 변경
print("\n가격 변경:")
books[0].price = 18000
print(f"  {books[0]}")

# 잘못된 가격 시도
books[0].price = -5000  # 오류 메시지 출력, 변경 안 됨

# 가격순 정렬
books.sort()
print("\n가격순 정렬:")
for book in books:
    print(f"  {book}")

# 통계
print(f"\n총 도서 수: {Book.get_total_books()}권")

# 가격 검증
print(f"\n15000원 유효한가? {Book.is_valid_price(15000)}")
print(f"200000원 유효한가? {Book.is_valid_price(200000)}")
```

**실행 결과:**

```
📚 도서 관리 시스템

등록된 도서:
  파이썬 기초 - 김철수 (20,000원)
  자료구조 - 박영희 (25,000원)
  알고리즘 - 이민수 (30,000원)

가격 변경:
  파이썬 기초 - 김철수 (18,000원)
❌ 가격은 0 이상이어야 합니다!

가격순 정렬:
  파이썬 기초 - 김철수 (18,000원)
  자료구조 - 박영희 (25,000원)
  알고리즘 - 이민수 (30,000원)

총 도서 수: 3권

15000원 유효한가? True
200000원 유효한가? False
```

이 예제에서 사용한 기능:

- ✅ 프로퍼티 (`@property`, `@price.setter`)
- ✅ 특수 메서드 (`__str__`, `__lt__`, `__eq__`)
- ✅ 정적 메서드 (`@staticmethod`)
- ✅ 클래스 메서드 (`@classmethod`)
- ✅ 클래스 변수 (`total_books`)

---

## 📝 **핵심 개념 정리**

### **특수 메서드**

`__`로 시작하고 끝나는 메서드, 연산자나 내장 함수와 연동

```python
def __str__(self):      # print()
def __eq__(self, other): # ==
def __add__(self, other): # +
def __len__(self):       # len()
```

### **프로퍼티**

속성 접근시 메서드 실행

```python
@property
def name(self):         # 읽기
    return self._name

@name.setter
def name(self, value):  # 쓰기
    self._name = value
```

### **정적/클래스 메서드**

```python
@staticmethod
def static_method():    # 독립 함수

@classmethod
def class_method(cls):  # 클래스 변수 접근
```

---

## 💡 **실습 과제**

### **과제 1: 분수 클래스**

```python
# 힌트
class Fraction:
    def __init__(self, numerator, denominator):
        pass
  
    def __add__(self, other):
        # 분수 덧셈
        pass
  
    def __str__(self):
        # 문자열 표현
        pass
```

### **과제 2: 은행 계좌 (프로퍼티)**

```python
# 힌트
class Account:
    def __init__(self, balance):
        self._balance = balance
  
    @property
    def balance(self):
        pass
  
    @balance.setter
    def balance(self, value):
        # 잔액 검증
        pass
```

---

## ✅ **퀴즈**

### **[초급] 1번**

print(obj) 시 호출되는 메서드는?

```python
1. __print__
2. __str__
3. __show__
4. __display__
```

### **[중급] 2번**

프로퍼티 데코레이터는?

```python
1. @prop
2. @property
3. @getter
4. @attribute
```

### **[중급] 3번**

정적 메서드 데코레이터는?

```python
1. @static
2. @staticmethod
3. @classmethod
4. @method
```

### **[고급] 4번**

`obj1 + obj2` 시 호출되는 메서드는?

```python
1. __plus__
2. __sum__
3. __add__
4. __combine__
```

### **[고급] 5번**

`len(obj)` 시 호출되는 메서드는?

```python
1. __length__
2. __size__
3. __len__
4. __count__
```

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
`__str__` 메서드가 print() 시 호출됩니다.

**2번 정답: 2**
`@property` 데코레이터로 프로퍼티를 만듭니다.

**3번 정답: 2**
`@staticmethod` 데코레이터로 정적 메서드를 만듭니다.

**4번 정답: 3**
`__add__` 메서드가 + 연산자를 처리합니다.

**5번 정답: 3**
`__len__` 메서드가 len() 함수를 처리합니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 GUI 프로그래밍을 배웁니다. tkinter를 사용하여 버튼, 텍스트 상자 등이 있는 윈도우 프로그램을 만들 수 있게 됩니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
