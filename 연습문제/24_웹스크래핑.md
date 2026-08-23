# 24장 웹 스크래핑 — 연습문제

---

## 📝 객관식 문제

---

### 🟢 초급

**문제 1.** 웹 스크래핑이란 무엇인가?

① 웹사이트를 만드는 기술
② 웹사이트에서 데이터를 자동으로 수집하는 기술
③ 웹사이트를 디자인하는 기술
④ 웹서버를 관리하는 기술

---

**문제 2.** 웹페이지를 다운로드하는 데 사용하는 라이브러리는?

① `beautifulsoup4`
② `requests`
③ `selenium`
④ `scrapy`

---

**문제 3.** HTML을 파싱(분석)하는 데 사용하는 라이브러리는?

① `requests`
② `csv`
③ `BeautifulSoup`
④ `json`

---

**문제 4.** 다음 중 HTML 태그가 아닌 것은?

① `<h1>`
② `<p>`
③ `<div>`
④ `<print>`

---

**문제 5.** BeautifulSoup 객체를 생성하는 올바른 코드는?

① `BeautifulSoup(html)`
② `BeautifulSoup(html, 'html.parser')`
③ `BeautifulSoup.parse(html)`
④ `BeautifulSoup.read(html)`

---

**문제 6.** HTML에서 여러 요소에 같은 스타일을 적용할 때 사용하는 속성은?

① `id`
② `name`
③ `class`
④ `style`

---

**문제 7.** `requests.get(url)` 실행 후 응답 코드가 200인 경우의 의미는?

① 페이지를 찾을 수 없음
② 서버 오류
③ 접근 거부
④ 성공

---

### 🟡 중급

**문제 8.** HTML에서 첫 번째 `<h2>` 태그만 찾는 코드로 올바른 것은?

① `soup.find_all('h2')`
② `soup.find('h2')`
③ `soup.get('h2')`
④ `soup.select('h2')`

---

**문제 9.** 특정 class를 가진 모든 `<div>` 태그를 찾는 코드로 올바른 것은?

① `soup.find_all('div', class='product')`
② `soup.find_all('div', class_='product')`
③ `soup.find_all('div', className='product')`
④ `soup.find_all('div', cls='product')`

---

**문제 10.** `<a href="https://example.com">링크</a>`에서 URL을 추출하는 코드는?

① `link.text`
② `link.get('href')`
③ `link.url`
④ `link.get('src')`

---

**문제 11.** `<a>` 태그에서 텍스트("링크")를 추출하는 코드는?

① `link.get('text')`
② `link.value`
③ `link.text`
④ `link.content`

---

**문제 12.** 서버 부담을 줄이기 위해 요청 사이에 대기 시간을 두는 코드는?

① `wait(2)`
② `time.sleep(2)`
③ `pause(2)`
④ `delay(2)`

---

### 🔴 고급

**문제 13.** 다음 코드에서 `class_='author'`를 사용하는 이유는?

```python
soup.find(class_='author')
```

① `class`가 HTML 속성이 아니라서
② `class`가 파이썬 예약어이기 때문에
③ BeautifulSoup의 문법 규칙이라서
④ 대소문자를 구분하기 위해서

---

**문제 14.** 다음 코드에서 가격 문자열 `"35,000원"`에서 숫자만 추출하는 올바른 코드는?

```python
import re
price_text = "35,000원"
```

① `int(price_text)`
② `price_text.strip('원')`
③ `int(re.sub(r'[^0-9]', '', price_text))`
④ `float(price_text)`

---

**문제 15.** 웹 스크래핑 시 User-Agent를 설정하는 이유는?

① 웹페이지 로딩 속도를 높이기 위해
② 일부 웹사이트가 봇을 차단하므로 브라우저처럼 보이기 위해
③ HTML 인코딩을 맞추기 위해
④ 파일 저장 형식을 설정하기 위해

---

## 📝 주관식 문제

---

### 🟢 초급

**문제 16.** 웹 스크래핑과 웹 크롤링의 차이점을 설명하시오. 각각의 실생활 활용 예시를 2가지씩 들어 설명하시오.

---

