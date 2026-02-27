# 22장 CSV 파일과 데이터 분석 — 연습문제

---

## 📝 객관식 문제

---

### 🟢 초급

**문제 1.** CSV는 무엇의 약자인가?

① Comma-Separated Variables  
② Comma-Separated Values  
③ Character-Separated Values  
④ Column-Separated Variables  

---

**문제 2.** CSV 파일을 읽을 때 사용하는 파이썬 기본 모듈은?

① `pandas`  
② `json`  
③ `csv`  
④ `excel`  

---

**문제 3.** CSV 파일을 리스트로 읽는 올바른 코드는?

① `csv.read(file)`  
② `csv.reader(file)`  
③ `csv.load(file)`  
④ `csv.open(file)`  

---

**문제 4.** CSV 파일을 쓸 때 빈 줄이 생기지 않도록 하는 옵션은?

① `encoding='utf-8'`  
② `mode='w'`  
③ `newline=''`  
④ `strip=True`  

---

**문제 5.** CSV 파일에서 첫 줄(헤더)을 건너뛰는 함수는?

① `skip()`  
② `next()`  
③ `pass()`  
④ `header()`  

---

**문제 6.** CSV 파일의 장점이 아닌 것은?

① 간단한 텍스트 형식  
② 모든 프로그래밍 언어에서 지원  
③ 용량이 작음  
④ **글자 색, 셀 병합 등 서식 저장 가능**  

---

**문제 7.** CSV 파일에서 한글이 깨지지 않도록 하는 옵션은?

① `newline=''`  
② `encoding='utf-8'`  
③ `mode='r'`  
④ `delimiter=','`  

---

### 🟡 중급

**문제 8.** 컬럼 이름으로 CSV 데이터에 접근하기 위해 사용하는 클래스는?

① `csv.reader`  
② `csv.DictReader`  
③ `csv.NameReader`  
④ `csv.HeaderReader`  

---

**문제 9.** `csv.DictWriter`에서 헤더를 파일에 쓰는 메서드는?

① `write_header()`  
② `writeheader()`  
③ `add_header()`  
④ `insert_header()`  

---

**문제 10.** 다음 코드의 실행 결과로 올바른 것은?

```python
import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(type(row))
        break
```

(data.csv: `이름,나이,학년`)

① `<class 'dict'>`  
② `<class 'str'>`  
③ `<class 'list'>`  
④ `<class 'tuple'>`  

---

**문제 11.** 기존 CSV 파일에 데이터를 추가(덧붙이기)하는 파일 모드는?

① `'w'`  
② `'r'`  
③ `'a'`  
④ `'x'`  

---

**문제 12.** 탭으로 구분된 TSV 파일을 읽을 때 사용하는 옵션은?

① `separator='\t'`  
② `delimiter='\t'`  
③ `split='\t'`  
④ `divider='\t'`  

---

### 🔴 고급

**문제 13.** 다음 코드의 실행 결과는?

```python
import csv

data = [
    {'이름': '김철수', '점수': 85},
    {'이름': '박영희', '점수': 92}
]

with open('test.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['이름', '점수'])
    writer.writeheader()
    writer.writerows(data)
```

생성된 test.csv 파일의 내용은?

① `김철수,85\n박영희,92`  
② `이름,점수\n김철수,85\n박영희,92`  
③ `{'이름': '김철수', '점수': 85}\n{'이름': '박영희', '점수': 92}`  
④ 오류 발생  

---

**문제 14.** 다음 코드에서 `students` 리스트에 저장된 나이 값의 타입은?

```python
import csv

students = []
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)
```

(data.csv: `이름,나이\n김철수,25`)

① `int`  
② `str`  
③ `float`  
④ `list`  

---

**문제 15.** 다음 코드에서 평균을 올바르게 계산하는 부분은?

```python
scores = [
    {'이름': '김철수', '국어': 85, '영어': 90, '수학': 78},
    {'이름': '박영희', '국어': 92, '영어': 88, '수학': 95}
]
```

