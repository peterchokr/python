# 14장 파일 입출력

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 텍스트 파일을 읽고 쓸 수 있으며, 프로그램이 종료된 후에도 데이터를 저장하고 불러올 수 있습니다. 파일 입출력은 실용적인 프로그램을 만드는 데 필수적인 기능입니다.

---

## 1️⃣ **파일 입출력이란?**

지금까지 만든 프로그램들은 실행이 끝나면 데이터가 모두 사라졌습니다. 파일에 데이터를 저장하면 프로그램을 다시 실행해도 이전 데이터를 불러올 수 있습니다.

```
프로그램 메모리 vs 파일

┌─────────────────┐      ┌─────────────────┐
│  프로그램 메모리 │      │    파일 저장     │
├─────────────────┤      ├─────────────────┤
│ 빠른 접근       │      │ 영구 보존       │
│ 일시적          │      │ 느린 접근       │
│ 종료시 삭제     │      │ 종료 후에도 유지│
└─────────────────┘      └─────────────────┘
```

---

## 2️⃣ **텍스트 파일 쓰기**

### **파일 열기와 닫기**

```python
# 파일 열기
file = open("test.txt", "w")  # w = write (쓰기 모드)
file.write("안녕하세요!")
file.close()  # 반드시 닫아야 함!
```

⚠️ **중요**: 파일을 열면 반드시 `close()`로 닫아야 합니다!

### **with 문 (권장)**

```python
# with 문 사용 (자동으로 닫힘)
with open("test.txt", "w") as file:
    file.write("안녕하세요!\n")
    file.write("파이썬 공부 중입니다.")
# 여기서 자동으로 파일이 닫힘
```

### **예제 1: 일기 쓰기**

일기를 파일로 저장하는 프로그램입니다.

```python
# 일기 쓰기 프로그램
print("📔" + "=" * 38 + "📔")
print("   일기장")
print("📔" + "=" * 38 + "📔")

# 날짜 입력
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")

print(f"\n오늘 날짜: {today}")
print("\n일기를 작성하세요 (종료: 빈 줄)")
print("-" * 40)

# 일기 내용 입력
diary_content = []

while True:
    line = input()
    if line == "":
        break
    diary_content.append(line)

# 파일에 저장
filename = f"diary_{today}.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"일기 - {today}\n")
    file.write("=" * 40 + "\n\n")
  
    for line in diary_content:
        file.write(line + "\n")

print("\n" + "-" * 40)
print(f"✓ '{filename}' 저장 완료!")
```

---

## 3️⃣ **텍스트 파일 읽기**

### **read() - 전체 읽기**

