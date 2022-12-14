# Цикл   For  задачи с числами.
# 1.Вывести на экран число "10" 20 раз столбиком.

for i in range(20):
    print('10')

# 2.Даны два числа a и b. Составить программу вывода на экран всех чисел от a до b.

a, b = map(int, input().split())
for i in range(a, b):
    print(i)

# 3.Дано число N. Составить программу выводящую кубы чисел от 1 до N в одну строку.

N = int(input('enter N:'))
for i in range(1, N):
    print(i**3, end=' ')

# 4.Выведите на экран в одну строку числа от 100 до
# -100 включительно.

for i in range(100, -101, -1):
    print(i, end=" ")

# 5.Необходимо вывести все четные числа на отрезке [a; a * 10]

a = int(input())
for i in range(a, a * 10):
    if i % 2 == 0:
        print(i, end= ' ')

# 6.Найти сумму всех целых чисел от 100 до 500 включительно.

sum = 0
for i in range(100, 501):
    if i % 2 == 0:
        sum += i
print('sum =', sum)

# 7.Найти произведение всех целых чисел от 5 до 20 включительно.

multiply = 1
for i in range(5, 21):
    if i % 2 == 0:
        multiply *= i
print('multiply =', multiply)

# 8.Дано натуральное число n. Вывести на экран факториал этого числа.

import math
n = int(input())
f = math.factorial(n)
print(f)

n = int(input())
factorial = 1
for i in range(2, n+1):
    factorial *= i
print(factorial)


# Цикл   For  задачи со строками. Метод split() в задачах не использовать!!!
# 9. Дан текст. Слова в тексте разделены одним или несколькими пробелами.
# Написать программу определяющую количество слов, заканчивающихся одной и той же буквой

s = input('enter sting:')
s +=" "
s1 =""
symbol = input('enter symbol:')
count = 0
for i in range(len(s)):
    if s[i] != ' ':
        s1 += s[i]
    elif s[i] == " " and len(s1) >= 1:
        print(s1)
        if s1[-1] == symbol:
            count += 1
        s1 = ""
print(count)

# 10. Вывести строку, удалив из нее повторные вхождения символов.

s = input()
s1 = ''
for elem in s:
    if elem not in s1:
        s1 += elem
print(s1)

# 11. Дана строка символов, состоящая из произвольных натуральных чисел, разделенных пробелами.
# Вывести четные числа этой строки.

s = input('enter sting:')
s +=" "
s1 =""
for i in range(len(s)):
    if s[i] != ' ':
        s1 += s[i]
    elif s[i] == " " and len(s1)>=1:
        if s1.isdigit():
            if int(s1) % 2 == 0:
                print(s1)
        s1 = ''

# 12. Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики
# студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы
# в строке. Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
# на этот символ и количество его повторений в этой позиции строки. Напишите программу,
# которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность
# на стандартный вывод. Кодирование должно учитывать регистр символов.
#
# Sample Input 1:
# Aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# Abc
# Sample Output 2:
# a1b1c1

s = input().lower()
s += ' '
s1 = ''
count = 1
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        s1 += s[i] +str(count)
        count = 1
print(s1)

# Дополнительные задачи:
#
# 13. С клавиатуры вводится натуральное число n <= 1000. Выведите n строк вида "На лугу n коров",
# склоняя слово "коров" в соответствии с числом n. Проверяем большие числа!!!
# Sample Input:
# 7
# Sample Output:
# На лугу 1 корова
# На лугу 2 коровы
# На лугу 3 коровы
# На лугу 4 коровы
# На лугу 5 коров
# На лугу 6 коров
# На лугу 7 коров
#
# 14. Числа Фибоначчи – известная числовая последовательность, в которой первые два члена равны единице,
# а каждый последующий получается сложением двух предыдущих.
# По введенному числу n выведите n чисел Фибоначчи через пробел.
# Sample Input:
# 8
# Sample Output:
# 1 1 2 3 5 8 13 21

f1 = 1
f2 = 1
n = int(input())
print(f1, f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')

#
# 15. Найти натуральное число из диапазона [n, m] (n, m – натуральные числа),
# которое имеет наибольшее количество делителей.
# 16. Даны натуральные числа n, m. Получить все числа меньше m взаимно простые с n.
#
