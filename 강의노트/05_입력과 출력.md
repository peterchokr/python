# 5장 입력과 출력

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 사용자로부터 다양한 형태의 입력을 받고, 출력을 보기 좋게 꾸미는 방법을 익히게 됩니다. 입력과 출력은 사용자와 프로그램이 소통하는 창구이므로, 이를 효과적으로 다루는 것은 매우 중요합니다.

---

## 1️⃣ **입력 받기 - input() 함수**

`input()` 함수는 사용자로부터 키보드 입력을 받는 가장 기본적인 방법입니다. 사용자가 입력한 값은 항상 문자열(str) 타입으로 반환됩니다.

### **기본 사용법**

```python
# 기본 입력
name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name}님!")

# 입력 프롬프트 없이 사용
age = input()
print(f"나이: {age}")
```

입력 프롬프트는 사용자에게 무엇을 입력해야 하는지 안내하는 메시지입니다. 명확한 프롬프트를 제공하면 사용자가 프로그램을 쉽게 사용할 수 있습니다.

### **입력값 타입 변환**

앞에서 배웠듯이 `input()`은 항상 문자열을 반환하므로, 숫자 계산이 필요하면 적절한 타입으로 변환해야 합니다.

```python
# 문자열로 입력받기
name = input("이름: ")

# 정수로 변환
age = int(input("나이: "))
height = int(input("키(cm): "))

# 실수로 변환
weight = float(input("몸무게(kg): "))
temperature = float(input("체온: "))

# 계산에 활용
bmi = weight / ((height / 100) ** 2)
print(f"BMI: {bmi:.2f}")
```

### **예제 1: 치킨 주문 시스템**

치킨집에서 주문을 받는 프로그램을 만들어봅시다.

```python
# 치킨 주문 시스템
print("=" * 40)
print("🍗 황금 치킨 주문 시스템 🍗")
print("=" * 40)

# 주문 정보 입력
customer_name = input("\n고객명: ")
phone = input("전화번호: ")
menu = input("메뉴 (후라이드/양념/반반): ")
quantity = int(input("수량: "))

# 가격 계산
price_per_chicken = 18000
total_price = price_per_chicken * quantity

# 배달비
delivery_fee = 3000

# 최종 금액
final_price = total_price + delivery_fee

# 주문 확인서 출력
print("\n" + "=" * 40)
print("주문 확인서")
print("=" * 40)
print(f"고객명: {customer_name}")
print(f"연락처: {phone}")
print(f"주문 메뉴: {menu} 치킨")
print(f"수량: {quantity}마리")
print("-" * 40)
print(f"치킨 금액: {total_price:,}원 ({price_per_chicken:,}원 × {quantity})")
print(f"배달비: {delivery_fee:,}원")
print("-" * 40)
print(f"총 결제 금액: {final_price:,}원")
print("=" * 40)
print("\n예상 배달 시간: 40~50분")
print("맛있게 드세요! 🍗")
```

---

## 2️⃣ **여러 값 동시 입력받기**

때로는 여러 값을 한 번에 입력받아야 할 때가 있습니다. `split()` 메서드를 활용하면 공백으로 구분된 값들을 분리할 수 있습니다.

```python
# 공백으로 구분된 여러 값 입력
data = input("이름과 나이를 입력하세요 (공백 구분): ")
name, age = data.split()
print(f"이름: {name}, 나이: {age}")

# 숫자 여러 개 입력
numbers = input("두 숫자를 입력하세요 (공백 구분): ")
num1, num2 = numbers.split()
num1 = int(num1)
num2 = int(num2)
print(f"합: {num1 + num2}")

# 더 간결하게
a, b = input("두 숫자 입력: ").split()
result = int(a) + int(b)
print(f"결과: {result}")
```

### **예제 2: 영화 티켓 예매**

영화관에서 티켓을 예매하는 프로그램입니다.

