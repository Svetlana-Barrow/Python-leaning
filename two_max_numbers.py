n = int(input())
max1 = 0
max2 = 0

for i in range(1, n + 1):
    a = int(input())    
    if a > max1:
        max1, max2 = a, max1
    elif a > max2:
        max2 = a
          
print(max1, max2, sep = '\n')
