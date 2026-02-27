# 10장 함수 2 (고급)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 다중 반환값, 변수의 스코프, 람다 함수, 재귀 함수 등 함수의 고급 기능을 이해하고 활용할 수 있습니다. 이러한 개념들은 더욱 효율적이고 강력한 프로그램을 작성하는 데 필수적입니다.

---

## 1️⃣ **여러 값 반환하기**

파이썬 함수는 여러 개의 값을 동시에 반환할 수 있습니다.

```python
# 여러 값 반환
def get_min_max(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
  
    min_value = a
    if b < min_value:
        min_value = b
    if c < min_value:
        min_value = c
  
    return min_value, max_value

# 여러 값 받기
minimum, maximum = get_min_max(10, 5, 20)
print(f"최솟값: {minimum}")  # 5
print(f"최댓값: {maximum}")  # 20
```

### **예제 1: 통계 계산**

여러 숫자의 합계, 평균, 최댓값, 최솟값을 한 번에 계산하는 함수입니다.

```python
# 통계 계산 함수
def calculate_statistics(numbers):
    total = 0
    for num in numbers:
        total = total + num
  
    average = total / len(numbers)
  
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
  
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
  
    return total, average, max_val, min_val

# 프로그램 시작
print("📊" + "=" * 38 + "📊")
print("   점수 통계 분석")
print("📊" + "=" * 38 + "📊")

student_count = int(input("\n학생 수: "))
scores = []

print("\n점수를 입력하세요:")
for i in range(student_count):
    score = int(input(f"{i+1}번 학생: "))
    scores.append(score)

# 통계 계산
sum_val, avg_val, max_val, min_val = calculate_statistics(scores)

# 결과 출력
print("\n" + "=" * 40)
print("분석 결과")
print("=" * 40)
print(f"총점: {sum_val}점")
print(f"평균: {avg_val:.1f}점")
print(f"최고점: {max_val}점")
print(f"최저점: {min_val}점")
print("=" * 40)
```

---

## 2️⃣ **변수의 스코프 (Scope)**

변수의 스코프는 변수가 접근 가능한 범위를 의미합니다.

### **지역 변수 (Local Variable)**

함수 안에서 만든 변수는 함수 안에서만 사용할 수 있습니다.

```python
def my_function():
    local_var = 10  # 지역 변수
    print(local_var)

my_function()  # 10
# print(local_var)  # 오류! 함수 밖에서 접근 불가
```

### **전역 변수 (Global Variable)**

함수 밖에서 만든 변수는 프로그램 전체에서 사용할 수 있습니다.

```python
global_var = 100  # 전역 변수

def my_function():
    print(global_var)  # 전역 변수 읽기 가능

my_function()  # 100
print(global_var)  # 100
```

### **전역 변수 수정하기**

함수 안에서 전역 변수를 수정하려면 `global` 키워드를 사용해야 합니다.

```python
count = 0  # 전역 변수

def increment():
    global count  # 전역 변수 사용 선언
    count = count + 1

print(count)  # 0
increment()
print(count)  # 1
increment()
print(count)  # 2
```

⚠️ **주의**: 전역 변수를 남용하면 코드가 복잡해지고 버그가 생기기 쉽습니다. 가능하면 매개변수와 반환값을 사용하세요!

### **예제 2: 게임 점수 관리**

전역 변수로 게임 점수를 관리하는 프로그램입니다.

