# 8장 반복문 2 (while 문 & 제어문)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 while 문으로 조건 기반 반복을 구현하고, break와 continue로 반복문의 흐름을 제어할 수 있습니다. 또한 중첩 반복문을 활용하여 복잡한 문제를 해결할 수 있습니다.

---

## 1️⃣ **while 문이란?**

while 문은 조건이 참(True)인 동안 계속 반복하는 구문입니다. for 문은 반복 횟수를 알 때 사용하고, while 문은 반복 횟수를 모를 때 사용합니다.

```python
# while 문 기본 구조
while 조건식:
    반복할 코드
    # 조건을 거짓으로 만드는 코드 필요!
```

```
while 문 vs for 문

┌─────────────┬──────────────┐
│   for 문    │  while 문    │
├─────────────┼──────────────┤
│ 횟수 정해짐 │ 조건 기반    │
│ range() 사용│ 조건식 사용  │
│ 자동 종료   │ 수동 제어    │
└─────────────┴──────────────┘
```

### **기본 예제**

```python
# while 문 예제
count = 1

while count <= 5:
    print(f"{count}번째 반복")
    count = count + 1  # 조건 변경 필수!

print("반복 종료")

# 출력:
# 1번째 반복
# 2번째 반복
# 3번째 반복
# 4번째 반복
# 5번째 반복
# 반복 종료
```

⚠️ **주의**: while 문에서는 반드시 조건을 거짓으로 만드는 코드가 필요합니다. 그렇지 않으면 무한 반복에 빠집니다!

```python
# 무한 반복 예제 (위험!)
# while True:
#     print("멈추지 않아요!")  # Ctrl+C로 강제 종료 필요
```

---

## 2️⃣ **while 문 활용**

### **예제 1: 비밀번호 확인**

올바른 비밀번호를 입력할 때까지 반복하는 프로그램입니다.

```python
# 비밀번호 확인 프로그램
print("🔐" + "=" * 38 + "🔐")
print("   로그인 시스템")
print("🔐" + "=" * 38 + "🔐")

correct_password = "python123"
max_attempts = 3
attempts = 0

print(f"\n비밀번호를 입력하세요 (최대 {max_attempts}회)")

while attempts < max_attempts:
    password = input(f"\n시도 {attempts + 1}/{max_attempts}: ")
  
    if password == correct_password:
        print("\n✅ 로그인 성공!")
        print("환영합니다! 🎉")
        break  # 반복 종료
    else:
        attempts = attempts + 1
        remaining = max_attempts - attempts
    
        if remaining > 0:
            print(f"❌ 비밀번호가 틀렸습니다.")
            print(f"남은 기회: {remaining}회")
        else:
            print("\n🚫 로그인 실패!")
            print("최대 시도 횟수를 초과했습니다.")
```

### **예제 2: 목표 달성 시뮬레이터**

목표 금액까지 저축하는 시뮬레이션 프로그램입니다.

```python
# 목표 저축 시뮬레이터
print("💰" + "=" * 38 + "💰")
print("   저축 목표 달성 시뮬레이터")
print("💰" + "=" * 38 + "💰")

target = int(input("\n목표 금액: "))
monthly_save = int(input("월 저축액: "))

current = 0
month = 0

print("\n" + "=" * 40)
print("저축 시뮬레이션")
print("=" * 40)

while current < target:
    month = month + 1
    current = current + monthly_save
  
    print(f"{month}개월차: {current:,}원")

print("\n" + "=" * 40)
print(f"🎉 {month}개월 후 목표 달성!")
print(f"총 저축액: {current:,}원")
print("=" * 40)
```

---

## 3️⃣ **break - 반복 중단**

`break`는 반복문을 즉시 종료합니다.

```python
# break 예제
for i in range(1, 11):
    if i == 5:
        break  # i가 5가 되면 반복 중단
    print(i)

# 출력: 1, 2, 3, 4
```

```
break의 동작

    ┌───────┐
    │ 반복  │
    │ 시작  │
    └───┬───┘
        │
    ┌───▼────┐
    │조건 검사│
    └───┬────┘
        │
    ┌───┴────┐
   Yes      No
    │        │
┌───▼──┐  ┌─▼──┐
│break!│  │계속 │
└───┬──┘  └─┬──┘
    │       │
    ▼       │
 종료   ────┘
```

### **예제 3: 숫자 찾기 게임**

특정 숫자를 찾으면 종료하는 게임입니다.

```python
# 숫자 찾기 게임
print("🎯" + "=" * 38 + "🎯")
print("   숫자 찾기 게임")
print("🎯" + "=" * 38 + "🎯")

import random
secret_number = random.randint(1, 100)
attempts = 0

print("\n1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    attempts = attempts + 1
    guess = int(input(f"\n{attempts}번째 시도: "))
  
    if guess == secret_number:
        print(f"\n🎉 정답! {attempts}번 만에 맞췄어요!")
        break
    elif guess < secret_number:
        print("⬆️ UP! 더 큰 숫자예요")
    else:
        print("⬇️ DOWN! 더 작은 숫자예요")
```

