# 10장 함수 2 (고급) — 연습문제

---

## 📝 객관식 문제

---

### 🟢 초급

**문제 1.** 다음 코드의 실행 결과는?

```python
def get_values():
    return 10, 20

a, b = get_values()
print(a + b)
```

① 10
② 20
③ 30
④ (10, 20)

---

**문제 2.** 함수 안에서 만든 변수의 이름은?

① 전역 변수
② 지역 변수
③ 클래스 변수
④ 상수

---

**문제 3.** 다음 코드의 실행 결과는?

```python
x = 100

def func():
    print(x)

func()
```

① 오류 발생
② None
③ 100
④ 0

---

**문제 4.** 람다 함수의 올바른 구문은?

① `lambda x: x * 2`
② `def lambda(x): return x * 2`
③ `lambda(x): x * 2`
④ `func x: x * 2`

---

**문제 5.** 다음 코드의 실행 결과는?

```python
double = lambda x: x * 2
print(double(5))
```

① 5
② 10
③ x * 2
④ 오류 발생

---

**문제 6.** 재귀 함수에 반드시 필요한 것은?

① return 문
② 전역 변수
③ 종료 조건 (기저 조건)
④ 람다 함수

---

**문제 7.** 다음 코드의 실행 결과는?

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
```

① 4
② 10
③ 24
④ 120

---

### 🟡 중급

**문제 8.** 함수 내에서 전역 변수를 수정하려면 어떤 키워드를 사용하는가?

① local
② global
③ nonlocal
④ static

---

**문제 9.** 다음 코드의 실행 결과는?

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()
print(count)
```

① 0
② 1
③ 3
④ 오류 발생

---

**문제 10.** 다음 코드의 실행 결과는?

```python
multiply = lambda a, b: a * b
result = multiply(3, 7)
print(result)
```

① 10
② 21
③ 37
④ 오류 발생

---

**문제 11.** 다음 코드의 실행 결과는?

```python
def func(n):
    if n == 0:
        return 0
    return n + func(n - 1)

print(func(4))
```

① 4
② 6
③ 10
④ 무한 반복

---

**문제 12.** 다음 코드의 실행 결과는?

```python
x = 10

def func():
    x = 20
    print(x)

func()
print(x)
```

① 20 / 20
② 10 / 10
③ 20 / 10
④ 10 / 20

---

### 🔴 고급

**문제 13.** 다음 코드의 실행 결과는?

```python
def calc_stats(a, b, c):
    total = a + b + c
    avg = total / 3
    return total, avg

t, a = calc_stats(80, 90, 70)
print(f"총점: {t}, 평균: {a:.1f}")
```

① 총점: 240, 평균: 80.0
② 총점: 80, 평균: 80.0
③ (240, 80.0)
④ 오류 발생

---

**문제 14.** 다음 코드의 실행 결과는?

```python
def fibonacci(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
```

① 5
② 8
③ 13
④ 21

---

**문제 15.** 재귀 함수와 반복문의 비교로 **틀린** 것은?

① 재귀는 코드가 직관적이다
② 재귀는 반복문보다 느리다
③ 재귀는 반복문보다 메모리를 적게 쓴다
④ 재귀는 기저 조건이 필수이다

---

## 📝 주관식 문제

---

### 🟢 초급

**문제 16.** 지역 변수와 전역 변수의 차이를 설명하고, 각각의 예시 코드를 작성하시오.

---

**문제 17.** 다음 코드의 실행 결과를 쓰시오.

```python
def swap(a, b):
    return b, a

x, y = swap(10, 20)
print(f"x={x}, y={y}")
```

---

**문제 18.** 람다 함수의 개념을 설명하고, `lambda x, y: x + y`와 동일한 기능의 일반 함수를 작성하시오.

---

### 🟡 중급

**문제 19.** 다음 코드의 실행 결과를 쓰고, `global` 키워드의 필요성을 설명하시오.

```python
total = 0

def add_score(score):
    global total
    total += score
    return total

print(add_score(80))
print(add_score(90))
print(f"최종: {total}")
```

---

**문제 20.** 다음 재귀 함수의 실행 결과를 쓰고, 호출 과정을 단계별로 설명하시오.

```python
def sum_recursive(n):
    if n <= 1:
        return n
    return n + sum_recursive(n - 1)

print(sum_recursive(5))
```

---

### 🔴 고급