**문제 17.** `find()`와 `find_all()`의 차이점을 설명하시오. 각 메서드의 반환값과 사용 상황을 코드 예시와 함께 서술하시오.

---

**문제 18.** 다음 HTML에서 BeautifulSoup을 사용하여 제목, 저자, 가격을 추출하는 과정을 단계별로 설명하시오.

```html
<div class="book">
    <h2>파이썬 기초</h2>
    <p class="author">저자: 김철수</p>
    <p class="price">가격: 20,000원</p>
</div>
```

---

### 🟡 중급

**문제 19.** 웹 스크래핑 시 지켜야 할 윤리적 규칙 5가지를 설명하시오. `robots.txt`의 역할과 확인 방법을 서술하시오.

---

**문제 20.** 다음 코드의 실행 결과를 쓰시오.

```python
from bs4 import BeautifulSoup

html = """
<html>
<body>
    <div class="product">
        <h3 class="name">노트북</h3>
        <p class="price">1,500,000원</p>
        <p class="stock">재고: 5개</p>
    </div>
    <div class="product">
        <h3 class="name">마우스</h3>
        <p class="price">30,000원</p>
        <p class="stock">재고: 20개</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
products = soup.find_all('div', class_='product')
print(f"총 {len(products)}개 상품")

for item in products:
    name = item.find('h3', class_='name').text
    price = item.find('p', class_='price').text
    print(f"{name}: {price}")
```

---

### 🔴 고급

**문제 21.** 정규표현식(`re` 모듈)을 활용한 데이터 추출에서 `re.sub()`과 `re.findall()`의 차이점을 설명하시오. 다음 문자열에서 각각을 사용하여 숫자를 추출하는 방법을 코드로 보이시오.

```
"가격: 35,000원", "평점: 4.5", "재고: 15개"
```

---

## 💻 실습형 문제

---

### 🟢 초급

**문제 22.** 다음 HTML 문자열에서 모든 링크의 텍스트와 URL을 추출하는 코드를 작성하시오.

```html
<html>
<body>
    <h1>추천 사이트</h1>
    <a href="https://www.python.org">파이썬 공식</a>
    <a href="https://www.github.com">깃허브</a>
    <a href="https://stackoverflow.com">스택오버플로우</a>
    <a href="https://docs.python.org">파이썬 문서</a>
</body>
</html>
```

> **출력 형식:**
>
> ```
> [1] 파이썬 공식 → https://www.python.org
> [2] 깃허브 → https://www.github.com
> ...
> 총 4개의 링크
> ```

---

**문제 23.** 다음 HTML 문자열에서 모든 도서 정보를 추출하여 화면에 출력하는 코드를 작성하시오.

```html
<html>
<body>
    <h1>도서 목록</h1>
    <div class="book">
        <h2>파이썬 입문</h2>
        <p class="author">저자: 홍길동</p>
        <p class="price">18,000원</p>
    </div>
    <div class="book">
        <h2>데이터 분석</h2>
        <p class="author">저자: 김데이터</p>
        <p class="price">25,000원</p>
    </div>
    <div class="book">
        <h2>웹 개발</h2>
        <p class="author">저자: 박웹</p>
        <p class="price">22,000원</p>
    </div>
</body>
</html>
```

> **요구사항:**
>
> - 제목, 저자, 가격 추출
> - 가격에서 숫자만 추출하여 정수로 변환
> - 총 도서 수와 평균 가격 출력

---

### 🟡 중급

**문제 24.** 다음 HTML 문자열에서 뉴스 정보를 추출하여 CSV 파일로 저장하는 코드를 작성하시오.

```html
<html>
<body>
    <h1>오늘의 뉴스</h1>
    <div class="news-item">
        <h2 class="headline">파이썬 4.0 출시 예정</h2>
        <p class="date">2024-03-15</p>
        <p class="summary">파이썬 4.0이 올해 말 출시될 예정입니다.</p>
        <a href="news1.html" class="link">더보기</a>
    </div>
    <div class="news-item">
        <h2 class="headline">AI 로봇 일상 진출</h2>
        <p class="date">2024-03-14</p>
        <p class="summary">AI 로봇이 가정용으로 보급되기 시작했습니다.</p>
        <a href="news2.html" class="link">더보기</a>
    </div>
    <div class="news-item">
        <h2 class="headline">전기차 배터리 혁신</h2>
        <p class="date">2024-03-13</p>
        <p class="summary">새로운 배터리 기술로 주행거리가 2배 늘었습니다.</p>
        <a href="news3.html" class="link">더보기</a>
    </div>
</body>
</html>
```

