# -*- coding: utf-8 -*-


def next_permutation(n):
    j = n - 2
    while j != -1 and a[j] >= a[j + 1]:
        j -= 1
    if j == -1:
        return False  # больше перестановок нет
    k = n - 1
    while a[j] >= a[k]:
        k -= 1
    a[j], a[k] = a[k], a[j]
    l, r = j + 1, n - 1;  # сортируем оставшуюся часть последовательности
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return True


def get_word(n):  # переводим в слово
    word = ''
    for i in range(n):
        word += letters[a[i]]
    return word + '\n'


letters = ['К', 'О', 'Л', 'А', 'Б', 'Р', 'Ц', 'И', 'Я']  # исх.алфавит
a = [0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8]  # переработка в циферки
f = open('words.txt', 'w')  # файл с результатом
f.write(get_word(12))  # первое слово
while next_permutation(12):
    f.write(get_word(12))
print("Все слова в файле :)")
f.close()
