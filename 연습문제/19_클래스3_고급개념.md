# 19장 클래스 3 (고급 개념) — 연습문제

---

## 📝 객관식 문제

---

### 🟢 초급

**문제 1.** `print(obj)` 호출 시 자동으로 실행되는 특수 메서드는?

① `__print__`
② `__str__`
③ `__show__`
④ `__display__`

---

**문제 2.** 특수 메서드(매직 메서드)의 이름 형태로 올바른 것은?

① `_method_`
② `__method`
③ `__method__`
④ `method__`

---

**문제 3.** 다음 코드의 실행 결과는?

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
  
    def __str__(self):
        return f"{self.title} ({self.price:,}원)"

book = Book("파이썬", 20000)
print(book)
```

① `<__main__.Book object at 0x...>`
② `파이썬 (20,000원)`
③ `Book(파이썬, 20000)`
④ 오류 발생

---

**문제 4.** `obj1 + obj2` 연산 시 호출되는 특수 메서드는?

① `__plus__`
② `__sum__`
③ `__add__`
④ `__combine__`

---

**문제 5.** `len(obj)` 호출 시 실행되는 특수 메서드는?

① `__length__`
② `__size__`
③ `__len__`
④ `__count__`

---

**문제 6.** 프로퍼티를 만들기 위한 데코레이터는?

① `@prop`
② `@property`
③ `@getter`
④ `@attribute`

---

**문제 7.** 정적 메서드(static method)의 데코레이터는?

① `@static`
② `@staticmethod`
③ `@classmethod`
④ `@method`

---

### 🟡 중급

**문제 8.** 다음 코드의 실행 결과는?

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
  
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2
print(v3)
```

① `(3, 4)`
② `(4, 6)`
③ `(1, 2)`
④ 오류 발생

---

**문제 9.** 프로퍼티에서 `@name.setter`의 역할은?

① 속성을 삭제할 때 호출
② **속성에 값을 쓸 때 호출** (검증 가능)
③ 속성을 읽을 때 호출
④ 속성을 출력할 때 호출

---

**문제 10.** 정적 메서드의 특징으로 올바른 것은?

① 반드시 `self`를 매개변수로 가진다
② 반드시 `cls`를 매개변수로 가진다
③ **객체 생성 없이 `클래스이름.메서드()`로 호출 가능**
④ 인스턴스 변수에 접근할 수 있다

---

**문제 11.** 다음 코드의 실행 결과는?

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
  
    def __eq__(self, other):
        return self.score == other.score
  
    def __lt__(self, other):
        return self.score < other.score

s1 = Student("김철수", 85)
s2 = Student("박영희", 85)
s3 = Student("이민수", 90)

print(s1 == s2)
print(s1 < s3)
```

① `False`, `True`
② `True`, `True`
③ `True`, `False`
④ `False`, `False`

---

**문제 12.** 클래스 메서드(`@classmethod`)의 첫 번째 매개변수는?

① `self`
② `cls`
③ `this`
④ 없음

---

### 🔴 고급

**문제 13.** 다음 코드의 실행 결과는?

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
  
    @property
    def celsius(self):
        return self._celsius
  
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            print("❌ 절대영도 이하 불가!")
            return
        self._celsius = value
  
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(100)
print(t.fahrenheit)
t.celsius = -300
print(t.celsius)
```

① `212.0`, `-300`
② `212.0`, `100`
③ `100`, `100`
④ 오류 발생

---

**문제 14.** 다음 코드의 실행 결과는?

```python
class Counter:
    def __init__(self):
        self.items = []
  
    def add(self, item):
        self.items.append(item)
  
    def __len__(self):
        return len(self.items)
  
    def __str__(self):
        return f"Counter({len(self)}개)"

c = Counter()
c.add("A")
c.add("B")
c.add("C")
print(len(c))
print(c)
```

① `0`, `Counter(0개)`
② `3`, `Counter(3개)`
③ 오류 발생
④ `3`, `[A, B, C]`

---

