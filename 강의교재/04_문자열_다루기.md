# 4장 문자열 다루기

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 문자열을 생성하고, 접근하고, 조작하는 다양한 방법을 익히게 됩니다. 문자열은 프로그래밍에서 가장 많이 다루는 데이터 타입 중 하나이므로, 이를 효과적으로 다루는 방법을 배우는 것은 매우 중요합니다.

---

## 1️⃣ **문자열 생성과 특징**

문자열(String)은 문자들의 연속된 나열입니다. 파이썬에서 문자열은 큰따옴표(`"`) 또는 작은따옴표(`'`)로 감싸서 만듭니다. 두 방법은 기능적으로 동일하지만, 문자열 내부에 따옴표를 포함할 때는 구분해서 사용할 수 있습니다.

```python
# 다양한 문자열 생성 방법
name1 = "홍길동"
name2 = '김영희'
message = "Hello, World!"
empty = ""  # 빈 문자열

# 문자열 안에 따옴표 포함
sentence1 = "He said, 'Hello!'"
sentence2 = 'She replied, "Goodbye!"'

print(sentence1)  # He said, 'Hello!'
print(sentence2)  # She replied, "Goodbye!"
```

### **여러 줄 문자열**

여러 줄에 걸친 긴 문자열을 만들 때는 삼중 따옴표(`"""` 또는 `'''`)를 사용합니다. 이는 주로 긴 텍스트나 문서를 저장할 때 유용합니다.

```python
# 여러 줄 문자열
poem = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한 사람 대한으로 길이 보전하세
"""

print(poem)

# 코드 내 긴 설명문
description = '''
이 프로그램은 학생 성적을 관리하는 시스템입니다.
기능: 성적 입력, 평균 계산, 등급 산출
개발자: 홍길동
버전: 1.0
'''
```

### **이스케이프 문자**

