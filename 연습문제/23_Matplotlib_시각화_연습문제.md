# 23장 Matplotlib 시각화 — 연습문제

---

## 📝 객관식 문제

---

### 🟢 초급

**문제 1.** 파이썬에서 그래프를 그리기 위해 가장 많이 사용되는 라이브러리는?

① `pandas`  
② `matplotlib`  
③ `seaborn`  
④ `tkinter`  

---

**문제 2.** matplotlib에서 그래프를 화면에 표시하는 함수는?

① `plt.draw()`  
② `plt.display()`  
③ `plt.show()`  
④ `plt.render()`  

---

**문제 3.** 꺾은선 그래프를 그리는 함수는?

① `plt.bar()`  
② `plt.line()`  
③ `plt.plot()`  
④ `plt.scatter()`  

---

**문제 4.** 막대 그래프를 그리는 함수는?

① `plt.plot()`  
② `plt.bar()`  
③ `plt.pie()`  
④ `plt.hist()`  

---

**문제 5.** 그래프에 제목을 추가하는 함수는?

① `plt.name()`  
② `plt.header()`  
③ `plt.title()`  
④ `plt.label()`  

---

**문제 6.** 그래프에 격자(눈금선)를 추가하는 함수는?

① `plt.line()`  
② `plt.grid()`  
③ `plt.mesh()`  
④ `plt.ruler()`  

---

**문제 7.** matplotlib을 import하는 올바른 코드는?

① `import matplotlib`  
② `import matplotlib.pyplot as plt`  
③ `from matplotlib import graph`  
④ `import plt`  

---

### 🟡 중급

**문제 8.** 원 그래프에서 각 항목의 비율(%)을 표시하는 옵션은?

① `percent='%1.1f%%'`  
② `autopct='%1.1f%%'`  
③ `ratio='%1.1f%%'`  
④ `label_pct='%1.1f%%'`  

---

**문제 9.** 한 화면에 여러 그래프를 배치하는 함수는?

① `plt.multi()`  
② `plt.subplot()`  
③ `plt.layout()`  
④ `plt.grid_plot()`  

---

**문제 10.** 산점도(Scatter Plot)를 그리는 함수는?

① `plt.dot()`  
② `plt.point()`  
③ `plt.scatter()`  
④ `plt.plot_dots()`  

---

**문제 11.** 그래프를 이미지 파일로 저장하는 함수는?

① `plt.save()`  
② `plt.savefig()`  
③ `plt.export()`  
④ `plt.write()`  

---

**문제 12.** 꺾은선 그래프에서 데이터 점의 모양을 설정하는 옵션은?

① `point='o'`  
② `dot='o'`  
③ `marker='o'`  
④ `shape='o'`  

---

### 🔴 고급

**문제 13.** 다음 코드에서 `plt.subplot(2, 3, 4)`가 의미하는 것은?

① 2행 3열 중 4번째 위치  
② 2행 3열 중 3번째 위치  
③ 4개의 그래프를 2x3으로 배치  
④ 4번째 행의 2~3번째 열  

---

**문제 14.** 다음 코드의 실행 결과로 올바른 것은?

```python
fruits = ['사과', '바나나', '오렌지']
sales = [150, 120, 180]
for i, v in enumerate(sales):
    plt.text(i, v + 5, str(v), ha='center')
```

① 각 막대 아래에 숫자가 표시됨  
② 각 막대 위에 해당 판매량 숫자가 표시됨  
③ X축에 판매량이 표시됨  
④ 범례에 숫자가 추가됨  

---

**문제 15.** 한글 폰트 깨짐을 해결하기 위한 코드 조합으로 올바른 것은?

① `plt.font('Malgun Gothic')`  
② `plt.rcParams['font.family'] = 'Malgun Gothic'`과 `plt.rcParams['axes.unicode_minus'] = False`  
③ `plt.set_font('한글')`  
④ `import korean_font`  

---

## 📝 주관식 문제

---

