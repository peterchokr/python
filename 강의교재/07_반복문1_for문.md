# 7장 반복문 1 (for 문)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 for 문을 사용하여 정해진 횟수만큼 코드를 반복 실행할 수 있습니다. 반복문은 프로그래밍의 핵심 기능으로, 같은 작업을 여러 번 자동으로 수행할 수 있게 해줍니다.

---

## 1️⃣ **for 문이란?**

for 문은 정해진 범위나 횟수만큼 코드를 반복 실행하는 구문입니다. "이 작업을 10번 해라", "이 리스트의 모든 항목에 대해 작업해라"와 같은 명령을 쉽게 구현할 수 있습니다.

```python
# for 문 없이 반복 작업
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

# for 문으로 간단하게
for i in range(5):
    print("안녕하세요")
```

```
for 문의 동작 원리

      시작
        │
        ▼
    ┌───────┐
    │ range │
    │  생성  │
    └───┬───┘
        │
    ┌───▼────┐
 ┌─>│남은 값?│
 │  └───┬────┘
 │      │
 │  ┌───┴───┐
 │ Yes     No
 │  │       │
 │┌─▼─┐  ┌─▼─┐
 ││반복│  │종료│
 ││실행│  └───┘
 │└─┬─┘
 │  │
 └──┘
```

---

## 2️⃣ **range() 함수**

`range()` 함수는 숫자 범위를 생성하는 함수입니다. for 문과 함께 가장 많이 사용됩니다.

### **range()의 세 가지 형태**

```python
# 1. range(끝)
# 0부터 (끝-1)까지
for i in range(5):
    print(i, end=" ")
# 출력: 0 1 2 3 4

print()

# 2. range(시작, 끝)
# 시작부터 (끝-1)까지
for i in range(1, 6):
    print(i, end=" ")
# 출력: 1 2 3 4 5

print()

# 3. range(시작, 끝, 간격)
# 시작부터 (끝-1)까지 간격만큼 증가
for i in range(0, 10, 2):
    print(i, end=" ")
# 출력: 0 2 4 6 8
```

```
range() 함수의 이해

range(5)
┌───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │
└───┴───┴───┴───┴───┘

range(1, 6)
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘

range(0, 10, 2)
┌───┬───┬───┬───┬───┐
│ 0 │ 2 │ 4 │ 6 │ 8 │
└───┴───┴───┴───┴───┘

range(10, 0, -1)
┌────┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 10 │ 9 │ 8 │ 7 │ 6 │ 5 │ 4 │ 3 │ 2 │ 1 │
└────┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

### **역순 반복**

```python
# 역순으로 반복 (간격을 음수로)
for i in range(5, 0, -1):
    print(i, end=" ")
# 출력: 5 4 3 2 1
```

### **예제 1: 카운트다운**

로켓 발사 카운트다운을 만드는 프로그램입니다.

```python
# 로켓 발사 카운트다운
print("🚀" + "=" * 38 + "🚀")
print("   로켓 발사 카운트다운")
print("🚀" + "=" * 38 + "🚀")

print("\n발사 준비 중...")
print()

# 10부터 1까지 카운트다운
for count in range(10, 0, -1):
    print(f"  {count}...")

print("\n🚀 발사!!! 🚀")
print()

# 상승 표시
for altitude in range(0, 101, 20):
    print(f"고도: {altitude}m")

print("\n✨ 발사 성공!")
```

---

## 3️⃣ **문자열 순회**

for 문으로 문자열의 각 문자를 하나씩 처리할 수 있습니다.

```python
# 문자열 순회
message = "PYTHON"

for char in message:
    print(char)

# 출력:
# P
# Y
# T
# H
# O
# N
```

### **문자 개수 세기**

```python
text = "Hello World"
vowel_count = 0

for char in text:
    if char in "aeiouAEIOU":
        vowel_count = vowel_count + 1

print(f"모음 개수: {vowel_count}")  # 3
```

### **예제 2: 이름 분석기**

입력받은 이름을 분석하는 프로그램입니다.

```python
# 이름 분석 프로그램
print("✨" + "=" * 38 + "✨")
print("   이름 분석기")
print("✨" + "=" * 38 + "✨")

name = input("\n이름을 입력하세요: ")

# 분석 결과
print("\n" + "=" * 40)
print("분석 결과")
print("=" * 40)

# 1. 글자 수
print(f"총 글자 수: {len(name)}자")

# 2. 각 글자 출력
print("\n글자 분리:")
for i in range(len(name)):
    print(f"  {i+1}번째: {name[i]}")

# 3. 거꾸로
print("\n거꾸로 쓰기:")
reverse_name = ""
for char in name:
    reverse_name = char + reverse_name
print(f"  {reverse_name}")

# 4. 대문자로 (영문인 경우)
print("\n대문자 변환:")
upper_name = ""
for char in name:
    upper_name = upper_name + char.upper()
print(f"  {upper_name}")