---

## 4️⃣ **continue - 다음 반복으로**

`continue`는 현재 반복을 건너뛰고 다음 반복으로 넘어갑니다.

```python
# continue 예제
for i in range(1, 6):
    if i == 3:
        continue  # i가 3일 때는 건너뛰기
    print(i)

# 출력: 1, 2, 4, 5 (3은 출력 안 됨)
```

```
continue의 동작

    ┌───────┐
    │ 반복  │
    └───┬───┘
        │
    ┌───▼─────┐
    │조건 검사 │
    └───┬─────┘
        │
    ┌───┴────┐
   Yes      No
    │        │
┌───▼────┐ ┌▼──┐
│continue│ │실행│
└───┬────┘ └┬──┘
    │       │
    └───┬───┘
        │
    다음 반복
```

### **예제 4: 짝수만 출력**

1부터 20까지 중 짝수만 출력하는 프로그램입니다.

```python
# 짝수만 출력
print("📊 1부터 20까지 짝수:")
print("-" * 40)

for i in range(1, 21):
    if i % 2 != 0:  # 홀수면
        continue    # 건너뛰기
    print(i, end=" ")

print("\n" + "-" * 40)
```

---

## 5️⃣ **while True와 break 조합**

무한 반복을 만들고 특정 조건에서 break로 빠져나오는 패턴은 매우 유용합니다.

### **예제 5: 쇼핑 장바구니**

원하는 만큼 상품을 담고, 종료 신호를 받으면 총 금액을 계산하는 프로그램입니다.

```python
# 쇼핑 장바구니 프로그램
print("🛒" + "=" * 38 + "🛒")
print("   쇼핑 장바구니")
print("🛒" + "=" * 38 + "🛒")

print("\n상품을 추가하세요 (종료: 'q' 입력)")
print("-" * 40)

total_price = 0
item_count = 0

while True:
    product = input("\n상품명 (종료: q): ")
  
    # 종료 조건
    if product == 'q' or product == 'Q':
        break
  
    # 빈 입력 무시
    if product == "":
        continue
  
    price = int(input("가격: "))
  
    # 가격이 0원 이하면 무시
    if price <= 0:
        print("⚠️ 올바른 가격을 입력하세요.")
        continue
  
    item_count = item_count + 1
    total_price = total_price + price
    print(f"✓ {product} 추가됨 ({price:,}원)")

# 결과 출력
print("\n" + "=" * 40)
print("장바구니 요약")
print("=" * 40)
print(f"총 상품 수: {item_count}개")
print(f"총 금액: {total_price:,}원")

# 배달비 계산
if total_price >= 30000:
    delivery = 0
    print(f"배달비: 무료")
else:
    delivery = 3000
    print(f"배달비: {delivery:,}원")

final_price = total_price + delivery
print("-" * 40)
print(f"최종 결제: {final_price:,}원")
print("=" * 40)
```

---

## 6️⃣ **중첩 반복문과 제어문**

중첩된 반복문에서 break와 continue를 사용할 때는 주의가 필요합니다.

```python
# 중첩 반복문에서 break
for i in range(1, 4):
    print(f"\n바깥 반복: {i}")
  
    for j in range(1, 4):
        if j == 2:
            break  # 안쪽 반복만 종료
        print(f"  안쪽 반복: {j}")

# 출력:
# 바깥 반복: 1
#   안쪽 반복: 1
# 바깥 반복: 2
#   안쪽 반복: 1
# 바깥 반복: 3
#   안쪽 반복: 1
```

### **예제 6: 구구단 게임**

구구단 문제를 맞출 때까지 반복하는 게임입니다.

```python
# 구구단 게임
print("📚" + "=" * 38 + "📚")
print("   구구단 게임")
print("📚" + "=" * 38 + "📚")

import random

score = 0
total_problems = 5

print(f"\n{total_problems}문제를 풀어보세요!")
print("=" * 40)

for problem_num in range(1, total_problems + 1):
    # 랜덤 문제 생성
    num1 = random.randint(2, 9)
    num2 = random.randint(1, 9)
    correct_answer = num1 * num2
  
    print(f"\n문제 {problem_num}: {num1} × {num2} = ?")
  
    # 정답을 맞출 때까지 반복
    while True:
        answer = int(input("답: "))
    
        if answer == correct_answer:
            print("✅ 정답!")
            score = score + 1
            break
        else:
            print("❌ 틀렸어요. 다시 시도하세요!")

# 결과 발표
print("\n" + "=" * 40)
print("게임 결과")
print("=" * 40)
print(f"맞춘 문제: {score}/{total_problems}")
print(f"정답률: {score/total_problems*100:.0f}%")

if score == total_problems:
    print("\n🎉 퍼펙트!")
elif score >= total_problems * 0.7:
    print("\n👍 잘했어요!")
else:
    print("\n💪 다시 도전해보세요!")

print("=" * 40)
```

---

## 7️⃣ **무한 루프 활용**

프로그램이 계속 실행되어야 할 때 무한 루프를 활용합니다.

### **예제 7: 간단한 계산기**

