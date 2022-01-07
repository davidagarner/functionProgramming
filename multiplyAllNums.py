# Python program to multiply all numbers
# in the list

#Solution 1
 
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((4, 12, 9, 6, 15, 4))) 
  
  
  
#Solution 2

import math
list1 = [4, 12, 9]
list2 = [6, 15, 4]
 
 
solution1 = math.prod(list1)
solution2 = math.prod(list2)
print(solution1)
print(solution2)
