flag = True

for i in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = False 
        
if flag:
    print('YES')
else:
    print('NO')