종료할 때까지 계속 계산하는 프로그램입니다.

```python
# 간단한 계산기
print("🔢" + "=" * 38 + "🔢")
print("   계산기")
print("🔢" + "=" * 38 + "🔢")

print("\n사용 가능한 연산:")
print("  + : 더하기")
print("  - : 빼기")
print("  * : 곱하기")
print("  / : 나누기")
print("  q : 종료")
print("=" * 40)

while True:
    operator = input("\n연산 선택 (+, -, *, /, q): ")
  
    # 종료
    if operator == 'q' or operator == 'Q':
        print("\n계산기를 종료합니다.")
        break
  
    # 올바른 연산자 체크
    if operator not in ['+', '-', '*', '/']:
        print("❌ 올바른 연산자를 입력하세요.")
        continue
  
    # 숫자 입력
    num1 = float(input("첫 번째 숫자: "))
    num2 = float(input("두 번째 숫자: "))
  
    # 계산
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("❌ 0으로 나눌 수 없습니다.")
            continue
        result = num1 / num2
  
    # 결과 출력
    print("-" * 40)
    print(f"결과: {num1} {operator} {num2} = {result}")
    print("-" * 40)
```

---

## 📝 **핵심 개념 정리**

while 문은 조건이 참인 동안 계속 반복하며, 반복 횟수를 모를 때 유용합니다. while 문에서는 반드시 조건을 거짓으로 만드는 코드가 있어야 무한 반복을 피할 수 있습니다.

`break`는 반복문을 즉시 종료하고, `continue`는 현재 반복을 건너뛰고 다음 반복으로 넘어갑니다. `while True`와 `break`를 조합하면 유연한 반복 제어가 가능합니다.

중첩 반복문에서 break는 가장 안쪽 반복문만 종료합니다. 반복문과 조건문, 제어문을 잘 조합하면 복잡한 프로그램 로직을 구현할 수 있습니다.

---

## 💡 **실습 과제**

### **과제 1: ATM 기계**

잔액 확인, 입금, 출금 기능이 있는 ATM 프로그램을 작성하세요.

```python
# 힌트
balance = 10000  # 초기 잔액

while True:
    print("\n1. 잔액 확인")
    print("2. 입금")
    print("3. 출금")
    print("4. 종료")
  
    choice = input("\n선택: ")
  
    if choice == "1":
        # 잔액 출력
        pass
    elif choice == "2":
        # 입금 처리
        pass
    elif choice == "3":
        # 출금 처리 (잔액 부족 체크)
        pass
    elif choice == "4":
        break
```

### **과제 2: 숫자 야구 게임**

컴퓨터가 생각한 3자리 숫자를 맞추는 게임을 만드세요.

```python
# 힌트
import random
# 1-9 사이의 서로 다른 숫자 3개 생성
# 사용자 입력 받기
# 스트라이크, 볼 계산
# 3 스트라이크면 게임 종료
```

---

## ✅ **퀴즈**

### **[초급] 1번**

다음 코드의 출력 횟수는?

```python
count = 0
while count < 3:
    print("*")
    count = count + 1
```

1. 2번
2. 3번
3. 4번
4. 무한 반복

### **[중급] 2번**

다음 코드의 출력 결과는?

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

1. 1 2 3
2. 1 2
3. 3 4 5
4. 1 2 3 4 5

### **[중급] 3번**

다음 코드의 출력 결과는?

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

1. 1 2 4 5
2. 1 2 3 4 5
3. 3
4. 1 2

### **[고급] 4번**

다음 코드는 무엇을 출력할까요?

```python
count = 1
while count <= 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
```

1. 1 2 3 4 5
2. 1 2 4 5
3. 1 2 3 4
4. 무한 반복

### **[고급] 5번**

break와 continue의 차이점은?

```python
1. break는 반복 종료, continue는 다음 반복
2. break는 건너뛰기, continue는 종료
3. 동일한 기능
4. break만 while에서 사용 가능
```

1. 1번
2. 2번
3. 3번
4. 4번

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
count가 0, 1, 2일 때 3번 반복됩니다. count가 3이 되면 조건 `count < 3`이 거짓이 되어 반복이 종료됩니다.

**2번 정답: 2**
i가 1, 2일 때 출력되고, i가 3이 되면 break로 반복이 종료됩니다. 따라서 "1 2"가 출력됩니다.

**3번 정답: 1**
i가 3일 때 continue로 print를 건너뛰므로, 1, 2, 4, 5만 출력됩니다.

**4번 정답: 2**
count가 1, 2일 때 출력되고, 3일 때는 continue로 건너뛴 후 count가 4가 되어, 4, 5가 출력됩니다. 결과: "1 2 4 5"

**5번 정답: 1**
break는 반복문을 완전히 종료하고, continue는 현재 반복만 건너뛰고 다음 반복을 계속합니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 함수의 기본에 대해 배웁니다. 자주 사용하는 코드를 함수로 만들어 재사용하는 방법을 학습하게 됩니다. 함수를 익히면 코드를 체계적으로 구성하고 관리할 수 있습니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