```python
# 게임 점수 관리 시스템
score = 0
level = 1

def earn_points(points):
    global score
    score = score + points
    print(f"+{points}점! 현재 점수: {score}")

def lose_points(points):
    global score
    score = score - points
    if score < 0:
        score = 0
    print(f"-{points}점! 현재 점수: {score}")

def level_up():
    global level, score
    if score >= level * 100:
        level = level + 1
        bonus = level * 50
        score = score + bonus
        print(f"\n🎉 레벨 업! 레벨 {level}")
        print(f"보너스 {bonus}점 획득!")
        return True
    return False

def show_status():
    print(f"\n현재 상태 - 레벨: {level}, 점수: {score}")

# 게임 시작
print("🎮" + "=" * 38 + "🎮")
print("   간단한 게임")
print("🎮" + "=" * 38 + "🎮")

show_status()

# 게임 진행
print("\n[ 라운드 1 ]")
earn_points(50)
earn_points(30)
lose_points(20)

if not level_up():
    print("레벨 업 조건 미달성")

print("\n[ 라운드 2 ]")
earn_points(60)
earn_points(40)

level_up()
show_status()
```

---

## 3️⃣ **람다 함수 (Lambda Function)**

람다 함수는 이름 없는 간단한 함수를 만드는 방법입니다.

```python
# 일반 함수
def add(x, y):
    return x + y

# 람다 함수
add_lambda = lambda x, y: x + y

# 사용법 동일
print(add(10, 20))         # 30
print(add_lambda(10, 20))  # 30
```

### **람다 함수의 구조**

```python
lambda 매개변수: 반환값

# 예제
square = lambda x: x ** 2
print(square(5))  # 25

# 여러 매개변수
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24
```

### **예제 3: 정렬 기준 지정**

람다 함수로 정렬 기준을 지정하는 프로그램입니다.

```python
# 학생 정보 정렬
students = [
    {"name": "김철수", "score": 85},
    {"name": "박영희", "score": 92},
    {"name": "이민수", "score": 78},
    {"name": "최지은", "score": 95}
]

print("📚" + "=" * 38 + "📚")
print("   학생 성적 정렬")
print("📚" + "=" * 38 + "📚")

# 점수 기준으로 정렬 (람다 사용)
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)

print("\n성적 순위:")
print("=" * 40)
for i, student in enumerate(sorted_students, 1):
    print(f"{i}위. {student['name']}: {student['score']}점")
print("=" * 40)
```

---

## 4️⃣ **재귀 함수 (Recursive Function)**

재귀 함수는 자기 자신을 호출하는 함수입니다.

```python
# 재귀 함수 예제 - 카운트다운
def countdown(n):
    if n <= 0:  # 기저 조건 (base case)
        print("발사! 🚀")
    else:
        print(n)
        countdown(n - 1)  # 자기 자신 호출

countdown(5)
# 출력:
# 5
# 4
# 3
# 2
# 1
# 발사! 🚀
```

```
재귀 함수의 동작

countdown(3)
   │
   ├─ print(3)
   └─ countdown(2)
         │
         ├─ print(2)
         └─ countdown(1)
               │
               ├─ print(1)
               └─ countdown(0)
                     │
                     └─ print("발사!")
```

### **팩토리얼 계산**

```python
# 팩토리얼 (n!)
# 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    if n <= 1:  # 기저 조건
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
print(factorial(4))  # 24
print(factorial(3))  # 6
```

⚠️ **중요**: 재귀 함수는 반드시 종료 조건(기저 조건)이 있어야 합니다. 그렇지 않으면 무한 반복에 빠집니다!

### **예제 4: 피보나치 수열**

재귀 함수로 피보나치 수열을 계산하는 프로그램입니다.

```python
# 피보나치 수열 계산 함수
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 프로그램 시작
print("🔢" + "=" * 38 + "🔢")
print("   피보나치 수열 생성기")
print("🔢" + "=" * 38 + "🔢")

count = int(input("\n몇 개의 수를 생성할까요? "))

print("\n피보나치 수열:")
print("=" * 40)

for i in range(count):
    value = fibonacci(i)
    print(f"F({i}) = {value}")

print("=" * 40)
```

---

## 5️⃣ **재귀 vs 반복문**

같은 문제를 재귀와 반복문으로 해결할 수 있습니다.

### **팩토리얼 비교**