① `sum(scores) / len(scores)`  
② `sum(s['국어'] for s in scores) / len(scores)`  
③ `scores.average('국어')`  
④ `csv.average(scores, '국어')`  

---

## 📝 주관식 문제

---

### 🟢 초급

**문제 16.** CSV 파일이란 무엇인지 설명하고, CSV 파일의 장점과 단점을 각각 2가지씩 서술하시오.

---

**문제 17.** `csv.reader`와 `csv.DictReader`의 차이점을 설명하시오. 각각의 데이터 접근 방식을 코드 예시로 보이시오.

---

**문제 18.** 다음 CSV 파일을 읽어 출력하는 코드의 실행 결과를 쓰시오.

```
이름,나이,학년
김철수,20,2
박영희,21,3
```

```python
import csv

with open('students.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['이름']}은(는) {row['나이']}살, {row['학년']}학년")
```

---

### 🟡 중급

**문제 19.** CSV 파일을 쓸 때 `newline=''`을 반드시 지정해야 하는 이유를 설명하시오. 또한 `encoding='utf-8'`이 필요한 이유를 서술하시오.

---

**문제 20.** 다음 코드의 실행 결과를 쓰시오.

```python
import csv

# scores.csv 내용:
# 이름,국어,영어,수학
# 김철수,85,90,78
# 박영희,92,88,95
# 이민수,78,85,82

students = []
with open('scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            '이름': row['이름'],
            '국어': int(row['국어']),
            '영어': int(row['영어']),
            '수학': int(row['수학'])
        })

for s in students:
    s['평균'] = (s['국어'] + s['영어'] + s['수학']) / 3

students.sort(key=lambda x: x['평균'], reverse=True)

for rank, s in enumerate(students, 1):
    print(f"{rank}등 {s['이름']}: {s['평균']:.1f}점")
```

---

### 🔴 고급

**문제 21.** 다음 매출 분석 코드에서 `defaultdict(int)`의 역할을 설명하시오. 일반 딕셔너리를 사용했을 때와의 차이점을 서술하시오.

```python
from collections import defaultdict

daily_revenue = defaultdict(int)
for sale in sales:
    daily_revenue[sale['날짜']] += sale['매출']
```

---

## 💻 실습형 문제

---

### 🟢 초급

**문제 22.** 다음 요구사항에 맞는 코드를 작성하시오.

> **학생 정보 CSV 만들기**
> - 아래 데이터를 `students.csv` 파일로 저장하시오.
> - `csv.writer`와 `csv.DictWriter` 두 가지 방법 모두 작성하시오.

```
이름,나이,학과
홍길동,22,컴퓨터공학
김영희,20,경영학
이철수,23,전자공학
박지민,21,디자인학
```

---

**문제 23.** 다음 요구사항에 맞는 코드를 작성하시오.

> **학생 CSV 읽기 및 검색**
> - `students.csv` 파일을 `DictReader`로 읽기
> - 전체 학생 목록 출력
> - 나이가 21세 이상인 학생만 필터링하여 출력
> - 총 학생 수와 평균 나이 출력

---

### 🟡 중급

**문제 24.** 다음 요구사항에 맞는 성적 분석 프로그램을 작성하시오.

> **성적 분석 프로그램**
>
> scores.csv 파일 내용:
> ```
> 이름,국어,영어,수학
> 김철수,85,90,78
> 박영희,92,88,95
> 이민수,78,85,82
> 최지은,88,92,90
> 정민호,95,78,88
> ```
>
> 기능:
> 1. 각 학생의 총점, 평균, 학점 계산 (90↑A, 80↑B, 70↑C, 60↑D, F)
> 2. 성적표 출력 (순위, 이름, 국어, 영어, 수학, 평균, 학점)
> 3. 과목별 평균, 최고점, 최저점 출력
> 4. 결과를 `result.csv`로 저장

---

**문제 25.** 다음 요구사항에 맞는 상품 재고 관리 프로그램을 작성하시오.

