# 22장 CSV 파일과 데이터 분석

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 CSV 파일을 읽고 쓰며, 데이터를 분석하고 처리할 수 있습니다. 엑셀 같은 표 형태의 데이터를 파이썬으로 다루는 방법을 익혀 실무에서 활용할 수 있게 됩니다.

---

## 1️⃣ **CSV 파일이란?**

CSV는 **Comma-Separated Values**의 약자로, 쉼표로 구분된 값들을 저장하는 파일 형식입니다.

### **왜 CSV를 배워야 할까?**

우리가 흔히 사용하는 엑셀도 CSV 파일로 저장할 수 있습니다. CSV는 데이터를 주고받을 때 가장 많이 사용되는 형식 중 하나입니다!

```
CSV 파일의 모습

이름,나이,직업
김철수,25,개발자
박영희,30,디자이너
이민수,28,기획자

↓ 엑셀에서 열면

┌────────┬─────┬──────────┐
│  이름  │ 나이│   직업   │
├────────┼─────┼──────────┤
│ 김철수 │  25 │  개발자  │
│ 박영희 │  30 │ 디자이너 │
│ 이민수 │  28 │  기획자  │
└────────┴─────┴──────────┘
```

### **CSV의 특징**

**장점:**

- ✅ 간단한 텍스트 형식 (메모장으로 열 수 있음)
- ✅ 엑셀, 구글 시트에서 바로 열림
- ✅ 용량이 작음
- ✅ 모든 프로그래밍 언어에서 지원

**단점:**

- ❌ 글자 색, 셀 병합 등 서식 저장 안 됨
- ❌ 하나의 시트만 저장 가능

### **실생활 사용 예시**

```
🏢 회사에서
- 직원 명단
- 매출 데이터
- 고객 목록

📊 데이터 분석
- 설문조사 결과
- 실험 데이터
- 통계 자료

🛒 전자상거래
- 상품 목록
- 주문 내역
- 재고 현황
```

---

## 2️⃣ **CSV 파일 읽기 - 기본**

CSV 파일을 읽는 가장 간단한 방법입니다.

### **csv 모듈 import**

```python
import csv
```

파이썬에 기본으로 포함되어 있어 별도 설치가 필요 없습니다!

### **실습용 CSV 파일 만들기**

먼저 실습에 사용할 CSV 파일을 만들어봅시다. 메모장이나 텍스트 에디터를 열어서 다음 내용을 입력하고 `students.csv`로 저장하세요.

**students.csv 파일 내용:**

```
이름,나이,학년
김철수,20,2
박영희,21,3
이민수,19,1
```

💡 **CSV 파일 만드는 법:**

1. 메모장(Windows) 또는 텍스트편집기(Mac) 열기
2. 위 내용 입력 (쉼표로 구분)
3. "다른 이름으로 저장" → 파일명: `students.csv` → 인코딩: UTF-8
4. 파이썬 파일과 같은 폴더에 저장

또는 엑셀에서:

1. 위 내용을 엑셀에 입력
2. "다른 이름으로 저장" → 파일 형식: CSV (쉼표로 분리)

### **CSV 파일 읽기 - 리스트로**

```python
import csv

# CSV 파일 열기
with open('students.csv', 'r', encoding='utf-8') as file:
    # CSV 리더 생성
    csv_reader = csv.reader(file)
  
    # 한 줄씩 읽기
    for row in csv_reader:
        print(row)
```

**실행 결과:**

```
['이름', '나이', '학년']
['김철수', '20', '2']
['박영희', '21', '3']
['이민수', '19', '1']
```

각 줄이 리스트로 반환됩니다!

### **첫 줄(헤더) 건너뛰기**

첫 줄은 보통 컬럼 이름이므로 건너뛰고 싶을 때:

```python
import csv

with open('students.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
  
    # 첫 줄 건너뛰기
    next(csv_reader)
  
    # 데이터만 읽기
    for row in csv_reader:
        print(f"이름: {row[0]}, 나이: {row[1]}, 학년: {row[2]}")
```

**실행 결과:**

```
이름: 김철수, 나이: 20, 학년: 2
이름: 박영희, 나이: 21, 학년: 3
이름: 이민수, 나이: 19, 학년: 1
```

---

## 3️⃣ **CSV 파일 읽기 - 딕셔너리로**