print("=" * 40)
```

---

## 4️⃣ **반복문과 누적**

반복문에서 값을 누적하여 합계, 평균 등을 계산할 수 있습니다.

```python
# 1부터 10까지의 합
total = 0

for i in range(1, 11):
    total = total + i
    print(f"{i}까지의 합: {total}")

print(f"\n최종 합계: {total}")  # 55
```

### **예제 3: 저금통 계산기**

매일 저축한 금액을 누적하여 계산하는 프로그램입니다.

```python
# 저금통 계산 프로그램
print("🐷" + "=" * 38 + "🐷")
print("   30일 저축 챌린지")
print("🐷" + "=" * 38 + "🐷")

print("\n매일 저축할 금액을 입력하세요")
daily_amount = int(input("일일 저축액: "))

total_saved = 0

print("\n" + "=" * 40)
print("저축 현황")
print("=" * 40)

# 30일 동안 저축
for day in range(1, 31):
    total_saved = total_saved + daily_amount
  
    # 7일마다 중간 보고
    if day % 7 == 0:
        print(f"{day}일차: {total_saved:,}원 💰")

# 최종 결과
print("\n" + "=" * 40)
print("30일 챌린지 완료!")
print("=" * 40)
print(f"총 저축액: {total_saved:,}원")
print(f"일 평균: {daily_amount:,}원")

# 목표 달성 여부
goal = 100000
if total_saved >= goal:
    print(f"\n🎉 목표 {goal:,}원 달성!")
else:
    shortage = goal - total_saved
    print(f"\n💡 목표까지 {shortage:,}원 부족")

print("=" * 40)
```

---

## 5️⃣ **중첩 for 문**

for 문 안에 또 다른 for 문을 넣을 수 있습니다. 2차원 패턴이나 표를 만들 때 유용합니다.

```python
# 중첩 for 문
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # 줄바꿈

# 출력:
# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)
```

### **예제 4: 구구단**

구구단을 출력하는 프로그램입니다.

```python
# 구구단 프로그램
print("📚" + "=" * 38 + "📚")
print("   구구단")
print("📚" + "=" * 38 + "📚")

start_dan = int(input("\n시작 단: "))
end_dan = int(input("끝 단: "))

print("\n" + "=" * 40)

# 각 단 출력
for dan in range(start_dan, end_dan + 1):
    print(f"\n[ {dan}단 ]")
    print("-" * 20)
  
    # 1부터 9까지 곱하기
    for num in range(1, 10):
        result = dan * num
        print(f"{dan} × {num} = {result}")

print("\n" + "=" * 40)
```

---

## 6️⃣ **별 패턴 출력**

중첩 반복문을 사용하여 다양한 패턴을 만들 수 있습니다.

### **패턴 1: 삼각형**

```python
# 별 삼각형
print("별 삼각형")
print("-" * 20)

for i in range(1, 6):
    print("★" * i)

# 출력:
# ★
# ★★
# ★★★
# ★★★★
# ★★★★★
```

### **패턴 2: 역삼각형**

```python
# 역삼각형
print("\n역삼각형")
print("-" * 20)

for i in range(5, 0, -1):
    print("★" * i)

# 출력:
# ★★★★★
# ★★★★
# ★★★
# ★★
# ★
```

### **예제 5: 패턴 출력기**

다양한 별 패턴을 출력하는 프로그램입니다.

```python
# 별 패턴 출력 프로그램
print("⭐" + "=" * 38 + "⭐")
print("   별 패턴 출력기")
print("⭐" + "=" * 38 + "⭐")

height = int(input("\n높이 입력 (1-10): "))

print("\n" + "=" * 40)
print("패턴 1: 직각삼각형")
print("=" * 40)

for i in range(1, height + 1):
    print("★" * i)

print("\n" + "=" * 40)
print("패턴 2: 역직각삼각형")
print("=" * 40)

for i in range(height, 0, -1):
    print("★" * i)

print("\n" + "=" * 40)
print("패턴 3: 피라미드")
print("=" * 40)

for i in range(1, height + 1):
    # 공백 출력
    spaces = " " * (height - i)
    # 별 출력
    stars = "★" * (2 * i - 1)
    print(spaces + stars)

print("\n" + "=" * 40)
print("패턴 4: 마름모")
print("=" * 40)

# 위쪽 삼각형
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "★" * (2 * i - 1)
    print(spaces + stars)

# 아래쪽 역삼각형
for i in range(height - 1, 0, -1):
    spaces = " " * (height - i)
    stars = "★" * (2 * i - 1)
    print(spaces + stars)

print("=" * 40)
```

---

## 7️⃣ **실전 활용 예제**

### **예제 6: 시험 점수 분석**

여러 학생의 점수를 입력받아 분석하는 프로그램입니다.

```python
# 시험 점수 분석 프로그램
print("📝" + "=" * 38 + "📝")
print("   시험 점수 분석")
print("📝" + "=" * 38 + "📝")

