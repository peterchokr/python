# 23장 Matplotlib 시각화

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 Matplotlib을 사용하여 데이터를 그래프로 시각화할 수 있습니다. 꺾은선 그래프, 막대 그래프, 원 그래프 등을 그려 데이터를 한눈에 이해하기 쉽게 표현할 수 있게 됩니다.

---

## 1️⃣ **데이터 시각화란?**

숫자로만 된 데이터는 이해하기 어렵습니다. 하지만 그래프로 그리면 한눈에 파악할 수 있습니다!

### **왜 시각화가 필요할까?**

```
숫자로만 본 데이터              그래프로 본 데이터
━━━━━━━━━━━━━━━━━━━━         ━━━━━━━━━━━━━━━━━━━━
1월: 100명                         ↑
2월: 120명                     150 │     ●
3월: 90명                          │   ●   ●
4월: 150명                     100 │ ●       ●
5월: 130명                         │
                                50 │
                                   └─────────────→
                                   1  2  3  4  5

? 뭔가 복잡...                    ✓ 한눈에 보임!
```

**시각화의 장점:**

- ✅ 패턴과 추세를 쉽게 발견
- ✅ 데이터 비교가 간편
- ✅ 이상값(특이값)을 빠르게 찾음
- ✅ 보고서와 발표에 효과적

### **Matplotlib이란?**

파이썬에서 가장 많이 사용되는 **그래프 그리기 라이브러리**입니다.

---

## 2️⃣ **Matplotlib 설치 및 기본 사용**

### **설치하기**

터미널이나 명령 프롬프트에서:

```bash
pip install matplotlib
```

### **첫 번째 그래프 그리기**

```python
import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y)

# 그래프 표시
plt.show()
```

**실행하면**: 꺾은선 그래프가 나타납니다!

### **그래프에 제목과 라벨 추가**

```python
import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y)

# 제목과 라벨 추가
plt.title('간단한 선 그래프')          # 제목
plt.xlabel('X축')                     # X축 이름
plt.ylabel('Y축')                     # Y축 이름

# 그래프 표시
plt.show()
```

### **한글 깨짐 해결**

한글이 깨진다면 폰트를 설정해야 합니다:

```python
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 이제 한글 사용 가능
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('한글 제목')
plt.xlabel('가로축')
plt.ylabel('세로축')
plt.show()
```

💡 **앞으로 모든 예제는 한글 폰트 설정이 되어있다고 가정합니다.**

---

## 3️⃣ **꺾은선 그래프 (Line Plot)**

시간에 따른 변화를 보여줄 때 가장 좋습니다.

### **기본 꺾은선 그래프**

```python
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 (월별 판매량)
months = [1, 2, 3, 4, 5, 6]
sales = [100, 120, 90, 150, 130, 170]

# 그래프 그리기
plt.plot(months, sales)

# 제목과 라벨
plt.title('월별 판매량', fontsize=16)
plt.xlabel('월', fontsize=12)
plt.ylabel('판매량 (개)', fontsize=12)

# 격자 추가
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
```

### **선 스타일 꾸미기**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

months = [1, 2, 3, 4, 5, 6]
sales = [100, 120, 90, 150, 130, 170]

# 선 스타일 지정
plt.plot(months, sales, 
         color='blue',           # 색상
         linewidth=2,            # 선 굵기
         linestyle='-',          # 선 스타일 ('-', '--', '-.', ':')
         marker='o',             # 점 모양 ('o', 's', '^', '*' 등)
         markersize=8,           # 점 크기
         label='2024년 판매량')   # 범례 이름

plt.title('월별 판매량', fontsize=16)
plt.xlabel('월', fontsize=12)
plt.ylabel('판매량 (개)', fontsize=12)
plt.legend()  # 범례 표시
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
```

### **여러 선 그리기**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

months = [1, 2, 3, 4, 5, 6]
sales_2023 = [80, 95, 85, 120, 100, 140]
sales_2024 = [100, 120, 90, 150, 130, 170]

# 두 개의 선 그리기
plt.plot(months, sales_2023, marker='o', label='2023년', linewidth=2)
plt.plot(months, sales_2024, marker='s', label='2024년', linewidth=2)

plt.title('연도별 판매량 비교', fontsize=16)
plt.xlabel('월', fontsize=12)
plt.ylabel('판매량 (개)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
```