컬럼 이름으로 접근하고 싶다면 `DictReader`를 사용합니다!

### **DictReader 사용법**

```python
import csv

with open('students.csv', 'r', encoding='utf-8') as file:
    # DictReader 생성 (첫 줄을 자동으로 헤더로 인식)
    csv_reader = csv.DictReader(file)
  
    for row in csv_reader:
        # 딕셔너리처럼 컬럼 이름으로 접근!
        print(f"이름: {row['이름']}, 나이: {row['나이']}, 학년: {row['학년']}")
```

**실행 결과:**

```
이름: 김철수, 나이: 20, 학년: 2
이름: 박영희, 나이: 21, 학년: 3
이름: 이민수, 나이: 19, 학년: 1
```

💡 **DictReader의 장점**: 인덱스(`row[0]`) 대신 컬럼 이름(`row['이름']`)으로 접근할 수 있어 코드가 읽기 쉽습니다!

### **데이터 리스트로 저장하기**

```python
import csv

students = []  # 빈 리스트 생성

with open('students.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
  
    for row in csv_reader:
        # 딕셔너리를 리스트에 추가
        student = {
            '이름': row['이름'],
            '나이': int(row['나이']),  # 숫자로 변환
            '학년': int(row['학년'])
        }
        students.append(student)

# 저장된 데이터 확인
print(f"총 {len(students)}명의 학생")
for student in students:
    print(student)
```

---

## 4️⃣ **CSV 파일 쓰기**

새로운 CSV 파일을 만들거나 데이터를 저장할 수 있습니다.

### **기본 쓰기**

```python
import csv

# 저장할 데이터
students = [
    ['이름', '나이', '학년'],  # 헤더
    ['홍길동', 22, 2],
    ['김영희', 20, 1],
    ['이철수', 23, 3]
]

# CSV 파일에 쓰기
with open('new_students.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
  
    # 모든 행 쓰기
    csv_writer.writerows(students)

print("파일 저장 완료!")
```

💡 **주의**: `newline=''`을 꼭 써야 합니다! 안 쓰면 빈 줄이 생깁니다.

### **DictWriter로 쓰기**

```python
import csv

# 저장할 데이터 (딕셔너리 리스트)
students = [
    {'이름': '홍길동', '나이': 22, '학년': 2},
    {'이름': '김영희', '나이': 20, '학년': 1},
    {'이름': '이철수', '나이': 23, '학년': 3}
]

# CSV 파일에 쓰기
with open('students_dict.csv', 'w', newline='', encoding='utf-8') as file:
    # 컬럼 이름 지정
    fieldnames = ['이름', '나이', '학년']
  
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
  
    # 헤더 쓰기
    csv_writer.writeheader()
  
    # 데이터 쓰기
    csv_writer.writerows(students)

print("파일 저장 완료!")
```

---

## 5️⃣ **데이터 분석 기초**

CSV 파일의 데이터를 읽어서 간단한 분석을 해봅시다.

### **예제 데이터 준비**

먼저 성적 데이터가 담긴 CSV 파일을 만들어봅시다.

**scores.csv 파일 만들기:**

메모장이나 텍스트 에디터를 열어서 다음 내용을 입력하고 `scores.csv`로 저장하세요.

**scores.csv 파일 내용:**

```
이름,국어,영어,수학
김철수,85,90,78
박영희,92,88,95
이민수,78,85,82
최지은,88,92,90
정민호,95,78,88
```

💡 **파일 구조 설명:**

- **1행(헤더)**: 컬럼 이름 (이름, 국어, 영어, 수학)
- **2-6행(데이터)**: 각 학생의 과목별 점수
- 쉼표(`,`)로 구분
- 인코딩: UTF-8로 저장

**엑셀에서 만드는 방법:**

```
┌────────┬──────┬──────┬──────┐
│  이름  │ 국어 │ 영어 │ 수학 │
├────────┼──────┼──────┼──────┤
│ 김철수 │  85  │  90  │  78  │
│ 박영희 │  92  │  88  │  95  │
│ 이민수 │  78  │  85  │  82  │
│ 최지은 │  88  │  92  │  90  │
│ 정민호 │  95  │  78  │  88  │
└────────┴──────┴──────┴──────┘

↓ "다른 이름으로 저장"
↓ 파일 형식: CSV (쉼표로 분리)
```