> **요구사항:**
>
> - 헤드라인, 날짜, 요약, 링크 추출
> - 콘솔에 번호 매겨 출력
> - `news_data.csv`로 저장 (컬럼: 번호, 헤드라인, 날짜, 요약, 링크)

---

**문제 25.** 다음 HTML 문자열에서 상품 정보를 추출하고 분석하는 코드를 작성하시오.

```html
<html>
<body>
    <h1>전자제품 매장</h1>
    <div class="product">
        <h3 class="name">무선 이어폰</h3>
        <p class="price">89,000원</p>
        <p class="rating">평점: 4.7</p>
        <p class="stock">재고: 25개</p>
        <p class="category">카테고리: 음향기기</p>
    </div>
    <div class="product">
        <h3 class="name">스마트워치</h3>
        <p class="price">250,000원</p>
        <p class="rating">평점: 4.3</p>
        <p class="stock">재고: 8개</p>
        <p class="category">카테고리: 웨어러블</p>
    </div>
    <div class="product">
        <h3 class="name">블루투스 스피커</h3>
        <p class="price">65,000원</p>
        <p class="rating">평점: 4.5</p>
        <p class="stock">재고: 30개</p>
        <p class="category">카테고리: 음향기기</p>
    </div>
    <div class="product">
        <h3 class="name">태블릿</h3>
        <p class="price">450,000원</p>
        <p class="rating">평점: 4.8</p>
        <p class="stock">재고: 3개</p>
        <p class="category">카테고리: 컴퓨터</p>
    </div>
    <div class="product">
        <h3 class="name">보조배터리</h3>
        <p class="price">25,000원</p>
        <p class="rating">평점: 4.1</p>
        <p class="stock">재고: 50개</p>
        <p class="category">카테고리: 액세서리</p>
    </div>
</body>
</html>
```

> **요구사항:**
>
> 1. 모든 상품 정보 추출 (이름, 가격, 평점, 재고, 카테고리)
> 2. 가격/평점/재고에서 숫자만 추출
> 3. 재고 10개 이하 상품 경고
> 4. 카테고리별 상품 수와 총 재고 가치 통계
> 5. 평점 높은 순 정렬
> 6. `products_report.csv`로 저장

---

### 🔴 고급

**문제 26.** 다음 HTML 문자열에서 학교 성적 데이터를 추출하여 종합 분석하는 코드를 작성하시오.

```html
<html>
<body>
    <h1>2024학년도 성적표</h1>
    <table class="grade-table">
        <tr class="header">
            <th>이름</th><th>학과</th><th>국어</th><th>영어</th><th>수학</th>
        </tr>
        <tr class="student">
            <td class="name">김철수</td><td class="dept">컴퓨터공학</td>
            <td class="score">85</td><td class="score">90</td><td class="score">78</td>
        </tr>
        <tr class="student">
            <td class="name">박영희</td><td class="dept">컴퓨터공학</td>
            <td class="score">92</td><td class="score">88</td><td class="score">95</td>
        </tr>
        <tr class="student">
            <td class="name">이민수</td><td class="dept">경영학</td>
            <td class="score">78</td><td class="score">85</td><td class="score">82</td>
        </tr>
        <tr class="student">
            <td class="name">최지은</td><td class="dept">경영학</td>
            <td class="score">88</td><td class="score">92</td><td class="score">90</td>
        </tr>
        <tr class="student">
            <td class="name">정민호</td><td class="dept">디자인학</td>
            <td class="score">95</td><td class="score">78</td><td class="score">88</td>
        </tr>
    </table>
</body>
</html>
```

