# 1) Дана строка. Ввод через input()
# - Сначала выведите третий символ этой строки.
# - Во второй строке выведите предпоследний символ этой строки.
# - В третьей строке выведите первые пять символов этой строки.
# - В четвертой строке выведите всю строку, кроме последних двух символов.
# - В пятой строке выведите все символы с четными индексами
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# - В седьмой строке выведите все символы в обратном порядке.
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# - В девятой строке выведите длину данной строки.
s = input('enter string: ')
print(s[2])
print(s[-2])
print(s[:4])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# 2) Дано слово. Верно ли, что оно начинается и оканчивается на одну и ту же букву?

w = input('enter word: ')
if w[0] == w[-1]:
    print(True)
else:
    print(False)

# 3) Дано слово. Получить его часть, образованную второй, третьей и четвертой буквами.

w = input('enter word: ')
w1 = w[1] + w[2] + w[3]
print(w1)

# 4) Из слова яблоко путем "вырезок" и "склеек" его букв получить слова блок и око.

w = 'яблоко'
w1 = w[1:5]
w2 = w[3:]
print(w1)
print(w2)

# 5) Дана строка “*”. Получить строку, состоящую из пяти звездочек (символов "*").

s = '*'
s1 = s * 5
print(s1)

# 6) Проверить является ли строка палиндромом.(шалаш).

s = input('enter string: ')
if s[::] == s[::-1]:
    print('yes')
else:
    print('no')

# 7) Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого появления и количество букв f.
# Если буква f в данной строке не встречается, ничего не выводите.



# 8)Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1,
# а если не встречается ни разу, выведите число -2.




# 9)Дана строка. Замените в этой строке все цифры 1 на слово one.

s = input('enter string: ')
print(s.replace('1', 'one'))

# 10) Напишите программу, которая вычисляет процентное содержание символов g и c в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
# Sample Input:
# aCggtGttat
# Sample Output:
# 40

s = input('enter string: ')
s = s.lower()
s1 = (s.count('g') * 100 / len(s)) + (s.count('c') * 100 / len(s))
print(s1)


# 11) Уберите точки из введенного IP-адреса. Выведите сначала четыре числа через пробел, а затем сумму получившихся чисел.
# Sample Input:
# 192.168.0.1
# Sample Output:
# 192 168 0 1
# 361

s = input('enter string: ')
s = s.replace('.', ' ')
print(s)
a = int(s[:3])
b = int(s[4:7])
c = int(s[8])
d = int(s[10])
print(a + b + c + d)