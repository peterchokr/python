# 성적을 받아서 학점을 결정하는 프로그램

score = int(input("성적을 입력하시오: "))

if score >= 90 :
	print("학점 A")
elif score >= 80 :
	print("학점 B")
elif score >= 70 :
	print("학점 C")
elif score >= 60 :
	print("학점 D")
else :
	print("학점 F")