**문제 15.** 다음 코드에서 `__repr__`과 `__str__`의 차이에 대한 설명으로 올바른 것은?

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
  
    def __str__(self):
        return f"{self.name} - {self.price:,}원"
  
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
```

① `__str__`은 개발자용, `__repr__`은 사용자용이다
② **`__str__`은 사용자용(`print`), `__repr__`은 개발자용(`repr`/디버깅)**
③ 둘은 완전히 같은 역할이다
④ `__repr__`은 항상 오류를 발생시킨다

---

## 📝 주관식 문제

---

### 🟢 초급

**문제 16.** 특수 메서드(매직 메서드)란 무엇인지 설명하고, 다음 특수 메서드들이 각각 언제 호출되는지 쓰시오.

- `__init__`
- `__str__`
- `__len__`
- `__add__`
- `__eq__`

---

**문제 17.** 다음 코드의 실행 결과를 쓰시오.

```python
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
  
    def __str__(self):
        return f"{self.name}: {self.price}원"
  
    def __add__(self, other):
        return self.price + other.price
  
    def __eq__(self, other):
        return self.price == other.price

a = Fruit("사과", 3000)
b = Fruit("바나나", 2000)
c = Fruit("포도", 3000)

print(a)
print(a + b)
print(a == c)
print(a == b)
```

---

**문제 18.** 일반 메서드, 정적 메서드(`@staticmethod`), 클래스 메서드(`@classmethod`)의 차이점을 표로 정리하시오. 각각의 첫 번째 매개변수와 사용 목적을 설명하시오.

---

### 🟡 중급

**문제 19.** 프로퍼티(`@property`)가 필요한 이유를 설명하시오. 다음 코드에서 나이에 음수 값이 들어가는 문제를 프로퍼티로 해결하는 방법을 서술하시오.

```python
# 문제가 있는 코드
class Person:
    def __init__(self, age):
        self.age = age

p = Person(25)
p.age = -5  # 음수 나이가 들어감!
```

---

**문제 20.** 다음 코드의 실행 결과를 쓰고, `@property`로 만든 `grade`가 읽기 전용인 이유를 설명하시오.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score
  
    @property
    def score(self):
        return self._score
  
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            print("❌ 0~100 사이만 가능!")
  
    @property
    def grade(self):
        if self._score >= 90: return "A"
        elif self._score >= 80: return "B"
        elif self._score >= 70: return "C"
        else: return "F"

s = Student("김철수", 85)
print(f"{s.name}: {s.score}점 ({s.grade})")
s.score = 95
print(f"{s.name}: {s.score}점 ({s.grade})")
s.score = 150
print(f"{s.name}: {s.score}점 ({s.grade})")
```

---

### 🔴 고급

**문제 21.** 다음 코드의 실행 결과를 쓰고, `__lt__`가 정의되면 `sort()`와 `min()`/`max()`를 사용할 수 있는 이유를 설명하시오.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
  
    def __lt__(self, other):
        return self.price < other.price
  
    def __str__(self):
        return f"{self.name}({self.price:,}원)"

products = [
    Product("마우스", 35000),
    Product("키보드", 120000),
    Product("웹캠", 80000)
]

products.sort()
for p in products:
    print(p)