> **상품 재고 관리**
>
> products.csv 파일 내용:
> ```
> 상품명,카테고리,재고,가격
> 노트북,전자기기,5,1500000
> 마우스,전자기기,3,30000
> 키보드,전자기기,15,120000
> 연필,문구류,50,500
> 지우개,문구류,30,300
> ```
>
> 기능:
> 1. 전체 상품 목록 출력
> 2. 재고 5개 이하 경고 표시
> 3. 카테고리별 상품 수와 총 재고 가치 계산
> 4. 가장 비싼 상품과 가장 싼 상품 찾기
> 5. 재고 가치 순으로 정렬하여 `inventory_report.csv`로 저장

---

### 🔴 고급

**문제 26.** 다음 요구사항에 맞는 설문조사 분석 프로그램을 작성하시오.

> **설문조사 분석**
>
> survey.csv 파일 내용:
> ```
> 이름,나이,성별,만족도,추천여부
> 김철수,25,남,5,예
> 박영희,30,여,4,예
> 이민수,28,남,3,아니오
> 최지은,22,여,5,예
> 정민호,35,남,4,예
> 강수진,27,여,2,아니오
> 한동건,31,남,5,예
> 윤서연,24,여,4,예
> ```
>
> 기능:
> 1. 기본 통계: 응답자 수, 평균 나이, 최소/최대 나이
> 2. 성별 분포: 남녀 인원수와 비율(%)
> 3. 만족도 분석: 평균 만족도, 만족도별 분포 (막대 그래프: ■ 문자 사용)
> 4. 성별 만족도 비교: 남성 평균 vs 여성 평균
> 5. 연령대별 분석: 20대/30대별 만족도 평균과 추천 비율
> 6. 분석 결과를 `survey_report.csv`로 저장

---
---

# 🔑 정답 및 해설

---

## 📝 객관식 정답

---

### 🟢 초급

**문제 1. 정답: ② Comma-Separated Values**

CSV는 Comma-Separated Values(쉼표로 구분된 값)의 약자입니다. 데이터를 쉼표로 구분하여 텍스트 파일로 저장합니다.

---

**문제 2. 정답: ③ `csv`**

`csv`는 파이썬 기본 내장 모듈로, 별도 설치 없이 `import csv`로 바로 사용할 수 있습니다.

---

**문제 3. 정답: ② `csv.reader(file)`**

`csv.reader(file)`로 CSV 리더 객체를 생성합니다. 각 행을 리스트로 반환합니다.

---

**문제 4. 정답: ③ `newline=''`**

CSV 파일을 쓸 때 `newline=''`을 지정하지 않으면 행 사이에 빈 줄이 생깁니다.

---

**문제 5. 정답: ② `next()`**

`next(csv_reader)`를 호출하면 첫 줄(헤더)을 건너뛰고 다음 줄부터 읽습니다.

---

**문제 6. 정답: ④ 글자 색, 셀 병합 등 서식 저장 가능**

CSV는 순수 텍스트 형식이므로 글자 색, 셀 병합, 수식 등의 서식 정보를 저장할 수 없습니다.

---

**문제 7. 정답: ② `encoding='utf-8'`**

`encoding='utf-8'`을 지정해야 한글이 깨지지 않습니다. UTF-8은 한글을 포함한 다국어를 지원하는 인코딩입니다.

---

### 🟡 중급

**문제 8. 정답: ② `csv.DictReader`**

`DictReader`는 첫 줄을 자동으로 헤더로 인식하고, 각 행을 딕셔너리로 반환합니다. `row['이름']`처럼 컬럼 이름으로 접근 가능합니다.

---

**문제 9. 정답: ② `writeheader()`**

`DictWriter`의 `writeheader()` 메서드로 `fieldnames`에 지정한 컬럼 이름을 헤더 행으로 씁니다.

---

**문제 10. 정답: ③ `<class 'list'>`**

`csv.reader`는 각 행을 리스트로 반환합니다. `['이름', '나이', '학년']` 형태입니다.

---

**문제 11. 정답: ③ `'a'`**

`'a'`(append) 모드는 기존 파일 끝에 데이터를 추가합니다. `'w'`는 기존 내용을 덮어씁니다.

---

**문제 12. 정답: ② `delimiter='\t'`**