특수한 기능을 하는 문자를 표현할 때는 백슬래시(`\`)를 사용합니다. 이를 이스케이프 문자라고 합니다.

```python
# 주요 이스케이프 문자
print("첫 번째 줄\n두 번째 줄")  # \n: 줄바꿈
print("탭\t간격\t조정")  # \t: 탭
print("큰따옴표 출력: \"Hello\"")  # \": 큰따옴표
print("작은따옴표 출력: \'Hi\'")  # \': 작은따옴표
print("백슬래시 출력: \\")  # \\: 백슬래시
```

```
이스케이프 문자 정리

┌──────────┬────────────────────┐
│ 이스케이프│      의미          │
├──────────┼────────────────────┤
│   \n     │  줄바꿈 (newline)   │
│   \t     │  탭 (tab)           │
│   \"     │  큰따옴표           │
│   \'     │  작은따옴표         │
│   \\     │  백슬래시           │
└──────────┴────────────────────┘
```

---

## 2️⃣ **문자열 인덱싱**

문자열의 각 문자는 위치(인덱스)를 가지고 있습니다. 인덱스는 0부터 시작하며, 대괄호(`[]`)를 사용하여 특정 위치의 문자에 접근할 수 있습니다.

```python
# 문자열 인덱싱
word = "Python"

# 양수 인덱스 (앞에서부터)
print(word[0])  # P (첫 번째 문자)
print(word[1])  # y
print(word[2])  # t
print(word[5])  # n (마지막 문자)

# 음수 인덱스 (뒤에서부터)
print(word[-1])  # n (마지막 문자)
print(word[-2])  # o (뒤에서 두 번째)
print(word[-6])  # P (첫 번째 문자)
```

인덱스는 양수와 음수 두 가지 방식으로 사용할 수 있습니다. 양수 인덱스는 앞에서부터 0, 1, 2... 순서로, 음수 인덱스는 뒤에서부터 -1, -2, -3... 순서로 접근합니다.

```
문자열 "Python"의 인덱스

양수 인덱스:  0   1   2   3   4   5
           ┌───┬───┬───┬───┬───┬───┐
           │ P │ y │ t │ h │ o │ n │
           └───┴───┴───┴───┴───┴───┘
음수 인덱스: -6  -5  -4  -3  -2  -1
```

### **예제 1: 주민등록번호 정보 추출**

주민등록번호에서 생년월일 정보를 추출하는 프로그램입니다.

```python
# 주민등록번호 정보 추출
print("=== 주민등록번호 분석기 ===")

# 주민등록번호 입력 (예: 990101-1234567)
resident_id = input("주민등록번호를 입력하세요 (예: 990101-1234567): ")

# 정보 추출 (슬라이싱 사용)
year = resident_id[0:2]  # 년도 (앞 2자리)
month = resident_id[2:4]  # 월
day = resident_id[4:6]  # 일
gender_code = resident_id[7]  # 성별 코드 (7번째 문자)

# 결과 출력
print(f"\n생년월일: {year}년 {month}월 {day}일")
print(f"성별 코드: {gender_code} (1,3: 남성 / 2,4: 여성)")
print(f"뒷자리: {resident_id[7:]}")
```

---

## 3️⃣ **문자열 슬라이싱**

슬라이싱은 문자열의 일부분을 추출하는 기능입니다. `[시작:끝]` 형식으로 사용하며, 시작 인덱스부터 끝 인덱스 직전까지의 부분 문자열을 반환합니다.

```python
# 문자열 슬라이싱
text = "Hello, Python!"

# 기본 슬라이싱
print(text[0:5])    # Hello (인덱스 0부터 4까지)
print(text[7:13])   # Python (인덱스 7부터 12까지)

# 시작 또는 끝 생략
print(text[:5])     # Hello (처음부터 4까지)
print(text[7:])     # Python! (7부터 끝까지)
print(text[:])      # Hello, Python! (전체)

# 음수 인덱스 사용
print(text[-7:])    # Python! (뒤에서 7번째부터 끝까지)
print(text[:-1])    # Hello, Python (마지막 문자 제외)

# 간격 지정
print(text[::2])    # Hlo yhn (2칸씩 건너뛰기)
print(text[::-1])   # !nohtyP ,olleH (역순)
```

슬라이싱에서 `[시작:끝:간격]` 형식을 사용하면 더 세밀한 제어가 가능합니다.

```
슬라이싱 문법

[시작:끝]      - 시작부터 (끝-1)까지
[시작:]        - 시작부터 끝까지
[:끝]          - 처음부터 (끝-1)까지
[:]            - 전체
[::간격]       - 전체를 간격만큼 건너뛰며
[::-1]         - 역순
```

### **예제 2: 이메일 주소 분석**

이메일 주소에서 아이디와 도메인을 분리하는 프로그램입니다.

```python
# 이메일 주소 분석 프로그램
print("=== 이메일 주소 분석기 ===")

email = input("이메일 주소를 입력하세요: ")

# @ 기호의 위치 찾기
at_position = email.find('@')

# 아이디와 도메인 분리
user_id = email[:at_position]
domain = email[at_position + 1:]

# 도메인에서 최상위 도메인 추출
dot_position = domain.rfind('.')  # 마지막 점의 위치
top_level_domain = domain[dot_position + 1:]

# 결과 출력
print(f"\n전체 이메일: {email}")
print(f"아이디: {user_id}")
print(f"도메인: {domain}")
print(f"최상위 도메인: {top_level_domain}")
print(f"이메일 길이: {len(email)}자")
```

---

## 4️⃣ **문자열 메서드**

파이썬은 문자열을 다루는 다양한 메서드를 제공합니다. 메서드는 문자열 객체에 점(`.`)을 찍고 호출하는 함수입니다.

### **대소문자 변환**

```python
text = "Hello, Python!"

# 대소문자 변환
print(text.upper())      # HELLO, PYTHON! (모두 대문자)
print(text.lower())      # hello, python! (모두 소문자)
print(text.capitalize()) # Hello, python! (첫 글자만 대문자)
print(text.title())      # Hello, Python! (각 단어 첫 글자 대문자)
print(text.swapcase())   # hELLO, pYTHON! (대소문자 반전)
```

### **검색과 확인**

```python
message = "Python is awesome"

# 검색
print(message.find('is'))      # 7 (찾은 위치의 인덱스)
print(message.find('Java'))    # -1 (못 찾으면 -1)
print(message.count('o'))      # 2 ('o'가 나타난 횟수)

# 확인
print(message.startswith('Python'))  # True (시작 확인)
print(message.endswith('some'))      # True (끝 확인)
print('awesome' in message)          # True (포함 확인)
```

### **공백 제거**

```python
text = "   Hello, World!   "

print(text.strip())   # "Hello, World!" (양쪽 공백 제거)
print(text.lstrip())  # "Hello, World!   " (왼쪽 공백 제거)
print(text.rstrip())  # "   Hello, World!" (오른쪽 공백 제거)

# 특정 문자 제거
url = "https://www.example.com/"
print(url.strip('https://'))  # www.example.com/
```

### **문자열 분리와 결합**

```python
# split - 문자열을 리스트로 분리
sentence = "Python is easy to learn"
words = sentence.split()  # 공백 기준으로 분리
print(words)  # ['Python', 'is', 'easy', 'to', 'learn']

date = "2024-03-15"
parts = date.split('-')  # '-' 기준으로 분리
print(parts)  # ['2024', '03', '15']

# join - 리스트를 문자열로 결합
fruits = ['apple', 'banana', 'orange']
result = ', '.join(fruits)
print(result)  # apple, banana, orange

# 경로 만들기
path_parts = ['users', 'documents', 'python']
path = '/'.join(path_parts)
print(path)  # users/documents/python
```

### **문자열 치환**

```python
message = "Hello, Java! Java is great!"

# replace - 문자열 치환
new_message = message.replace('Java', 'Python')
print(new_message)  # Hello, Python! Python is great!

# 치환 횟수 제한
new_message = message.replace('Java', 'Python', 1)  # 첫 번째만 치환
print(new_message)  # Hello, Python! Java is great!
```

### **예제 3: 이름 카드 출력**

사용자 정보를 입력받아 보기 좋은 이름 카드를 출력하는 프로그램입니다.

```python
# 이름 카드 출력 프로그램
print("=== 이름 카드 생성기 ===")

# 정보 입력
name = input("이름: ")
company = input("회사명: ")
position = input("직책: ")
phone = input("전화번호: ")
email = input("이메일: ")

# 카드 너비 설정
width = 40
line = "=" * width

# 이름 카드 출력
print("\n" + line)
print(name.upper().center(width))  # 이름을 대문자로 중앙 정렬
print(position.center(width))  # 직책 중앙 정렬
print(line)
print(f"회사: {company}")
print(f"전화: {phone}")
print(f"이메일: {email}")
print(line)

# 추가 정보
print(f"\n이름 길이: {len(name)}자")
print(f"이메일 도메인: {email.split('@')[1]}")
print(f"이니셜: {name[0].upper()}")
```

---

## 5️⃣ **문자열 포매팅**

문자열 포매팅은 변수의 값을 문자열에 삽입하는 방법입니다. 파이썬은 여러 가지 포매팅 방법을 제공하는데, 가장 현대적이고 권장되는 방법은 f-string입니다.

### **f-string (포맷 문자열)**

f-string은 파이썬 3.6 이상에서 사용할 수 있는 가장 간편한 포매팅 방법입니다. 문자열 앞에 `f`를 붙이고, 중괄호 안에 변수나 표현식을 넣습니다.

```python
# f-string 기본 사용법
name = "홍길동"
age = 25
height = 175.5

# 변수 삽입
message = f"제 이름은 {name}이고, 나이는 {age}세입니다."
print(message)

# 표현식 사용
print(f"내년 나이: {age + 1}세")
print(f"키: {height}cm, 미터: {height / 100}m")

# 메서드 호출
text = "python"
print(f"대문자: {text.upper()}")
```

### **포매팅 옵션**

f-string은 다양한 포매팅 옵션을 제공합니다.

```python
# 소수점 자릿수 지정
pi = 3.14159265359
print(f"파이: {pi:.2f}")      # 3.14 (소수점 2자리)
print(f"파이: {pi:.4f}")      # 3.1416 (소수점 4자리)

# 천 단위 구분자
price = 1234567
print(f"가격: {price:,}원")   # 가격: 1,234,567원

# 정렬 (< 왼쪽, > 오른쪽, ^ 가운데)
name = "Python"
print(f"|{name:<10}|")  # |Python    |
print(f"|{name:>10}|")  # |    Python|
print(f"|{name:^10}|")  # |  Python  |

# 0으로 채우기
number = 42
print(f"{number:05}")   # 00042 (5자리, 빈 곳을 0으로 채움)

# 여러 옵션 조합
money = 1234567.89
print(f"금액: {money:>15,.2f}원")  # 금액:    1,234,567.89원
```

### **format() 메서드**

format() 메서드는 f-string 이전에 사용되던 방법으로, 여전히 유용하게 사용됩니다.

```python
# format() 메서드 사용
name = "김영희"
age = 22

message = "이름: {}, 나이: {}세".format(name, age)
print(message)

# 인덱스 지정
message = "이름: {0}, 나이: {1}세, 다시 이름: {0}".format(name, age)
print(message)

# 키워드 사용
message = "이름: {name}, 나이: {age}세".format(name="이철수", age=30)
print(message)
```

### **예제 4: 성적표 출력**

학생의 성적을 보기 좋은 표 형식으로 출력하는 프로그램입니다.

```python
# 성적표 출력 프로그램
print("=== 성적표 생성기 ===")

# 학생 정보 입력
student_name = input("학생 이름: ")
student_id = input("학번: ")

# 과목별 점수 입력
korean = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))

