﻿def add(*numbers) :
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

print(add(10, 20))
print(add(10, 20, 30))
