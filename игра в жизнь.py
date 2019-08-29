import random


print("Укажите размеры поля: ", end = '')
n, m = map(int, input().split())  # нужно определить размеры поля вводом в консоль чисел n на m
print("Введите время симуляции жизни океана: ", end='')
f = int(input())
a = [0] * n
c = ['.', '&', '1', '0']
for i in range(0, n):
    a[i] = [0] * m
for i in range(0, n):
    for j in range(0, m):
        a[i][j] = random.choice(c)
# рыба '1', креветка '0', скала '#', ничего '.'
b = [0] * n
for i in range(0, n):
    b[i] = [0] * m
for i in range(0, n):
    for j in range(0, m):
        b[i][j] = '-'
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
print()
for x in range(f):
    for i in range(n):
        s = 0
        k = 0
        for j in range(m):
            if i == 0 and j == 0:
                if a[i + 1][j] == '1':
                    s += 1
                elif a[i + 1][j] == '0':
                    k += 1
                if a[i + 1][j + 1] == '1':
                    s += 1
                elif a[i + 1][j + 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
            elif i == n - 1 and j == m - 1:
                if a[i - 1][j] == '1':
                    s += 1
                elif a[i - 1][j] == '0':
                    k += 1
                if a[i - 1][j - 1] == '1':
                    s += 1
                elif a[i - 1][j - 1] == '0':
                    k += 1
                if a[i][j - 1] == '1':
                    s += 1
                elif a[i][j - 1] == '0':
                    k += 1
            elif i == 0 and j == m - 1:
                if a[i][j - 1] == '1':
                    s += 1
                elif i == 0 and j == m - 1:
                    k += 1
                if a[i + 1][j] == '1':
                    s += 1
                elif a[i + 1][j] == '0':
                    k += 1
                if a[i + 1][j - 1] == '1':
                    s += 1
                elif a[i + 1][j - 1] == '0':
                    k += 1
            elif i == n - 1 and j == 0:
                if a[i - 1][j] == '1':
                    s += 1
                elif a[i - 1][j] == '0':
                    k += 1
                if a[i - 1][j + 1] == '1':
                    s += 1
                elif a[i - 1][j + 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
            elif i == 0:
                if a[i][j - 1] == '1':
                    s += 1
                elif a[i][j - 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
                if a[i + 1][j] == '1':
                    s += 1
                elif a[i + 1][j] == '0':
                    k += 1
                if a[i + 1][j + 1] == '1':
                    s += 1
                elif a[i + 1][j + 1] == '0':
                    k += 1
                if a[i + 1][j - 1] == '1':
                    s += 1
                elif a[i + 1][j - 1] == '0':
                    k += 1
            elif j == 0:
                if a[i + 1][j] == '1':
                    s += 1
                elif a[i + 1][j] == '0':
                    k += 1
                if a[i - 1][j] == '1':
                    s += 1
                elif a[i - 1][j] == '0':
                    k += 1
                if a[i + 1][j + 1] == '1':
                    s += 1
                elif a[i + 1][j + 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
                if a[i - 1][j + 1] == '1':
                    s += 1
                elif a[i - 1][j + 1] == '0':
                    k += 1
            elif i == n - 1:
                if a[i][j - 1] == '1':
                    s += 1
                elif a[i][j - 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
                if a[i - 1][j] == '1':
                    s += 1
                elif a[i - 1][j] == '0':
                    k += 1
                if a[i - 1][j + 1] == '1':
                    s += 1
                elif a[i - 1][j + 1] == '0':
                    k += 1
                if a[i - 1][j - 1] == '1':
                    s += 1
                elif a[i - 1][j - 1] == '0':
                    k += 1
            elif i == n - 1:
                if a[i][j - 1] == '1':
                    s += 1
                elif a[i][j - 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
                if a[i - 1][j] == '1':
                    s += 1
                elif a[i - 1][j] == '0':
                    k += 1
                if a[i - 1][j + 1] == '1':
                    s += 1
                elif a[i - 1][j + 1] == '0':
                    k += 1
                if a[i - 1][j - 1] == '1':
                    s += 1
                elif a[i - 1][j - 1] == '0':
                    k += 1
            elif j == m - 1:
                if a[i - 1][j] == '1':
                    s += 1
                elif a[i - 1][j] == '0':
                    k += 1
                if a[i + 1][j] == '1':
                    s += 1
                elif a[i + 1][j] == '0':
                    k += 1
                if a[i][j - 1] == '1':
                    s += 1
                elif a[i][j - 1] == '0':
                    k += 1
                if a[i - 1][j - 1] == '1':
                    s += 1
                elif a[i - 1][j - 1] == '0':
                    k += 1
                if a[i + 1][j - 1] == '1':
                    s += 1
                elif a[i + 1][j - 1] == '0':
                    k += 1
            else:
                if a[i - 1][j] == '1':
                    s += 1
                if a[i - 1][j] == '0':
                    k += 1
                elif a[i - 1][j - 1] == '1':
                    s += 1
                if a[i - 1][j - 1] == '0':
                    k += 1
                elif a[i - 1][j + 1] == '1':
                    s += 1
                elif a[i - 1][j + 1] == '0':
                    k += 1
                if a[i + 1][j] == '1':
                    s += 1
                elif a[i + 1][j] == '0':
                    k += 1
                if a[i + 1][j - 1] == '1':
                    s += 1
                elif a[i + 1][j - 1] == '0':
                    k += 1
                if a[i + 1][j + 1] == '1':
                    s += 1
                elif a[i + 1][j + 1] == '0':
                    k += 1
                if a[i][j + 1] == '1':
                    s += 1
                elif a[i][j + 1] == '0':
                    k += 1
                if a[i][j - 1] == '1':
                    s += 1
                elif a[i][j - 1] == '0':
                    k += 1
            if a[i][j] == '&':
                b[i][j] = '&'
            if a[i][j] == '.':
                b[i][j] = '.'
            if a[i][j] == '.':
                if s == 3:
                    b[i][j] == '1'
                elif k == 3:
                    b[i][j] == '0'
            if a[i][j] == '1':
                if s >= 4 or s < 2:
                    b[i][j] = '.'
                else:
                    b[i][j] = '1'
            elif a[i][j] == '0':
                if k >= 4 or k < 2:
                    b[i][j] = '.'
                else:
                    b[i][j] = '0'
    for i1 in range(n):
        for j1 in range(m):
            a[i][j] = b[i][j]
    if a == b:
        break
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()