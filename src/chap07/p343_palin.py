s = input("문자열을 입력하시오: ")

s1 = s[::-1]			# 문자열을 거꾸로 만든다. 

if(s == s1):
        print("회문입니다.")
else:
        print("회문이 아닙니다.")