```python
# 영화 티켓 예매 시스템
print("🎬" + "=" * 38 + "🎬")
print("     CGV 영화 티켓 예매")
print("🎬" + "=" * 38 + "🎬")

# 영화 정보
movie_title = input("\n영화 제목: ")
screening_time = input("상영 시간 (예: 14:30): ")

# 예매 정보 (공백으로 구분하여 입력)
print("\n예매자 정보를 입력하세요")
name, phone = input("이름 전화번호: ").split()

# 티켓 수량
adult = int(input("성인 티켓 수: "))
teen = int(input("청소년 티켓 수: "))

# 가격 계산
adult_price = 14000
teen_price = 11000

total = (adult * adult_price) + (teen * teen_price)

# 예매 확인서
print("\n" + "🎟️" * 20)
print("예매 확인증")
print("🎟️" * 20)
print(f"\n영화: {movie_title}")
print(f"상영시간: {screening_time}")
print(f"예매자: {name}")
print(f"연락처: {phone}")
print("-" * 40)
print(f"성인 {adult}매 × {adult_price:,}원 = {adult * adult_price:,}원")
print(f"청소년 {teen}매 × {teen_price:,}원 = {teen * teen_price:,}원")
print("-" * 40)
print(f"총 결제금액: {total:,}원")
print("🎟️" * 20)
print("\n즐거운 관람 되세요! 🍿")
```

---

## 3️⃣ **출력하기 - print() 함수 심화**

`print()` 함수는 단순히 값을 출력하는 것 이상의 다양한 기능을 제공합니다.

### **여러 값 동시 출력**

```python
# 여러 값을 쉼표로 구분하여 출력
name = "김철수"
age = 25
city = "서울"

print(name, age, city)  # 김철수 25 서울 (기본: 공백으로 구분)
```

### **구분자 변경 (sep 매개변수)**

`sep` 매개변수를 사용하면 값들 사이의 구분자를 변경할 수 있습니다.

```python
# 구분자 변경
print("사과", "바나나", "오렌지")  # 사과 바나나 오렌지
print("사과", "바나나", "오렌지", sep=", ")  # 사과, 바나나, 오렌지
print("사과", "바나나", "오렌지", sep=" / ")  # 사과 / 바나나 / 오렌지
print("2024", "12", "25", sep="-")  # 2024-12-25

# 구분자 없이
print("010", "1234", "5678", sep="-")  # 010-1234-5678
print("Hello", "World", sep="")  # HelloWorld
```

### **줄바꿈 제어 (end 매개변수)**

기본적으로 `print()`는 출력 후 자동으로 줄을 바꿉니다. `end` 매개변수로 이를 변경할 수 있습니다.

```python
# 기본 동작 (줄바꿈)
print("첫 번째 줄")
print("두 번째 줄")

# 줄바꿈 제거
print("같은 줄에 ", end="")
print("출력됩니다")  # 같은 줄에 출력됩니다

# 다른 문자로 끝내기
print("로딩중", end="...")
print("완료!")  # 로딩중...완료!

# 프로그레스 바 표현
print("[", end="")
print("■" * 10, end="")
print("] 100%")  # [■■■■■■■■■■] 100%
```

### **예제 3: 카페 음료 주문서**

카페에서 음료를 주문하고 영수증을 출력하는 프로그램입니다.

```python
# 카페 음료 주문 시스템
print("☕" + "=" * 38 + "☕")
print("   스타벅스 주문 시스템")
print("☕" + "=" * 38 + "☕")

# 주문 정보
customer = input("\n고객명: ")
drink = input("음료: ")
size = input("사이즈 (Tall/Grande/Venti): ")

# 사이즈별 가격 안내
print("\n가격 안내:")
print("Tall: 4,500원")
print("Grande: 5,000원") 
print("Venti: 5,500원")

price = int(input(f"\n{size} 사이즈 가격 입력: "))

# 영수증 출력
print("\n" + "=" * 40)
print("STARBUCKS RECEIPT")
print("=" * 40)
print(f"Customer: {customer}")
print("-" * 40)
print(f"{drink} ({size})", end="")
print(f"{price:>22,}원")
print("-" * 40)
print(f"{'TOTAL':<20}{price:>20,}원")
print("=" * 40)
print("\n즐거운 하루 되세요! ☕")
```

---

## 4️⃣ **이스케이프 시퀀스 활용**

이스케이프 시퀀스를 활용하면 특수한 출력 효과를 만들 수 있습니다.

```python
# 다양한 이스케이프 시퀀스
print("첫 줄\n두 번째 줄\n세 번째 줄")  # 줄바꿈
print("이름\t나이\t도시")  # 탭
print("큰따옴표: \"Hello\"")  # 따옴표
print("경로: C:\\Users\\Python")  # 백슬래시

# 여러 줄 문자열
menu = """
┌─────────────────────┐
│      메뉴판         │
├─────────────────────┤
│ 1. 아메리카노  4,500원│
│ 2. 카페라떼    5,000원│
│ 3. 카푸치노    5,500원│
└─────────────────────┘
"""
print(menu)
```

