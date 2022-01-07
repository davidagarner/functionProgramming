# Python program to find the max
# of three given numbers
  
def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest
  
  
# Test code 
a = 7
b = 17
c = 27
print(maximum(a, b, c))