# 계산
total = korean + english + math
average = total / 3

# 성적표 출력
print("\n" + "=" * 50)
print(f"{'성적표':^50}")
print("=" * 50)
print(f"이름: {student_name:<10} 학번: {student_id}")
print("-" * 50)
print(f"{'과목':<10} {'점수':>10}")
print("-" * 50)
print(f"{'국어':<10} {korean:>10}점")
print(f"{'영어':<10} {english:>10}점")
print(f"{'수학':<10} {math:>10}점")
print("-" * 50)
print(f"{'총점':<10} {total:>10}점")
print(f"{'평균':<10} {average:>10.2f}점")
print("=" * 50)
```

---

## 6️⃣ **문자열 불변성**

파이썬의 문자열은 불변(immutable)입니다. 한 번 생성된 문자열은 수정할 수 없으며, 수정이 필요하면 새로운 문자열을 만들어야 합니다.

```python
# 문자열은 변경 불가능
text = "Hello"
# text[0] = 'h'  # 오류 발생! 문자열은 수정할 수 없음

# 새로운 문자열 생성
text = "hello"  # 가능 (새로운 문자열로 대체)
new_text = text.replace('h', 'H')  # 새 문자열 생성
print(new_text)  # Hello
```

이러한 불변성 때문에 문자열을 수정하는 것처럼 보이는 메서드들(upper, lower, replace 등)은 실제로는 새로운 문자열을 반환합니다. 원본 문자열은 변하지 않습니다.

```python
# 원본은 변하지 않음
original = "Python"
modified = original.upper()

