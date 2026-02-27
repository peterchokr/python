# 11장 리스트

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 리스트를 사용하여 여러 개의 값을 순서대로 저장하고 관리할 수 있습니다. 리스트는 파이썬에서 가장 많이 사용되는 자료구조로, 대량의 데이터를 효율적으로 처리하는 핵심 도구입니다.

---

## 1️⃣ **리스트란 무엇인가?**

리스트는 여러 개의 값을 순서대로 저장하는 자료구조입니다. 마치 쇼핑 목록처럼 여러 항목을 하나의 목록으로 관리할 수 있습니다.

```python
# 리스트 없이 여러 값 저장
student1 = "김철수"
student2 = "박영희"
student3 = "이민수"
student4 = "최지은"

# 리스트로 간단하게!
students = ["김철수", "박영희", "이민수", "최지은"]
```

### **리스트 생성하기**

리스트는 대괄호 `[]`로 만들며, 값들은 쉼표로 구분합니다.

```python
# 빈 리스트
empty = []

# 숫자 리스트
scores = [85, 90, 78, 92, 88]

# 문자열 리스트
fruits = ["사과", "바나나", "오렌지"]

# 출력
print(scores)  # [85, 90, 78, 92, 88]
print(fruits)  # ['사과', '바나나', '오렌지']
```

```
리스트의 구조

    인덱스:  0      1        2         3
           ┌──────┬────────┬─────────┬──────┐
fruits =   │ 사과 │ 바나나 │ 오렌지  │ 포도 │
           └──────┴────────┴─────────┴──────┘
    역인덱스: -4     -3       -2       -1
```

### **예제 1: 영화 관람 기록**

본 영화들을 리스트로 관리하는 프로그램입니다.

```python
# 영화 관람 기록 프로그램
print("🎬" + "=" * 38 + "🎬")
print("   영화 관람 기록")
print("🎬" + "=" * 38 + "🎬")

# 영화 목록
movies = [
    "기생충",
    "어벤져스",
    "인터스텔라",
    "타이타닉",
    "겨울왕국"
]

# 목록 출력
print("\n📽️ 관람한 영화:")
print("-" * 40)

for i in range(len(movies)):
    print(f"{i+1}. {movies[i]}")

print("-" * 40)
print(f"총 {len(movies)}편 관람")
```

---

## 2️⃣ **리스트 인덱싱**

리스트의 각 항목은 인덱스(위치)로 접근할 수 있습니다. 인덱스는 0부터 시작합니다.

```python
# 리스트 인덱싱
fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]

# 양수 인덱스 (앞에서부터)
print(fruits[0])   # 사과
print(fruits[1])   # 바나나
print(fruits[4])   # 딸기

# 음수 인덱스 (뒤에서부터)
print(fruits[-1])  # 딸기 (마지막)
print(fruits[-2])  # 포도 (마지막에서 두 번째)
```

### **인덱스 값 변경하기**

```python
# 값 변경
menu = ["커피", "주스", "우유"]
print(menu)  # ['커피', '주스', '우유']

menu[1] = "차"
print(menu)  # ['커피', '차', '우유']
```

### **예제 2: 주간 판매 기록**

요일별 판매량을 저장하고 수정하는 프로그램입니다.

```python
# 주간 판매 기록 프로그램
print("📊" + "=" * 38 + "📊")
print("   주간 판매 기록 관리")
print("📊" + "=" * 38 + "📊")

# 요일별 판매량
weekdays = ["월", "화", "수", "목", "금", "토", "일"]
sales = [120, 150, 140, 160, 180, 250, 230]

# 현재 기록 출력
print("\n📈 이번 주 판매량:")
print("-" * 40)

for i in range(len(weekdays)):
    print(f"{weekdays[i]}요일: {sales[i]}개")

print("-" * 40)

# 특정 요일 데이터 수정
print("\n수요일 판매량을 수정합니다.")
sales[2] = 145

print("\n📈 수정된 판매량:")
print("-" * 40)

for i in range(len(weekdays)):
    print(f"{weekdays[i]}요일: {sales[i]}개")

print("-" * 40)

# 통계
total = 0
for sale in sales:
    total = total + sale

average = total / len(sales)

print(f"\n총 판매량: {total}개")
print(f"일 평균: {average:.1f}개")
```

---

## 3️⃣ **리스트 슬라이싱**

리스트의 일부분을 잘라낼 수 있습니다.