**문제 21.** 다음 코드의 실행 결과를 쓰고, 재귀와 반복문 방식의 차이를 설명하시오.

```python
def power_recursive(base, exp):
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)

def power_loop(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

print(power_recursive(2, 8))
print(power_loop(2, 8))
```

---

## 💻 실습형 문제

---

### 🟢 초급

**문제 22.** 다음 요구사항에 맞는 프로그램을 작성하시오.

> 두 수를 받아 **합, 차, 곱**을 동시에 반환하는 함수 `calc(a, b)`를 작성하시오.

출력 예시:

```
calc(10, 3):
합: 13, 차: 7, 곱: 30
```

---

**문제 23.** 다음 요구사항에 맞는 프로그램을 작성하시오.

> 람다 함수를 사용하여 섭씨를 화씨로 변환하시오. (공식: `화씨 = 섭씨 × 1.8 + 32`)

출력 예시:

```
0°C = 32.0°F
100°C = 212.0°F
36.5°C = 97.7°F
```

---

**문제 24.** 다음 요구사항에 맞는 프로그램을 작성하시오.

> 재귀 함수를 사용하여 `n`부터 1까지 카운트다운을 출력하시오. 0이 되면 `"발사!"`를 출력하시오.

출력 예시 (n=5):

```
5
4
3
2
1
발사!
```

---

### 🟡 중급

**문제 25.** 다음 요구사항에 맞는 프로그램을 작성하시오.

> 전역 변수 `balance = 10000`을 사용하여 간단한 은행 시스템을 구현하시오.
>
> - `deposit(amount)` : 입금 (잔액 증가)
> - `withdraw(amount)` : 출금 (잔액 부족 시 "잔액 부족" 출력)
> - `check_balance()` : 잔액 출력

출력 예시:

```
현재 잔액: 10,000원
5,000원 입금 → 잔액: 15,000원
3,000원 출금 → 잔액: 12,000원
20,000원 출금 → 잔액 부족!
현재 잔액: 12,000원
```

---

### 🔴 고급

**문제 26.** 다음 요구사항에 맞는 프로그램을 작성하시오.

> 재귀 함수를 사용하여 두 수의 **최대공약수(GCD)**를 구하시오. (유클리드 호제법)
> 추가로 **최소공배수(LCM)**도 계산하시오. (공식: `LCM = a × b ÷ GCD`)

출력 예시:

```
=== GCD / LCM 계산기 ===
a = 48, b = 18
GCD(48, 18) = 6
LCM(48, 18) = 144

a = 100, b = 35
GCD(100, 35) = 5
LCM(100, 35) = 700
```

---

---

# 🔑 정답 및 해설

---

## 📝 객관식 정답

---

### 🟢 초급

**문제 1. 정답: ③ 30**

함수가 `10, 20`을 반환하면 자동으로 튜플 `(10, 20)`이 됩니다. `a, b = get_values()`로 언패킹하여 `a=10`, `b=20`. `10 + 20 = 30`.

---

**문제 2. 정답: ② 지역 변수**

함수 안에서 만든 변수는 **지역 변수(local variable)**로, 해당 함수 안에서만 접근 가능합니다. 함수가 끝나면 소멸됩니다.

---

**문제 3. 정답: ③ 100**

함수 내부에서 전역 변수를 **읽는 것**은 `global` 선언 없이도 가능합니다. `x = 100`은 전역 변수이므로 함수 안에서 읽어 100을 출력합니다.

---

**문제 4. 정답: ① `lambda x: x * 2`**

람다 함수는 `lambda 매개변수: 표현식` 형태입니다. 괄호 없이 매개변수를 쓰고, 콜론 뒤에 반환할 표현식을 작성합니다.

---

**문제 5. 정답: ② 10**

`double = lambda x: x * 2`에서 `double(5)`는 `5 * 2 = 10`을 반환합니다.

---

**문제 6. 정답: ③ 종료 조건 (기저 조건)**

재귀 함수는 자기 자신을 호출하므로, 종료 조건이 없으면 무한히 호출되어 오류(`RecursionError`)가 발생합니다.

---

**문제 7. 정답: ③ 24**

`factorial(4) = 4 × factorial(3) = 4 × 3 × factorial(2) = 4 × 3 × 2 × factorial(1) = 4 × 3 × 2 × 1 = 24`.

---

### 🟡 중급