print(original)  # Python (변하지 않음)
print(modified)  # PYTHON (새로운 문자열)
```

### **예제 5: 문자열 정보 분석**

입력받은 텍스트의 다양한 정보를 분석하는 프로그램입니다.

```python
# 문자열 정보 분석 프로그램
print("=== 텍스트 분석기 ===")

text = input("분석할 텍스트를 입력하세요: ")

# 기본 정보
total_length = len(text)
without_spaces = text.replace(' ', '')
space_count = total_length - len(without_spaces)

# 특정 문자 개수 세기
a_count = text.lower().count('a')
e_count = text.lower().count('e')
i_count = text.lower().count('i')

# 대소문자 변환
uppercase = text.upper()
lowercase = text.lower()
titlecase = text.title()

# 결과 출력
print("\n" + "=" * 40)
print("텍스트 분석 결과")
print("=" * 40)
print(f"원본 텍스트: {text}")
print(f"전체 길이: {total_length}자")
print(f"공백 제외 길이: {len(without_spaces)}자")
print(f"공백 개수: {space_count}개")
print(f"'a' 개수: {a_count}개")
print(f"'e' 개수: {e_count}개")
print(f"'i' 개수: {i_count}개")
print("-" * 40)
print(f"대문자 변환: {uppercase}")
print(f"소문자 변환: {lowercase}")
print(f"제목 형식: {titlecase}")
print(f"역순: {text[::-1]}")
print("=" * 40)
```

### **예제 6: 상품 코드 생성기**

회사명과 상품명을 입력받아 표준 상품 코드를 생성하는 프로그램입니다.

```python
# 상품 코드 생성 프로그램
print("=== 상품 코드 생성기 ===")

# 정보 입력
company = input("회사명: ")
product = input("상품명: ")
year = input("출시년도 (4자리): ")
sequence = input("일련번호 (3자리): ")

# 코드 생성
company_code = company[:3].upper()  # 회사명 앞 3글자 대문자
product_code = product[:4].upper()  # 상품명 앞 4글자 대문자
year_code = year[2:]  # 년도 뒤 2자리

# 상품 코드 조합
product_id = f"{company_code}-{product_code}-{year_code}-{sequence}"

# 바코드 형식 (숫자만)
barcode = sequence.zfill(13)  # 13자리로 0 채우기

