total = 0
answer = "yes"				# 반복이 수행되려면 answer의 초기값은 "yes"
# answer = "nos"			# 초기값이 no 이면 반복문은 실행되지 않는다.
while answer == "yes":		# answer가 “yes”인지를 검사한다.
	number = int(input("숫자를 입력하시오:  "))
	total = total + number
	answer = input("계속?(yes/no): ")
print("합계는 : ", total)
