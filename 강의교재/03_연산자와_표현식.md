# 3장 연산자와 표현식

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 다양한 연산자를 사용하여 계산을 수행하고, 조건을 판단하며, 복잡한 표현식을 작성할 수 있게 됩니다. 연산자는 프로그래밍의 기본 도구이며, 이를 잘 활용하면 강력한 프로그램을 만들 수 있습니다.

---

## 1️⃣ **산술 연산자**

산술 연산자는 수학 계산을 수행하는 연산자입니다. 우리가 일상생활에서 계산기를 사용할 때처럼, 프로그래밍에서도 덧셈, 뺄셈, 곱셈, 나눗셈 등의 기본 연산을 수행할 수 있습니다.

### **기본 산술 연산자**

파이썬은 다음과 같은 산술 연산자를 제공합니다.

```python
# 덧셈 (+)
result = 10 + 5
print(result)  # 15

# 뺄셈 (-)
result = 10 - 5
print(result)  # 5

# 곱셈 (*)
result = 10 * 5
print(result)  # 50

# 나눗셈 (/)
result = 10 / 3
print(result)  # 3.3333333333333335 (항상 실수 반환)
```

나눗셈(`/`)은 항상 실수(float)를 반환한다는 점을 기억하세요. 정수끼리 나누더라도 결과는 실수입니다. 예를 들어 `10 / 2`의 결과는 `5`가 아니라 `5.0`입니다.

### **특수 산술 연산자**

파이썬은 일반적인 산술 연산자 외에도 특별한 기능을 가진 연산자들을 제공합니다.

```python
# 정수 나눗셈 또는 몫 (//)
result = 10 // 3
print(result)  # 3 (소수점 이하 버림)

# 나머지 (%)
result = 10 % 3
print(result)  # 1 (10을 3으로 나눈 나머지)

# 거듭제곱 (**)
result = 2 ** 3
print(result)  # 8 (2의 3승)
```

정수 나눗셈(`//`)은 나눗셈의 몫만 반환하며, 소수점 이하는 버립니다. 나머지 연산자(`%`)는 나눗셈의 나머지를 반환합니다. 이 두 연산자는 짝수/홀수 판별, 배수 확인 등 다양한 곳에서 유용하게 사용됩니다.

```
산술 연산자 정리

┌─────────────┬──────────┬─────────────┐
│  연산자     │   기호    │   예시      │
├─────────────┼──────────┼─────────────┤
│  덧셈        │    +     │  10 + 3 = 13│
│  뺄셈        │    -     │  10 - 3 = 7 │
│  곱셈        │    *     │  10 * 3 = 30│
│  나눗셈      │    /     │  10 / 3 = 3.33│
│  정수 나눗셈 │    //    │  10 // 3 = 3│
│  나머지      │    %     │  10 % 3 = 1 │
│  거듭제곱    │    **    │  2 ** 3 = 8 │
└─────────────┴──────────┴─────────────┘
```

### **예제 1: 쇼핑몰 할인 계산기**

실생활에서 온라인 쇼핑을 할 때 할인가를 계산하는 프로그램을 만들어봅시다.

```python
# 쇼핑몰 할인 계산 프로그램
print("=== 쇼핑몰 할인 계산기 ===")

# 상품 정보 입력
original_price = int(input("원가를 입력하세요: "))
discount_rate = int(input("할인율을 입력하세요 (예: 20): "))

# 할인 금액 계산
discount_amount = original_price * discount_rate / 100

# 최종 가격 계산
final_price = original_price - discount_amount

# 결과 출력
print(f"\n원가: {original_price:,}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {discount_amount:,.0f}원")
print(f"최종 가격: {final_price:,.0f}원")
```

이 프로그램은 원가에 할인율을 곱해서 할인 금액을 계산하고, 원가에서 할인 금액을 빼서 최종 가격을 구합니다. 실제 쇼핑몰 앱에서 사용하는 것과 같은 계산 방식입니다.

---

## 2️⃣ **비교 연산자**

비교 연산자는 두 값을 비교하여 참(True) 또는 거짓(False)을 반환하는 연산자입니다. 조건문을 작성할 때 매우 중요하게 사용됩니다.

### **기본 비교 연산자**