> **요구사항:**
>
> 1. `<table>` 태그에서 모든 학생 정보 추출 (이름, 학과, 국어, 영어, 수학)
> 2. 각 학생의 평균, 학점 계산 (90↑A, 80↑B, 70↑C, 60↑D, F)
> 3. 성적 순위표 출력 (평균 내림차순)
> 4. 학과별 평균 성적 통계
> 5. 과목별 최고점/최저점 학생
> 6. `grade_report.csv`로 저장

---

---

# 🔑 정답 및 해설

---

## 📝 객관식 정답

---

### 🟢 초급

**문제 1. 정답: ② 웹사이트에서 데이터를 자동으로 수집하는 기술**

웹 스크래핑은 웹사이트의 HTML에서 원하는 데이터(가격, 제목 등)를 자동으로 추출하는 기술입니다.

---

**문제 2. 정답: ② `requests`**

`requests` 라이브러리는 HTTP 요청을 보내 웹페이지의 HTML을 다운로드합니다.

---

**문제 3. 정답: ③ `BeautifulSoup`**

`BeautifulSoup`(`beautifulsoup4` 패키지)은 HTML을 파싱하여 원하는 태그와 데이터를 쉽게 추출할 수 있게 합니다.

---

**문제 4. 정답: ④ `<print>`**

`<print>`는 HTML 태그가 아닙니다. `<h1>`, `<p>`, `<div>`는 모두 표준 HTML 태그입니다.

---

**문제 5. 정답: ② `BeautifulSoup(html, 'html.parser')`**

첫 번째 인자는 HTML 문자열, 두 번째 인자는 파서(parser)를 지정합니다. `'html.parser'`는 파이썬 내장 파서입니다.

---

**문제 6. 정답: ③ `class`**

`class`는 여러 요소에 같은 스타일을 적용할 때 사용합니다. `id`는 고유한 하나의 요소를 식별합니다.

---

**문제 7. 정답: ④ 성공**

HTTP 상태 코드 200은 요청 성공을 의미합니다. 404는 페이지 없음, 403은 접근 거부, 500은 서버 오류입니다.

---

### 🟡 중급

**문제 8. 정답: ② `soup.find('h2')`**

`find()`는 조건에 맞는 첫 번째 요소 하나만 반환합니다. `find_all()`은 모든 요소를 리스트로 반환합니다.

---

**문제 9. 정답: ② `soup.find_all('div', class_='product')`**

`class`는 파이썬 예약어이므로 `class_`를 사용해야 합니다.

---

**문제 10. 정답: ② `link.get('href')`**

`get('속성명')`으로 태그의 속성 값을 가져옵니다. `link['href']`로도 가능합니다.

---

**문제 11. 정답: ③ `link.text`**

`.text` 속성은 태그 안의 텍스트 내용을 반환합니다. `<a>` 태그의 경우 링크 텍스트("링크")를 가져옵니다.

---

**문제 12. 정답: ② `time.sleep(2)`**

`time.sleep(2)`은 2초간 프로그램 실행을 일시 중지합니다. 서버에 과부하를 주지 않기 위해 사용합니다.

---

### 🔴 고급

**문제 13. 정답: ② `class`가 파이썬 예약어이기 때문에**

`class`는 파이썬에서 클래스를 정의하는 예약어(keyword)이므로, BeautifulSoup에서는 `class_`로 언더스코어를 붙여 사용합니다.

---

**문제 14. 정답: ③ `int(re.sub(r'[^0-9]', '', price_text))`**

`re.sub(r'[^0-9]', '', price_text)`는 숫자가 아닌 모든 문자(`[^0-9]`)를 빈 문자열로 치환합니다. `"35,000원"` → `"35000"` → `int()` → `35000`

---

**문제 15. 정답: ② 일부 웹사이트가 봇을 차단하므로 브라우저처럼 보이기 위해**

User-Agent 헤더는 요청을 보내는 클라이언트 정보를 담습니다. 브라우저 정보를 설정하면 봇 차단을 피할 수 있습니다.

---

## 📝 주관식 정답

---

### 🟢 초급

**문제 16. 모범답안:**

**웹 스크래핑**: 웹사이트에서 **특정 데이터를 추출**하는 기술

- 예시: 쇼핑몰 상품 가격 비교, 뉴스 헤드라인 수집

**웹 크롤링**: 웹사이트 **전체를 탐색**하는 기술 (검색엔진처럼)