```python
# 재귀 방식
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 반복문 방식
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# 둘 다 같은 결과
print(factorial_recursive(5))  # 120
print(factorial_loop(5))       # 120
```

**장단점 비교:**

| 구분        | 재귀 함수       | 반복문        |
| ----------- | --------------- | ------------- |
| 가독성      | 직관적          | 약간 복잡     |
| 속도        | 느림            | 빠름          |
| 메모리      | 많이 사용       | 적게 사용     |
| 적합한 경우 | 트리, 수학 문제 | 일반적인 반복 |

---

## 6️⃣ **함수의 다양한 활용**

### **예제 5: 메뉴 기반 계산기**

여러 함수를 조합한 종합 계산기 프로그램입니다.

```python
# 계산 함수들
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다"
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        return "음수는 불가능합니다"
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 메뉴 출력 함수
def show_menu():
    print("\n" + "=" * 40)
    print("계산기 메뉴")
    print("=" * 40)
    print("1. 덧셈 (+)")
    print("2. 뺄셈 (-)")
    print("3. 곱셈 (×)")
    print("4. 나눗셈 (÷)")
    print("5. 거듭제곱 (^)")
    print("6. 팩토리얼 (!)")
    print("7. 종료")
    print("=" * 40)

# 프로그램 시작
print("🔢" + "=" * 38 + "🔢")
print("   다기능 계산기")
print("🔢" + "=" * 38 + "🔢")

while True:
    show_menu()
    choice = input("\n선택: ")
  
    if choice == "7":
        print("\n계산기를 종료합니다.")
        break
  
    if choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("\n첫 번째 숫자: "))
        num2 = float(input("두 번째 숫자: "))
  
        if choice == "1":
            result = add(num1, num2)
            print(f"\n결과: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\n결과: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\n결과: {num1} × {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"\n결과: {num1} ÷ {num2} = {result}")
        elif choice == "5":
            result = power(num1, num2)
            print(f"\n결과: {num1} ^ {num2} = {result}")
  
    elif choice == "6":
        num = int(input("\n숫자 입력: "))
        result = factorial(num)
        print(f"\n결과: {num}! = {result}")
  
    else:
        print("\n❌ 올바른 메뉴를 선택하세요.")
```

---

## 7️⃣ **고급 패턴: 헬퍼 함수**

복잡한 함수를 작은 함수들로 나누어 작성하는 패턴입니다.

### **예제 6: 성적 관리 시스템**

여러 헬퍼 함수를 사용하는 종합 프로그램입니다.

```python
# 헬퍼 함수들
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

def count_pass(scores):
    count = 0
    for score in scores:
        if score >= 60:
            count = count + 1
    return count

def analyze_scores(scores):
    avg = calculate_average(scores)
    pass_count = count_pass(scores)
    pass_rate = (pass_count / len(scores)) * 100
  
    max_score = scores[0]
    min_score = scores[0]
    for score in scores:
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
  
    return avg, pass_count, pass_rate, max_score, min_score

# 프로그램 시작
print("📊" + "=" * 38 + "📊")
print("   성적 관리 시스템")
print("📊" + "=" * 38 + "📊")

student_count = int(input("\n학생 수: "))
scores_list = []

print("\n점수를 입력하세요:")
for i in range(student_count):
    score = int(input(f"{i+1}번: "))
    scores_list.append(score)

# 분석
avg, pass_cnt, pass_pct, max_s, min_s = analyze_scores(scores_list)

# 결과 출력
print("\n" + "=" * 40)
print("분석 결과")
print("=" * 40)
print(f"평균 점수: {avg:.1f}점")
print(f"합격자: {pass_cnt}명 ({pass_pct:.0f}%)")
print(f"최고점: {max_s}점")
print(f"최저점: {min_s}점")

print("\n등급 분포:")
grade_count = {}
for score in scores_list:
    grade = get_grade(score)
    if grade in grade_count:
        grade_count[grade] = grade_count[grade] + 1
    else:
        grade_count[grade] = 1

for grade in ["A", "B", "C", "D", "F"]:
    count = grade_count.get(grade, 0)
    print(f"  {grade}등급: {count}명")

print("=" * 40)
```