```python
# 파일 전체를 문자열로 읽기
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

### **readline() - 한 줄씩 읽기**

```python
# 한 줄씩 읽기
with open("test.txt", "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)
```

### **readlines() - 모든 줄을 리스트로**

```python
# 모든 줄을 리스트로 읽기
with open("test.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip()으로 줄바꿈 제거
```

### **예제 2: 할 일 목록**

할 일을 파일로 저장하고 불러오는 프로그램입니다.

```python
# 할 일 목록 프로그램
print("✅" + "=" * 38 + "✅")
print("   할 일 목록 (파일 저장)")
print("✅" + "=" * 38 + "✅")

filename = "todo_list.txt"

while True:
    print("\n" + "=" * 40)
    print("1. 할 일 추가")
    print("2. 할 일 보기")
    print("3. 할 일 완료")
    print("4. 종료")
    print("=" * 40)
  
    choice = input("\n선택: ")
  
    if choice == "1":
        task = input("\n할 일: ")
  
        # 파일에 추가 (append 모드)
        with open(filename, "a", encoding="utf-8") as file:
            file.write(task + "\n")
  
        print(f"✓ '{task}' 추가됨")
  
    elif choice == "2":
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
    
            if len(lines) == 0:
                print("\n할 일이 없습니다.")
            else:
                print("\n📋 할 일 목록:")
                print("-" * 40)
                for i, task in enumerate(lines, 1):
                    print(f"{i}. {task.strip()}")
                print("-" * 40)
                print(f"총 {len(lines)}개")
  
        except FileNotFoundError:
            print("\n할 일이 없습니다.")
  
    elif choice == "3":
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
    
            if len(lines) == 0:
                print("\n할 일이 없습니다.")
                continue
    
            print("\n📋 할 일 목록:")
            for i, task in enumerate(lines, 1):
                print(f"{i}. {task.strip()}")
    
            num = int(input("\n완료한 번호: "))
    
            if 1 <= num <= len(lines):
                completed = lines[num - 1].strip()
        
                # 해당 항목 제거
                lines.pop(num - 1)
        
                # 파일 전체를 다시 쓰기
                with open(filename, "w", encoding="utf-8") as file:
                    for task in lines:
                        file.write(task)
        
                print(f"\n✅ '{completed}' 완료!")
            else:
                print("\n잘못된 번호입니다.")
  
        except FileNotFoundError:
            print("\n할 일이 없습니다.")
  
    elif choice == "4":
        print("\n프로그램을 종료합니다.")
        break
  
    else:
        print("\n잘못된 선택입니다.")
```

---

## 4️⃣ **파일 모드**

파일을 열 때 사용하는 모드들입니다.

```
파일 모드

┌──────┬────────────────────────────┐
│ 모드 │ 설명                       │
├──────┼────────────────────────────┤
│  r   │ 읽기 (파일이 없으면 오류)  │
│  w   │ 쓰기 (기존 내용 삭제)      │
│  a   │ 추가 (파일 끝에 추가)      │
│  r+  │ 읽기+쓰기                  │
│  w+  │ 쓰기+읽기 (기존 내용 삭제) │
│  a+  │ 추가+읽기                  │
└──────┴────────────────────────────┘
```

```python
# w 모드 - 기존 내용 삭제
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("새로운 내용")  # 기존 내용이 모두 삭제됨

# a 모드 - 기존 내용 유지하고 끝에 추가
with open("test.txt", "a", encoding="utf-8") as file:
    file.write("추가 내용")  # 기존 내용 뒤에 추가
```

### **예제 3: 방문록**

방문자 이름을 계속 추가하는 프로그램입니다.

```python
# 방문록 프로그램
print("📝" + "=" * 38 + "📝")
print("   방문록")
print("📝" + "=" * 38 + "📝")

filename = "guestbook.txt"

while True:
    print("\n" + "=" * 40)
    print("1. 방문 기록")
    print("2. 방문록 보기")
    print("3. 종료")
    print("=" * 40)
  
    choice = input("\n선택: ")
  
    if choice == "1":
        name = input("\n이름: ")
        message = input("메시지: ")
  
        # 현재 시간
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
  
        # 파일에 추가
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"[{now}] {name}: {message}\n")
  
        print(f"\n✓ 방문 감사합니다, {name}님!")
  
    elif choice == "2":
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
    
            if content.strip() == "":
                print("\n아직 방문자가 없습니다.")
            else:
                print("\n" + "=" * 40)
                print("📖 방문록")
                print("=" * 40)
                print(content)
                print("=" * 40)
  
        except FileNotFoundError:
            print("\n아직 방문자가 없습니다.")
  
    elif choice == "3":
        print("\n프로그램을 종료합니다.")
        break
  
    else:
        print("\n잘못된 선택입니다.")
```

---

## 5️⃣ **파일 존재 확인**

파일이 있는지 확인하는 방법입니다.

```python
import os

# 파일 존재 확인
if os.path.exists("test.txt"):
    print("파일이 존재합니다.")
else:
    print("파일이 없습니다.")

# 파일 삭제
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("파일이 삭제되었습니다.")
```

### **예제 4: 메모장**

여러 메모를 파일로 저장하는 프로그램입니다.

```python
# 메모장 프로그램
import os

print("📝" + "=" * 38 + "📝")
print("   메모장")
print("📝" + "=" * 38 + "📝")

memo_folder = "memos"

# 폴더가 없으면 생성
if not os.path.exists(memo_folder):
    os.makedirs(memo_folder)

while True:
    print("\n" + "=" * 40)
    print("1. 새 메모 작성")
    print("2. 메모 읽기")
    print("3. 메모 목록")
    print("4. 메모 삭제")
    print("5. 종료")
    print("=" * 40)
  
    choice = input("\n선택: ")
  
    if choice == "1":
        title = input("\n메모 제목: ")
        print("내용 입력 (종료: 빈 줄):")
  
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
  
        # 파일로 저장
        filename = os.path.join(memo_folder, f"{title}.txt")
  
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
  
        print(f"\n✓ '{title}' 저장 완료")
  
    elif choice == "2":
        title = input("\n메모 제목: ")
        filename = os.path.join(memo_folder, f"{title}.txt")
  
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
    
            print("\n" + "=" * 40)
            print(f"📄 {title}")
            print("=" * 40)
            print(content)
            print("=" * 40)
        else:
            print(f"\n'{title}' 메모가 없습니다.")
  
    elif choice == "3":
        files = os.listdir(memo_folder)
        txt_files = [f for f in files if f.endswith(".txt")]
  
        if len(txt_files) == 0:
            print("\n저장된 메모가 없습니다.")
        else:
            print("\n📚 메모 목록:")
            print("-" * 40)
            for i, filename in enumerate(txt_files, 1):
                title = filename[:-4]  # .txt 제거
                print(f"{i}. {title}")
            print("-" * 40)
            print(f"총 {len(txt_files)}개")
  
    elif choice == "4":
        title = input("\n삭제할 메모 제목: ")
        filename = os.path.join(memo_folder, f"{title}.txt")
  
        if os.path.exists(filename):
            confirm = input(f"'{title}'를 삭제하시겠습니까? (Y/N): ")
            if confirm == "Y" or confirm == "y":
                os.remove(filename)
                print(f"\n✓ '{title}' 삭제됨")
            else:
                print("\n취소되었습니다.")
        else:
            print(f"\n'{title}' 메모가 없습니다.")
  
    elif choice == "5":
        print("\n프로그램을 종료합니다.")
        break
  
    else:
        print("\n잘못된 선택입니다.")
```

---

## 6️⃣ **JSON 파일 다루기**

JSON은 딕셔너리와 비슷한 형식으로 데이터를 저장합니다.

```python
import json

# 딕셔너리를 JSON 파일로 저장
data = {
    "이름": "김철수",
    "나이": 20,
    "취미": ["독서", "음악", "운동"]
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# JSON 파일에서 딕셔너리로 읽기
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(loaded_data)  # {'이름': '김철수', '나이': 20, ...}
```

### **예제 5: 게임 설정 저장**

게임 설정을 JSON으로 저장하는 프로그램입니다.

```python
# 게임 설정 관리 프로그램
import json
import os

print("🎮" + "=" * 38 + "🎮")
print("   게임 설정")
print("🎮" + "=" * 38 + "🎮")

config_file = "game_config.json"

# 기본 설정
default_config = {
    "소리": 70,
    "음악": 50,
    "화면": "전체화면",
    "난이도": "보통",
    "언어": "한국어"
}

def load_config():
    """설정 불러오기"""
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return default_config.copy()

def save_config(config):
    """설정 저장"""
    with open(config_file, "w", encoding="utf-8") as file:
        json.dump(config, file, ensure_ascii=False, indent=2)

# 설정 불러오기
config = load_config()

while True:
    print("\n" + "=" * 40)
    print("현재 설정")
    print("=" * 40)
    for key, value in config.items():
        print(f"{key}: {value}")
    print("=" * 40)
  
    print("\n1. 소리 조절")
    print("2. 음악 조절")
    print("3. 화면 모드 변경")
    print("4. 난이도 변경")
    print("5. 기본값으로 초기화")
    print("6. 저장 후 종료")
    print("7. 저장 안 하고 종료")
  
    choice = input("\n선택: ")
  
    if choice == "1":
        volume = int(input("소리 (0-100): "))
        if 0 <= volume <= 100:
            config["소리"] = volume
            print(f"✓ 소리가 {volume}으로 설정됨")
        else:
            print("0-100 사이 값을 입력하세요.")
  
    elif choice == "2":
        music = int(input("음악 (0-100): "))
        if 0 <= music <= 100:
            config["음악"] = music
            print(f"✓ 음악이 {music}으로 설정됨")
        else:
            print("0-100 사이 값을 입력하세요.")
  
    elif choice == "3":
        print("\n1. 전체화면")
        print("2. 창모드")
        mode = input("선택: ")
  
        if mode == "1":
            config["화면"] = "전체화면"
        elif mode == "2":
            config["화면"] = "창모드"
  
        print(f"✓ 화면 모드: {config['화면']}")
  
    elif choice == "4":
        print("\n1. 쉬움")
        print("2. 보통")
        print("3. 어려움")
        level = input("선택: ")
  
        levels = {"1": "쉬움", "2": "보통", "3": "어려움"}
        if level in levels:
            config["난이도"] = levels[level]
            print(f"✓ 난이도: {config['난이도']}")
  
    elif choice == "5":
        confirm = input("기본값으로 초기화하시겠습니까? (Y/N): ")
        if confirm == "Y" or confirm == "y":
            config = default_config.copy()
            print("✓ 기본값으로 초기화됨")
  
    elif choice == "6":
        save_config(config)
        print("\n✓ 설정이 저장되었습니다.")
        print("프로그램을 종료합니다.")
        break
  
    elif choice == "7":
        confirm = input("저장하지 않고 종료하시겠습니까? (Y/N): ")
        if confirm == "Y" or confirm == "y":
            print("\n프로그램을 종료합니다.")
            break
  
    else:
        print("잘못된 선택입니다.")
```

---

## 📝 **핵심 개념 정리**

파일을 열 때는 `open()` 함수를 사용하고, 사용 후에는 반드시 `close()`로 닫아야 합니다. `with` 문을 사용하면 자동으로 파일이 닫히므로 권장됩니다.

파일 모드는 `"r"`(읽기), `"w"`(쓰기), `"a"`(추가)가 있으며, `encoding="utf-8"`을 지정하여 한글을 올바르게 처리할 수 있습니다.

`read()`는 전체 내용을, `readline()`은 한 줄을, `readlines()`는 모든 줄을 리스트로 읽습니다. `write()`로 파일에 내용을 씁니다.

CSV 파일은 데이터를 쉼표로 구분하여 저장하며, `split(",")`으로 파싱할 수 있습니다. JSON은 딕셔너리와 유사한 형식으로 `json.dump()`와 `json.load()`로 처리합니다.

---

## 💡 **실습 과제**

### **과제 1: 단어장**

영어 단어와 뜻을 파일에 저장하고 퀴즈를 내는 프로그램을 작성하세요.

```python
# 힌트
# words.txt 파일 형식:
# apple,사과
# banana,바나나
# cherry,체리

# 1. 단어 추가
# 2. 랜덤 퀴즈
# 3. 전체 보기
```

### **과제 2: 가계부**

수입과 지출을 기록하고 통계를 보여주는 프로그램을 작성하세요.

```python
# 힌트
# ledger.csv 파일 형식:
# 날짜,구분,항목,금액
# 2024-01-01,수입,월급,3000000
# 2024-01-02,지출,식비,50000

# 통계: 총 수입, 총 지출, 잔액
```

---

## ✅ **퀴즈**

### **[초급] 1번**

파일을 쓰기 모드로 여는 코드는?

```python
1. open("file.txt", "r")
2. open("file.txt", "w")
3. open("file.txt", "a")
4. open("file.txt", "x")
```

### **[중급] 2번**

다음 코드의 역할은?

```python
with open("test.txt", "a") as file:
    file.write("Hello")
```

1. 파일을 읽는다
2. 파일을 새로 만들고 쓴다
3. 파일 끝에 추가한다
4. 파일을 삭제한다

### **[중급] 3번**

파일의 모든 줄을 리스트로 읽는 메서드는?

```python
1. read()
2. readline()
3. readlines()
4. readall()
```

### **[고급] 4번**

다음 코드의 실행 결과는?

```python
with open("test.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

with open("test.txt", "r") as file:
    content = file.read()
    print(len(content.split("\n")))
```

1. 2
2. 3
3. 4
4. 오류 발생

### **[고급] 5번**

CSV 파일의 한 줄 "김철수,20,컴퓨터"를 리스트로 분리하는 코드는?

```python
1. line.split()
2. line.split(",")
3. line.split(":")
4. line.strip()
```

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
`"w"` 모드는 파일을 쓰기 모드로 엽니다. 파일이 없으면 새로 만들고, 있으면 기존 내용을 삭제합니다.

**2번 정답: 3**
`"a"` 모드는 append(추가) 모드로, 파일 끝에 내용을 추가합니다. 기존 내용은 유지됩니다.

**3번 정답: 3**
`readlines()` 메서드는 파일의 모든 줄을 리스트로 반환합니다.

**4번 정답: 2**
"Line 1\nLine 2\n"를 `\n`으로 split하면 ["Line 1", "Line 2", ""]가 되어 길이는 3입니다.

**5번 정답: 2**
CSV는 쉼표로 구분되므로 `split(",")`을 사용하여 ["김철수", "20", "컴퓨터"]로 분리합니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 예외 처리에 대해 배웁니다. 프로그램 실행 중 발생하는 오류를 감지하고 처리하는 방법을 학습하여, 더욱 안정적이고 견고한 프로그램을 만들 수 있게 됩니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