student_count = int(input("\n학생 수: "))

total_score = 0
highest_score = 0
lowest_score = 100
pass_count = 0  # 60점 이상

print("\n점수를 입력하세요:")

for i in range(1, student_count + 1):
    score = int(input(f"{i}번 학생: "))
  
    # 합계 누적
    total_score = total_score + score
  
    # 최고점 찾기
    if score > highest_score:
        highest_score = score
  
    # 최저점 찾기
    if score < lowest_score:
        lowest_score = score
  
    # 합격자 수 세기
    if score >= 60:
        pass_count = pass_count + 1

# 평균 계산
average = total_score / student_count

# 결과 출력
print("\n" + "=" * 40)
print("분석 결과")
print("=" * 40)
print(f"총 학생 수: {student_count}명")
print(f"평균 점수: {average:.1f}점")
print(f"최고 점수: {highest_score}점")
print(f"최저 점수: {lowest_score}점")
print(f"합격자 수: {pass_count}명 ({pass_count/student_count*100:.0f}%)")

# 등급 분포
print("\n등급 분포:")
print("  A등급 (90점 이상)")
print("  B등급 (80-89점)")
print("  C등급 (70-79점)")
print("  D등급 (60-69점)")
print("  F등급 (60점 미만)")

print("=" * 40)
```

---

## 📝 **핵심 개념 정리**

for 문은 정해진 범위나 횟수만큼 코드를 반복 실행합니다. `range()` 함수로 숫자 범위를 지정하며, `range(끝)`, `range(시작, 끝)`, `range(시작, 끝, 간격)` 세 가지 형태로 사용할 수 있습니다.

문자열도 for 문으로 순회할 수 있으며, 각 문자를 하나씩 처리할 수 있습니다. 반복문에서 변수에 값을 누적하여 합계, 평균, 최댓값, 최솟값 등을 계산할 수 있습니다.

중첩 for 문은 반복문 안에 또 다른 반복문을 넣는 것으로, 2차원 패턴이나 표를 만들 때 유용합니다. 별 패턴, 구구단, 좌석 배치도 등 다양한 프로그램을 만들 수 있습니다.

---

## 💡 **실습 과제**

### **과제 1: 구구단 선택 출력**

사용자가 원하는 단 하나만 출력하는 프로그램을 작성하세요.

```python
# 힌트
dan = int(input("몇 단? "))

print(f"\n{dan}단")
print("=" * 20)

for i in range(1, 10):
    print(f"{dan} × {i} = {dan * i}")
```

### **과제 2: 별 사각형 출력**

가로와 세로 크기를 입력받아 별로 사각형을 그리는 프로그램을 작성하세요.

```python
# 힌트
width = int(input("가로: "))
height = int(input("세로: "))

for i in range(height):
    print("★" * width)
```

---

## ✅ **퀴즈**

### **[초급] 1번**

다음 코드의 출력 횟수는?

```python
for i in range(5):
    print("Hello")
```

1. 4번
2. 5번
3. 6번
4. 무한 반복

### **[중급] 2번**

다음 코드의 출력 결과는?

```python
for i in range(2, 5):
    print(i, end=" ")
```

1. 2 3 4
2. 2 3 4 5
3. 3 4 5
4. 1 2 3 4 5

### **[중급] 3번**

다음 코드의 total 값은?

```python
total = 0
for i in range(1, 6):
    total = total + i
```

1. 5
2. 10
3. 15
4. 21

### **[고급] 4번**

다음 코드의 출력 줄 수는?

```python
for i in range(1, 4):
    for j in range(1, 3):
        print("*")
```

1. 3줄
2. 4줄
3. 6줄
4. 9줄

### **[고급] 5번**

다음 중 역순으로 출력하는 코드는?

```python
1) for i in range(5, 0):
2) for i in range(5, 0, -1):
3) for i in range(0, 5, -1):
4) for i in range(5, -1, 1):
```

1. 1번
2. 2번
3. 3번
4. 4번

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
`range(5)`는 0, 1, 2, 3, 4를 생성하므로 총 5번 반복됩니다.

**2번 정답: 1**
`range(2, 5)`는 2부터 4까지(5는 포함 안 됨)이므로 "2 3 4"가 출력됩니다.

**3번 정답: 3**
1+2+3+4+5 = 15입니다. range(1, 6)은 1부터 5까지를 의미합니다.

**4번 정답: 3**
바깥 반복문이 3번(i=1,2,3), 안쪽 반복문이 각각 2번(j=1,2) 실행되므로 총 3×2 = 6줄이 출력됩니다.

**5번 정답: 2**
`range(5, 0, -1)`은 5부터 1까지 역순으로 출력합니다. 1번은 범위가 비어있고, 3번도 범위가 비어있으며, 4번도 출력이 없습니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 while 문과 break, continue에 대해 배웁니다. 조건이 참인 동안 반복하는 while 문과, 반복문의 흐름을 제어하는 방법을 학습하게 됩니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
