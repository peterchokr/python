score = 0

ans = input("가장 쉬운 프로그래밍 언어는? ")
check = (ans=="파이썬")
print(check)
score += int(check)

ans = input("거듭제곱을 계산하는 연산자는? ")
check = (ans=="**")
print(check)
score += int(check)

ans = input("파이썬에서 출력시에 사용하는 함수이름은? ")
check = (ans=="print")
print(check)
score += int(check)

print(f"점수 = {score}")