### **평균 계산**

```python
import csv

# 데이터 읽기
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

# 각 학생의 평균 계산
print("=" * 50)
print("학생별 평균")
print("=" * 50)

for student in students:
    average = (student['국어'] + student['영어'] + student['수학']) / 3
    print(f"{student['이름']:8} : {average:.1f}점")

# 과목별 평균 계산
print("\n" + "=" * 50)
print("과목별 평균")
print("=" * 50)

korean_total = sum(s['국어'] for s in students)
english_total = sum(s['영어'] for s in students)
math_total = sum(s['수학'] for s in students)

count = len(students)

print(f"국어 평균: {korean_total / count:.1f}점")
print(f"영어 평균: {english_total / count:.1f}점")
print(f"수학 평균: {math_total / count:.1f}점")
```

**실행 결과:**

```
==================================================
학생별 평균
==================================================
김철수      : 84.3점
박영희      : 91.7점
이민수      : 81.7점
최지은      : 90.0점
정민호      : 87.0점

==================================================
과목별 평균
==================================================
국어 평균: 87.6점
영어 평균: 86.6점
수학 평균: 86.6점
```

### **최고점, 최저점 찾기**

```python
import csv

# 데이터 읽기
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

# 각 학생의 총점 계산
for student in students:
    student['총점'] = student['국어'] + student['영어'] + student['수학']

# 총점 순으로 정렬
students.sort(key=lambda x: x['총점'], reverse=True)

# 결과 출력
print("=" * 60)
print("성적표 (총점 순)")
print("=" * 60)
print(f"{'순위':^4} {'이름':^8} {'국어':^6} {'영어':^6} {'수학':^6} {'총점':^6}")
print("-" * 60)

for rank, student in enumerate(students, 1):
    print(f"{rank:^4} {student['이름']:^8} {student['국어']:^6} {student['영어']:^6} {student['수학']:^6} {student['총점']:^6}")

print("=" * 60)
print(f"\n🥇 1등: {students[0]['이름']} ({students[0]['총점']}점)")
print(f"🥈 2등: {students[1]['이름']} ({students[1]['총점']}점)")
print(f"🥉 3등: {students[2]['이름']} ({students[2]['총점']}점)")
```

---

## 6️⃣ **실전 예제: 매출 분석 프로그램**

간단한 매출 데이터를 분석하는 프로그램입니다.

### **데이터 준비**

먼저 매출 데이터 파일을 만들어봅시다.

**sales.csv 파일 만들기:**

**sales.csv 파일 내용:**

```
날짜,상품,수량,가격
2024-01-01,노트북,2,1500000
2024-01-01,마우스,5,30000
2024-01-02,키보드,3,120000
2024-01-02,모니터,1,350000
2024-01-03,노트북,1,1500000
2024-01-03,마우스,3,30000
```

💡 **파일 구조 설명:**

- **날짜**: 판매 날짜 (YYYY-MM-DD 형식)
- **상품**: 상품 이름
- **수량**: 판매 수량
- **가격**: 개당 가격 (원)
- **매출 = 수량 × 가격** (프로그램에서 계산)

### **매출 분석 코드**

