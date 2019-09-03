import random

file = input()
a = file
b = a.split()
alph = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЯЧСМИТЬБЮЖЭ"
nfile = ""
alph2 = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЯЧСМИТЬБЮЖЭ"
eend = []
endword = ""
D = {}
for i in range(0, len(b)):
    for j in b[i]:
        s = b[i]
        if j == '.' or j == '!' or j == '?':
            endword = s[:len(s) - 1]
            endword = str(endword)
            if endword[len(endword) - 1] == '.':
                endword = endword[:len(endword) - 2]
            eend.append(endword)
            if endword not in D:
                D[endword] = D.get(endword, ['.'])
            break

for i in range(0, len(a)):
    if a[i] in alph:
        s = str(a[i])
        s = s.lower()
        nfile += s
    else:
        nfile += " "
#print(oone)        
a = nfile.split()
for i in range(0, len(a)):
    if a[i] not in D:
        D[a[i]] = D.get(a[i], [])
    if i != len(a) - 1:
        D[a[i]] += [a[i + 1]]
w = list(D.keys())
#print(D)
word = random.choice(w)
k = 1
while k == 1:
    print("Введите команду gen для генерации текста: ", end="")
    n = input()
    if n == "gen":
        while word != '.':
            print(word, end = " ")
            word = random.choice(list(D[word]))
        print('.')
        word = random.choice(w)
    print("Для продолжения нажмите 1: ", end = "")
    n1 = int(input())
    if n1 != 1:
        break