---

## 5️⃣ **실용적인 입출력 패턴**

### **입력 검증 메시지**

```python
# 사용자에게 친절한 안내
print("=" * 40)
print("회원가입")
print("=" * 40)
print("\n※ 아이디는 5자 이상 입력해주세요")
user_id = input("아이디: ")

print("\n※ 비밀번호는 8자 이상 입력해주세요")
password = input("비밀번호: ")

print(f"\n가입 완료! 환영합니다, {user_id}님!")
```

### **진행 상황 표시**

```python
# 단계별 진행 표시
print("📝 주문 진행 중...")
print()

print("[1/4] 상품 선택")
product = input("상품명: ")

print("\n[2/4] 수량 입력")
quantity = int(input("수량: "))

print("\n[3/4] 배송지 입력")
address = input("주소: ")

print("\n[4/4] 연락처 입력")
phone = input("전화번호: ")

print("\n✅ 주문이 완료되었습니다!")
```

### **예제 4: 운동 칼로리 계산기**

운동량을 입력받아 소모 칼로리를 계산하는 프로그램입니다.

```python
# 운동 칼로리 계산기
print("🏃" + "=" * 38 + "🏃")
print("   운동 칼로리 계산기")
print("🏃" + "=" * 38 + "🏃")

# 사용자 정보
print("\n[1/5] 기본 정보 입력")
name = input("이름: ")
weight = float(input("체중(kg): "))

# 운동 정보
print("\n[2/5] 걷기 운동")
walk_time = int(input("걷기 시간(분): "))

print("\n[3/5] 달리기 운동")
run_time = int(input("달리기 시간(분): "))

print("\n[4/5] 자전거 운동")
bike_time = int(input("자전거 시간(분): "))

print("\n[5/5] 수영 운동")
swim_time = int(input("수영 시간(분): "))

# 칼로리 계산 (체중 60kg 기준 보정)
walk_cal = walk_time * 3.5 * (weight / 60)
run_cal = run_time * 10 * (weight / 60)
bike_cal = bike_time * 7 * (weight / 60)
swim_cal = swim_time * 11 * (weight / 60)

total_cal = walk_cal + run_cal + bike_cal + swim_cal
total_time = walk_time + run_time + bike_time + swim_time

# 결과 출력
print("\n" + "╔" + "═" * 48 + "╗")
print("║" + f"{name}님의 운동 리포트".center(48) + "║")
print("╠" + "═" * 48 + "╣")
print("║ " + "운동 종류".ljust(20) + "시간".rjust(10) + "칼로리".rjust(16) + " ║")
print("╟" + "─" * 48 + "╢")
print("║ " + "걷기".ljust(20) + f"{walk_time}분".rjust(10) + f"{walk_cal:.0f}kcal".rjust(16) + " ║")
print("║ " + "달리기".ljust(20) + f"{run_time}분".rjust(10) + f"{run_cal:.0f}kcal".rjust(16) + " ║")
print("║ " + "자전거".ljust(20) + f"{bike_time}분".rjust(10) + f"{bike_cal:.0f}kcal".rjust(16) + " ║")
print("║ " + "수영".ljust(20) + f"{swim_time}분".rjust(10) + f"{swim_cal:.0f}kcal".rjust(16) + " ║")
print("╟" + "─" * 48 + "╢")
print("║ " + "총 운동 시간".ljust(20) + f"{total_time}분".rjust(24) + " ║")
print("║ " + "총 소모 칼로리".ljust(20) + f"{total_cal:.0f}kcal".rjust(24) + " ║")
print("╚" + "═" * 48 + "╝")

# 치킨 환산
chicken_calories = 1800
chicken_count = total_cal / chicken_calories
print(f"\n🍗 치킨 환산: 약 {chicken_count:.2f}마리 소모!")
print("💪 오늘도 수고하셨습니다!")
```

---

## 📝 **핵심 개념 정리**