### 🟢 초급

**문제 16.** 데이터 시각화가 필요한 이유를 4가지 이상 서술하시오. 숫자 데이터를 그래프로 표현했을 때의 장점을 구체적으로 설명하시오.

---

**문제 17.** matplotlib의 주요 그래프 6가지를 나열하고, 각 그래프의 함수명과 적합한 사용 상황을 설명하시오.

---

**문제 18.** 다음 코드의 실행 결과를 설명하시오. 각 함수의 역할을 서술하시오.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, color='red', marker='s', linewidth=2, label='매출')
plt.title('월별 매출', fontsize=16)
plt.xlabel('월')
plt.ylabel('매출 (만원)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

---

### 🟡 중급

**문제 19.** 그룹 막대 그래프를 그리기 위해 `np.arange()`와 `width`를 사용하는 이유를 설명하시오. 다음 코드에서 `x - width/2`와 `x + width/2`의 역할을 서술하시오.

```python
x = np.arange(len(categories))
width = 0.35
plt.bar(x - width/2, product_a, width, label='제품 A')
plt.bar(x + width/2, product_b, width, label='제품 B')
plt.xticks(x, categories)
```

---

**문제 20.** `plt.savefig()`의 주요 옵션 3가지를 설명하시오. PNG, JPG, PDF, SVG 형식의 차이점과 각각 적합한 사용 상황을 서술하시오.

---

### 🔴 고급

**문제 21.** 다음 CSV 데이터를 읽어 2x2 subplot으로 4개 그래프를 그리는 절차를 단계별로 설명하시오. 각 단계에서 사용되는 주요 함수를 명시하시오.

```
이름,국어,영어,수학
김철수,85,90,78
박영희,92,88,95
이민수,78,85,82
```

> 1번: 과목별 비교 (그룹 막대), 2번: 학생별 평균 (꺾은선), 3번: 과목별 평균 (막대), 4번: 점수 분포 (히스토그램)

---

## 💻 실습형 문제

---

### 🟢 초급

**문제 22.** 다음 데이터를 사용하여 꺾은선 그래프를 작성하시오.

> **요구사항:**
> - 데이터: 월(1~6), 기온([2, 5, 12, 18, 23, 27])
> - 선 색상: 빨강, 마커: 원형(o), 선 굵기: 2
> - 제목: "상반기 월별 기온"
> - X축: "월", Y축: "기온 (°C)"
> - 범례: "2024년 기온"
> - 격자 표시

---

**문제 23.** 다음 데이터를 사용하여 막대 그래프와 원 그래프를 subplot(1행 2열)으로 작성하시오.

> **데이터:** 프로그래밍 언어 선호도
> - 언어: Python, Java, JavaScript, C++, Go
> - 응답수: 45, 30, 35, 15, 10
>
> **요구사항:**
> - 왼쪽: 막대 그래프 (각 막대 위에 숫자 표시, 서로 다른 색상)
> - 오른쪽: 원 그래프 (비율% 표시, 1위 항목 강조)
> - 전체 크기: figsize=(12, 5)

---

### 🟡 중급

**문제 24.** 다음 CSV 데이터를 읽어 그래프로 시각화하시오.

> **sales.csv 파일 내용:**
> ```
> 월,제품A,제품B,제품C
> 1,120,90,60
> 2,150,110,80
> 3,130,120,90
> 4,170,100,110
> 5,160,130,100
> 6,190,140,120
> ```
>
> **요구사항 (2x2 subplot):**
> 1. 제품별 월별 추이 (꺾은선 그래프, 3개 선, 범례 포함)
> 2. 6개월 합계 비교 (막대 그래프, 막대 위에 합계 숫자 표시)
> 3. 6개월 매출 비율 (원 그래프, 비율% 표시)
> 4. 월별 총 매출 추이 (막대 그래프, 색상 그라데이션)
> - 그래프를 `sales_chart.png`로 저장

---

**문제 25.** 다음 데이터를 사용하여 학생 성적 분석 그래프를 작성하시오.

> **데이터:**
> ```python
> students = ['김철수', '박영희', '이민수', '최지은', '정민호']
> korean = [85, 92, 78, 88, 95]
> english = [90, 88, 85, 92, 78]
> math = [78, 95, 82, 90, 88]
> ```
>
> **요구사항 (2x2 subplot):**
> 1. 학생별 과목 점수 (그룹 막대 그래프, 3과목 비교)
> 2. 과목별 평균 비교 (가로 막대 그래프)
> 3. 전체 점수 분포 (히스토그램, bins=5)
> 4. 국어-수학 상관관계 (산점도, 각 점에 학생 이름 표시)
> - `plt.tight_layout()` 적용

---

### 🔴 고급

**문제 26.** 다음 CSV 데이터를 읽어 종합 데이터 분석 대시보드를 만드시오.

> **weather.csv 파일 내용:**
> ```
> 월,평균기온,강수량,일조시간
> 1,2.5,20,150
> 2,4.8,25,160
> 3,10.2,45,180
> 4,15.8,60,200
> 5,20.5,80,220
> 6,24.3,120,190
> 7,27.8,250,160
> 8,28.5,230,170
> 9,23.7,140,190
> 10,17.2,50,200
> 11,10.8,40,160
> 12,4.5,25,140
> ```
>
> **요구사항 (2x2 subplot):**
> 1. 기온 변화 (꺾은선, 빨강, 마커) + 가장 더운 달과 추운 달 표시(plt.text)
> 2. 월별 강수량 (막대, 파랑) + 평균선(plt.axhline) 표시
> 3. 일조시간 비율 (원 그래프, 4분기별 합산: 1~3월/4~6월/7~9월/10~12월)
> 4. 기온-강수량 상관관계 (산점도, 점 크기를 일조시간에 비례)
>
> **추가:**
> - 전체 제목: "2024년 기상 데이터 분석"
> - 통계 출력: 연평균 기온, 총 강수량, 총 일조시간
> - 가장 더운 달, 강수량 최다 달 출력
> - `weather_dashboard.png`로 저장 (dpi=300)

---
---

# 🔑 정답 및 해설

---

## 📝 객관식 정답

---

### 🟢 초급

**문제 1. 정답: ② `matplotlib`**

matplotlib은 파이썬에서 가장 널리 사용되는 데이터 시각화 라이브러리입니다. `matplotlib.pyplot`을 `plt`로 import하여 사용합니다.

---

**문제 2. 정답: ③ `plt.show()`**

`plt.show()`는 현재까지 그린 그래프를 화면(윈도우)에 표시합니다.

---

**문제 3. 정답: ③ `plt.plot()`**

`plt.plot(x, y)`는 꺾은선 그래프(Line Plot)를 그립니다. 시간에 따른 변화를 보여줄 때 적합합니다.

---

**문제 4. 정답: ② `plt.bar()`**

`plt.bar(x, y)`는 세로 막대 그래프를, `plt.barh(x, y)`는 가로 막대 그래프를 그립니다.

---

**문제 5. 정답: ③ `plt.title()`**

`plt.title('제목')`으로 그래프 상단에 제목을 추가합니다. `fontsize` 옵션으로 크기를 조절할 수 있습니다.

---

**문제 6. 정답: ② `plt.grid()`**

`plt.grid(True)`로 격자를 표시합니다. `linestyle`, `alpha` 등으로 스타일을 조절합니다.

---

**문제 7. 정답: ② `import matplotlib.pyplot as plt`**

`matplotlib.pyplot` 모듈을 `plt`라는 별칭으로 import하는 것이 관례입니다.

---

### 🟡 중급

**문제 8. 정답: ② `autopct='%1.1f%%'`**

`autopct` 옵션은 원 그래프의 각 조각에 비율(%)을 자동으로 표시합니다. `%1.1f%%`는 소수점 1자리까지 표시합니다.

---

**문제 9. 정답: ② `plt.subplot()`**

`plt.subplot(행, 열, 번호)`로 한 화면에 여러 그래프를 배치합니다. 예: `plt.subplot(2, 2, 1)`은 2x2 격자의 1번째 위치입니다.

---

**문제 10. 정답: ③ `plt.scatter()`**

`plt.scatter(x, y)`는 산점도를 그립니다. 두 변수 간의 관계(상관관계)를 파악할 때 사용합니다.

---

**문제 11. 정답: ② `plt.savefig()`**

`plt.savefig('파일명.png')`로 그래프를 이미지 파일로 저장합니다. `dpi` 옵션으로 해상도를 설정합니다.

---

**문제 12. 정답: ③ `marker='o'`**

`marker` 옵션은 데이터 점의 모양을 설정합니다. `'o'`(원), `'s'`(사각형), `'^'`(삼각형), `'*'`(별) 등이 있습니다.

---

### 🔴 고급

**문제 13. 정답: ① 2행 3열 중 4번째 위치**

`plt.subplot(2, 3, 4)`는 2행 3열(총 6칸) 격자에서 4번째 위치(2행 1열)에 그래프를 배치합니다. 번호는 왼쪽 위부터 오른쪽으로 1, 2, 3, 다음 줄 4, 5, 6 순서입니다.

---

**문제 14. 정답: ② 각 막대 위에 해당 판매량 숫자가 표시됨**

`plt.text(i, v + 5, str(v), ha='center')`는 각 막대(`i` 위치)의 상단(`v + 5` 높이)에 값(`str(v)`)을 중앙 정렬(`ha='center'`)로 표시합니다.

---

**문제 15. 정답: ② `plt.rcParams['font.family'] = 'Malgun Gothic'`과 `plt.rcParams['axes.unicode_minus'] = False`**

`font.family`는 한글 폰트를 설정하고, `axes.unicode_minus = False`는 마이너스 기호(`-`)가 깨지는 것을 방지합니다.

---

## 📝 주관식 정답

---

### 🟢 초급

**문제 16. 모범답안:**

데이터 시각화가 필요한 이유:
1. **패턴과 추세 발견**: 숫자만으로는 파악하기 어려운 데이터의 변화 추세를 한눈에 파악할 수 있습니다.
2. **데이터 비교의 용이성**: 여러 항목이나 기간의 데이터를 시각적으로 쉽게 비교할 수 있습니다.
3. **이상값 탐지**: 데이터 중 비정상적인 값(이상값, 특이값)을 빠르게 발견할 수 있습니다.
4. **효과적인 커뮤니케이션**: 보고서, 발표 등에서 그래프를 사용하면 정보 전달이 더 효과적입니다.
5. **의사결정 지원**: 시각화된 데이터는 빠르고 정확한 의사결정에 도움을 줍니다.

---

**문제 17. 모범답안:**

| 그래프 | 함수 | 적합한 사용 상황 |
|---|---|---|
| 꺾은선 그래프 | `plt.plot()` | 시간에 따른 변화 추이 (월별 매출, 기온 변화) |
| 막대 그래프 | `plt.bar()` | 항목 간 크기 비교 (과일별 판매량, 과목별 점수) |
| 가로 막대 그래프 | `plt.barh()` | 항목명이 긴 경우의 크기 비교 |
| 원 그래프 | `plt.pie()` | 전체에서 각 항목의 비율 표시 (시장 점유율, 설문 비율) |
| 산점도 | `plt.scatter()` | 두 변수 간의 관계/상관관계 (키-몸무게, 공부시간-점수) |
| 히스토그램 | `plt.hist()` | 데이터의 분포 파악 (시험 점수 분포, 나이 분포) |

---

**문제 18. 모범답안:**

실행 결과: 빨간색 사각형 마커가 있는 꺾은선 그래프가 표시됩니다.

각 함수의 역할:
- `plt.plot(x, y, ...)`: x, y 데이터로 꺾은선 그래프를 그립니다.
  - `color='red'`: 선 색상을 빨강으로 설정
  - `marker='s'`: 데이터 점을 사각형(square)으로 표시
  - `linewidth=2`: 선 굵기를 2로 설정
  - `label='매출'`: 범례에 표시할 이름
- `plt.title('월별 매출', fontsize=16)`: 제목을 16pt 크기로 표시
- `plt.xlabel('월')`: X축 라벨 설정
- `plt.ylabel('매출 (만원)')`: Y축 라벨 설정
- `plt.legend()`: `label`에서 지정한 범례를 화면에 표시
- `plt.grid(True, linestyle='--', alpha=0.5)`: 점선(`--`) 격자를 반투명(`alpha=0.5`)으로 표시
- `plt.show()`: 그래프를 화면에 출력

---

### 🟡 중급

**문제 19. 모범답안:**

그룹 막대 그래프에서는 같은 카테고리에 여러 막대를 나란히 배치해야 합니다.

**`np.arange(len(categories))`를 사용하는 이유:**
카테고리가 `['1분기', '2분기', '3분기', '4분기']`일 때, `np.arange(4)`는 `[0, 1, 2, 3]`을 생성합니다. 이 숫자 배열을 X축의 기준 위치로 사용합니다.

**`width`를 사용하는 이유:**
두 막대가 겹치지 않도록 너비를 지정합니다.

**`x - width/2`와 `x + width/2`의 역할:**
- `x - width/2`: 기준 위치에서 왼쪽으로 `width/2`만큼 이동 → 제품 A 막대
- `x + width/2`: 기준 위치에서 오른쪽으로 `width/2`만큼 이동 → 제품 B 막대
- 결과적으로 두 막대가 기준 위치를 중심으로 나란히 배치됩니다.

**`plt.xticks(x, categories)`**: 숫자 위치(0, 1, 2, 3)에 실제 카테고리 이름을 표시합니다.

---

**문제 20. 모범답안:**

**`plt.savefig()` 주요 옵션:**
1. `dpi`: 해상도(dots per inch). 기본값 100, 고품질은 300 사용.
2. `bbox_inches='tight'`: 그래프 주변의 불필요한 여백을 제거합니다.
3. `transparent=True`: 배경을 투명하게 저장합니다.

**파일 형식별 차이점:**
- **PNG**: 무손실 압축, 투명 배경 지원 → 웹, 보고서, 일반 용도
- **JPG**: 손실 압축, 파일 크기 작음 → 사진, 용량 절약 필요 시
- **PDF**: 벡터 형식, 확대해도 깨지지 않음 → 논문, 인쇄물, 공식 문서
- **SVG**: 벡터 형식, 웹 호환 → 웹페이지, 편집 가능한 그래프

---

### 🔴 고급

**문제 21. 모범답안:**

**1단계: 라이브러리 import 및 한글 설정**
```python
import matplotlib.pyplot as plt
import csv
```
`plt.rcParams['font.family']`로 한글 폰트를 설정합니다.

**2단계: CSV 데이터 읽기**
`csv.DictReader`로 파일을 읽고, 학생 이름, 과목별 점수 리스트를 생성합니다. `int()`로 문자열을 정수로 변환합니다.

**3단계: Figure 생성**
`plt.figure(figsize=(12, 10))`으로 전체 크기를 설정합니다.

**4단계: 각 subplot 그리기**
- `plt.subplot(2, 2, 1)`: 그룹 막대 — `plt.bar()`를 3번 호출 (x-width, x, x+width)
- `plt.subplot(2, 2, 2)`: 꺾은선 — `plt.plot()`으로 학생별 평균을 선으로 연결
- `plt.subplot(2, 2, 3)`: 막대 — `plt.bar()`로 과목별 평균 표시, `plt.text()`로 값 추가
- `plt.subplot(2, 2, 4)`: 히스토그램 — `plt.hist()`로 모든 점수(국어+영어+수학)의 분포 표시

**5단계: 마무리**
`plt.tight_layout()`으로 간격 조정 후 `plt.show()` 또는 `plt.savefig()`로 출력/저장합니다.

---

## 💻 실습형 정답

---

### 🟢 초급

**문제 22. 모범답안:**

```python
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
months = [1, 2, 3, 4, 5, 6]
temps = [2, 5, 12, 18, 23, 27]

# 꺾은선 그래프
plt.plot(months, temps,
         color='red',
         marker='o',
         linewidth=2,
         markersize=8,
         label='2024년 기온')

# 제목과 라벨
plt.title('상반기 월별 기온', fontsize=16)
plt.xlabel('월', fontsize=12)
plt.ylabel('기온 (°C)', fontsize=12)

# 범례와 격자
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
```

핵심: `plt.plot()`의 `color`, `marker`, `linewidth`, `label` 옵션을 조합하여 꺾은선 그래프를 꾸밉니다.

---

**문제 23. 모범답안:**

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
languages = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
counts = [45, 30, 35, 15, 10]
colors = ['#3776AB', '#f89820', '#f7df1e', '#00599C', '#00ADD8']

plt.figure(figsize=(12, 5))

# 1. 막대 그래프
plt.subplot(1, 2, 1)
plt.bar(languages, counts, color=colors, width=0.6)
for i, v in enumerate(counts):
    plt.text(i, v + 1, str(v), ha='center', fontsize=11, fontweight='bold')
plt.title('프로그래밍 언어 선호도', fontsize=14)
plt.ylabel('응답 수 (명)', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 2. 원 그래프
plt.subplot(1, 2, 2)
explode = (0.08, 0, 0, 0, 0)  # Python 강조
plt.pie(counts, labels=languages, colors=colors,
        autopct='%1.1f%%', startangle=90,
        explode=explode, shadow=True)
plt.title('프로그래밍 언어 비율', fontsize=14)
plt.axis('equal')

plt.tight_layout()
plt.show()
```

핵심: `plt.text()`로 막대 위에 숫자를 표시하고, `explode`로 원 그래프의 1위 항목을 강조합니다.

---

### 🟡 중급

**문제 24. 모범답안:**

```python
import matplotlib.pyplot as plt
import csv

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 읽기
months, prod_a, prod_b, prod_c = [], [], [], []
with open('sales.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        months.append(int(row['월']))
        prod_a.append(int(row['제품A']))
        prod_b.append(int(row['제품B']))
        prod_c.append(int(row['제품C']))

plt.figure(figsize=(12, 10))

# 1. 제품별 월별 추이 (꺾은선)
plt.subplot(2, 2, 1)
plt.plot(months, prod_a, marker='o', label='제품A', linewidth=2)
plt.plot(months, prod_b, marker='s', label='제품B', linewidth=2)
plt.plot(months, prod_c, marker='^', label='제품C', linewidth=2)
plt.title('제품별 월별 매출 추이', fontsize=13)
plt.xlabel('월')
plt.ylabel('매출')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# 2. 6개월 합계 비교 (막대)
plt.subplot(2, 2, 2)
totals = [sum(prod_a), sum(prod_b), sum(prod_c)]
products = ['제품A', '제품B', '제품C']
plt.bar(products, totals, color=['skyblue', 'lightcoral', 'lightgreen'])
for i, v in enumerate(totals):
    plt.text(i, v + 10, str(v), ha='center', fontsize=11, fontweight='bold')
plt.title('6개월 총 매출 비교', fontsize=13)
plt.ylabel('합계')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 3. 매출 비율 (원)
plt.subplot(2, 2, 3)
plt.pie(totals, labels=products, autopct='%1.1f%%',
        colors=['skyblue', 'lightcoral', 'lightgreen'],
        startangle=90, shadow=True)
plt.title('제품별 매출 비율', fontsize=13)
plt.axis('equal')

# 4. 월별 총 매출 (막대)
plt.subplot(2, 2, 4)
monthly_total = [a + b + c for a, b, c in zip(prod_a, prod_b, prod_c)]
color_values = [0.3 + 0.1 * i for i in range(6)]
colors_grad = plt.cm.Blues(color_values)
plt.bar(months, monthly_total, color=colors_grad)
plt.title('월별 총 매출', fontsize=13)
plt.xlabel('월')
plt.ylabel('총 매출')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('sales_chart.png', dpi=300, bbox_inches='tight')
print("✓ sales_chart.png 저장 완료!")
plt.show()
```

핵심: CSV 데이터를 읽어 다양한 그래프로 시각화하고, `plt.cm.Blues`로 색상 그라데이션을 적용합니다.

---

**문제 25. 모범답안:**

```python
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
students = ['김철수', '박영희', '이민수', '최지은', '정민호']
korean = [85, 92, 78, 88, 95]
english = [90, 88, 85, 92, 78]
math = [78, 95, 82, 90, 88]

plt.figure(figsize=(12, 10))

# 1. 그룹 막대 그래프
plt.subplot(2, 2, 1)
x = np.arange(len(students))
width = 0.25
plt.bar(x - width, korean, width, label='국어', color='skyblue')
plt.bar(x, english, width, label='영어', color='lightgreen')
plt.bar(x + width, math, width, label='수학', color='lightcoral')
plt.title('학생별 과목 점수', fontsize=13)
plt.xlabel('학생')
plt.ylabel('점수')
plt.xticks(x, students)
plt.legend()
plt.grid(axis='y', alpha=0.3)

# 2. 가로 막대 (과목별 평균)
plt.subplot(2, 2, 2)
subjects = ['국어', '영어', '수학']
avgs = [sum(korean)/len(korean), sum(english)/len(english), sum(math)/len(math)]
colors = ['skyblue', 'lightgreen', 'lightcoral']
bars = plt.barh(subjects, avgs, color=colors)
for bar, v in zip(bars, avgs):
    plt.text(v + 0.5, bar.get_y() + bar.get_height()/2, f'{v:.1f}',
             va='center', fontsize=11)
plt.title('과목별 평균', fontsize=13)
plt.xlabel('평균 점수')
plt.grid(axis='x', alpha=0.3)

# 3. 히스토그램 (전체 점수 분포)
plt.subplot(2, 2, 3)
all_scores = korean + english + math
plt.hist(all_scores, bins=5, color='lightblue', edgecolor='black', alpha=0.7)
plt.title('전체 점수 분포', fontsize=13)
plt.xlabel('점수 구간')
plt.ylabel('빈도')
plt.grid(axis='y', alpha=0.3)

# 4. 산점도 (국어-수학 상관관계)
plt.subplot(2, 2, 4)
plt.scatter(korean, math, s=100, c='purple', alpha=0.7)
for i, name in enumerate(students):
    plt.text(korean[i] + 0.5, math[i] + 0.5, name, fontsize=9)
plt.title('국어-수학 상관관계', fontsize=13)
plt.xlabel('국어 점수')
plt.ylabel('수학 점수')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

핵심: `np.arange`와 `width`로 그룹 막대를 배치하고, `plt.text()`로 산점도에 학생 이름을 표시합니다.

---

### 🔴 고급

**문제 26. 모범답안:**

```python
import matplotlib.pyplot as plt
import csv

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 읽기
months, temps, rain, sun = [], [], [], []
with open('weather.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        months.append(int(row['월']))
        temps.append(float(row['평균기온']))
        rain.append(int(row['강수량']))
        sun.append(int(row['일조시간']))

# 통계 출력
print("=" * 50)
print("📊 2024년 기상 통계")
print("=" * 50)
print(f"연평균 기온: {sum(temps)/len(temps):.1f}°C")
print(f"총 강수량: {sum(rain)}mm")
print(f"총 일조시간: {sum(sun)}시간")

max_temp_month = months[temps.index(max(temps))]
max_rain_month = months[rain.index(max(rain))]
min_temp_month = months[temps.index(min(temps))]
print(f"가장 더운 달: {max_temp_month}월 ({max(temps)}°C)")
print(f"가장 추운 달: {min_temp_month}월 ({min(temps)}°C)")
print(f"강수량 최다: {max_rain_month}월 ({max(rain)}mm)")

# 그래프
plt.figure(figsize=(14, 10))
plt.suptitle('2024년 기상 데이터 분석', fontsize=18, fontweight='bold')

# 1. 기온 변화 (꺾은선)
plt.subplot(2, 2, 1)
plt.plot(months, temps, color='red', marker='o', linewidth=2, markersize=6)
max_idx = temps.index(max(temps))
min_idx = temps.index(min(temps))
plt.text(months[max_idx], temps[max_idx] + 1.5,
         f'{max(temps)}°C', ha='center', fontsize=9, color='red', fontweight='bold')
plt.text(months[min_idx], temps[min_idx] - 2,
         f'{min(temps)}°C', ha='center', fontsize=9, color='blue', fontweight='bold')
plt.title('월별 평균 기온', fontsize=13)
plt.xlabel('월')
plt.ylabel('기온 (°C)')
plt.xticks(months)
plt.grid(True, linestyle='--', alpha=0.5)

# 2. 강수량 (막대) + 평균선
plt.subplot(2, 2, 2)
plt.bar(months, rain, color='steelblue', alpha=0.8)
avg_rain = sum(rain) / len(rain)
plt.axhline(y=avg_rain, color='red', linestyle='--', linewidth=1.5,
            label=f'평균 {avg_rain:.0f}mm')
plt.title('월별 강수량', fontsize=13)
plt.xlabel('월')
plt.ylabel('강수량 (mm)')
plt.xticks(months)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 3. 일조시간 (원 그래프, 분기별)
plt.subplot(2, 2, 3)
q1 = sum(sun[0:3])
q2 = sum(sun[3:6])
q3 = sum(sun[6:9])
q4 = sum(sun[9:12])
quarters = [q1, q2, q3, q4]
q_labels = ['1분기(1~3월)', '2분기(4~6월)', '3분기(7~9월)', '4분기(10~12월)']
colors_q = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.pie(quarters, labels=q_labels, autopct='%1.1f%%',
        colors=colors_q, startangle=90, shadow=True)
plt.title('분기별 일조시간 비율', fontsize=13)
plt.axis('equal')

# 4. 기온-강수량 산점도 (점 크기 = 일조시간)
plt.subplot(2, 2, 4)
sizes = [s * 0.8 for s in sun]
plt.scatter(temps, rain, s=sizes, c=months, cmap='coolwarm',
            alpha=0.7, edgecolors='black', linewidths=0.5)
plt.colorbar(label='월')
plt.title('기온-강수량 관계 (크기=일조시간)', fontsize=13)
plt.xlabel('평균 기온 (°C)')
plt.ylabel('강수량 (mm)')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('weather_dashboard.png', dpi=300, bbox_inches='tight')
print("\n✓ weather_dashboard.png 저장 완료!")
plt.show()
```

핵심 포인트:
- `plt.suptitle()`로 전체 제목을 설정합니다.
- `plt.text()`로 최고/최저 기온에 주석을 표시합니다.
- `plt.axhline()`으로 평균선을 가로로 표시합니다.
- 분기별로 리스트 슬라이싱(`sun[0:3]` 등)하여 합산합니다.
- 산점도에서 `s=sizes`로 점 크기를 일조시간에 비례, `c=months`와 `cmap`으로 월별 색상을 적용합니다.
- `plt.colorbar()`로 색상 범례를 표시합니다.
- `tight_layout(rect=[0, 0, 1, 0.95])`으로 suptitle 공간을 확보합니다.

---

조정현 교수 (peterchokr@gmail.com)  
영남이공대학교