print(f"최저가: {min(products)}")
print(f"최고가: {max(products)}")
```

---

## 💻 실습형 문제

---

### 🟢 초급

**문제 22.** 다음 요구사항에 맞는 `Money` 클래스를 작성하시오.

> - `__init__(amount)`: 금액 저장
> - `__str__()`: `"10,000원"` 형태로 반환
> - `__add__(other)`: 금액 더하기 → 새 Money 객체 반환
> - `__sub__(other)`: 금액 빼기 → 새 Money 객체 반환
> - `__eq__(other)`: 금액 비교

출력 예시:

```python
m1 = Money(10000)
m2 = Money(5000)
m3 = m1 + m2
m4 = m1 - m2
print(m1)        # 10,000원
print(m3)        # 15,000원
print(m4)        # 5,000원
print(m1 == m2)  # False
```

---

**문제 23.** 다음 요구사항에 맞는 `WordCounter` 클래스를 작성하시오.

> - `__init__(text)`: 문장 저장
> - `__str__()`: 원본 문장 반환
> - `__len__()`: 단어 수 반환
> - `count_char()` 메서드: 공백 제외 글자 수 반환

출력 예시:

```python
wc = WordCounter("Hello Python World")
print(wc)         # Hello Python World
print(len(wc))    # 3
print(wc.count_char())  # 16
```

---

### 🟡 중급

**문제 24.** 다음 요구사항에 맞는 `BankAccount` 클래스를 작성하시오.

> - `_balance`를 프로퍼티로 관리
>   - `@property balance`: 잔액 읽기
>   - `@balance.setter`: 음수 불가 검증
> - `@property is_vip`: 잔액 100만원 이상이면 `True` (읽기 전용)
> - `deposit(amount)`, `withdraw(amount)` 메서드
> - `__str__()`: `"홍길동님 (잔액: 1,000,000원, VIP)"`

출력 예시:

```
acc = BankAccount("홍길동", 500000)
print(acc)          # 홍길동님 (잔액: 500,000원)
acc.deposit(600000)
print(acc)          # 홍길동님 (잔액: 1,100,000원, VIP)
print(acc.is_vip)   # True
acc.balance = -100  # ❌ 잔액은 음수일 수 없습니다!
```

---

**문제 25.** 다음 요구사항에 맞는 `Scoreboard` 클래스를 작성하시오.

> - 점수 리스트를 내부에 저장
> - `add(score)`: 0~100 사이만 추가
> - `__len__()`: 점수 개수
> - `__str__()`: 모든 점수 문자열
> - `__lt__(other)`: 평균 점수로 비교
> - `@property average`: 평균 (읽기 전용)
> - `@property best`: 최고 점수 (읽기 전용)
> - `@staticmethod is_passing(score)`: 60점 이상이면 `True`

출력 예시:

```
수학 = Scoreboard("수학")
영어 = Scoreboard("영어")
수학 점수: [85, 90, 78], 영어 점수: [92, 88, 95]

수학: 84.3점 (3개)
영어: 91.7점 (3개)
수학 < 영어? True
Scoreboard.is_passing(55) → False
```

---

### 🔴 고급

**문제 26.** 다음 요구사항에 맞는 `Playlist` 클래스를 작성하시오.

> 음악 재생 목록 관리 시스템입니다.
>
> - `Song` 클래스: `title`, `artist`, `duration`(초) 속성
>   - `__str__()`: `"제목 - 아티스트 (3:30)"` 형태
>   - `__eq__()`: 제목과 아티스트가 같으면 동일
>   - `__lt__()`: 재생시간으로 비교
> - `Playlist` 클래스: 곡 목록 관리
>   - `add(song)`: 곡 추가 (중복 방지: `__eq__` 활용)
>   - `remove(title)`: 제목으로 삭제
>   - `__len__()`: 곡 수
>   - `__str__()`: 전체 목록 출력
>   - `@property total_duration`: 총 재생시간 (읽기 전용)
>   - `@staticmethod format_time(seconds)`: 초를 `"분:초"` 형태로 변환
>   - `sort_by_duration()`: 재생시간순 정렬

출력 예시:

```
=== 내 플레이리스트 (3곡) ===
1. Dynamite - BTS (3:19)
2. FLOWER - JISOO (3:10)
3. Super Shy - NewJeans (2:34)
총 재생시간: 9:03