`input()` 함수는 사용자로부터 입력을 받으며, 항상 문자열을 반환합니다. 숫자 계산이 필요하면 `int()`나 `float()`로 변환해야 합니다. 여러 값을 동시에 입력받을 때는 `split()` 메서드를 활용할 수 있습니다.

`print()` 함수는 값을 출력하는 기본 함수로, `sep` 매개변수로 구분자를 변경하고 `end` 매개변수로 줄바꿈을 제어할 수 있습니다. 여러 값을 쉼표로 구분하여 한 번에 출력할 수 있습니다.

출력을 꾸밀 때는 박스 문자(`┌─┐│└┘╔═╗║╚╝`), 이모지, 정렬 기능 등을 활용하면 사용자에게 보기 좋은 인터페이스를 제공할 수 있습니다. f-string 포매팅과 문자열 메서드를 조합하면 전문적인 출력 형태를 만들 수 있습니다.

---

## 💡 **실습 과제**

### **과제 1: 배달 음식 주문 시스템**

피자 배달 주문을 받는 프로그램을 작성하세요. 고객 정보, 피자 종류, 사이즈, 수량을 입력받아 주문서를 출력하세요.

```
- 피자 가격: L(25,000원), M(20,000원), S(15,000원)
- 배달비: 3,000원
- 주문서를 보기 좋게 박스 형태로 출력
```

### **과제 2: 반려동물 정보 카드**

반려동물의 이름, 종류, 나이, 몸무게를 입력받아 예쁜 정보 카드를 만드는 프로그램을 작성하세요.

```python
# 힌트
print("🐶 반려동물 등록 🐶\n")

pet_name = input("이름: ")
pet_type = input("종류 (강아지/고양이/기타): ")
pet_age = int(input("나이: "))
pet_weight = float(input("몸무게(kg): "))

# 여기에 예쁜 카드 형태로 출력하는 코드를 작성하세요
```

---

## ✅ **퀴즈**

### **[초급] 1번**

`input()` 함수가 반환하는 데이터 타입은?

1. int
2. float
3. str
4. bool

### **[중급] 2번**

다음 코드의 실행 결과는?

```python
print("A", "B", "C", sep="-")
```

1. A B C
2. A-B-C
3. ABC
4. A, B, C

### **[중급] 3번**

다음 중 줄바꿈 없이 출력하는 방법은?

```python
print("Hello", _______)
```

1. sep=""
2. end=""
3. line=False
4. newline=False

### **[중급] 4번**

다음 코드에서 a와 b에 각각 10과 20을 입력했을 때 결과는?

```python
data = input("두 숫자 입력: ")
a, b = data.split()
result = int(a) + int(b)
print(result)
```

1. 1020
2. 30
3. "30"
4. 오류 발생

### **[고급] 5번**

다음 코드의 실행 결과는?

```python
name = "Python"
print("언어:", name, sep="***", end="!!!\n")
print("재미있어요")
```

1. 언어: Python!!!재미있어요
2. 언어***Python!!!재미있어요
3. 언어***Python재미있어요
4. 언어: Python
   재미있어요

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 3**
`input()` 함수는 사용자 입력을 항상 문자열(str) 타입으로 반환합니다. 숫자로 사용하려면 `int()`나 `float()`로 변환해야 합니다.

**2번 정답: 2**
`sep` 매개변수는 출력할 값들 사이의 구분자를 지정합니다. `sep="-"`는 값들을 `-`로 연결하므로 "A-B-C"가 출력됩니다.

**3번 정답: 2**
`end=""` 매개변수를 사용하면 print() 함수의 기본 줄바꿈을 제거할 수 있습니다. 기본값은 `end="\n"`입니다.

**4번 정답: 2**
"10 20"을 입력하면 `split()`으로 "10"과 "20"으로 분리되고, 각각 정수로 변환되어 10 + 20 = 30이 출력됩니다.

**5번 정답: 2**
`sep="***"`는 "언어"와 name 사이를 `***`로 연결하고, `end="!!!\n"`는 출력 끝에 `!!!`와 줄바꿈을 추가합니다. 따라서 "언어***Python!!!" 다음 줄에 "재미있어요"가 출력됩니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 조건문에 대해 배웁니다. if, elif, else를 사용하여 프로그램이 상황에 따라 다른 동작을 하도록 만드는 방법을 학습하게 됩니다. 드디어 프로그램에 판단 능력을 부여할 수 있게 됩니다!

---

수고했습니다.  
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