```python
# 슬라이싱
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [시작:끝]
print(numbers[2:5])    # [2, 3, 4]
print(numbers[:4])     # [0, 1, 2, 3] (처음부터 3까지)
print(numbers[6:])     # [6, 7, 8, 9] (6부터 끝까지)

# [시작:끝:간격]
print(numbers[::2])    # [0, 2, 4, 6, 8] (2칸씩)
print(numbers[::-1])   # [9, 8, 7, ..., 0] (역순)
```

### **예제 3: 학생 성적 그룹**

전체 학생을 그룹으로 나누는 프로그램입니다.

```python
# 학생 성적 그룹 나누기
print("📚" + "=" * 38 + "📚")
print("   학생 성적 그룹 관리")
print("📚" + "=" * 38 + "📚")

# 전체 학생 점수 (30명)
scores = [
    85, 92, 78, 95, 88, 76, 90, 84, 87, 91,
    79, 93, 82, 88, 94, 77, 89, 86, 81, 92,
    75, 90, 83, 87, 94, 80, 88, 91, 85, 89
]

print(f"\n전체 학생 수: {len(scores)}명")

# 그룹 나누기 (각 10명씩)
group1 = scores[:10]
group2 = scores[10:20]
group3 = scores[20:]

# 각 그룹 평균 계산
def calculate_average(score_list):
    total = 0
    for score in score_list:
        total = total + score
    return total / len(score_list)

avg1 = calculate_average(group1)
avg2 = calculate_average(group2)
avg3 = calculate_average(group3)

# 결과 출력
print("\n" + "=" * 40)
print("그룹별 평균")
print("=" * 40)
print(f"1그룹 (1-10번): {avg1:.1f}점")
print(f"2그룹 (11-20번): {avg2:.1f}점")
print(f"3그룹 (21-30번): {avg3:.1f}점")
print("=" * 40)
```

---

## 4️⃣ **리스트에 항목 추가하기**

### **append() - 끝에 추가**

```python
# append() 메서드
fruits = ["사과", "바나나"]
print(fruits)  # ['사과', '바나나']

fruits.append("오렌지")
print(fruits)  # ['사과', '바나나', '오렌지']

fruits.append("포도")
print(fruits)  # ['사과', '바나나', '오렌지', '포도']
```

### **insert() - 특정 위치에 추가**

```python
# insert(위치, 값)
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)  # 인덱스 2에 3 삽입
print(numbers)  # [1, 2, 3, 4, 5]
```

### **예제 4: 쇼핑 카트**

쇼핑 카트에 상품을 추가하는 프로그램입니다.

```python
# 쇼핑 카트 프로그램
print("🛒" + "=" * 38 + "🛒")
print("   쇼핑 카트")
print("🛒" + "=" * 38 + "🛒")

cart = []
prices = []

print("\n상품을 추가하세요 (종료: q)")

while True:
    item = input("\n상품명 (종료: q): ")
  
    if item == "q" or item == "Q":
        break
  
    price = int(input("가격: "))
  
    # 카트에 추가
    cart.append(item)
    prices.append(price)
  
    print(f"✓ {item} 추가됨")

# 장바구니 내용
print("\n" + "=" * 40)
print("🛒 장바구니")
print("=" * 40)

if len(cart) == 0:
    print("장바구니가 비어있습니다.")
else:
    for i in range(len(cart)):
        print(f"{i+1}. {cart[i]}: {prices[i]:,}원")
  
    total = 0
    for price in prices:
        total = total + price
  
    print("-" * 40)
    print(f"총 금액: {total:,}원")

print("=" * 40)
```

---

## 5️⃣ **리스트에서 항목 제거하기**

### **remove() - 값으로 제거**

```python
# remove(값)
fruits = ["사과", "바나나", "오렌지", "바나나"]
fruits.remove("바나나")  # 첫 번째 "바나나"만 제거
print(fruits)  # ['사과', '오렌지', '바나나']
```

### **pop() - 위치로 제거**

```python
# pop() - 마지막 항목 제거하고 반환
fruits = ["사과", "바나나", "오렌지"]
last = fruits.pop()
print(last)    # 오렌지
print(fruits)  # ['사과', '바나나']

# pop(인덱스) - 특정 위치 제거
fruits = ["사과", "바나나", "오렌지"]
item = fruits.pop(1)
print(item)    # 바나나
print(fruits)  # ['사과', '오렌지']
```

### **예제 5: TO-DO 리스트**

할 일을 추가하고 완료하는 프로그램입니다.