```python
import csv
from collections import defaultdict

# 데이터 읽기
sales = []
with open('sales.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        sales.append({
            '날짜': row['날짜'],
            '상품': row['상품'],
            '수량': int(row['수량']),
            '가격': int(row['가격'])
        })

# 각 판매의 매출 계산
for sale in sales:
    sale['매출'] = sale['수량'] * sale['가격']

# 1. 전체 매출
total_revenue = sum(sale['매출'] for sale in sales)

print("=" * 60)
print("📊 매출 분석 리포트")
print("=" * 60)
print(f"\n💰 전체 매출: {total_revenue:,}원")

# 2. 날짜별 매출
daily_revenue = defaultdict(int)
for sale in sales:
    daily_revenue[sale['날짜']] += sale['매출']

print("\n📅 날짜별 매출:")
print("-" * 60)
for date, revenue in sorted(daily_revenue.items()):
    print(f"{date}: {revenue:,}원")

# 3. 상품별 매출
product_revenue = defaultdict(int)
product_quantity = defaultdict(int)

for sale in sales:
    product_revenue[sale['상품']] += sale['매출']
    product_quantity[sale['상품']] += sale['수량']

print("\n📦 상품별 매출:")
print("-" * 60)
for product in product_revenue:
    revenue = product_revenue[product]
    quantity = product_quantity[product]
    print(f"{product:10} : {revenue:,}원 (판매량: {quantity}개)")

# 4. 베스트 상품
best_product = max(product_revenue, key=product_revenue.get)
print("\n⭐ 베스트 상품:")
print(f"   {best_product} - {product_revenue[best_product]:,}원")

# 5. 결과를 새 CSV 파일로 저장
print("\n💾 분석 결과를 report.csv로 저장 중...")

with open('report.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['구분', '항목', '매출']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
  
    csv_writer.writeheader()
  
    # 날짜별 매출 저장
    for date, revenue in sorted(daily_revenue.items()):
        csv_writer.writerow({
            '구분': '날짜별',
            '항목': date,
            '매출': revenue
        })
  
    # 상품별 매출 저장
    for product, revenue in product_revenue.items():
        csv_writer.writerow({
            '구분': '상품별',
            '항목': product,
            '매출': revenue
        })

print("✓ 저장 완료!")
print("=" * 60)
```

---

## 7️⃣  **데이터 필터링과 정렬**

CSV 데이터를 조건에 맞게 필터링하고 정렬하는 방법입니다.

### **필터링 예제**

```python
import csv

# 데이터 읽기
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

# 총점 계산
for student in students:
    student['총점'] = student['국어'] + student['영어'] + student['수학']
    student['평균'] = student['총점'] / 3

# 1. 평균 90점 이상 학생 찾기
print("🏆 평균 90점 이상 우수 학생:")
excellent = [s for s in students if s['평균'] >= 90]
for student in excellent:
    print(f"   {student['이름']}: {student['평균']:.1f}점")

# 2. 수학 80점 이상 학생 찾기
print("\n📐 수학 80점 이상 학생:")
good_math = [s for s in students if s['수학'] >= 80]
for student in good_math:
    print(f"   {student['이름']}: {student['수학']}점")

# 3. 필터링된 데이터를 새 CSV로 저장
with open('excellent_students.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['이름', '국어', '영어', '수학', '총점', '평균']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
  
    csv_writer.writeheader()
    csv_writer.writerows(excellent)

print("\n✓ 우수 학생 명단이 excellent_students.csv로 저장되었습니다.")
```

---

## 8️⃣ **CSV 파일 다루기 팁**

### **팁 1: 파일 존재 확인**

```python
import csv
import os

filename = 'data.csv'

if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # 파일 읽기
else:
    print(f"❌ {filename} 파일이 없습니다!")
```

### **팁 2: 빈 줄 건너뛰기**

```python
import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if not row:  # 빈 줄이면
            continue  # 건너뛰기
        print(row)
```

### **팁 3: 데이터 추가 모드**

```python
import csv

# 기존 파일에 데이터 추가
with open('students.csv', 'a', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['홍길동', 24, 4])  # 새 데이터 추가

print("✓ 데이터 추가 완료!")
```

### **팁 4: 다른 구분자 사용**

CSV가 아닌 TSV(탭으로 구분) 등을 읽을 때:

```python
import csv

# 탭으로 구분된 파일
with open('data.tsv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for row in csv_reader:
        print(row)
```

---

## 📝 **핵심 개념 정리**

### **CSV 읽기**

```python
import csv

# 리스트로 읽기
with open('file.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# 딕셔너리로 읽기
with open('file.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['컬럼명'])
```

### **CSV 쓰기**

```python
# 리스트로 쓰기
with open('file.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# 딕셔너리로 쓰기
with open('file.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.DictWriter(file, fieldnames=['컬럼1', '컬럼2'])
    csv_writer.writeheader()
    csv_writer.writerows(data)
```

### **주의사항**

- `encoding='utf-8'` 필수 (한글 깨짐 방지)
- `newline=''` 필수 (빈 줄 방지)
- 숫자는 문자로 읽힘 → `int()`, `float()` 변환 필요

---

## 💡 **실습 과제**

### **과제 1: 성적 관리 프로그램**

**목표**: CSV 파일을 읽어 성적을 분석하고 등급을 부여한 후 새 파일로 저장