**문제 8. 정답: ② global**

함수 내에서 전역 변수를 **수정**하려면 `global 변수이름`을 선언해야 합니다. 선언하지 않으면 같은 이름의 새로운 지역 변수가 생성됩니다.

---

**문제 9. 정답: ③ 3**

`global count`로 전역 변수를 사용하므로, `increment()`를 3번 호출하면 `count`가 0 → 1 → 2 → 3으로 변합니다.

---

**문제 10. 정답: ② 21**

`lambda a, b: a * b`에서 `multiply(3, 7)` = `3 × 7 = 21`.

---

**문제 11. 정답: ③ 10**

`func(4) = 4 + func(3) = 4 + 3 + func(2) = 4 + 3 + 2 + func(1) = 4 + 3 + 2 + 1 + func(0) = 4 + 3 + 2 + 1 + 0 = 10`.

---

**문제 12. 정답: ③ 20 / 10**

함수 내부의 `x = 20`은 **지역 변수**입니다(`global` 선언 없음). 전역 변수 `x = 10`은 변경되지 않습니다. 함수 안에서 20, 밖에서 10이 출력됩니다.

---

### 🔴 고급

**문제 13. 정답: ① 총점: 240, 평균: 80.0**

`80 + 90 + 70 = 240`, `240 / 3 = 80.0`. 다중 반환값을 `t, a`로 언패킹합니다.

---

**문제 14. 정답: ② 8**

피보나치 수열: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8. `fibonacci(6) = fibonacci(5) + fibonacci(4) = 5 + 3 = 8`.

---

**문제 15. 정답: ③ 재귀는 반복문보다 메모리를 적게 쓴다**

이것은 **틀린** 설명입니다. 재귀는 호출할 때마다 스택 프레임이 쌓이므로 반복문보다 **메모리를 더 많이** 사용합니다.

---

## 📝 주관식 정답

---

### 🟢 초급

**문제 16. 모범답안:**

**지역 변수:** 함수 **내부**에서 만든 변수. 함수 안에서만 접근 가능하고, 함수 종료 시 소멸됩니다.

```python
def func():
    local_var = 10       # 지역 변수
    print(local_var)     # 함수 안에서 사용 가능

func()
# print(local_var)       # 오류! 함수 밖에서 접근 불가
```

**전역 변수:** 함수 **외부**(프로그램 최상위)에서 만든 변수. 프로그램 전체에서 접근 가능합니다.

```python
global_var = 100         # 전역 변수

def func():
    print(global_var)    # 함수 안에서 읽기 가능

func()                   # 100
print(global_var)        # 100
```

---

**문제 17. 모범답안:**

```
x=20, y=10
```

`swap(10, 20)`은 `b, a` 즉 `20, 10`을 반환합니다. 다중 반환값을 `x, y`로 언패킹하여 `x=20`, `y=10`이 됩니다.

---

**문제 18. 모범답안:**

**람다 함수:** `lambda` 키워드로 만드는 이름 없는 간단한 한 줄 함수입니다. 복잡한 로직 없이 간단한 연산을 수행할 때 사용합니다.

```python
# 람다 함수
add_lambda = lambda x, y: x + y

# 동일한 일반 함수
def add(x, y):
    return x + y

print(add_lambda(3, 5))  # 8
print(add(3, 5))          # 8
```

---

### 🟡 중급

**문제 19. 모범답안:**

실행 결과:

```
80
170
최종: 170
```

**동작 과정:**

- `add_score(80)`: `total = 0 + 80 = 80` → 80 반환 및 출력
- `add_score(90)`: `total = 80 + 90 = 170` → 170 반환 및 출력
- `total`은 전역 변수이므로 함수 밖에서도 170

**`global` 필요성:** `global` 없이 `total += score`를 하면 파이썬은 `total`을 지역 변수로 인식합니다. 그런데 `+=`는 읽기와 쓰기를 동시에 하므로, 아직 값이 할당되지 않은 지역 변수를 읽으려 해서 `UnboundLocalError`가 발생합니다.

---

**문제 20. 모범답안:**

실행 결과:

```
15
```

**호출 과정:**

```
sum_recursive(5)
= 5 + sum_recursive(4)
= 5 + 4 + sum_recursive(3)
= 5 + 4 + 3 + sum_recursive(2)
= 5 + 4 + 3 + 2 + sum_recursive(1)
= 5 + 4 + 3 + 2 + 1    ← 기저 조건 (n=1 → return 1)
= 15
```