[재생시간순 정렬]
1. Super Shy - NewJeans (2:34)
2. FLOWER - JISOO (3:10)
3. Dynamite - BTS (3:19)
```

---

---

# 🔑 정답 및 해설

---

## 📝 객관식 정답

---

### 🟢 초급

**문제 1. 정답: ② `__str__`**

`print()` 호출 시 객체의 `__str__` 메서드가 자동으로 호출되어 문자열을 반환합니다.

---

**문제 2. 정답: ③ `__method__`**

특수 메서드(매직 메서드)는 `__`(언더스코어 2개)로 시작하고 끝나는 형태입니다. 예: `__init__`, `__str__`, `__add__`

---

**문제 3. 정답: ② `파이썬 (20,000원)`**

`__str__`이 정의되어 있으므로 `print(book)` 시 `__str__`이 호출되어 `"파이썬 (20,000원)"`이 출력됩니다.

---

**문제 4. 정답: ③ `__add__`**

`+` 연산자를 사용하면 왼쪽 객체의 `__add__` 메서드가 호출됩니다.

---

**문제 5. 정답: ③ `__len__`**

`len()` 함수 호출 시 객체의 `__len__` 메서드가 자동으로 호출됩니다.

---

**문제 6. 정답: ② `@property`**

`@property` 데코레이터로 메서드를 속성처럼 접근할 수 있게 만듭니다.

---

**문제 7. 정답: ② `@staticmethod`**

`@staticmethod` 데코레이터로 `self` 없이 독립적으로 동작하는 정적 메서드를 만듭니다.

---

### 🟡 중급

**문제 8. 정답: ② `(4, 6)`**

`v1 + v2`는 `v1.__add__(v2)`를 호출합니다. `Vector(3+1, 4+2) = Vector(4, 6)`. `__str__`에 의해 `"(4, 6)"`이 출력됩니다.

---

**문제 9. 정답: ② 속성에 값을 쓸 때 호출 (검증 가능)**

`@name.setter`는 `obj.name = 값` 형태로 속성에 값을 대입할 때 호출됩니다. 이 안에서 값의 유효성을 검사할 수 있습니다.

---

**문제 10. 정답: ③ 객체 생성 없이 `클래스이름.메서드()`로 호출 가능**

정적 메서드는 `self`가 없어 객체 데이터에 접근하지 않으며, `클래스이름.메서드()`로 직접 호출할 수 있습니다.

---

**문제 11. 정답: ② `True`, `True`**

- `s1 == s2`: `85 == 85` → `True` (`__eq__`)
- `s1 < s3`: `85 < 90` → `True` (`__lt__`)

---

**문제 12. 정답: ② `cls`**

클래스 메서드는 첫 번째 매개변수로 클래스 자체를 가리키는 `cls`를 받습니다.

---

### 🔴 고급

**문제 13. 정답: ② `212.0`, `100`**

- `t.fahrenheit` → `100 * 9/5 + 32 = 212.0`
- `t.celsius = -300` → `-300 < -273`이므로 "절대영도 이하 불가!" 출력, 변경 안 됨
- `t.celsius` → 여전히 `100`

---

**문제 14. 정답: ② `3`, `Counter(3개)`**

- `len(c)` → `__len__` 호출 → `len(self.items) = 3`
- `print(c)` → `__str__` 호출 → `f"Counter({len(self)}개)"` → `"Counter(3개)"`

---

**문제 15. 정답: ② `__str__`은 사용자용(`print`), `__repr__`은 개발자용(`repr`/디버깅)**

`__str__`은 `print()` 시 호출되어 사용자에게 보기 좋은 문자열을 반환합니다. `__repr__`은 `repr()` 호출이나 대화형 셸에서 호출되어 개발자가 디버깅하기 좋은 정보를 반환합니다.

---

## 📝 주관식 정답

---

### 🟢 초급

**문제 16. 모범답안:**

특수 메서드(매직 메서드)는 `__`로 시작하고 끝나는 메서드로, 파이썬의 내장 함수나 연산자와 연동됩니다.

- **`__init__`**: 객체가 **생성될 때** 자동으로 호출됩니다. (생성자)
- **`__str__`**: **`print()`** 호출 시 문자열을 반환합니다.
- **`__len__`**: **`len()`** 호출 시 길이를 반환합니다.
- **`__add__`**: **`+` 연산자** 사용 시 호출됩니다.
- **`__eq__`**: **`==` 연산자** 사용 시 호출됩니다.

---

**문제 17. 모범답안:**

```
사과: 3000원
5000
True
False
```

- `print(a)` → `__str__` 호출 → `"사과: 3000원"`
- `a + b` → `__add__` 호출 → `3000 + 2000 = 5000`
- `a == c` → `__eq__` 호출 → `3000 == 3000` → `True`
- `a == b` → `__eq__` 호출 → `3000 == 2000` → `False`

---

**문제 18. 모범답안:**

| 구분          | 데코레이터        | 첫 번째 매개변수      | 사용 목적                                                          |
| ------------- | ----------------- | --------------------- | ------------------------------------------------------------------ |
| 일반 메서드   | 없음              | `self` (객체 자신)  | 객체의 데이터(`self.속성`)에 접근하고 변경할 때                  |
| 정적 메서드   | `@staticmethod` | 없음                  | 객체/클래스와 무관한 독립 함수. 관련 유틸리티를 클래스에 묶어 정리 |
| 클래스 메서드 | `@classmethod`  | `cls` (클래스 자체) | 클래스 변수에 접근하거나 변경할 때                                 |

---

### 🟡 중급

**문제 19. 모범답안:**

프로퍼티가 필요한 이유: 속성에 직접 접근하면 유효하지 않은 값(음수 나이, 150점 이상 등)이 들어갈 수 있습니다. 프로퍼티를 사용하면 값을 읽거나 쓸 때 자동으로 검증 함수가 실행됩니다.

해결 방법:

```python
class Person:
    def __init__(self, age):
        self._age = age  # 내부 변수로 저장
  
    @property
    def age(self):          # 읽기
        return self._age
  
    @age.setter
    def age(self, value):   # 쓰기 + 검증
        if value < 0:
            print("❌ 나이는 음수일 수 없습니다!")
            return
        self._age = value
