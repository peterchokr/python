# Chapter 24. 웹 스크래핑

---

## 📚 학습 목표 (Learning Objectives)

이번 장을 마치면 여러분은 웹 스크래핑 기술을 활용하여 웹사이트에서 데이터를 자동으로 수집할 수 있습니다. 뉴스 기사, 상품 정보, 날씨 등 다양한 웹 데이터를 파이썬으로 추출하고 분석할 수 있게 됩니다.

---

## 1️⃣ 웹 스크래핑이란?

웹 스크래핑(Web Scraping)은 웹사이트에서 데이터를 자동으로 수집하는 기술입니다. 수작업으로 정보를 복사하고 붙여넣는 대신, 프로그램을 이용해 훨씬 더 효율적이고 정확하게 데이터를 추출할 수 있습니다.

### 웹 스크래핑이 왜 필요할까?

수작업으로 데이터를 수집하려면 각 웹사이트를 방문하고, 정보를 찾아 복사해서 스프레드시트에 붙여넣는 작업을 반복해야 합니다. 이것은 매우 시간이 오래 걸리고 실수하기 쉽습니다. 웹 스크래핑을 사용하면 이 전체 과정을 자동화하여 몇 초 안에 수백 개 또는 수천 개의 항목을 완벽한 정확도로 수집할 수 있습니다.

```
수작업으로 데이터 수집           웹 스크래핑
━━━━━━━━━━━━━━━━━━━━━━━━━     ━━━━━━━━━━━━━━━━━━━━━━━━━
1. 웹사이트 접속               1. 파이썬 실행
2. 상품 정보 복사              2. 커피 한 잔 ☕
3. 엑셀에 붙여넣기             3. 데이터 수집 완료!
4. 다음 페이지 이동
5. 반복... (100개 상품)        시간: 몇 초
시간: 몇 시간 😫               정확도: 100% ✅
정확도: 실수 가능 ❌
```

### 실생활 활용 예시

웹 스크래핑은 다양한 산업에서 많은 실용적인 응용 분야가 있습니다. 웹 스크래핑이 실제로 큰 역할을 하는 몇 가지 일반적인 사용 사례를 살펴봅시다.

```
🛒 쇼핑
- 상품 가격 비교
- 재고 확인
- 리뷰 분석

📰 뉴스/정보
- 뉴스 헤드라인 수집
- 날씨 정보
- 환율 정보

📊 데이터 분석
- 부동산 시세
- 주식 정보
- SNS 트렌드
```

쇼핑과 전자상거래 분야에서는 여러 상점의 상품 가격을 비교하고, 재고 가용성을 모니터링하고, 고객 리뷰를 분석할 수 있습니다. 뉴스와 정보 분야에서는 뉴스 헤드라인과 기사를 수집하고, 날씨를 추적하고, 환율을 모니터링할 수 있습니다. 데이터 분석 및 연구 분야에서는 부동산 가격을 추적하고, 주식 정보를 모니터링하고, 소셜 미디어 트렌드를 분석할 수 있습니다.

### 웹 스크래핑 vs 웹 크롤링

웹 스크래핑과 웹 크롤링의 차이를 이해하는 것이 중요합니다. 이 두 용어가 때때로 혼용되기도 합니다. 웹 스크래핑은 하나 또는 여러 웹페이지에서 특정 데이터(가격, 제목 등)를 추출하는 것에 초점을 맞춥니다. 반면 웹 크롤링은 검색 엔진처럼 웹사이트 전체를 체계적으로 탐색하고 링크를 따라가며 인덱싱하는 광범위한 프로세스입니다.

---

## 2️⃣ 라이브러리 설치

파이썬에서 웹 스크래핑을 하려면 두 가지 필수 라이브러리를 설치해야 합니다. 이 라이브러리들은 웹페이지 다운로드와 콘텐츠 파싱의 기술적 측면을 처리합니다. 터미널이나 명령 프롬프트를 열고 다음 설치 명령어를 실행하세요.

```bash
pip install requests
pip install beautifulsoup4
```

### 라이브러리 역할

설치 후에는 파이썬 스크립트에서 이 라이브러리들을 임포트할 수 있습니다:

```python
import requests              # 웹페이지 다운로드
from bs4 import BeautifulSoup  # HTML 분석하기
```

**requests 라이브러리**: 이 라이브러리는 인터넷에서 웹페이지를 다운로드하는 역할을 합니다. 웹 서버와의 통신을 처리하고 HTML 콘텐츠를 반환합니다. URL을 제공하면 requests가 페이지 콘텐츠를 검색합니다. 또한 응답 상태 코드, 헤더 및 기타 HTTP 관련 정보를 관리합니다.

