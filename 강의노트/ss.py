total = 0
st = ""
while True : 
    print("메뉴판")
    print("1 - 라면(2000원)")
    print("2 - 삼각김밥(1500원)")
    print("3 - 사이다(1000원)")
    print("x - 주문 마침")
    
    menu = input("메뉴를 선택(1,2,3,x)")
    if menu == "x" :
        break
    else :
        if menu == "1" :
            s = "라면"
            price = 2000
        elif menu == "2" :
            s = "삼각김밥"
            price = 1500
        elif menu == "3" :
            s = "사이다"
            price = 1000
        else :
            print("잘못된 입력")
            continue
            
        cnt = input("수량을 입력 : ")
        if st == "" :
            st = s + cnt
        else : 
            st = st + "," + s + cnt
            
        total = total + (price * int(cnt))  
        
        from datetime import datetime
        now = datetime.now()
        # '2026-09-21 14:32:00' 형태로 변환
        formatted_time = now.strftime("%Y.%m.%d %H:%M:%S")     
        
        # 주문일시-라면20,삼각김밥20,사이다20-합계
        
with open("menu.txt", "a", encoding="utf-8")  as f :
    f.write(formatted_time + "-" + st + "-" + str(total) + "\n")