**1단계: 데이터 파일 준비**

`students.csv` 파일을 만드세요:

```
이름,국어,영어,수학
홍길동,85,90,75
김영희,92,88,95
이철수,78,82,80
박지민,95,87,92
최민수,88,78,85
```

**2단계: 요구사항**

다음 기능을 구현하세요:

1. **평균 계산**: 각 학생의 3과목 평균 계산
2. **등급 부여**:
   - 90점 이상: A
   - 80점 이상: B
   - 70점 이상: C
   - 60점 이상: D
   - 60점 미만: F
3. **석차 계산**: 평균 점수 순으로 등수 매기기
4. **결과 저장**: `result.csv`로 저장 (이름, 국어, 영어, 수학, 평균, 등급, 석차 포함)

**3단계: 출력 예시**

```
====================================
성적표
====================================
이름      국어  영어  수학  평균   등급
------------------------------------
홍길동     85    90    75   83.3   B
김영희     92    88    95   91.7   A
...
====================================

✓ 결과가 result.csv에 저장되었습니다.
```

**힌트:**

```python
# 1. 데이터 읽고 평균 계산
for student in students:
    student['평균'] = (student['국어'] + student['영어'] + student['수학']) / 3

# 2. 등급 부여
def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    # ...

# 3. 정렬 후 석차
students.sort(key=lambda x: x['평균'], reverse=True)
for rank, student in enumerate(students, 1):
    student['석차'] = rank
```

---

### **과제 2: 상품 재고 관리**

**목표**: 상품 재고를 분석하고 경고 메시지 출력

**1단계: 데이터 파일 준비**

`products.csv` 파일을 만드세요:

```
상품명,재고,가격
노트북,5,1500000
마우스,3,30000
키보드,15,120000
모니터,2,350000
웹캠,8,80000
```

**2단계: 요구사항**

다음 정보를 출력하세요:

1. **전체 상품 목록**: 상품명, 재고, 가격 표시
2. **재고 부족 경고**: 재고가 5개 이하인 상품 표시
3. **총 재고 가치**: 모든 상품의 (재고 × 가격) 합계
4. **가장 비싼 상품**: 가격이 가장 높은 상품
5. **재고 많은 순으로 정렬**: 재고 순으로 정렬하여 `inventory_sorted.csv`로 저장

**3단계: 출력 예시**

```
====================================
📦 재고 현황
====================================
상품명        재고    가격
------------------------------------
노트북         5개    1,500,000원
마우스         3개       30,000원
...

⚠️  재고 부족 경고!
------------------------------------
마우스: 3개 (긴급 주문 필요)
모니터: 2개 (긴급 주문 필요)

💰 총 재고 가치: 10,290,000원

⭐ 가장 비싼 상품: 노트북 (1,500,000원)

✓ 정렬된 재고 목록이 inventory_sorted.csv에 저장되었습니다.
```

**힌트:**

```python
# 1. 재고 부족 상품 찾기
low_stock = [p for p in products if p['재고'] <= 5]

# 2. 총 재고 가치
total_value = sum(p['재고'] * p['가격'] for p in products)

# 3. 가장 비싼 상품
most_expensive = max(products, key=lambda x: x['가격'])

# 4. 재고 순 정렬
products.sort(key=lambda x: x['재고'], reverse=True)
```

---

## ✅ **퀴즈**

### **[초급] 1번**

CSV 파일을 읽을 때 사용하는 모듈은?

### **[중급] 2번**

딕셔너리로 CSV를 읽을 때 사용하는 클래스는?

### **[중급] 3번**

CSV 파일을 쓸 때 필수 옵션은?

### **[고급] 4번**

CSV 파일의 첫 줄을 건너뛰는 함수는?

### **[고급] 5번**

기존 CSV 파일에 데이터를 추가하는 모드는?

---

## 🔑 **퀴즈 정답**

**1번**: csv   
**2번**: DictReader   
**3번**: newline='', encoding='utf-8'   
**4번**: next()   
**5번**: 'a' (append 모드)   

---

## 🎯 **다음 장 예고**

다음 장에서는 Matplotlib을 사용한 데이터 시각화를 배웁니다. CSV 데이터를 읽어 그래프로 만들어 보기 쉽게 표현하는 방법을 학습합니다!

---

수고했습니다.  
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
