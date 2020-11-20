import time


def fac(x):
    return int(lines[x])


def c(n, m):
    return fac(n) / (fac(m) * fac(n - m))


def p(x):
    return fac(x)


def gen(n, word=""):
    global words, c
    if len(word) == n:
        c1 = c3 = c5 = 0
        for letter in A:
            if word.count(letter) == 5:
                c5 += 1
            elif word.count(letter) == 3:
                c3 += 1
            elif word.count(letter) == 1:
                c1 += 1
        if len(word) == (c1 + 3 * c5 + c3):
            words.append(word)
        print(c)
        c += 1
        if c == 100:
            return None
    else:
        for letter in A:
            word += letter
            gen(n, word)
            word = word[:-1]  # удаление последнего символа


n = int(input("Введите количество позиций в слове: "))  # начальное условие
f = open("factorial.txt", 'r')
lines = f.readlines()

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']  # алфавит

c = 0
words = []
st = time.time()
gen(n)
fn = time.time()
print("Время на прогу: ", fn - st)