# 결과 출력
print("\n" + "=" * 40)
print("생성된 상품 코드")
print("=" * 40)
print(f"회사 코드: {company_code}")
print(f"상품 코드: {product_code}")
print(f"년도 코드: {year_code}")
print(f"일련번호: {sequence}")
print("-" * 40)
print(f"표준 상품 코드: {product_id}")
print(f"바코드 번호: {barcode}")
print(f"전체 길이: {len(product_id)}자")
print("=" * 40)
```

---

## 📝 **핵심 개념 정리**

문자열은 따옴표로 감싸서 만들며, 여러 줄 문자열은 삼중 따옴표를 사용합니다. 이스케이프 문자(`\n`, `\t` 등)를 사용하면 특수한 문자를 표현할 수 있습니다.

인덱싱은 대괄호와 인덱스 번호로 특정 위치의 문자에 접근하는 방법이며, 0부터 시작하는 양수 인덱스와 -1부터 시작하는 음수 인덱스를 사용할 수 있습니다. 슬라이싱은 `[시작:끝:간격]` 형식으로 문자열의 일부를 추출합니다.

문자열 메서드는 대소문자 변환(upper, lower), 검색(find, count), 공백 제거(strip), 분리(split), 결합(join), 치환(replace) 등 다양한 기능을 제공합니다.

문자열 포매팅은 f-string을 사용하는 것이 가장 간편하며, 중괄호 안에 변수나 표현식을 넣고 다양한 포매팅 옵션을 지정할 수 있습니다. 문자열은 불변이므로 수정이 필요하면 새로운 문자열을 생성해야 합니다.

---

## 💡 **실습 과제**

### **과제 1: URL 분석기**

웹 주소(URL)를 입력받아 프로토콜, 도메인, 경로를 분리하는 프로그램을 작성하세요.

예시:

```
입력: https://www.example.com/path/to/page
출력:
프로토콜: https
도메인: www.example.com
경로: /path/to/page
```

### **과제 2: 회문(Palindrome) 검사기**

단어를 입력받아 회문인지 확인하는 프로그램을 작성하세요. 회문은 앞에서 읽으나 뒤에서 읽으나 같은 단어입니다.

```python
# 힌트
text = input("단어를 입력하세요: ")

# 소문자로 변환하고 공백 제거
cleaned = text.lower().replace(' ', '')

# 회문 검사 (역순과 비교)
is_palindrome = cleaned == cleaned[::-1]

print(f"입력한 단어: {text}")
print(f"정리된 단어: {cleaned}")
print(f"역순: {cleaned[::-1]}")
print(f"회문 여부: {is_palindrome}")
```

---

## ✅ **퀴즈**

### **[초급] 1번**

다음 코드의 실행 결과는?

```python
text = "Python"
print(text[0] + text[-1])
```

1. Pn
2. Py
3. Python
4. 오류 발생

### **[중급] 2번**

다음 중 "Hello, World!"에서 "World"를 추출하는 올바른 방법은?

```python
text = "Hello, World!"
```

1. text[7:12]
2. text[7:13]
3. text[8:13]
4. text[7:11]

### **[중급] 3번**

다음 코드의 실행 결과는?

```python
text = "  Python  "
print(len(text.strip()))
```

1. 10
2. 8
3. 6
4. 4

### **[중급] 4번**

다음 중 결과가 다른 하나는?

```python
name = "홍길동"
age = 25
```

1. f"이름: {name}, 나이: {age}"
2. "이름: {}, 나이: {}".format(name, age)
3. "이름: " + name + ", 나이: " + age
4. "이름: {0}, 나이: {1}".format(name, age)

### **[고급] 5번**

다음 코드의 실행 결과는?

```python
text = "Python Programming"
result = text.split()[1][:4].upper()
print(result)
```

1. PROG
2. PYTHON
3. PROGRAMMING
4. PROG

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 1**
`text[0]`은 'P'이고, `text[-1]`은 'n'입니다. 두 문자열을 `+` 연산자로 연결하면 "Pn"이 됩니다. 문자열의 덧셈은 연결(concatenation)을 의미합니다.

**2번 정답: 1**
"Hello, World!"에서 'W'는 인덱스 7, 'd'는 인덱스 11입니다. 슬라이싱에서 끝 인덱스는 포함되지 않으므로 `[7:12]`가 정답입니다. `text[7:12]`는 인덱스 7부터 11까지를 의미합니다.

**3번 정답: 3**
`text.strip()`은 양쪽 공백을 제거하여 "Python"을 반환합니다. "Python"의 길이는 6입니다. 원본 문자열 "  Python  "의 길이는 10이지만, strip() 후에는 6이 됩니다.

**4번 정답: 3**
3번은 오류가 발생합니다. 문자열과 정수를 직접 연결할 수 없기 때문에 `str(age)`로 변환해야 합니다. 나머지는 모두 올바르게 작동하여 같은 결과를 출력합니다.

**5번 정답: 1**
단계별로 살펴보면: `text.split()`은 `['Python', 'Programming']`, `[1]`로 'Programming' 선택, `[:4]`로 'Prog' 추출, `.upper()`로 'PROG'로 변환합니다. 문자열 메서드는 체이닝(연속 호출)이 가능합니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 입력과 출력에 대해 배웁니다. input() 함수를 활용한 다양한 입력 방법과 print() 함수의 고급 기능, 파일 입출력의 기초를 학습하게 됩니다.

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