`csv.reader(file, delimiter='\t')`로 탭 구분자를 지정합니다.

---

### 🔴 고급

**문제 13. 정답: ② `이름,점수\n김철수,85\n박영희,92`**

`writeheader()`로 헤더(`이름,점수`)가 먼저 쓰이고, `writerows()`로 데이터 행들이 쓰입니다.

---

**문제 14. 정답: ② `str`**

CSV에서 읽은 모든 값은 **문자열**입니다. 숫자로 사용하려면 `int()` 또는 `float()`로 변환해야 합니다. `row['나이']`는 `'25'`(문자열)입니다.

---

**문제 15. 정답: ② `sum(s['국어'] for s in scores) / len(scores)`**

제너레이터 표현식으로 각 학생의 국어 점수를 합산한 후 학생 수로 나눕니다.

---

## 📝 주관식 정답

---

### 🟢 초급

**문제 16. 모범답안:**

CSV(Comma-Separated Values)는 데이터를 쉼표로 구분하여 텍스트 파일로 저장하는 형식입니다. 각 줄이 하나의 행(레코드)이고, 쉼표로 구분된 값들이 열(컬럼)입니다.

**장점:**
1. 간단한 텍스트 형식으로, 메모장으로도 열어볼 수 있으며 용량이 작습니다.
2. 엑셀, 구글 시트, 모든 프로그래밍 언어에서 지원합니다.

**단점:**
1. 글자 색, 셀 병합, 수식 등 서식 정보를 저장할 수 없습니다.
2. 하나의 시트(테이블)만 저장할 수 있습니다.

---

**문제 17. 모범답안:**

**`csv.reader`**: 각 행을 **리스트**로 반환합니다. 인덱스로 접근합니다.
```python
reader = csv.reader(file)
for row in reader:
    print(row[0], row[1])  # 인덱스로 접근
```

**`csv.DictReader`**: 첫 줄을 헤더로 인식하고, 각 행을 **딕셔너리**로 반환합니다. 컬럼 이름으로 접근합니다.
```python
reader = csv.DictReader(file)
for row in reader:
    print(row['이름'], row['나이'])  # 컬럼 이름으로 접근
```

`DictReader`가 코드 가독성이 좋지만, `reader`는 헤더가 없는 파일에서도 사용할 수 있다는 장점이 있습니다.

---

**문제 18. 모범답안:**

```
김철수은(는) 20살, 2학년
박영희은(는) 21살, 3학년
```

`DictReader`는 첫 줄(`이름,나이,학년`)을 자동으로 헤더로 인식하여 건너뛰고, 나머지 행을 딕셔너리로 반환합니다.

---

### 🟡 중급

**문제 19. 모범답안:**

**`newline=''`이 필요한 이유:**
Windows에서 CSV 파일을 쓸 때, `csv.writer`가 자체적으로 줄바꿈을 처리합니다. `newline=''`을 지정하지 않으면 파이썬의 `open()` 함수도 줄바꿈을 추가하여 **줄바꿈이 이중으로 발생**합니다. 결과적으로 행 사이에 빈 줄이 생깁니다.

**`encoding='utf-8'`이 필요한 이유:**
기본 인코딩은 운영체제에 따라 다릅니다 (Windows는 cp949 등). 한글을 포함한 데이터를 저장할 때 `utf-8`을 명시하지 않으면 **한글이 깨지거나 읽기 오류**가 발생할 수 있습니다. UTF-8은 국제 표준 인코딩으로, 한글을 안전하게 저장할 수 있습니다.

---

**문제 20. 모범답안:**

```
1등 박영희: 91.7점
2등 정민호: 87.0점
3등 최지은: 90.0점
```

**수정: 올바른 결과 계산:**
- 김철수: (85+90+78)/3 = 84.3
- 박영희: (92+88+95)/3 = 91.7
- 이민수: (78+85+82)/3 = 81.7
- 최지은: (88+92+90)/3 = 90.0
- 정민호: (95+78+88)/3 = 87.0

평균 내림차순 정렬 후:

```
1등 박영희: 91.7점
2등 최지은: 90.0점
3등 정민호: 87.0점
4등 김철수: 84.3점
5등 이민수: 81.7점
```

---

### 🔴 고급

**문제 21. 모범답안:**

`defaultdict(int)`는 존재하지 않는 키에 접근하면 자동으로 기본값(`int`의 경우 `0`)을 생성합니다.

**일반 딕셔너리를 사용하는 경우:**
```python
daily_revenue = {}
for sale in sales:
    date = sale['날짜']
    if date in daily_revenue:
        daily_revenue[date] += sale['매출']
    else:
        daily_revenue[date] = sale['매출']  # 키가 없으면 먼저 생성 필요
```

**defaultdict를 사용하는 경우:**
```python
daily_revenue = defaultdict(int)
for sale in sales:
    daily_revenue[sale['날짜']] += sale['매출']  # 키가 없어도 바로 += 가능
```

일반 딕셔너리는 존재하지 않는 키에 `+=`를 하면 `KeyError`가 발생합니다. `defaultdict(int)`는 새 키가 나타나면 자동으로 `0`을 초기값으로 설정하므로, 조건문 없이 바로 누적할 수 있어 코드가 간결해집니다.

---

## 💻 실습형 정답

---

### 🟢 초급

**문제 22. 모범답안:**

```python
import csv

# 방법 1: csv.writer (리스트로 쓰기)
data = [
    ['이름', '나이', '학과'],
    ['홍길동', 22, '컴퓨터공학'],
    ['김영희', 20, '경영학'],
    ['이철수', 23, '전자공학'],
    ['박지민', 21, '디자인학']
]

with open('students_list.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("방법 1: students_list.csv 저장 완료!")

# 방법 2: csv.DictWriter (딕셔너리로 쓰기)
students = [
    {'이름': '홍길동', '나이': 22, '학과': '컴퓨터공학'},
    {'이름': '김영희', '나이': 20, '학과': '경영학'},
    {'이름': '이철수', '나이': 23, '학과': '전자공학'},
    {'이름': '박지민', '나이': 21, '학과': '디자인학'}
]

with open('students_dict.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['이름', '나이', '학과']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("방법 2: students_dict.csv 저장 완료!")
```

핵심: `writer`는 리스트의 리스트를, `DictWriter`는 딕셔너리의 리스트를 저장합니다.

---

**문제 23. 모범답안:**

```python
import csv

# 데이터 읽기
students = []
with open('students.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            '이름': row['이름'],
            '나이': int(row['나이']),
            '학과': row['학과']
        })

# 전체 학생 목록
print("=" * 40)
print("전체 학생 목록")
print("=" * 40)
for s in students:
    print(f"  {s['이름']} ({s['나이']}세) - {s['학과']}")

# 21세 이상 필터링
print("\n21세 이상 학생:")
adults = [s for s in students if s['나이'] >= 21]
for s in adults:
    print(f"  {s['이름']} ({s['나이']}세)")

# 통계
ages = [s['나이'] for s in students]
print(f"\n총 학생 수: {len(students)}명")
print(f"평균 나이: {sum(ages) / len(ages):.1f}세")
```

핵심: `int(row['나이'])`로 문자열을 숫자로 변환해야 비교와 계산이 가능합니다.

---

### 🟡 중급

**문제 24. 모범답안:**

