import time


def fac(x):
    return int(lines[x])


def c(n, m):
    return fac(n) / (fac(m) * fac(n - m))


def p(x):
    return fac(x)


def gen(n, word=""):
    global words
    if len(word) == n:
        c1 = c3 = c5 = 0
        for letter in A:
            if word.count(letter) == 1:
                c1 += 1
            elif word.count(letter) == 3:
                c3 += 1
            elif word.count(letter) == 5:
                c5 += 1
        if len(word) == c1 + 3 * c3 + 5 * c3:
            words.append(word)
    else:
        for letter in A:
            word += letter
            gen(n, word)
            word = word[:-1]  # удаление последнего символа


n = int(input("Введите количество позиций в слове: "))  # начальное условие
E = [i for i in range(18, 25)]  # разрешённые значения n
if n not in E:
    while n not in E:
        print("Введённое n не удовлетворяет условиям задачи.")
        n = int(input("Введите количество позиций в слове: "))

f = open("factorial.txt", 'r')
lines = f.readlines()
res=int(c(10, 3) * c(7, 1))
print("Количество слов: ",res)

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']  # алфавит