---

## 📝 **핵심 개념 정리**

함수는 여러 개의 값을 튜플 형태로 반환할 수 있으며, 언패킹을 통해 여러 변수에 동시에 할당할 수 있습니다.

변수의 스코프는 지역(함수 내부)과 전역(프로그램 전체)으로 나뉘며, 함수 내에서 전역 변수를 수정하려면 `global` 키워드가 필요합니다.

람다 함수는 `lambda` 키워드로 만드는 간단한 익명 함수로, 주로 정렬이나 필터링의 기준으로 사용됩니다.

재귀 함수는 자기 자신을 호출하는 함수로, 반드시 종료 조건(기저 조건)이 있어야 합니다. 재귀는 직관적이지만 반복문보다 느리고 메모리를 많이 사용합니다.

복잡한 기능은 작은 함수들(헬퍼 함수)로 나누어 작성하면 코드의 가독성과 유지보수성이 향상됩니다.

---

## 💡 **실습 과제**

### **과제 1: 최대공약수 구하기**

재귀 함수로 두 수의 최대공약수를 구하는 함수를 작성하세요. (유클리드 호제법)

```python
# 힌트
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 테스트
print(gcd(48, 18))  # 6
print(gcd(100, 35))  # 5
```

### **과제 2: 리스트 뒤집기**

재귀 함수로 리스트를 뒤집는 함수를 작성하세요.

```python
# 힌트
def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])

# 테스트
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

---

## ✅ **퀴즈**

### **[초급] 1번**

다음 코드의 실행 결과는?

```python
def get_values():
    return 10, 20

a, b = get_values()
print(a + b)
```

1. 10
2. 20
3. 30
4. 오류 발생

### **[중급] 2번**

람다 함수를 올바르게 작성한 것은?

```python
1. lambda x: x * 2
2. def lambda(x): return x * 2
3. lambda(x): x * 2
4. lambda: x * 2
```

1. 1번
2. 2번
3. 3번
4. 4번

### **[중급] 3번**

다음 재귀 함수의 결과는?

```python
def func(n):
    if n == 0:
        return 0
    return n + func(n - 1)

print(func(3))
```

1. 0
2. 3
3. 6
4. 무한 반복

### **[고급] 4번**

전역 변수를 수정하는 올바른 방법은?

```python
x = 10

def modify():
    ___
    x = 20

1. global x
2. local x
3. nonlocal x
4. 아무것도 필요 없음
```

1. 1번
2. 2번
3. 3번
4. 4번

### **[고급] 5번**

다음 중 재귀 함수의 필수 요소는?

```python
1. 자기 자신을 호출
2. 종료 조건 (기저 조건)
3. 반환값
4. 1번과 2번 모두
```

1. 1번만
2. 2번만
3. 3번만
4. 4번

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 3**
함수가 10과 20을 반환하고, a=10, b=20이 되어 10 + 20 = 30이 출력됩니다.

**2번 정답: 1**
람다 함수는 `lambda 매개변수: 표현식` 형태로 작성합니다. 1번이 올바릅니다.

**3번 정답: 3**
func(3) = 3 + func(2) = 3 + 2 + func(1) = 3 + 2 + 1 + func(0) = 3 + 2 + 1 + 0 = 6

**4번 정답: 1**
함수 내에서 전역 변수를 수정하려면 `global x`를 선언해야 합니다.

**5번 정답: 4**
재귀 함수는 자기 자신을 호출하고, 반드시 종료 조건이 있어야 무한 반복을 피할 수 있습니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 리스트에 대해 배웁니다. 여러 개의 값을 순서대로 저장하고 관리하는 방법을 학습하게 됩니다. 리스트는 파이썬에서 가장 많이 사용되는 자료구조입니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