```python
import csv

# 1. 데이터 읽기
students = []
with open('scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            '이름': row['이름'],
            '국어': int(row['국어']),
            '영어': int(row['영어']),
            '수학': int(row['수학'])
        })

# 2. 총점, 평균, 학점 계산
def get_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

for s in students:
    s['총점'] = s['국어'] + s['영어'] + s['수학']
    s['평균'] = s['총점'] / 3
    s['학점'] = get_grade(s['평균'])

# 3. 평균 내림차순 정렬 (순위)
students.sort(key=lambda x: x['평균'], reverse=True)

# 4. 성적표 출력
print("=" * 65)
print("성적표")
print("=" * 65)
print(f"{'순위':^4} {'이름':^8} {'국어':^5} {'영어':^5} {'수학':^5} {'평균':^7} {'학점':^4}")
print("-" * 65)

for rank, s in enumerate(students, 1):
    s['순위'] = rank
    print(f"{rank:^4} {s['이름']:^8} {s['국어']:^5} {s['영어']:^5} {s['수학']:^5} {s['평균']:^7.1f} {s['학점']:^4}")

print("=" * 65)

# 5. 과목별 통계
print("\n과목별 통계:")
for subject in ['국어', '영어', '수학']:
    scores = [s[subject] for s in students]
    avg = sum(scores) / len(scores)
    print(f"  {subject}: 평균 {avg:.1f}점 | 최고 {max(scores)}점 | 최저 {min(scores)}점")

# 6. 결과 CSV 저장
with open('result.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['순위', '이름', '국어', '영어', '수학', '평균', '학점']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for s in students:
        writer.writerow({
            '순위': s['순위'],
            '이름': s['이름'],
            '국어': s['국어'],
            '영어': s['영어'],
            '수학': s['수학'],
            '평균': f"{s['평균']:.1f}",
            '학점': s['학점']
        })

print("\n✓ result.csv에 저장 완료!")
```

핵심: `sort(key=lambda x: x['평균'], reverse=True)`로 내림차순 정렬 후 `enumerate()`로 순위를 매깁니다.

---

**문제 25. 모범답안:**

```python
import csv
from collections import defaultdict

# 1. 데이터 읽기
products = []
with open('products.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append({
            '상품명': row['상품명'],
            '카테고리': row['카테고리'],
            '재고': int(row['재고']),
            '가격': int(row['가격'])
        })

# 재고 가치 계산
for p in products:
    p['재고가치'] = p['재고'] * p['가격']

# 2. 전체 상품 목록
print("=" * 55)
print("📦 재고 현황")
print("=" * 55)
print(f"{'상품명':^10} {'카테고리':^10} {'재고':^6} {'가격':>12}")
print("-" * 55)
for p in products:
    print(f"{p['상품명']:^10} {p['카테고리']:^10} {p['재고']:^6}개 {p['가격']:>10,}원")

# 3. 재고 부족 경고
low_stock = [p for p in products if p['재고'] <= 5]
if low_stock:
    print(f"\n⚠️  재고 부족 경고!")
    print("-" * 55)
    for p in low_stock:
        print(f"  {p['상품명']}: {p['재고']}개 (긴급 주문 필요)")

# 4. 카테고리별 분석
print(f"\n📊 카테고리별 분석:")
category_count = defaultdict(int)
category_value = defaultdict(int)
for p in products:
    category_count[p['카테고리']] += 1
    category_value[p['카테고리']] += p['재고가치']

for cat in category_count:
    print(f"  {cat}: {category_count[cat]}개 상품 | 재고 가치: {category_value[cat]:,}원")

# 5. 가장 비싼/싼 상품
most_expensive = max(products, key=lambda x: x['가격'])
cheapest = min(products, key=lambda x: x['가격'])
print(f"\n💰 가장 비싼 상품: {most_expensive['상품명']} ({most_expensive['가격']:,}원)")
print(f"💸 가장 싼 상품: {cheapest['상품명']} ({cheapest['가격']:,}원)")

# 6. 총 재고 가치
total_value = sum(p['재고가치'] for p in products)
print(f"\n💎 총 재고 가치: {total_value:,}원")

# 7. 재고 가치 순 정렬 후 CSV 저장
products.sort(key=lambda x: x['재고가치'], reverse=True)

with open('inventory_report.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['상품명', '카테고리', '재고', '가격', '재고가치']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print("\n✓ inventory_report.csv에 저장 완료!")
```

핵심: `defaultdict`로 카테고리별 집계, `max()`/`min()`의 `key` 매개변수, 리스트 컴프리헨션을 활용합니다.

---

### 🔴 고급

**문제 26. 모범답안:**