---

## 4️⃣ **막대 그래프 (Bar Chart)**

항목 간의 크기를 비교할 때 사용합니다.

### **기본 막대 그래프**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 (과일별 판매량)
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
sales = [150, 120, 180, 90, 200]

# 막대 그래프
plt.bar(fruits, sales, color='skyblue', width=0.6)

plt.title('과일별 판매량', fontsize=16)
plt.xlabel('과일', fontsize=12)
plt.ylabel('판매량 (개)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
```

### **막대 색상 다르게**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
sales = [150, 120, 180, 90, 200]
colors = ['red', 'yellow', 'orange', 'purple', 'pink']

# 막대 색상 지정
plt.bar(fruits, sales, color=colors, width=0.6)

plt.title('과일별 판매량', fontsize=16)
plt.xlabel('과일', fontsize=12)
plt.ylabel('판매량 (개)', fontsize=12)

# 각 막대 위에 숫자 표시
for i, v in enumerate(sales):
    plt.text(i, v + 5, str(v), ha='center', fontsize=10)

plt.show()
```

### **가로 막대 그래프**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
sales = [150, 120, 180, 90, 200]

# 가로 막대 그래프
plt.barh(fruits, sales, color='lightgreen')

plt.title('과일별 판매량', fontsize=16)
plt.xlabel('판매량 (개)', fontsize=12)
plt.ylabel('과일', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.show()
```

### **그룹 막대 그래프**

```python
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
categories = ['1분기', '2분기', '3분기', '4분기']
product_a = [100, 120, 90, 150]
product_b = [90, 110, 100, 130]

# x축 위치
x = np.arange(len(categories))
width = 0.35  # 막대 너비

# 그룹 막대 그래프
plt.bar(x - width/2, product_a, width, label='제품 A', color='skyblue')
plt.bar(x + width/2, product_b, width, label='제품 B', color='lightcoral')

plt.title('분기별 제품 판매량', fontsize=16)
plt.xlabel('분기', fontsize=12)
plt.ylabel('판매량', fontsize=12)
plt.xticks(x, categories)  # x축 라벨 설정
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
```

---

## 5️⃣ **원 그래프 (Pie Chart)**

전체에서 각 항목이 차지하는 비율을 보여줄 때 사용합니다.

### **기본 원 그래프**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 (취미 선호도)
hobbies = ['운동', '독서', '영화', '게임', '음악']
counts = [30, 25, 20, 15, 10]

# 원 그래프
plt.pie(counts, labels=hobbies, autopct='%1.1f%%', startangle=90)

plt.title('취미 선호도', fontsize=16)
plt.axis('equal')  # 원을 정확한 원으로

plt.show()
```

### **원 그래프 꾸미기**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

hobbies = ['운동', '독서', '영화', '게임', '음악']
counts = [30, 25, 20, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)  # 첫 번째 조각 강조

# 원 그래프 (꾸미기)
plt.pie(counts, 
        labels=hobbies,
        colors=colors,
        autopct='%1.1f%%',     # 퍼센트 표시
        startangle=90,          # 시작 각도
        explode=explode,        # 조각 띄우기
        shadow=True)            # 그림자

plt.title('취미 선호도', fontsize=16)
plt.axis('equal')

plt.show()
```

---

## 6️⃣ **산점도 (Scatter Plot)**

두 변수 간의 관계를 보여줄 때 사용합니다.

### **기본 산점도**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 (키와 몸무게)
height = [160, 165, 170, 175, 180, 185]
weight = [55, 60, 65, 70, 75, 80]

# 산점도
plt.scatter(height, weight, s=100, c='blue', alpha=0.6)

plt.title('키와 몸무게의 관계', fontsize=16)
plt.xlabel('키 (cm)', fontsize=12)
plt.ylabel('몸무게 (kg)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
```

### **그룹별 색상 다르게**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 남성 데이터
male_height = [170, 175, 180, 185, 190]
male_weight = [65, 70, 75, 80, 85]

# 여성 데이터
female_height = [155, 160, 165, 170, 175]
female_weight = [50, 55, 60, 65, 70]

# 산점도 (그룹별)
plt.scatter(male_height, male_weight, s=100, c='blue', label='남성', alpha=0.6)
plt.scatter(female_height, female_weight, s=100, c='red', label='여성', alpha=0.6)

plt.title('성별 키와 몸무게의 관계', fontsize=16)
plt.xlabel('키 (cm)', fontsize=12)
plt.ylabel('몸무게 (kg)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
```

---

## 7️⃣ **히스토그램 (Histogram)**

데이터의 분포를 보여줄 때 사용합니다.

### **기본 히스토그램**

```python
import matplotlib.pyplot as plt
import random

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 (시험 점수)
scores = [random.randint(0, 100) for _ in range(100)]

# 히스토그램
plt.hist(scores, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

plt.title('시험 점수 분포', fontsize=16)
plt.xlabel('점수', fontsize=12)
plt.ylabel('학생 수', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
```

---

## 8️⃣ **여러 그래프 한 번에 그리기 (Subplot)**

한 화면에 여러 그래프를 배치할 수 있습니다.

### **2x2 배치**

```python
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Figure 생성 (2행 2열)
plt.figure(figsize=(10, 8))

# 1번 그래프 (꺾은선)
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o')
plt.title('꺾은선 그래프')
plt.grid(True)

# 2번 그래프 (막대)
plt.subplot(2, 2, 2)
plt.bar(x, y, color='skyblue')
plt.title('막대 그래프')
plt.grid(axis='y')

# 3번 그래프 (산점도)
plt.subplot(2, 2, 3)
plt.scatter(x, y, s=100, c='red')
plt.title('산점도')
plt.grid(True)

# 4번 그래프 (원 그래프)
plt.subplot(2, 2, 4)
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title('원 그래프')

# 그래프 간격 조정
plt.tight_layout()
plt.show()
```

---

## 9️⃣ **실전 예제: CSV 데이터 시각화**

CSV 파일의 데이터를 읽어서 그래프로 그려봅시다.

### **데이터 파일 준비**

먼저 시각화할 CSV 파일을 만들어봅시다.

**scores.csv 파일 만들기:**

메모장을 열어 다음 내용을 입력하고 `scores.csv`로 저장하세요 (인코딩: UTF-8):

```
이름,국어,영어,수학
김철수,85,90,78
박영희,92,88,95
이민수,78,85,82
최지은,88,92,90
정민호,95,78,88
```

💡 **파일 구조:**

- 1행: 컬럼 이름 (헤더)
- 2-6행: 각 학생의 점수
- 쉼표로 구분

### **학생 성적 시각화**

```python
import matplotlib.pyplot as plt
import csv

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 파일 읽기
students = []
with open('scores.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        students.append({
            '이름': row['이름'],
            '국어': int(row['국어']),
            '영어': int(row['영어']),
            '수학': int(row['수학'])
        })

# 데이터 추출
names = [s['이름'] for s in students]
korean = [s['국어'] for s in students]
english = [s['영어'] for s in students]
math = [s['수학'] for s in students]

# 평균 계산
averages = [(s['국어'] + s['영어'] + s['수학']) / 3 for s in students]

# Figure 생성
plt.figure(figsize=(12, 10))

# 1. 과목별 비교 (그룹 막대)
plt.subplot(2, 2, 1)
x = range(len(names))
width = 0.25

plt.bar([i - width for i in x], korean, width, label='국어', color='skyblue')
plt.bar([i for i in x], english, width, label='영어', color='lightgreen')
plt.bar([i + width for i in x], math, width, label='수학', color='lightcoral')

plt.title('과목별 점수 비교', fontsize=14)
plt.xlabel('학생', fontsize=11)
plt.ylabel('점수', fontsize=11)
plt.xticks(x, names, rotation=45)
plt.legend()
plt.grid(axis='y', alpha=0.3)

# 2. 평균 점수 (꺾은선)
plt.subplot(2, 2, 2)
plt.plot(names, averages, marker='o', linewidth=2, markersize=8, color='purple')
plt.title('학생별 평균 점수', fontsize=14)
plt.xlabel('학생', fontsize=11)
plt.ylabel('평균 점수', fontsize=11)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# 3. 과목별 평균 (막대)
plt.subplot(2, 2, 3)
subject_avg = [sum(korean)/len(korean), sum(english)/len(english), sum(math)/len(math)]
subjects = ['국어', '영어', '수학']
colors = ['skyblue', 'lightgreen', 'lightcoral']

plt.bar(subjects, subject_avg, color=colors)
plt.title('과목별 평균', fontsize=14)
plt.ylabel('평균 점수', fontsize=11)

for i, v in enumerate(subject_avg):
    plt.text(i, v + 1, f'{v:.1f}', ha='center', fontsize=10)

plt.grid(axis='y', alpha=0.3)

# 4. 점수 분포 (히스토그램)
plt.subplot(2, 2, 4)
all_scores = korean + english + math
plt.hist(all_scores, bins=10, color='lightblue', edgecolor='black', alpha=0.7)
plt.title('전체 점수 분포', fontsize=14)
plt.xlabel('점수 구간', fontsize=11)
plt.ylabel('빈도', fontsize=11)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 🔟 **그래프 저장하기**

그린 그래프를 이미지 파일로 저장할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 그래프 그리기
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title('샘플 그래프')
plt.xlabel('X축')
plt.ylabel('Y축')
plt.grid(True)

# 파일로 저장
plt.savefig('graph.png', dpi=300, bbox_inches='tight')
print("✓ graph.png로 저장되었습니다!")

# 화면에 표시
plt.show()
```

**주요 옵션:**

- `dpi`: 해상도 (기본 100, 고해상도는 300)
- `bbox_inches='tight'`: 여백 최소화
- 지원 형식: png, jpg, pdf, svg 등

---

## 📝 **핵심 개념 정리**

### **기본 구조**

```python
import matplotlib.pyplot as plt

plt.plot(x, y)           # 그래프 그리기
plt.title('제목')
plt.xlabel('X축')
plt.ylabel('Y축')
plt.grid(True)
plt.legend()
plt.show()               # 화면에 표시
```

### **주요 그래프**

- `plt.plot()`: 꺾은선 그래프
- `plt.bar()`: 막대 그래프
- `plt.barh()`: 가로 막대 그래프
- `plt.pie()`: 원 그래프
- `plt.scatter()`: 산점도
- `plt.hist()`: 히스토그램

### **한글 설정**

```python
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
```

### **subplot**

```python
plt.subplot(행, 열, 번호)
```

---

## 💡 **실습 과제**

### **과제 1: 월별 날씨 데이터 시각화**

**목표**: 1년간의 날씨 데이터를 읽어 그래프로 시각화

**1단계: 데이터 파일 준비**

`weather.csv` 파일을 만드세요:

```
월,평균기온,강수량
1,2.5,20
2,4.8,25
3,10.2,45
4,15.8,60
5,20.5,80
6,24.3,120
7,27.8,250
8,28.5,230
9,23.7,140
10,17.2,50
11,10.8,40
12,4.5,25
```

💡 **컬럼 설명:**

- **월**: 1~12월
- **평균기온**: 해당 월 평균 온도 (°C)
- **강수량**: 해당 월 총 강수량 (mm)

**2단계: 요구사항**

다음 2개의 그래프를 subplot으로 배치하세요:

1. **평균 기온 그래프** (꺾은선)

   - X축: 월 (1~12)
   - Y축: 평균기온 (°C)
   - 선 색상: 빨강
   - 마커: 원형
   - 격자 표시
2. **강수량 그래프** (막대)

   - X축: 월 (1~12)
   - Y축: 강수량 (mm)
   - 막대 색상: 파랑
   - 격자 표시

**3단계: 추가 기능**

- 전체 제목: "2024년 월별 날씨 통계"
- 가장 더운 달과 강수량이 가장 많은 달을 출력
- 그래프를 `weather_chart.png`로 저장

**힌트:**

```python
import matplotlib.pyplot as plt
import csv

# 1. CSV 읽기
months = []
temps = []
rain = []

with open('weather.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        months.append(int(row['월']))
        temps.append(float(row['평균기온']))
        rain.append(int(row['강수량']))

# 2. 그래프 그리기
plt.figure(figsize=(12, 5))

# 2-1. 기온 그래프
plt.subplot(1, 2, 1)
plt.plot(months, temps, marker='o', color='red', linewidth=2)
# ...

# 2-2. 강수량 그래프
plt.subplot(1, 2, 2)
plt.bar(months, rain, color='blue')
# ...

# 3. 최댓값 찾기
max_temp_idx = temps.index(max(temps))
max_rain_idx = rain.index(max(rain))
print(f"가장 더운 달: {months[max_temp_idx]}월 ({temps[max_temp_idx]}°C)")
print(f"강수량 최대: {months[max_rain_idx]}월 ({rain[max_rain_idx]}mm)")

# 4. 저장
plt.tight_layout()
plt.savefig('weather_chart.png', dpi=300)
plt.show()
```

**예상 출력:**

```
가장 더운 달: 8월 (28.5°C)
강수량 최대: 7월 (250mm)
✓ 그래프가 weather_chart.png로 저장되었습니다.
```

---

### **과제 2: 설문조사 결과 시각화**

**목표**: 설문조사 결과를 다양한 그래프로 표현

**1단계: 데이터 파일 준비**

`survey.csv` 파일을 만드세요:

```
이름,나이,성별,만족도
김철수,25,남,5
박영희,30,여,4
이민수,28,남,5
최지은,22,여,3
정민호,35,남,4
강수진,27,여,5
이하늘,24,남,4
박서연,29,여,5
윤동혁,26,남,3
한지민,31,여,4
```

💡 **컬럼 설명:**

- **나이**: 응답자 나이
- **성별**: 남/여
- **만족도**: 1~5점 (5점이 가장 높음)

**2단계: 요구사항**

2x2 레이아웃으로 다음 4개 그래프를 그리세요:

1. **연령대별 응답자 수** (막대 그래프)

   - 20대, 30대로 구분
   - 가로축: 연령대, 세로축: 인원 수
2. **성별 분포** (원 그래프)

   - 남성과 여성의 비율
   - 퍼센트 표시
3. **만족도 분포** (막대 그래프)

   - 가로축: 만족도 (1~5), 세로축: 응답자 수
   - 각 만족도별로 다른 색상
4. **나이와 만족도 관계** (산점도)

   - X축: 나이, Y축: 만족도
   - 남성/여성 다른 색상으로 표시

**3단계: 통계 출력**

```
====================================
📊 설문조사 분석 결과
====================================
총 응답자: 10명
평균 나이: 27.7세
평균 만족도: 4.2/5.0

성별 분포:
  남성: 5명 (50.0%)
  여성: 5명 (50.0%)

연령대별:
  20대: 8명
  30대: 2명
====================================
```

**힌트:**

```python
# 연령대 구분
age_20s = sum(1 for age in ages if 20 <= age < 30)
age_30s = sum(1 for age in ages if 30 <= age < 40)

# 성별 카운트
from collections import Counter
gender_count = Counter(genders)

# 만족도별 카운트
satisfaction_count = Counter(satisfactions)

# 산점도 (성별로 분리)
male_ages = [ages[i] for i in range(len(ages)) if genders[i] == '남']
male_sats = [satisfactions[i] for i in range(len(satisfactions)) if genders[i] == '남']
# 여성도 동일하게...

plt.scatter(male_ages, male_sats, label='남성', color='blue', s=100)
plt.scatter(female_ages, female_sats, label='여성', color='red', s=100)
```

---

## ✅ **퀴즈**

### **[초급] 1번**

그래프를 그리는 파이썬 라이브러리는?

### **[중급] 2번**

막대 그래프를 그리는 함수는?

### **[중급] 3번**

그래프를 화면에 표시하는 함수는?

### **[고급] 4번**

한 화면에 여러 그래프를 배치하는 함수는?

### **[고급] 5번**

그래프를 파일로 저장하는 함수는?

---

## 🔑 **퀴즈 정답**

**1번**: matplotlib   
**2번**: plt.bar()   
**3번**: plt.show()   
**4번**: plt.subplot()   
**5번**: plt.savefig()   

---

## 🎯 **다음 장 예고**

다음 장에서는 웹 스크래핑을 배웁니다. 웹사이트에서 데이터를 자동으로 수집하는 방법을 학습합니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