- 예시: 구글 검색엔진의 웹페이지 인덱싱, 사이트맵 생성

주요 차이점: 스크래핑은 **특정 데이터 추출**이 목적이고, 크롤링은 **웹페이지 탐색/발견**이 목적입니다.

---

**문제 17. 모범답안:**

**`find()`**: 조건에 맞는 **첫 번째 요소 하나만** 반환합니다.

```python
first_h2 = soup.find('h2')  # 첫 번째 h2 태그
# 반환값: Tag 객체 (또는 None)
```

사용 상황: 하나만 있는 태그(제목, ID 등)를 찾을 때

**`find_all()`**: 조건에 맞는 **모든 요소를 리스트**로 반환합니다.

```python
all_h2 = soup.find_all('h2')  # 모든 h2 태그
# 반환값: 리스트 (비어있으면 [])
```

사용 상황: 여러 개의 같은 태그(상품 목록, 뉴스 목록 등)를 찾을 때

---

**문제 18. 모범답안:**

1단계: HTML을 BeautifulSoup으로 파싱

```python
soup = BeautifulSoup(html, 'html.parser')
```

2단계: `class="book"` div를 찾기

```python
book = soup.find('div', class_='book')
```

3단계: 내부 태그에서 데이터 추출

```python
title = book.find('h2').text           # "파이썬 기초"
author = book.find(class_='author').text  # "저자: 김철수"
price = book.find(class_='price').text    # "가격: 20,000원"
```

4단계: `.text`로 태그 안의 텍스트만 추출합니다. 필요하면 `replace()`나 정규표현식으로 불필요한 문자를 제거합니다.

---

### 🟡 중급

**문제 19. 모범답안:**

**윤리적 규칙 5가지:**

1. `robots.txt`를 확인하고 허용된 범위 내에서만 수집합니다.
2. `time.sleep()`으로 요청 간격을 두어 서버에 과부하를 주지 않습니다.
3. 저작권이 있는 콘텐츠를 무단으로 수집하지 않습니다.
4. 개인정보를 수집하지 않습니다.
5. 수집한 데이터를 허락 없이 상업적으로 이용하지 않습니다.

**robots.txt의 역할:**
웹사이트 관리자가 수집을 허용/금지하는 영역을 명시한 파일입니다. `https://사이트주소/robots.txt`로 확인할 수 있습니다.

```
User-agent: *
Disallow: /admin/    # 수집 금지
Allow: /public/      # 수집 허용
```

---

**문제 20. 모범답안:**

```
총 2개 상품
노트북: 1,500,000원
마우스: 30,000원
```

`find_all('div', class_='product')`로 2개의 상품 div를 찾고, 각각의 내부에서 `find('h3', class_='name').text`로 상품명, `find('p', class_='price').text`로 가격을 추출합니다.

---

### 🔴 고급

**문제 21. 모범답안:**

**`re.sub(패턴, 대체, 문자열)`**: 패턴에 맞는 부분을 대체 문자열로 **치환**합니다.
**`re.findall(패턴, 문자열)`**: 패턴에 맞는 모든 부분을 리스트로 **추출**합니다.

```python
import re

# 1. "가격: 35,000원" → 숫자만 추출
price_text = "가격: 35,000원"
price = int(re.sub(r'[^0-9]', '', price_text))     # 35000
# re.sub: 숫자가 아닌 문자를 모두 제거

# 2. "평점: 4.5" → 소수점 포함 추출
rating_text = "평점: 4.5"
rating = float(re.findall(r'\d+\.\d+', rating_text)[0])  # 4.5
# re.findall: "숫자.숫자" 패턴을 찾아 리스트로 반환

# 3. "재고: 15개" → 정수 추출
stock_text = "재고: 15개"
stock = int(re.findall(r'\d+', stock_text)[0])      # 15
# re.findall: 연속된 숫자를 찾아 리스트로 반환
```

`re.sub`은 **제거/치환**이 목적이고, `re.findall`은 **패턴 매칭/추출**이 목적입니다.

---

## 💻 실습형 정답

---

### 🟢 초급

**문제 22. 모범답안:**

