n = int(input())

if n <= 1:
    print('Не корректные данные')
else:
    for i in range(n):
        print(n * '*')
        n = n - 1
        
        