`n=1`에서 기저 조건에 도달하여 1을 반환하고, 이후 역순으로 값이 누적되어 최종 15가 반환됩니다.

---

### 🔴 고급

**문제 21. 모범답안:**

실행 결과:

```
256
256
```

**재귀 방식** (`power_recursive`):

```
power_recursive(2, 8)
= 2 × power_recursive(2, 7)
= 2 × 2 × power_recursive(2, 6)
= ... (8단계)
= 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 1
= 256
```

기저 조건 `exp == 0`에서 1을 반환하고, 역순으로 `base`를 곱합니다. 총 9번의 함수 호출(스택 프레임 9개)이 필요합니다.

**반복문 방식** (`power_loop`):
`result`에 `base`를 8번 곱합니다. 함수 호출 없이 단순 반복이므로 메모리를 적게 사용합니다.

두 방식 모두 같은 결과를 내지만, 반복문이 메모리와 속도 면에서 효율적입니다.

---

## 💻 실습형 정답

---

### 🟢 초급

**문제 22. 모범답안:**

```python
def calc(a, b):
    return a + b, a - b, a * b

s, d, p = calc(10, 3)
print(f"calc(10, 3):")
print(f"합: {s}, 차: {d}, 곱: {p}")
```

핵심: `return`에서 쉼표로 여러 값을 반환하고, 호출 시 언패킹으로 여러 변수에 받습니다.

---

**문제 23. 모범답안:**

```python
c_to_f = lambda c: c * 1.8 + 32

print(f"0°C = {c_to_f(0)}°F")
print(f"100°C = {c_to_f(100)}°F")
print(f"36.5°C = {c_to_f(36.5)}°F")
```

핵심: `lambda c: c * 1.8 + 32`로 섭씨→화씨 변환을 한 줄로 정의합니다.

---

**문제 24. 모범답안:**

```python
def countdown(n):
    if n <= 0:
        print("발사!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
```

핵심: 기저 조건(`n <= 0`)에서 "발사!"를 출력하고 재귀를 멈춥니다. 그 외에는 `n`을 출력한 후 `countdown(n-1)`을 호출합니다.

---

### 🟡 중급

**문제 25. 모범답안:**

```python
balance = 10000

def deposit(amount):
    global balance
    balance += amount
    print(f"{amount:,}원 입금 → 잔액: {balance:,}원")

def withdraw(amount):
    global balance
    if amount > balance:
        print(f"{amount:,}원 출금 → 잔액 부족!")
    else:
        balance -= amount
        print(f"{amount:,}원 출금 → 잔액: {balance:,}원")

def check_balance():
    print(f"현재 잔액: {balance:,}원")

# 테스트
check_balance()
deposit(5000)
withdraw(3000)
withdraw(20000)
check_balance()
```

핵심 포인트:

- `global balance`로 전역 변수를 함수 내에서 수정합니다.
- `withdraw`에서 잔액 부족 체크를 `if`로 수행합니다.

---

### 🔴 고급

**문제 26. 모범답안:**

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

# 테스트
print("=== GCD / LCM 계산기 ===")

a, b = 48, 18
print(f"a = {a}, b = {b}")
print(f"GCD({a}, {b}) = {gcd(a, b)}")
print(f"LCM({a}, {b}) = {lcm(a, b)}")

print()

a, b = 100, 35
print(f"a = {a}, b = {b}")
print(f"GCD({a}, {b}) = {gcd(a, b)}")
print(f"LCM({a}, {b}) = {lcm(a, b)}")
```

핵심 포인트:

- **유클리드 호제법**: `gcd(a, b)` = `gcd(b, a%b)`, `b=0`이면 `a`가 GCD.
- 재귀 과정: `gcd(48, 18)` → `gcd(18, 12)` → `gcd(12, 6)` → `gcd(6, 0)` → 6
- **LCM 공식**: `a × b ÷ GCD`. `48 × 18 ÷ 6 = 144`.
- `//` 정수 나눗셈으로 정수 결과를 보장합니다.
- 검증: gcd(100, 35) → gcd(35, 30) → gcd(30, 5) → gcd(5, 0) → 5. lcm = 100 × 35 ÷ 5 = 700.

---


수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 연습문제는 Claude 및 Gemini와 협업으로 제작되었습니다.