```python
# 같음 (==)
print(5 == 5)   # True
print(5 == 3)   # False

# 같지 않음 (!=)
print(5 != 3)   # True
print(5 != 5)   # False

# 크다 (>)
print(5 > 3)    # True
print(3 > 5)    # False

# 작다 (<)
print(3 < 5)    # True
print(5 < 3)    # False

# 크거나 같다 (>=)
print(5 >= 5)   # True
print(5 >= 3)   # True
print(3 >= 5)   # False

# 작거나 같다 (<=)
print(3 <= 5)   # True
print(5 <= 5)   # True
print(5 <= 3)   # False
```

비교 연산자를 사용할 때 주의할 점이 있습니다. 등호(`=`)와 비교 연산자(`==`)를 혼동하지 말아야 합니다. 등호는 값을 할당하는 것이고, 이중 등호는 두 값이 같은지 비교하는 것입니다.

```python
# 잘못된 예
x = 5
# if x = 10:  # 오류! 할당 연산자를 사용

# 올바른 예
if x == 10:  # 비교 연산자 사용
    print("x는 10입니다")
```

### **예제 2: 나이 확인 프로그램**

사용자의 나이를 입력받아 성인인지 미성년자인지 판별하는 프로그램입니다.

```python
# 나이 확인 프로그램
print("=== 나이 확인 시스템 ===")

age = int(input("나이를 입력하세요: "))

# 성인 여부 확인
is_adult = age >= 18

print(f"\n입력하신 나이: {age}세")
print(f"성인 여부: {is_adult}")

if is_adult:
    print("성인입니다. 모든 콘텐츠에 접근할 수 있습니다.")
else:
    print("미성년자입니다. 일부 콘텐츠가 제한됩니다.")
```

---

## 3️⃣ **논리 연산자**

논리 연산자는 여러 조건을 결합하여 복잡한 조건식을 만들 때 사용합니다. 일상생활에서 "그리고", "또는", "아니다"와 같은 논리를 프로그래밍으로 표현하는 방법입니다.

### **기본 논리 연산자**

파이썬은 세 가지 논리 연산자를 제공합니다: `and`, `or`, `not`.

```python
# and 연산자 - 두 조건이 모두 참일 때만 True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# or 연산자 - 둘 중 하나라도 참이면 True
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# not 연산자 - 참을 거짓으로, 거짓을 참으로
print(not True)         # False
print(not False)        # True
```

논리 연산자는 비교 연산자와 함께 사용하여 복잡한 조건을 만들 수 있습니다.

```python
age = 25
has_license = True

# 18세 이상이고 면허가 있으면
can_drive = age >= 18 and has_license
print(can_drive)  # True

# 18세 미만이거나 면허가 없으면
cannot_drive = age < 18 or not has_license
print(cannot_drive)  # False
```

```
논리 연산자 진리표

AND 연산자
┌───────┬───────┬────────┐
│   A   │   B   │ A and B│
├───────┼───────┼────────┤
│ True  │ True  │  True  │
│ True  │ False │  False │
│ False │ True  │  False │
│ False │ False │  False │
└───────┴───────┴────────┘

OR 연산자
┌───────┬───────┬────────┐
│   A   │   B   │ A or B │
├───────┼───────┼────────┤
│ True  │ True  │  True  │
│ True  │ False │  True  │
│ False │ True  │  True  │
│ False │ False │  False │
└───────┴───────┴────────┘

NOT 연산자
┌───────┬────────┐
│   A   │ not A  │
├───────┼────────┤
│ True  │ False  │
│ False │ True   │
└───────┴────────┘
```

### **예제 3: 학점 판정 시스템**

학생의 출석률과 시험 점수를 종합하여 합격 여부를 판정하는 프로그램입니다.

```python
# 학점 판정 시스템
print("=== 학점 판정 시스템 ===")

# 학생 정보 입력
attendance_rate = int(input("출석률을 입력하세요 (0-100): "))
exam_score = int(input("시험 점수를 입력하세요 (0-100): "))

# 합격 조건: 출석률 80% 이상 AND 시험 점수 60점 이상
passed = attendance_rate >= 80 and exam_score >= 60

# 우수 학생: 출석률 95% 이상 AND 시험 점수 90점 이상
excellent = attendance_rate >= 95 and exam_score >= 90

# 재수강 대상: 출석률 80% 미만 OR 시험 점수 60점 미만
retake = attendance_rate < 80 or exam_score < 60

# 결과 출력
print(f"\n출석률: {attendance_rate}%")
print(f"시험 점수: {exam_score}점")
print(f"합격 여부: {passed}")
print(f"우수 학생: {excellent}")
print(f"재수강 대상: {retake}")

if excellent:
    print("축하합니다! 우수 학생입니다.")
elif passed:
    print("합격입니다.")
else:
    print("재수강이 필요합니다.")
```