```python
from bs4 import BeautifulSoup

html = """
<html>
<body>
    <h1>추천 사이트</h1>
    <a href="https://www.python.org">파이썬 공식</a>
    <a href="https://www.github.com">깃허브</a>
    <a href="https://stackoverflow.com">스택오버플로우</a>
    <a href="https://docs.python.org">파이썬 문서</a>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# 모든 링크 찾기
links = soup.find_all('a')

print("=" * 50)
print("🔗 추천 사이트 목록")
print("=" * 50)

for idx, link in enumerate(links, 1):
    text = link.text
    url = link.get('href')
    print(f"[{idx}] {text} → {url}")

print(f"\n총 {len(links)}개의 링크")
```

핵심: `find_all('a')`로 모든 `<a>` 태그를 찾고, `.text`로 텍스트, `.get('href')`로 URL을 추출합니다.

---

**문제 23. 모범답안:**

```python
from bs4 import BeautifulSoup
import re

html = """
<html>
<body>
    <h1>도서 목록</h1>
    <div class="book">
        <h2>파이썬 입문</h2>
        <p class="author">저자: 홍길동</p>
        <p class="price">18,000원</p>
    </div>
    <div class="book">
        <h2>데이터 분석</h2>
        <p class="author">저자: 김데이터</p>
        <p class="price">25,000원</p>
    </div>
    <div class="book">
        <h2>웹 개발</h2>
        <p class="author">저자: 박웹</p>
        <p class="price">22,000원</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
books = soup.find_all('div', class_='book')

print("=" * 40)
print("📚 도서 목록")
print("=" * 40)

prices = []
for idx, book in enumerate(books, 1):
    title = book.find('h2').text
    author = book.find('p', class_='author').text
    price_text = book.find('p', class_='price').text
    price = int(re.sub(r'[^0-9]', '', price_text))
    prices.append(price)

    print(f"\n[{idx}] {title}")
    print(f"    {author}")
    print(f"    가격: {price:,}원")

print(f"\n총 {len(books)}권")
print(f"평균 가격: {sum(prices) // len(prices):,}원")
```

핵심: `re.sub(r'[^0-9]', '', price_text)`로 가격 문자열에서 숫자만 추출합니다.

---

### 🟡 중급

**문제 24. 모범답안:**

```python
from bs4 import BeautifulSoup
import csv

html = """
<html>
<body>
    <h1>오늘의 뉴스</h1>
    <div class="news-item">
        <h2 class="headline">파이썬 4.0 출시 예정</h2>
        <p class="date">2024-03-15</p>
        <p class="summary">파이썬 4.0이 올해 말 출시될 예정입니다.</p>
        <a href="news1.html" class="link">더보기</a>
    </div>
    <div class="news-item">
        <h2 class="headline">AI 로봇 일상 진출</h2>
        <p class="date">2024-03-14</p>
        <p class="summary">AI 로봇이 가정용으로 보급되기 시작했습니다.</p>
        <a href="news2.html" class="link">더보기</a>
    </div>
    <div class="news-item">
        <h2 class="headline">전기차 배터리 혁신</h2>
        <p class="date">2024-03-13</p>
        <p class="summary">새로운 배터리 기술로 주행거리가 2배 늘었습니다.</p>
        <a href="news3.html" class="link">더보기</a>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
news_items = soup.find_all('div', class_='news-item')

print("=" * 60)
print("📰 오늘의 뉴스")
print("=" * 60)

news_data = []
for idx, item in enumerate(news_items, 1):
    headline = item.find('h2', class_='headline').text
    date = item.find('p', class_='date').text
    summary = item.find('p', class_='summary').text
    link = item.find('a', class_='link').get('href')

    print(f"\n[{idx}] {headline}")
    print(f"    날짜: {date}")
    print(f"    요약: {summary}")
    print(f"    링크: {link}")

    news_data.append({
        '번호': idx,
        '헤드라인': headline,
        '날짜': date,
        '요약': summary,
        '링크': link
    })

print(f"\n총 {len(news_items)}개의 뉴스")

# CSV 저장
with open('news_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['번호', '헤드라인', '날짜', '요약', '링크']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(news_data)

print("✓ news_data.csv 저장 완료!")
```