**BeautifulSoup 라이브러리**: 이 라이브러리는 HTML 콘텐츠를 파싱하고 분석합니다. 웹페이지의 HTML을 얻으면 BeautifulSoup은 구조를 탐색하고 특정 요소를 추출하는 데 도움을 줍니다. 태그를 찾고, 텍스트를 추출하고, 속성에 접근하는 편리한 메서드들을 제공합니다.

---

## 3️⃣ HTML 기초 이해

웹페이지는 HTML(Hypertext Markup Language)로 만들어져 있으며, 이는 태그와 요소를 사용하여 콘텐츠를 구조화하는 마크업 언어입니다. 웹 스크래핑을 효과적으로 하려면 HTML이 어떻게 조직되어 있는지 이해해야 합니다. 구조를 이해하면 필요한 특정 정보를 식별하고 추출하는 방법을 알게 됩니다.

### HTML의 기본 구조

일반적인 HTML 문서는 표준 구조를 가집니다. `<html>` 태그는 모든 것을 포함하는 루트 요소입니다. 그 안에는 `<head>`와 `<body>` 섹션이 있습니다. head는 페이지 제목과 같은 메타데이터를 포함하고, body는 사용자가 볼 수 있는 시각적 콘텐츠를 포함합니다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>Large Heading</h1>
    <p>Paragraph content</p>
    <a href="https://example.com">Link</a>
    <img src="image.jpg">
</body>
</html>
```

### 주요 HTML 태그

HTML은 태그를 사용하여 콘텐츠를 표시합니다. 각 태그는 시작 태그, 콘텐츠, 종료 태그로 구성됩니다. 시작 태그는 `<`, 태그 이름, `>`으로 끝납니다. 종료 태그는 비슷하지만 태그 이름 앞에 슬래시가 포함됩니다.

```

```

태그 구조는 다음과 같습니다:

```
<태그이름>내용</태그이름>
   ↑      ↑       ↑
시작태그 내용  종료태그

예시:
<h1>제목입니다</h1>
<p>문단입니다</p>
<a href="url">링크</a>
```

### 자주 사용하는 태그

웹사이트를 스크래핑할 때 다양한 HTML 태그를 접하게 됩니다. 다음은 알아야 할 가장 일반적인 것들입니다:

- `<h1>` ~ `<h6>`: 다양한 수준의 제목
- `<p>`: 문단
- `<a>`: 링크, href 속성을 통해 접근
- `<img>`: 이미지, src 속성을 통해 접근
- `<div>`: 요소를 그룹화하기 위한 컨테이너
- `<span>`: 텍스트 스타일링을 위한 인라인 요소
- `<ul>`, `<li>`: 비정렬 목록과 목록 항목

### 클래스와 ID

HTML 요소들은 class와 id 속성을 사용하여 식별하고 스타일을 지정할 수 있습니다. 이 속성들은 웹 스크래핑에서 특정 요소를 정확하게 대상으로 삼는 데 도움이 되므로 매우 중요합니다. class 속성은 여러 요소가 공유할 수 있어서 유사한 항목을 그룹화하는 데 유용합니다. id 속성은 페이지 내에서 고유해야 하므로 단일의 특정 요소를 식별하는 데 유용합니다.

```html
<div class="product">Product Item</div>
<div id="main">Main Content</div>
```

---

## 4️⃣ 첫 번째 웹 스크래핑

이제 HTML의 기본을 이해했으니, 간단한 HTML 파일을 사용하여 실습 프로젝트를 시작합시다. 이 방식은 실제 웹사이트로 작업하는 것보다 좋습니다. HTML 구조를 제어할 수 있고 네트워크 문제나 변경되는 웹사이트 구조를 걱정하지 않으면서 스크래핑 기술에 집중할 수 있기 때문입니다.

### 실습용 HTML 파일 만들기

텍스트 편집기를 열고 파일을 만드세요. 다음 HTML 코드를 복사하여 `sample.html`로 저장하세요. 이것이 우리의 연습 데이터셋이 될 것입니다.

**sample.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Web Scraping Practice</title>
</head>
<body>
    <h1>Python Book List</h1>
  
    <div class="book">
        <h2>Python Basics</h2>
        <p class="author">Author: Kim Chulsu</p>
        <p class="price">Price: 20,000 won</p>
    </div>
  
    <div class="book">
        <h2>Advanced Python</h2>
        <p class="author">Author: Park Young-hee</p>
        <p class="price">Price: 25,000 won</p>
    </div>
  
    <div class="book">
        <h2>Data Analysis</h2>
        <p class="author">Author: Lee Min-su</p>
        <p class="price">Price: 30,000 won</p>
    </div>
</body>
</html>
```