---

## 4️⃣ **대입 연산자**

대입 연산자는 변수에 값을 저장하는 연산자입니다. 기본 대입 연산자(`=`) 외에도 산술 연산과 대입을 동시에 수행하는 복합 대입 연산자들이 있습니다.

### **복합 대입 연산자**

복합 대입 연산자는 변수의 값을 변경할 때 코드를 간결하게 만들어줍니다.

```python
# 기본 대입
x = 10

# 복합 대입 연산자
x += 5   # x = x + 5와 동일
print(x)  # 15

x -= 3   # x = x - 3과 동일
print(x)  # 12

x *= 2   # x = x * 2와 동일
print(x)  # 24

x /= 4   # x = x / 4와 동일
print(x)  # 6.0

x //= 2  # x = x // 2와 동일
print(x)  # 3.0

x %= 2   # x = x % 2와 동일
print(x)  # 1.0

x **= 3  # x = x ** 3과 동일
print(x)  # 1.0
```

복합 대입 연산자는 특히 카운터 변수를 증가시키거나 누적 합계를 계산할 때 자주 사용됩니다.

```python
# 점수 누적 계산
total_score = 0
total_score += 85  # 첫 번째 시험
total_score += 90  # 두 번째 시험
total_score += 88  # 세 번째 시험
print(f"총점: {total_score}")  # 263

# 카운터 증가
count = 0
count += 1  # 1 증가
count += 1  # 1 증가
count += 1  # 1 증가
print(f"카운트: {count}")  # 3
```

### **예제 4: 게임 점수 계산**

게임에서 점수를 누적하고 레벨을 올리는 프로그램입니다.

```python
# 게임 점수 계산 프로그램
print("=== 게임 점수 시스템 ===")

# 초기값 설정
score = 0
level = 1

# 게임 진행
print("스테이지 1 클리어!")
score += 100
print(f"현재 점수: {score}")

print("\n보너스 아이템 획득!")
score *= 2  # 점수 2배
print(f"현재 점수: {score}")

print("\n스테이지 2 클리어!")
score += 150
print(f"현재 점수: {score}")

# 레벨업 조건 확인 (300점 이상)
if score >= 300:
    level += 1
    print(f"\n레벨업! 현재 레벨: {level}")

print(f"\n최종 점수: {score}")
print(f"최종 레벨: {level}")
```

---

## 5️⃣ **연산자 우선순위**

하나의 표현식에 여러 연산자가 있을 때, 어떤 연산자를 먼저 계산할지 정해진 규칙이 있습니다. 이를 연산자 우선순위라고 합니다. 수학에서 곱셈과 나눗셈을 덧셈과 뺄셈보다 먼저 계산하는 것과 같은 원리입니다.

### **우선순위 규칙**

파이썬의 연산자 우선순위는 다음과 같습니다 (위에서 아래로 높은 순서):

```
연산자 우선순위 (높음 → 낮음)

1. ()          괄호
2. **          거듭제곱
3. *, /, //, % 곱셈, 나눗셈, 정수 나눗셈, 나머지
4. +, -        덧셈, 뺄셈
5. ==, !=, >, <, >=, <=  비교 연산자
6. not         논리 부정
7. and         논리 AND
8. or          논리 OR
```

```python
# 연산자 우선순위 예제
result = 2 + 3 * 4
print(result)  # 14 (곱셈 먼저: 2 + 12)

result = (2 + 3) * 4
print(result)  # 20 (괄호 먼저: 5 * 4)

result = 10 - 5 - 2
print(result)  # 3 (왼쪽부터: (10 - 5) - 2)

result = 2 ** 3 ** 2
print(result)  # 512 (오른쪽부터: 2 ** (3 ** 2) = 2 ** 9)
```

복잡한 표현식을 작성할 때는 괄호를 사용하여 명확하게 하는 것이 좋습니다. 괄호는 가장 높은 우선순위를 가지므로 괄호 안의 연산이 먼저 수행됩니다.

```python
# 복잡한 계산 - 평균 구하기
korean = 85
english = 90
math = 88

# 잘못된 방법 (우선순위 문제)
# average = korean + english + math / 3  # 88/3을 먼저 계산
# print(average)  # 204.33333... (잘못된 결과)

# 올바른 방법
average = (korean + english + math) / 3
print(average)  # 87.66666... (올바른 결과)
```