```python
# TO-DO 리스트 관리 프로그램
print("✅" + "=" * 38 + "✅")
print("   TO-DO 리스트")
print("✅" + "=" * 38 + "✅")

todo_list = []

while True:
    print("\n" + "=" * 40)
    print("1. 할 일 추가")
    print("2. 할 일 완료")
    print("3. 목록 보기")
    print("4. 종료")
    print("=" * 40)
  
    choice = input("\n선택: ")
  
    if choice == "1":
        task = input("\n할 일: ")
        todo_list.append(task)
        print(f"✓ '{task}' 추가됨")
  
    elif choice == "2":
        if len(todo_list) == 0:
            print("\n할 일이 없습니다.")
        else:
            print("\n📋 현재 목록:")
            for i in range(len(todo_list)):
                print(f"{i+1}. {todo_list[i]}")
        
            num = int(input("\n완료한 번호: "))
            if 1 <= num <= len(todo_list):
                completed = todo_list.pop(num - 1)
                print(f"\n✅ '{completed}' 완료!")
            else:
                print("\n잘못된 번호입니다.")
  
    elif choice == "3":
        print("\n📋 TO-DO 리스트:")
        print("-" * 40)
        if len(todo_list) == 0:
            print("할 일이 없습니다.")
        else:
            for i in range(len(todo_list)):
                print(f"{i+1}. {todo_list[i]}")
        print("-" * 40)
        print(f"총 {len(todo_list)}개")
  
    elif choice == "4":
        print("\n프로그램을 종료합니다.")
        break
  
    else:
        print("\n잘못된 선택입니다.")
```

---

## 6️⃣ **리스트 정렬하기**

### **sort() - 리스트 자체를 정렬**

```python
# 오름차순 정렬
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]

# 내림차순 정렬
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 2, 1]
```

### **reverse() - 순서 뒤집기**

```python
# 순서 뒤집기
fruits = ["사과", "바나나", "오렌지"]
fruits.reverse()
print(fruits)  # ['오렌지', '바나나', '사과']
```

### **예제 6: 시험 성적 처리**

학생 성적을 분석하고 순위를 매기는 프로그램입니다.

```python
# 시험 성적 처리 프로그램
print("📝" + "=" * 38 + "📝")
print("   시험 성적 처리 시스템")
print("📝" + "=" * 38 + "📝")

student_count = int(input("\n학생 수: "))

names = []
scores = []

print("\n학생 정보를 입력하세요:")
for i in range(student_count):
    print(f"\n[{i+1}번 학생]")
    name = input("이름: ")
    score = int(input("점수: "))
  
    names.append(name)
    scores.append(score)

# 성적 순위 (점수 내림차순)
# 원본 보존을 위해 복사
sorted_scores = scores.copy()
sorted_scores.sort(reverse=True)

# 결과 출력
print("\n" + "=" * 40)
print("성적 순위")
print("=" * 40)

for i, score in enumerate(sorted_scores, 1):
    # 해당 점수를 받은 학생 찾기
    index = scores.index(score)
    print(f"{i}위. {names[index]}: {score}점")

# 통계
average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print("\n" + "=" * 40)
print("통계")
print("=" * 40)
print(f"평균: {average:.1f}점")
print(f"최고점: {highest}점")
print(f"최저점: {lowest}점")
print("=" * 40)
```

---

## 7️⃣ **리스트 컴프리헨션**

리스트를 간결하게 만드는 방법입니다.

```python
# 기본 방법
numbers = []
for i in range(1, 11):
    numbers.append(i * 2)
print(numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 리스트 컴프리헨션
numbers = [i * 2 for i in range(1, 11)]
print(numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### **조건이 있는 컴프리헨션**

```python
# 짝수만
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 제곱 (3의 배수만)
squares = [i**2 for i in range(1, 11) if i % 3 == 0]
print(squares)  # [9, 36, 81]
```

### **예제 7: 할인 가격 계산**

여러 상품의 할인 가격을 계산하는 프로그램입니다.

```python
# 할인 가격 계산 프로그램
print("💰" + "=" * 38 + "💰")
print("   할인 가격 계산기")
print("💰" + "=" * 38 + "💰")

# 원래 가격
original_prices = [50000, 30000, 80000, 120000, 45000]

print("\n원래 가격:")
for i, price in enumerate(original_prices, 1):
    print(f"{i}. {price:,}원")

# 할인율 입력
discount_rate = int(input("\n할인율 (%): "))

