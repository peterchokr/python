# 전화번호부 등록

telebook = dict()

def create_telebook() :
    with open("telebook.txt", "w", encoding="utf-8") as f :
        f.write("전화번호부")

def input_telebook() :
    global telebook
    name = input("이름 : ")
    tele = input("전화번호 : ")
    telebook[name] = tele
    print(telebook)

def add_telebook() :
    global telebook
    with open("telebook.txt", "a", encoding="utf-8") as f :
        for i, j in telebook.items() :
            f.write(f"이름 : {i}, 전화번호 : {j}\n")

print("메뉴")
print("1. 전화번호부 만들기")
print("2. 전화번호 입력")
print("3. 전화번호부에 저장하기")
print("4. 종료")

while True :
    choice = int(input("원하는 작업을 선택 : "))
    if choice == 1 :
        create_telebook()
    elif choice == 2:
        input_telebook()
    elif choice == 3:
        add_telebook()
    elif choice == 4 :
        break
    else :
        print("잘못된 선택....")