### **예제 5: 온라인 쇼핑 최종 금액 계산**

상품 가격, 배송비, 할인 쿠폰을 고려하여 최종 결제 금액을 계산하는 프로그램입니다.

```python
# 온라인 쇼핑 최종 금액 계산
print("=== 온라인 쇼핑 결제 계산기 ===")

# 입력
product_price = int(input("상품 가격: "))
quantity = int(input("수량: "))
shipping_fee = int(input("배송비: "))
coupon_discount = int(input("쿠폰 할인액: "))

# 계산 (우선순위에 주의)
subtotal = product_price * quantity  # 상품 금액
total_before_discount = subtotal + shipping_fee  # 배송비 포함
final_price = total_before_discount - coupon_discount  # 쿠폰 할인

# 무료 배송 조건 확인 (50,000원 이상)
if subtotal >= 50000:
    final_price -= shipping_fee
    free_shipping = True
else:
    free_shipping = False

# 결과 출력
print(f"\n상품 금액: {subtotal:,}원")
print(f"배송비: {shipping_fee:,}원")
print(f"쿠폰 할인: {coupon_discount:,}원")
print(f"무료 배송: {free_shipping}")
print(f"최종 결제 금액: {final_price:,}원")
```

---

## 6️⃣ **문자열 연산**

파이썬에서는 숫자뿐만 아니라 문자열에도 일부 연산자를 사용할 수 있습니다. 문자열을 연결하거나 반복하는 작업을 쉽게 할 수 있습니다.

### **문자열 연결 (+)**

덧셈 연산자(`+`)를 문자열에 사용하면 두 문자열이 연결됩니다.

```python
# 문자열 연결
first_name = "길동"
last_name = "홍"
full_name = last_name + first_name
print(full_name)  # 홍길동

# 여러 문자열 연결
greeting = "안녕하세요, " + full_name + "님!"
print(greeting)  # 안녕하세요, 홍길동님!
```

문자열과 숫자를 직접 연결할 수는 없습니다. 숫자를 문자열로 변환한 후 연결해야 합니다.

```python
age = 20
# message = "나이: " + age  # 오류 발생!
message = "나이: " + str(age)  # 올바른 방법
print(message)  # 나이: 20
```

### **문자열 반복 (*)**

곱셈 연산자(`*`)를 문자열과 정수에 사용하면 문자열이 반복됩니다.

```python
# 문자열 반복
stars = "*" * 10
print(stars)  # **********

divider = "-" * 30
print(divider)  # ------------------------------

# 패턴 만들기
pattern = "♥" * 5
print(pattern)  # ♥♥♥♥♥
```

### **예제 6: 영수증 출력 프로그램**

상품 구매 내역을 보기 좋은 형식의 영수증으로 출력하는 프로그램입니다.

```python
# 영수증 출력 프로그램
print("=== 영수증 생성기 ===")

# 상점 정보
store_name = "파이썬 마트"
store_address = "서울시 강남구 파이썬로 123"

# 구매 정보 입력
product_name = input("상품명: ")
unit_price = int(input("단가: "))
quantity = int(input("수량: "))

# 계산
total_price = unit_price * quantity

# 영수증 출력
line = "=" * 40
print("\n" + line)
print(store_name.center(40))  # 중앙 정렬
print(store_address.center(40))
print(line)
print("상품명".ljust(20) + "수량".rjust(10) + "금액".rjust(10))
print(line)
print(product_name.ljust(20) + str(quantity).rjust(10) + f"{unit_price:,}원".rjust(10))
print(line)
print("합계".ljust(30) + f"{total_price:,}원".rjust(10))
print(line)
print("\n감사합니다!".center(40))
print(line)
```

---

## 📝 **핵심 개념 정리**