핵심: `find()`로 각 뉴스의 세부 정보를 추출하고, `encoding='utf-8-sig'`로 엑셀 한글 호환 CSV를 저장합니다.

---

**문제 25. 모범답안:**

```python
from bs4 import BeautifulSoup
import csv
import re
from collections import defaultdict

html = """
<html>
<body>
    <h1>전자제품 매장</h1>
    <div class="product">
        <h3 class="name">무선 이어폰</h3>
        <p class="price">89,000원</p>
        <p class="rating">평점: 4.7</p>
        <p class="stock">재고: 25개</p>
        <p class="category">카테고리: 음향기기</p>
    </div>
    <div class="product">
        <h3 class="name">스마트워치</h3>
        <p class="price">250,000원</p>
        <p class="rating">평점: 4.3</p>
        <p class="stock">재고: 8개</p>
        <p class="category">카테고리: 웨어러블</p>
    </div>
    <div class="product">
        <h3 class="name">블루투스 스피커</h3>
        <p class="price">65,000원</p>
        <p class="rating">평점: 4.5</p>
        <p class="stock">재고: 30개</p>
        <p class="category">카테고리: 음향기기</p>
    </div>
    <div class="product">
        <h3 class="name">태블릿</h3>
        <p class="price">450,000원</p>
        <p class="rating">평점: 4.8</p>
        <p class="stock">재고: 3개</p>
        <p class="category">카테고리: 컴퓨터</p>
    </div>
    <div class="product">
        <h3 class="name">보조배터리</h3>
        <p class="price">25,000원</p>
        <p class="rating">평점: 4.1</p>
        <p class="stock">재고: 50개</p>
        <p class="category">카테고리: 액세서리</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
product_items = soup.find_all('div', class_='product')

products = []
for item in product_items:
    name = item.find('h3', class_='name').text
    price = int(re.sub(r'[^0-9]', '', item.find('p', class_='price').text))
    rating = float(re.findall(r'\d+\.\d+', item.find('p', class_='rating').text)[0])
    stock = int(re.findall(r'\d+', item.find('p', class_='stock').text)[0])
    category = item.find('p', class_='category').text.replace('카테고리: ', '')

    products.append({
        '상품명': name, '가격': price, '평점': rating,
        '재고': stock, '카테고리': category
    })

# 1. 상품 목록 출력
print("=" * 60)
print("🛒 상품 목록")
print("=" * 60)
for p in products:
    print(f"\n  {p['상품명']}")
    print(f"    가격: {p['가격']:,}원 | 평점: {p['평점']} | 재고: {p['재고']}개")

# 2. 재고 부족 경고
low_stock = [p for p in products if p['재고'] <= 10]
if low_stock:
    print(f"\n⚠️  재고 부족 경고!")
    for p in low_stock:
        print(f"  {p['상품명']}: {p['재고']}개")

# 3. 카테고리별 통계
print(f"\n📊 카테고리별 통계:")
cat_count = defaultdict(int)
cat_value = defaultdict(int)
for p in products:
    cat_count[p['카테고리']] += 1
    cat_value[p['카테고리']] += p['가격'] * p['재고']

for cat in cat_count:
    print(f"  {cat}: {cat_count[cat]}개 상품 | 재고 가치: {cat_value[cat]:,}원")

# 4. 평점 순 정렬
products.sort(key=lambda x: x['평점'], reverse=True)
print(f"\n⭐ 평점 순위:")
for rank, p in enumerate(products, 1):
    print(f"  {rank}위: {p['상품명']} (평점 {p['평점']})")

# 5. CSV 저장
with open('products_report.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['상품명', '가격', '평점', '재고', '카테고리']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f"\n✓ products_report.csv 저장 완료!")
```

핵심: `re.sub()`과 `re.findall()`로 텍스트에서 숫자를 추출하고, `defaultdict`로 카테고리별 집계합니다.

---

### 🔴 고급

**문제 26. 모범답안:**