# 리스트 컴프리헨션으로 할인 가격 계산
discounted_prices = [
    int(price * (100 - discount_rate) / 100)
    for price in original_prices
]

# 결과 출력
print("\n" + "=" * 40)
print(f"{discount_rate}% 할인 가격")
print("=" * 40)

for i in range(len(original_prices)):
    saving = original_prices[i] - discounted_prices[i]
    print(f"{i+1}. {original_prices[i]:,}원 → {discounted_prices[i]:,}원")
    print(f"   (절약: {saving:,}원)")

total_original = sum(original_prices)
total_discounted = sum(discounted_prices)
total_saving = total_original - total_discounted

print("\n" + "-" * 40)
print(f"전체 원가: {total_original:,}원")
print(f"할인 후: {total_discounted:,}원")
print(f"총 절약: {total_saving:,}원")
print("=" * 40)
```

---

## 📝 **핵심 개념 정리**

리스트는 대괄호 `[]`로 만들며, 여러 값을 순서대로 저장합니다. 인덱스는 0부터 시작하며, 음수 인덱스로 뒤에서부터 접근할 수 있습니다.

`append()`로 끝에 항목을 추가하고, `insert()`로 특정 위치에 삽입합니다. `remove()`로 값으로 제거하고, `pop()`으로 위치로 제거하며 제거된 값을 반환합니다.

`sort()`로 리스트를 정렬하고, `reverse()`로 순서를 뒤집습니다. 슬라이싱으로 리스트의 일부분을 가져올 수 있습니다.

리스트 컴프리헨션은 `[표현식 for 항목 in 리스트]` 형태로 리스트를 간결하게 만드는 방법입니다. 조건을 추가하여 필터링할 수도 있습니다.

---

## 💡 **실습 과제**

### **과제 1: 최댓값/최솟값 찾기**

리스트에서 max()와 min() 함수를 사용하지 않고 최댓값과 최솟값을 찾는 프로그램을 작성하세요.

```python
# 힌트
numbers = [23, 45, 12, 67, 34, 89, 21]

max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

# 최솟값도 동일한 방식으로
```

### **과제 2: 중복 제거**

리스트에서 중복된 값을 제거하는 프로그램을 작성하세요.

```python
# 힌트
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 3]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)  # [1, 2, 3, 4, 5]
```

---

## ✅ **퀴즈**

### **[초급] 1번**

다음 코드의 출력 결과는?

```python
fruits = ["사과", "바나나", "오렌지"]
print(fruits[1])
```

1. 사과
2. 바나나
3. 오렌지
4. 오류 발생

### **[중급] 2번**

다음 코드 실행 후 리스트는?

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

1. [1, 2, 3]
2. [1, 2, 3, 4]
3. [4, 1, 2, 3]
4. 오류 발생

### **[중급] 3번**

다음 코드의 출력 결과는?

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])
```

1. [1, 2, 3]
2. [2, 3, 4]
3. [1, 2, 3, 4]
4. [2, 3]

### **[고급] 4번**

다음 코드 실행 후 리스트는?

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)
```

1. [3, 1, 4, 1, 5]
2. [1, 1, 3, 4, 5]
3. [5, 4, 3, 1, 1]
4. [1, 3, 4, 5]

### **[고급] 5번**

리스트 컴프리헨션으로 1-10 중 홀수만 만들기

```python
1. [i for i in range(1, 11)]
2. [i for i in range(1, 11) if i % 2 == 0]
3. [i for i in range(1, 11) if i % 2 == 1]
4. [i % 2 for i in range(1, 11)]
```

1. 1번
2. 2번
3. 3번
4. 4번

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
인덱스 1은 두 번째 항목인 "바나나"를 가리킵니다.

**2번 정답: 2**
`append(4)`는 리스트 끝에 4를 추가하므로 [1, 2, 3, 4]가 됩니다.

**3번 정답: 2**
슬라이싱 [1:4]는 인덱스 1부터 3까지(4 직전까지)를 의미하므로 [2, 3, 4]입니다.

**4번 정답: 2**
`sort()`는 리스트를 오름차순으로 정렬하므로 [1, 1, 3, 4, 5]가 됩니다.

**5번 정답: 3**
홀수는 2로 나눈 나머지가 1인 수이므로 `if i % 2 == 1` 조건을 사용합니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 튜플과 세트에 대해 배웁니다. 튜플은 변경할 수 없는 리스트이고, 세트는 중복을 허용하지 않는 집합입니다. 두 자료구조의 특징과 활용법을 학습하게 됩니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