연산자는 데이터를 조작하고 계산하는 기본 도구입니다. 산술 연산자(+, -, *, /, //, %, **)는 수학적 계산을 수행하며, 비교 연산자(==, !=, >, <, >=, <=)는 두 값을 비교하여 불린 값을 반환합니다.

논리 연산자(and, or, not)는 여러 조건을 결합하여 복잡한 조건식을 만들 수 있게 해줍니다. and는 모든 조건이 참일 때, or는 하나라도 참일 때, not은 참과 거짓을 반대로 바꿉니다.

대입 연산자는 변수에 값을 저장하며, 복합 대입 연산자(+=, -=, *=, /= 등)는 계산과 대입을 동시에 수행합니다. 연산자 우선순위는 괄호가 가장 높고, 거듭제곱, 곱셈/나눗셈, 덧셈/뺄셈, 비교, 논리 연산자 순입니다.

문자열에도 + 연산자로 연결하고 * 연산자로 반복할 수 있습니다. 복잡한 표현식은 괄호를 사용하여 명확하게 작성하는 것이 좋습니다.

---

## 💡 **실습 과제**

### **과제 1: 급여 계산 프로그램**

시급, 근무 시간, 야간 근무 시간을 입력받아 총 급여를 계산하는 프로그램을 작성하세요. 야간 근무는 시급의 1.5배를 적용합니다.

```python
# 힌트
hourly_wage = int(input("시급: "))
regular_hours = int(input("일반 근무 시간: "))
night_hours = int(input("야간 근무 시간: "))

# 여기에 계산 코드를 작성하세요
# 일반 근무 급여 = 시급 * 일반 근무 시간
# 야간 근무 급여 = 시급 * 1.5 * 야간 근무 시간
# 총 급여 = 일반 근무 급여 + 야간 근무 급여
```

### **과제 2: 윤년 판별 프로그램**

연도를 입력받아 윤년인지 판별하는 프로그램을 작성하세요. 윤년 조건은 다음과 같습니다:

- 4로 나누어떨어지고
- 100으로 나누어떨어지지 않거나
- 400으로 나누어떨어지는 해

```python
# 힌트
year = int(input("연도를 입력하세요: "))

# 윤년 조건 확인
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(f"{year}년은 윤년입니까? {is_leap_year}")
```

---

## ✅ **퀴즈**

### **[초급] 1번**

다음 코드의 실행 결과는?

```python
x = 10
x += 5
print(x)
```

1. 10
2. 15
3. 5
4. 오류 발생

### **[중급] 2번**

다음 중 연산 결과가 다른 하나는?

```python
1) 10 / 2
2) float(10 // 2)
3) 5.0
4) 5
```

1. 1번
2. 2번
3. 3번
4. 4번

### **[중급] 3번**

다음 코드의 실행 결과는?

```python
result = 2 + 3 * 4
print(result)
```

1. 14
2. 20
3. 24
4. 11

### **[중급] 4번**

다음 중 True를 반환하는 것은?

```python
age = 25
has_license = True
```

1. age < 18 and has_license
2. age >= 18 or not has_license
3. not (age >= 18 and has_license)
4. age < 18 or not has_license

### **[고급] 5번**

다음 코드의 실행 결과는?

```python
x = 10
y = 3
result = x % y == 1 and x // y > 2
print(result)
```

1. True
2. False
3. 1
4. 오류 발생

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
`x += 5`는 `x = x + 5`와 같으므로 `x`는 10 + 5 = 15가 됩니다. 복합 대입 연산자는 변수의 현재 값에 연산을 수행한 후 다시 저장합니다.

**2번 정답: 4**
1번 `10 / 2`는 5.0(실수), 2번 `float(10 // 2)`는 5(정수)를 실수로, 3번은 5.0(실수), 4번은 5(정수)입니다. 따라서 4번만 정수형이고 나머지는 모두 실수형이거나 실수 값입니다. 일반 나눗셈(`/`)은 항상 실수를 반환합니다.

**3번 정답: 1**
연산자 우선순위에 따라 곱셈이 먼저 계산됩니다. `3 * 4 = 12`, 그 다음 `2 + 12 = 14`입니다. 만약 `(2 + 3) * 4`였다면 20이 됩니다.

**4번 정답: 2**
`age >= 18`은 True, `has_license`는 True입니다. (2) `True or not True` = `True or False` = True입니다. (1) `False and True` = False, (3) `not (True and True)` = `not True` = False, (4) `False or False` = False입니다.

**5번 정답: 1**
`x % y`는 10 % 3 = 1, `x // y`는 10 // 3 = 3입니다. 따라서 `1 == 1 and 3 > 2`는 `True and True`가 되어 True를 반환합니다. 이 문제는 산술 연산, 비교 연산, 논리 연산이 모두 포함된 복합 표현식입니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 문자열을 다루는 방법에 대해 자세히 배웁니다. 문자열 인덱싱, 슬라이싱, 다양한 문자열 메서드를 사용하여 텍스트 데이터를 효과적으로 처리하는 방법을 학습하게 됩니다.

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