### HTML 파일 읽고 파싱하기

이제 HTML 파일을 읽고 BeautifulSoup을 사용하여 파싱해야 합니다. HTML 파일을 읽으면 문자열이 됩니다. BeautifulSoup은 그 문자열을 구조화된 객체로 변환하여 탐색하고 검색할 수 있게 합니다.

```python
from bs4 import BeautifulSoup

# Read HTML file (HTML 파일 읽기)
with open('sample.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Create BeautifulSoup object (BeautifulSoup 객체 생성)
soup = BeautifulSoup(html, 'html.parser')

# Get heading (제목 가져오기)
title = soup.find('h1')
print(title.text)  # Python Book List
```

**실행 결과:**

```
Python Book List
```

---

## 5️⃣ 태그 찾기

BeautifulSoup은 HTML 요소를 찾고 탐색하기 위한 여러 강력한 메서드를 제공합니다. 이 메서드들은 웹 스크래핑의 기초입니다. `find()`와 `find_all()`을 올바르게 사용하는 방법을 이해하면 HTML에서 모든 데이터를 추출할 수 있습니다.

### find() - 첫 번째 하나만

`find()` 메서드는 기준과 일치하는 첫 번째 요소를 검색하여 반환합니다. 일치하는 것이 없으면 None을 반환합니다. 페이지 제목이나 단일 특집 상품과 같이 페이지의 특정 고유 요소를 찾을 때 유용합니다.

```python
from bs4 import BeautifulSoup

with open('sample.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# 첫 번째 h2 태그 찾기
first_book = soup.find('h2')
print(first_book.text)  # Python Basics

# 첫 번째 .author 클래스 찾기
first_author = soup.find(class_='author')
print(first_author.text)  # Author: Kim Chulsu
```

⚠️ **중요**: `class`는 파이썬 예약어이므로, BeautifulSoup에서는 충돌을 피하기 위해 `class_='클래스명'` 문법을 사용합니다. 'class' 다음의 언더스코어에 주목하세요.

### find_all() - 모두 찾기

`find_all()` 메서드는 기준과 일치하는 모든 요소를 찾아 리스트로 반환합니다. 이것은 웹 스크래핑에서 가장 일반적인 메서드입니다. 왜냐하면 일반적으로 카테고리의 모든 상품이나 뉴스 페이지의 모든 기사와 같이 페이지에서 같은 타입의 여러 항목을 추출하기를 원하기 때문입니다.

```python
from bs4 import BeautifulSoup

with open('sample.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# 모든 h2 태그 찾기
all_books = soup.find_all('h2')
for book in all_books:
    print(book.text)
```

**실행 결과:**

```
Python Basics
Advanced Python
Data Analysis
```

### 클래스로 찾기

클래스 이름을 사용하여 요소를 검색할 수 있습니다. 이것은 개발자들이 관련 요소들을 그룹화하기 위해 자주 class 속성을 사용하므로 매우 실용적입니다. class로 검색하면 HTML 전체에 산재되어 있더라도 특정 타입의 모든 항목을 쉽게 추출할 수 있습니다.

```python
from bs4 import BeautifulSoup

with open('sample.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# book 클래스를 가진 모든 div 찾기
books = soup.find_all('div', class_='book')

print(f"Total: {len(books)} books")

for book in books:
    title = book.find('h2').text
    author = book.find(class_='author').text
    price = book.find(class_='price').text
  
    print(f"\nTitle: {title}")
    print(f"{author}")
    print(f"{price}")
```

**실행 결과:**

```
Total: 3 books

Title: Python Basics
Author: Kim Chulsu
Price: 20,000 won

Title: Advanced Python
Author: Park Young-hee
Price: 25,000 won

Title: Data Analysis
Author: Lee Min-su
Price: 30,000 won
```

---

## 6️⃣ 속성 가져오기

HTML 요소들은 종종 중요한 정보를 포함하는 속성을 가집니다. 예를 들어, `<a>` 태그는 URL을 포함하는 `href` 속성을 가지고, `<img>` 태그는 이미지 파일을 가리키는 `src` 속성을 가집니다. 이 속성들을 추출하는 것을 배우는 것이 필수적입니다. 왜냐하면 웹 스크래핑의 많은 유용한 데이터는 요소의 텍스트 콘텐츠보다는 속성에서 나오기 때문입니다.

### 실습용 HTML 파일 만들기

링크와 이미지가 있는 `links.html`라는 새 파일을 만드세요:

**links.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Link Collection</title>
</head>
<body>
    <h1>Useful Websites</h1>
  
    <a href="https://www.python.org">Official Python Site</a>
    <a href="https://www.github.com">GitHub</a>
    <a href="https://stackoverflow.com">Stack Overflow</a>
  
    <h2>Images</h2>
    <img src="logo.png" alt="Logo">
</body>
</html>
```

### 링크 추출하기

웹페이지에서 링크를 추출하려면 모든 `<a>` 태그를 찾고 `href` 속성에 접근합니다. `.get()` 메서드는 속성 값을 검색하거나 `.['href']`와 같은 대괄호 표기법을 사용할 수 있습니다. `.get()` 메서드는 속성이 없을 때 오류를 발생시키지 않고 None을 반환하므로 더 안전합니다.

```python
from bs4 import BeautifulSoup

with open('links.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# 모든 링크 찾기
links = soup.find_all('a')

print("Website List:")
print("=" * 50)

for link in links:
    text = link.text
    url = link.get('href')  # Or use link['href']
    print(f"{text}: {url}")
```

**실행 결과:**

```
Website List:
==================================================
Official Python Site: https://www.python.org
GitHub: https://www.github.com
Stack Overflow: https://stackoverflow.com
```

### 이미지 정보 추출하기

링크를 추출하는 것과 유사하게, 모든 `<img>` 태그를 찾고 속성에 접근하여 이미지 정보를 추출할 수 있습니다. `src` 속성은 이미지 파일 경로를 포함하고, `alt` 속성은 설명 텍스트를 포함합니다. 이들은 이미지를 조직하거나 이미지 갤러리를 구축하는 데 유용합니다.

```python
from bs4 import BeautifulSoup

with open('links.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# 모든 이미지 찾기
images = soup.find_all('img')

for img in images:
    src = img.get('src')
    alt = img.get('alt')
    print(f"Image: {src}")
    print(f"Description: {alt}")
```

---

## 7️⃣실제 웹사이트 스크래핑

이제 로컬 HTML 파일로 기본을 마스터했으니, 인터넷의 실제 웹사이트를 스크래핑하는 것으로 넘어갈 수 있습니다. 프로세스는 유사하지만, 파일을 읽는 대신 requests 라이브러리를 사용하여 웹페이지를 다운로드합니다. 그 후 이전과 마찬가지로 HTML을 파싱합니다.

### 웹페이지 다운로드

requests 라이브러리는 웹페이지를 다운로드하는 것을 매우 간단하게 만듭니다. URL을 제공하면 페이지 콘텐츠와 상태 코드와 같은 응답에 대한 메타데이터를 반환합니다. 상태 코드는 요청이 성공했는지 또는 오류가 있었는지 알려줍니다. 상태 코드 200은 성공을 의미합니다.

```python
import requests
from bs4 import BeautifulSoup

# 웹페이지 가져오기
url = "https://example.com"
response = requests.get(url)

# 응답 확인
if response.status_code == 200:
    print("✓ Web page downloaded successfully!")
    html = response.text
  
    # HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')
  
    # 제목 가져오기
    title = soup.find('h1')
    if title:
        print(f"Title: {title.text}")
else:
    print(f"❌ Error: {response.status_code}")
```

**HTTP 상태 코드:**

상태 코드를 이해하는 것은 웹 스크래핑 문제를 디버깅하는 데 중요합니다:

- **200**: 성공 - 페이지가 성공적으로 검색됨
- **404**: 찾을 수 없음 - URL이 존재하지 않음
- **403**: 금지됨 - 이 페이지에 접근할 권한이 없음
- **500**: 서버 오류 - 웹 서버에 오류 발생

### Setting User-Agent Headers (User-Agent 설정)

일부 웹사이트는 자동화된 접근을 방지하기 위해 프로그램의 요청을 차단합니다. 이를 해결하려면 파이썬 프로그램을 일반 웹 브라우저처럼 보이게 하는 User-Agent 헤더를 설정할 수 있습니다. 이것은 일반적이고 정당한 관행이지만, 항상 웹사이트의 이용약관을 존중해야 합니다.

```python
import requests

url = "https://example.com"

# User-Agent 헤더 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)
print(response.status_code)
```

---

## 8️⃣ 실전 예제: 뉴스 헤드라인 수집

이제 웹사이트에서 뉴스 헤드라인을 수집하는 완전한 실전 예제를 살펴봅시다. 이 예제는 다운로드부터 파싱까지 데이터 저장까지의 전체 웹 스크래핑 워크플로우를 보여줍니다.

### 실습용 HTML 파일 만들기

먼저 뉴스 웹사이트를 시뮬레이션하는 `news.html` 파일을 만드세요:

**news.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>News Site</title>
</head>
<body>
    <h1>Today's News</h1>
  
    <div class="news-item">
        <h2 class="headline">Python Ranked Most Popular Programming Language</h2>
        <p class="date">2024-01-15</p>
        <p class="summary">Python topped the 2024 developer survey, beating Java and JavaScript.</p>
        <a href="news1.html" class="more">Read More</a>
    </div>
  
    <div class="news-item">
        <h2 class="headline">AI Technology Revolutionizes Medical Field</h2>
        <p class="date">2024-01-14</p>
        <p class="summary">Artificial intelligence significantly improves disease diagnosis accuracy.</p>
        <a href="news2.html" class="more">Read More</a>
    </div>
  
    <div class="news-item">
        <h2 class="headline">Electric Vehicle Market Projected to Grow 30% This Year</h2>
        <p class="date">2024-01-13</p>
        <p class="summary">Global electric vehicle sales are expected to increase significantly.</p>
        <a href="news3.html" class="more">Read More</a>
    </div>
</body>
</html>
```

### 헤드라인 스크래핑

이제 헤드라인 정보를 추출하는 파이썬 스크립트를 작성하세요. 이 스크립트는 여러 뉴스 항목을 찾고, 각각에서 데이터를 추출하고, 구조화된 방식으로 정리하는 방법을 보여줍니다.

```python
from bs4 import BeautifulSoup

# Read HTML file (HTML 파일 읽기)
with open('news.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all news items (모든 뉴스 항목 찾기)
news_items = soup.find_all('div', class_='news-item')

print("=" * 70)
print("📰 News Headlines")
print("=" * 70)

for i, item in enumerate(news_items, 1):
    headline = item.find('h2', class_='headline').text
    date = item.find('p', class_='date').text
    summary = item.find('p', class_='summary').text
    link = item.find('a', class_='more').get('href')
  
    print(f"\n[{i}] {headline}")
    print(f"    Date: {date}")
    print(f"    Summary: {summary}")
    print(f"    Link: {link}")

print("\n" + "=" * 70)
```

**실행 결과:**

```
======================================================================
📰 News Headlines
======================================================================

[1] Python Ranked Most Popular Programming Language
    Date: 2024-01-15
    Summary: Python topped the 2024 developer survey, beating Java and JavaScript.
    Link: news1.html

[2] AI Technology Revolutionizes Medical Field
    Date: 2024-01-14
    Summary: Artificial intelligence significantly improves disease diagnosis accuracy.
    Link: news2.html

[3] Electric Vehicle Market Projected to Grow 30% This Year
    Date: 2024-01-13
    Summary: Global electric vehicle sales are expected to increase significantly.
    Link: news3.html

======================================================================
```

### CSV 파일로 저장

데이터를 더 유용하게 만들기 위해 파일로 저장해야 합니다. CSV(Comma-Separated Values)는 표 형식 데이터를 저장하는 일반적인 형식입니다. 다음 스크립트는 뉴스 데이터를 스크래핑하여 Excel 또는 다른 스프레드시트 애플리케이션에서 열 수 있는 CSV 파일로 저장합니다.

```python
from bs4 import BeautifulSoup
import csv

# Read HTML file (HTML 파일 읽기)
with open('news.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Collect news data (뉴스 데이터 수집)
news_data = []
news_items = soup.find_all('div', class_='news-item')

for item in news_items:
    headline = item.find('h2', class_='headline').text
    date = item.find('p', class_='date').text
    summary = item.find('p', class_='summary').text
  
    news_data.append({
        'Headline': headline,
        'Date': date,
        'Summary': summary
    })

# Save to CSV file (CSV 파일로 저장)
with open('news_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    fieldnames = ['Headline', 'Date', 'Summary']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
  
    csv_writer.writeheader()
    csv_writer.writerows(news_data)

print(f"✓ {len(news_data)} news articles saved to news_data.csv!")
```

⚠️ **인코딩에 대한 주의**: `encoding='utf-8-sig'` 매개변수는 한글 텍스트를 다룰 때 중요합니다. CSV 파일이 Excel에서 문자가 깨지지 않고 올바르게 표시되도록 보장합니다.

---

## 9️⃣ 실전 예제: 상품 정보 수집

전자상거래에서 흔히 사용되는 또 다른 실전 예제인 상품 정보 수집을 살펴봅시다. 이 예제는 숫자 데이터를 추출하고 스크래핑된 데이터에 대해 기본 계산을 수행하는 방법을 보여줍니다.

### 실습용 HTML 파일

상품 정보를 포함하는 `products.html` 파일을 만드세요:

**products.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Product List</title>
</head>
<body>
    <h1>Computer Products</h1>
  
    <div class="product">
        <h3 class="name">Wireless Mouse</h3>
        <p class="price">35,000 won</p>
        <p class="rating">⭐⭐⭐⭐⭐ (4.5)</p>
        <p class="stock">Stock: 15 items</p>
    </div>
  
    <div class="product">
        <h3 class="name">Mechanical Keyboard</h3>
        <p class="price">120,000 won</p>
        <p class="rating">⭐⭐⭐⭐ (4.2)</p>
        <p class="stock">Stock: 8 items</p>
    </div>
  
    <div class="product">
        <h3 class="name">27-inch Monitor</h3>
        <p class="price">350,000 won</p>
        <p class="rating">⭐⭐⭐⭐⭐ (4.8)</p>
        <p class="stock">Stock: 3 items</p>
    </div>
  
    <div class="product">
        <h3 class="name">Webcam</h3>
        <p class="price">80,000 won</p>
        <p class="rating">⭐⭐⭐⭐ (4.0)</p>
        <p class="stock">Stock: 20 items</p>
    </div>
</body>
</html>
```

### 상품 정보 스크래핑

이 스크립트는 텍스트에서 숫자를 추출하고 계산을 수행하는 더 복잡한 스크래핑 작업을 보여줍니다. 정규표현식을 사용하여 텍스트에서 숫자 값만 추출합니다.

```python
from bs4 import BeautifulSoup
import csv
import re

# Read HTML file (HTML 파일 읽기)
with open('products.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Collect product information (상품 정보 수집)
products = []
product_items = soup.find_all('div', class_='product')

print("=" * 70)
print("🛒 Product Information")
print("=" * 70)

for item in product_items:
    name = item.find('h3', class_='name').text
    price_text = item.find('p', class_='price').text
    rating_text = item.find('p', class_='rating').text
    stock_text = item.find('p', class_='stock').text
  
    # Extract numbers only (숫자만 추출)
    price = int(re.sub(r'[^0-9]', '', price_text))
    rating = float(re.findall(r'\d+\.\d+', rating_text)[0])
    stock = int(re.findall(r'\d+', stock_text)[0])
  
    products.append({
        'Product Name': name,
        'Price': price,
        'Rating': rating,
        'Stock': stock
    })
  
    print(f"\nProduct: {name}")
    print(f"Price: {price:,} won")
    print(f"Rating: {rating}")
    print(f"Stock: {stock} items")
  
    # Warn about low stock (재고 부족 경고)
    if stock < 10:
        print("⚠️  Low Stock!")

# Save to CSV file (CSV 파일로 저장)
with open('products_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    fieldnames = ['Product Name', 'Price', 'Rating', 'Stock']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
  
    csv_writer.writeheader()
    csv_writer.writerows(products)

print("\n" + "=" * 70)
print(f"✓ {len(products)} products saved to products_data.csv!")

# Statistics (통계)
total_value = sum(p['Price'] * p['Stock'] for p in products)
avg_rating = sum(p['Rating'] for p in products) / len(products)

print(f"\n📊 Statistics:")
print(f"Total Inventory Value: {total_value:,} won")
print(f"Average Rating: {avg_rating:.2f}")
```

---

## 🔟 웹 스크래핑 윤리와 법

웹 스크래핑은 강력한 도구이지만, 다른 강력한 도구처럼 책임감 있게 사용해야 합니다. 웹사이트를 스크래핑하기 전에 이해해야 할 법적 및 윤리적 고려사항이 있습니다. 뭔가를 스크래핑할 수 있다는 것이 반드시 해야 한다는 뜻은 아니라는 것을 항상 기억하세요.

### ⚠️ 주의사항

**✅ 해도 되는 것:**

- 공개된 정보 수집
- robots.txt를 따르고 웹사이트의 스크래핑 정책 존중
- 서버 부담을 주지 않도록 요청 사이에 적절한 지연 사용
- 개인 프로젝트와 학습 목적으로 스크래핑 데이터 사용

**❌ 하면 안 되는 것:**

- 저작권이 있는 콘텐츠 무단 수집
- 개인정보 수집
- 서버에 부하를 주는 대량 요청
- 로그인이 필요한 정보 무단 수집
- 수집한 데이터를 허락 없이 상업적 이용

### robots.txt 확인

모든 웹사이트는 웹사이트의 어느 부분을 스크래핑할 수 있는지 지정하는 `robots.txt` 파일을 가질 수 있습니다. 스크래핑 전에 항상 이 파일을 확인하세요. robots.txt 파일은 웹사이트의 루트에 위치합니다.

```
https://example.com/robots.txt

User-agent: *
Disallow: /admin/        # 수집 금지
Disallow: /private/      # 수집 금지
Allow: /public/          # 수집 허용
```

### 요청 간격 설정

여러 페이지를 스크래핑할 때 항상 요청 사이에 지연을 포함하세요. 이것은 예의이자 필요합니다. 짧은 시간에 너무 많은 요청을 하면 다른 사용자의 웹사이트 속도를 낮추거나 서버를 다운시킬 수도 있습니다.

```python
import requests
import time

urls = ['url1', 'url2', 'url3']

for url in urls:
    response = requests.get(url)
    # Process data... (데이터 처리...)
  
    time.sleep(2)  # 요청 사이 2초 대기
```

### 법적 책임

웹 스크래핑 자체는 불법이 아닙니다. 하지만 스크래핑한 데이터를 사용하는 방식이 불법일 수 있습니다. 웹사이트의 이용약관이 중요하므로, 스크래핑 전에 항상 주의 깊게 읽으세요. 확신이 없으면 웹사이트 소유자에게 허락을 구하세요.

- 웹 스크래핑 자체는 불법이 아닙니다
- 하지만 데이터 사용 방식이 문제가 될 수 있습니다
- 상업적 이용 전 반드시 웹사이트 이용약관 확인
- 스크래핑 데이터를 개인 학습용으로만 사용하세요

---

## 📝 핵심 개념 정리

웹 스크래핑의 기본 워크플로우를 이해하면 모든 웹사이트에 이를 적용할 수 있습니다. 추출하려는 데이터가 무엇이든 기본 프로세스는 항상 동일합니다.

### 기본 구조

웹 스크래핑 프로세스는 다음 네 가지 필수 단계를 따릅니다:

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Download the web page (단계 1: 웹페이지 다운로드)
response = requests.get(url)
html = response.text

# Step 2: Parse HTML (단계 2: HTML 파싱)
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Find desired elements (단계 3: 원하는 요소 찾기)
elements = soup.find_all('tag', class_='classname')

# Step 4: Extract data (단계 4: 데이터 추출)
for element in elements:
    text = element.text
    link = element.get('href')
```

### 주요 메서드

웹 스크래핑에 필요한 필수 메서드들입니다:

- **`find()`**: 첫 번째 일치하는 요소 찾기
- **`find_all()`**: 모든 일치하는 요소를 찾고 리스트 반환
- **`.text`**: 요소의 텍스트 콘텐츠 추출
- **`.get('attribute')`**: 특정 속성의 값 가져오기

### 주의사항

스크래핑할 때 이 주요 사항들을 기억하세요:

- 스크래핑 전 robots.txt 확인
- 요청 사이에 적절한 지연 설정
- 프로그램을 식별하기 위해 User-Agent 헤더 설정
- 항상 try-except 블록으로 예외 처리

---

## 💡실습 과제

### 과제 1: 도서 목록 수집기

**목표**: HTML 파일에서 도서 정보를 수집하여 CSV 파일로 저장하세요.

**1단계: 샘플 데이터 준비**

`books.html` 파일을 만드세요:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Book List</title>
</head>
<body>
    <h1>Programming Books</h1>
  
    <div class="book">
        <h3 class="title">Python Complete Guide</h3>
        <p class="author">Author: Kim Python</p>
        <p class="publisher">Publisher: Coding Press</p>
        <p class="price">28,000 won</p>
        <p class="pages">450 pages</p>
    </div>
  
    <div class="book">
        <h3 class="title">JavaScript Basics</h3>
        <p class="author">Author: Lee JavaScript</p>
        <p class="publisher">Publisher: Web Development Press</p>
        <p class="price">25,000 won</p>
        <p class="pages">380 pages</p>
    </div>
  
    <div class="book">
        <h3 class="title">Data Science Introduction</h3>
        <p class="author">Author: Park Data</p>
        <p class="publisher">Publisher: AI Press</p>
        <p class="price">32,000 won</p>
        <p class="pages">520 pages</p>
    </div>
</body>
</html>
```

**2단계: 요구사항**

1. Extract all book information (title, author, publisher, price, page count)
2. Extract numbers from price and pages fields
3. Display book information in table format on console
4. Save to `books_data.csv`

**3단계: 예상 출력**

```
======================================================================
📚 Book List
======================================================================

[1] Python Complete Guide
    Author: Kim Python
    Publisher: Coding Press
    Price: 28,000 won
    Pages: 450 pages

[2] JavaScript Basics
    Author: Lee JavaScript
    Publisher: Web Development Press
    Price: 25,000 won
    Pages: 380 pages

[3] Data Science Introduction
    Author: Park Data
    Publisher: AI Press
    Price: 32,000 won
    Pages: 520 pages

======================================================================
Total 3 books

✓ Saved to books_data.csv!
```

---

### 과제 2: 날씨 정보 수집기

**목표**: HTML 파일에서 주간 날씨 정보를 수집하여 통계 계산을 수행하세요.

**1단계: 샘플 데이터 준비**

`weather.html` 파일을 만드세요:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Weekly Weather</title>
</head>
<body>
    <h1>Seoul Weekly Weather</h1>
  
    <div class="day">
        <p class="date">2024-01-15 (Monday)</p>
        <p class="weather">Clear</p>
        <p class="temp">High 5°C / Low -2°C</p>
        <p class="humidity">Humidity: 45%</p>
    </div>
  
    <div class="day">
        <p class="date">2024-01-16 (Tuesday)</p>
        <p class="weather">Cloudy</p>
        <p class="temp">High 3°C / Low -4°C</p>
        <p class="humidity">Humidity: 60%</p>
    </div>
  
    <div class="day">
        <p class="date">2024-01-17 (Wednesday)</p>
        <p class="weather">Snow</p>
        <p class="temp">High 0°C / Low -6°C</p>
        <p class="humidity">Humidity: 75%</p>
    </div>
  
    <div class="day">
        <p class="date">2024-01-18 (Thursday)</p>
        <p class="weather">Clear</p>
        <p class="temp">High 6°C / Low -1°C</p>
        <p class="humidity">Humidity: 40%</p>
    </div>
</body>
</html>
```

**2단계: 요구사항**

1. Extract all weather information (date, weekday, weather, high/low temp, humidity)
2. Extract numbers from temperature and humidity fields
3. Calculate weekly average temperature
4. Calculate weather statistics by type
5. Save to `weather_data.csv`

**3단계: 예상 출력**

```
======================================================================
🌤️  Seoul Weekly Weather
======================================================================

[Monday] 2024-01-15
  Weather: Clear
  Temperature: High 5°C / Low -2°C
  Humidity: 45%

[Tuesday] 2024-01-16
  Weather: Cloudy
  Temperature: High 3°C / Low -4°C
  Humidity: 60%

...

======================================================================
📊 Weekly Statistics

Average High Temperature: 3.5°C
Average Low Temperature: -3.2°C
Average Humidity: 55.0%

Weather by Type:
  Clear: 2 days
  Cloudy: 1 day
  Snow: 1 day

✓ Saved to weather_data.csv!
```

---

## ✅ 퀴즈

### [초급] 1번

웹페이지를 가져오는 라이브러리는?

1. BeautifulSoup
2. requests
3. csv
4. pandas

### [중급] 2번

HTML을 파싱하는 라이브러리는?

1. requests
2. csv
3. BeautifulSoup
4. json

### [중급] 3번

Which method finds only the first matching element?

find_all()

1. find()
2. search()
3. locate()

### [고급]  4번

요소의 속성 값을 가져오는 메서드는?

1. get_attr()
2. attr()
3. get()
4. ['attribute']

### [고급] 5번

요청 사이에 지연을 추가하는 함수는?

1. time.wait()
2. time.delay()
3. time.sleep()
4. time.pause()

---

## 🔑 퀴즈 정답 및 해설

**1번 정답: 2**

requests 라이브러리는 웹사이트에서 콘텐츠를 다운로드하기 위해 특별히 설계되었습니다. `response = requests.get(url)`을 사용하여 웹페이지의 HTML 콘텐츠를 검색합니다.

**2번 정답: 3**

BeautifulSoup은 HTML 구조를 파싱하고 분석하기 위한 라이브러리입니다. HTML을 탐색하고 특정 요소와 데이터를 추출할 수 있습니다.

**3번 정답: 2**

`find()` 메서드는 검색 기준과 일치하는 첫 번째 요소만 반환합니다. 모든 일치하는 요소가 필요하면 대신 `find_all()`을 사용하세요.

**4번 정답: 3**

`get()` 메서드는 요소의 속성 값을 검색합니다. 예를 들어, `link.get('href')`는 `<a>` 태그에서 URL을 가져옵니다. 대괄호 표기법도 사용할 수 있습니다: `link['href']`.

**5번 정답: 3**

`time.sleep()` 함수는 프로그램을 지정된 시간(초)만큼 일시 중지합니다. 이것은 너무 많은 빠른 요청으로 서버에 부하를 주지 않도록 하기 위해 책임감 있는 웹 스크래핑에 필수입니다.

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
