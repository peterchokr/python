﻿# 코드 1
list1 = [1, 2, 3, 4, 15, 99] 

# 리스트를 정렬한다. 
list1.sort() 
  
# 뒤에서 두 번째 요소를 출력한다. 
print("두 번째로 큰 수=", list1[-2]) 


# 코드 2
list1 = [1, 2, 3, 4, 15, 99] 
 
# 제일 큰 수는 삭제한다. 
list1.remove(max(list1)) 
 
# 그 다음으로 큰 수를 출력한다. 리스트는 변경되었다. 
print("두 번째로 큰 수=", max(list1)) 