```

`person.age = -5` 실행 시 setter가 호출되어 음수를 거부합니다. 사용자는 `person.age`처럼 일반 변수와 동일하게 사용하면서도 자동으로 검증이 이루어집니다.

---

**문제 20. 모범답안:**

**실행 결과:**

```
김철수: 85점 (B)
김철수: 95점 (A)
❌ 0~100 사이만 가능!
김철수: 95점 (A)
```

- `score = 85` → B학점 출력
- `score = 95` → setter에서 0~100 범위 확인 후 변경 → A학점
- `score = 150` → 범위 초과로 오류 메시지, 값 변경 안 됨 → 여전히 95점 A학점

`grade`가 읽기 전용인 이유: `@property`만 있고 `@grade.setter`가 없기 때문입니다. 학점은 점수에 따라 자동으로 계산되는 값이므로 직접 변경할 수 없어야 합니다.

---

### 🔴 고급

**문제 21. 모범답안:**

**실행 결과:**

```
마우스(35,000원)
웹캠(80,000원)
키보드(120,000원)
최저가: 마우스(35,000원)
최고가: 키보드(120,000원)
```

`__lt__`(less than)가 정의되면 파이썬의 `sort()`, `min()`, `max()` 등의 정렬/비교 함수가 자동으로 이 메서드를 사용합니다. `sort()`는 내부적으로 `<` 연산자를 반복 사용하여 정렬하고, `min()`/`max()`도 요소끼리 비교할 때 `__lt__`를 호출합니다. 따라서 `__lt__`만 정의해도 가격 기준 정렬과 최소/최대 찾기가 모두 가능합니다.

---

## 💻 실습형 정답

---

### 🟢 초급

**문제 22. 모범답안:**

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
  
    def __str__(self):
        return f"{self.amount:,}원"
  
    def __add__(self, other):
        return Money(self.amount + other.amount)
  
    def __sub__(self, other):
        return Money(self.amount - other.amount)
  
    def __eq__(self, other):
        return self.amount == other.amount

# 테스트
m1 = Money(10000)
m2 = Money(5000)
m3 = m1 + m2
m4 = m1 - m2
print(m1)
print(m3)
print(m4)
print(m1 == m2)
```

핵심: `__add__`와 `__sub__`는 새로운 `Money` 객체를 반환하여 원본을 변경하지 않습니다.

---

**문제 23. 모범답안:**

```python
class WordCounter:
    def __init__(self, text):
        self.text = text
  
    def __str__(self):
        return self.text
  
    def __len__(self):
        return len(self.text.split())
  
    def count_char(self):
        return len(self.text.replace(" ", ""))

# 테스트
wc = WordCounter("Hello Python World")
print(wc)
print(len(wc))
print(wc.count_char())
```

핵심: `__len__`을 정의하면 `len(wc)` 형태로 호출할 수 있습니다.

---

### 🟡 중급