```python
import csv
from collections import Counter, defaultdict

# 1. 데이터 읽기
responses = []
with open('survey.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        responses.append({
            '이름': row['이름'],
            '나이': int(row['나이']),
            '성별': row['성별'],
            '만족도': int(row['만족도']),
            '추천여부': row['추천여부']
        })

print("=" * 60)
print("📊 설문조사 결과 분석")
print("=" * 60)

# 2. 기본 통계
ages = [r['나이'] for r in responses]
print(f"\n응답자 수: {len(responses)}명")
print(f"평균 나이: {sum(ages)/len(ages):.1f}세")
print(f"최소/최대 나이: {min(ages)}세 / {max(ages)}세")

# 3. 성별 분포
gender_count = Counter(r['성별'] for r in responses)
print("\n👥 성별 분포:")
for gender, count in gender_count.items():
    pct = count / len(responses) * 100
    print(f"  {gender}: {count}명 ({pct:.1f}%)")

# 4. 만족도 분석
satisfactions = [r['만족도'] for r in responses]
avg_sat = sum(satisfactions) / len(satisfactions)
print(f"\n⭐ 평균 만족도: {avg_sat:.2f}/5.0")

sat_count = Counter(satisfactions)
print("\n만족도 분포:")
for score in sorted(sat_count.keys(), reverse=True):
    count = sat_count[score]
    bar = '■' * count
    print(f"  {score}점: {bar} ({count}명)")

# 5. 성별 만족도 비교
print("\n성별 만족도 비교:")
male_sat = [r['만족도'] for r in responses if r['성별'] == '남']
female_sat = [r['만족도'] for r in responses if r['성별'] == '여']

if male_sat:
    print(f"  남성 평균: {sum(male_sat)/len(male_sat):.2f}")
if female_sat:
    print(f"  여성 평균: {sum(female_sat)/len(female_sat):.2f}")

# 6. 연령대별 분석
print("\n📈 연령대별 분석:")
age_groups = {'20대': [], '30대': []}
rec_groups = {'20대': [], '30대': []}

for r in responses:
    if 20 <= r['나이'] < 30:
        age_groups['20대'].append(r['만족도'])
        rec_groups['20대'].append(r['추천여부'])
    elif 30 <= r['나이'] < 40:
        age_groups['30대'].append(r['만족도'])
        rec_groups['30대'].append(r['추천여부'])

for group in ['20대', '30대']:
    sats = age_groups[group]
    recs = rec_groups[group]
    if sats:
        avg = sum(sats) / len(sats)
        rec_rate = recs.count('예') / len(recs) * 100
        print(f"  {group}: 만족도 {avg:.2f} | 추천율 {rec_rate:.1f}% ({len(sats)}명)")

# 7. 결과 CSV 저장
print(f"\n💾 분석 결과 저장 중...")
with open('survey_report.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['항목', '값']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'항목': '응답자 수', '값': f'{len(responses)}명'})
    writer.writerow({'항목': '평균 나이', '값': f'{sum(ages)/len(ages):.1f}세'})
    writer.writerow({'항목': '평균 만족도', '값': f'{avg_sat:.2f}/5.0'})

    for gender, count in gender_count.items():
        pct = count / len(responses) * 100
        writer.writerow({'항목': f'{gender} 인원', '값': f'{count}명 ({pct:.1f}%)'})

    if male_sat:
        writer.writerow({'항목': '남성 만족도', '값': f'{sum(male_sat)/len(male_sat):.2f}'})
    if female_sat:
        writer.writerow({'항목': '여성 만족도', '값': f'{sum(female_sat)/len(female_sat):.2f}'})

print("✓ survey_report.csv 저장 완료!")
print("=" * 60)
```

핵심 포인트:
- `Counter`로 성별/만족도 빈도를 간결하게 집계합니다.
- 리스트 컴프리헨션으로 성별, 연령대별 필터링을 수행합니다.
- `■` 문자를 횟수만큼 반복하여 텍스트 기반 막대 그래프를 만듭니다.
- 연령대별 추천 비율은 `recs.count('예') / len(recs)`로 계산합니다.
- 분석 결과를 구조화된 CSV로 저장합니다.

---

조정현 교수 (peterchokr@gmail.com)  
영남이공대학교