```python
from bs4 import BeautifulSoup
import csv
from collections import defaultdict

html = """
<html>
<body>
    <h1>2024학년도 성적표</h1>
    <table class="grade-table">
        <tr class="header">
            <th>이름</th><th>학과</th><th>국어</th><th>영어</th><th>수학</th>
        </tr>
        <tr class="student">
            <td class="name">김철수</td><td class="dept">컴퓨터공학</td>
            <td class="score">85</td><td class="score">90</td><td class="score">78</td>
        </tr>
        <tr class="student">
            <td class="name">박영희</td><td class="dept">컴퓨터공학</td>
            <td class="score">92</td><td class="score">88</td><td class="score">95</td>
        </tr>
        <tr class="student">
            <td class="name">이민수</td><td class="dept">경영학</td>
            <td class="score">78</td><td class="score">85</td><td class="score">82</td>
        </tr>
        <tr class="student">
            <td class="name">최지은</td><td class="dept">경영학</td>
            <td class="score">88</td><td class="score">92</td><td class="score">90</td>
        </tr>
        <tr class="student">
            <td class="name">정민호</td><td class="dept">디자인학</td>
            <td class="score">95</td><td class="score">78</td><td class="score">88</td>
        </tr>
    </table>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# 1. 학생 데이터 추출
students = []
rows = soup.find_all('tr', class_='student')

for row in rows:
    name = row.find('td', class_='name').text
    dept = row.find('td', class_='dept').text
    scores = row.find_all('td', class_='score')
    korean = int(scores[0].text)
    english = int(scores[1].text)
    math = int(scores[2].text)

    students.append({
        '이름': name, '학과': dept,
        '국어': korean, '영어': english, '수학': math
    })

# 2. 평균, 학점 계산
def get_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

for s in students:
    s['평균'] = (s['국어'] + s['영어'] + s['수학']) / 3
    s['학점'] = get_grade(s['평균'])

# 3. 성적 순위표
students.sort(key=lambda x: x['평균'], reverse=True)

print("=" * 70)
print("📋 2024학년도 성적 순위표")
print("=" * 70)
print(f"{'순위':^4} {'이름':^8} {'학과':^10} {'국어':^5} {'영어':^5} {'수학':^5} {'평균':^7} {'학점':^4}")
print("-" * 70)

for rank, s in enumerate(students, 1):
    s['순위'] = rank
    print(f"{rank:^4} {s['이름']:^8} {s['학과']:^10} {s['국어']:^5} {s['영어']:^5} {s['수학']:^5} {s['평균']:^7.1f} {s['학점']:^4}")

# 4. 학과별 통계
print(f"\n📊 학과별 평균 성적:")
dept_avgs = defaultdict(list)
for s in students:
    dept_avgs[s['학과']].append(s['평균'])

for dept, avgs in dept_avgs.items():
    avg = sum(avgs) / len(avgs)
    print(f"  {dept}: {avg:.1f}점 ({len(avgs)}명)")

# 5. 과목별 최고/최저
print(f"\n🏆 과목별 최고점/최저점:")
for subject in ['국어', '영어', '수학']:
    best = max(students, key=lambda x: x[subject])
    worst = min(students, key=lambda x: x[subject])
    print(f"  {subject}: 최고 {best['이름']}({best[subject]}점) | 최저 {worst['이름']}({worst[subject]}점)")

# 6. CSV 저장
with open('grade_report.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['순위', '이름', '학과', '국어', '영어', '수학', '평균', '학점']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for s in students:
        s_copy = s.copy()
        s_copy['평균'] = f"{s['평균']:.1f}"
        writer.writerow(s_copy)

print(f"\n✓ grade_report.csv 저장 완료!")
print("=" * 70)
```

핵심 포인트:

- `<table>` 구조에서 `find_all('tr', class_='student')`로 행을 추출합니다.
- 각 행 내에서 `find_all('td', class_='score')`로 점수 셀들을 리스트로 가져옵니다.
- `defaultdict(list)`로 학과별 평균을 그룹화합니다.
- `max()`, `min()`의 `key` 매개변수로 과목별 최고/최저 학생을 찾습니다.
- CSV 저장 시 평균을 포맷팅(`f"{:.1f}"`)하여 소수점 1자리로 저장합니다.

---


수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 연습문제는 Claude 및 Gemini와 협업으로 제작되었습니다.