**문제 24. 모범답안:**

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
  
    @property
    def balance(self):
        return self._balance
  
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("❌ 잔액은 음수일 수 없습니다!")
            return
        self._balance = value
  
    @property
    def is_vip(self):
        return self._balance >= 1000000
  
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
  
    def withdraw(self, amount):
        if amount > self._balance:
            print("❌ 잔액 부족!")
            return
        self._balance -= amount
  
    def __str__(self):
        vip = ", VIP" if self.is_vip else ""
        return f"{self.owner}님 (잔액: {self._balance:,}원{vip})"

# 테스트
acc = BankAccount("홍길동", 500000)
print(acc)
acc.deposit(600000)
print(acc)
print(acc.is_vip)
acc.balance = -100
```

핵심: `balance`를 프로퍼티로 관리하여 음수 방지. `is_vip`는 읽기 전용 프로퍼티입니다.

---

**문제 25. 모범답안:**

```python
class Scoreboard:
    def __init__(self, subject):
        self.subject = subject
        self.scores = []
  
    def add(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
  
    def __len__(self):
        return len(self.scores)
  
    def __str__(self):
        return f"{self.subject}: {self.average:.1f}점 ({len(self)}개)"
  
    def __lt__(self, other):
        return self.average < other.average
  
    @property
    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)
  
    @property
    def best(self):
        if len(self.scores) == 0:
            return 0
        return max(self.scores)
  
    @staticmethod
    def is_passing(score):
        return score >= 60

# 테스트
math_board = Scoreboard("수학")
eng_board = Scoreboard("영어")

for s in [85, 90, 78]:
    math_board.add(s)
for s in [92, 88, 95]:
    eng_board.add(s)

print(math_board)
print(eng_board)
print(f"수학 < 영어? {math_board < eng_board}")
print(f"수학 최고: {math_board.best}")
print(f"55점 합격? {Scoreboard.is_passing(55)}")
```

핵심: `__lt__`로 평균 비교, `@property`로 평균/최고점 자동 계산, `@staticmethod`로 독립 유틸 함수 제공.

---

### 🔴 고급

**문제 26. 모범답안:**

```python
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # 초 단위
  
    def __str__(self):
        time_str = Playlist.format_time(self.duration)
        return f"{self.title} - {self.artist} ({time_str})"
  
    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist
  
    def __lt__(self, other):
        return self.duration < other.duration

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
  
    def add(self, song):
        if song in self.songs:
            print(f"❌ '{song.title}'은(는) 이미 있습니다!")
            return
        self.songs.append(song)
  
    def remove(self, title):
        for i, song in enumerate(self.songs):
            if song.title == title:
                self.songs.pop(i)
                return
  
    def __len__(self):
        return len(self.songs)
  
    def __str__(self):
        result = f"=== {self.name} ({len(self)}곡) ==="
        for i, song in enumerate(self.songs, 1):
            result += f"\n{i}. {song}"
        total = Playlist.format_time(self.total_duration)
        result += f"\n총 재생시간: {total}"
        return result
  
    @property
    def total_duration(self):
        total = 0
        for song in self.songs:
            total += song.duration
        return total
  
    @staticmethod
    def format_time(seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"
  
    def sort_by_duration(self):
        self.songs.sort()

# 테스트
playlist = Playlist("내 플레이리스트")
playlist.add(Song("Dynamite", "BTS", 199))
playlist.add(Song("FLOWER", "JISOO", 190))
playlist.add(Song("Super Shy", "NewJeans", 154))

print(playlist)

print("\n[재생시간순 정렬]")
playlist.sort_by_duration()
for i, song in enumerate(playlist.songs, 1):
    print(f"{i}. {song}")
```

핵심 포인트:

- `Song`의 `__eq__`을 정의하여 `if song in self.songs`로 중복 검사가 가능합니다.
- `Song`의 `__lt__`을 정의하여 `self.songs.sort()`로 재생시간순 정렬이 가능합니다.
- `@property total_duration`은 곡 목록이 변경될 때마다 자동으로 재계산됩니다.
- `@staticmethod format_time`은 객체와 무관하게 초→분:초 변환만 수행합니다.

---


수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 연습문제는 Claude 및 Gemini와 협업으로 제작되었습니다.
