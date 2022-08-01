'''1)	Напишите программу, которая проверяет последнюю цифру числа.
Если последняя цифра числа 3, то вывести True иначе вывести False
'''
number = int(input('enter number: '))
if number % 10 == 3:
    print(True)
else:
    print(False)
'''
2)	Напишите программу, которая выводит True, если хотя бы одно из чисел А, В, С отрицательно. 
Если нет вывести False. Числа вводятся с клавиатуры в одной строке.
'''
A, B, C = map(int,input('enter A B C: ').split())
if A < 0 or B < 0 or C < 0:
    print(True)
else:
    print(False)
'''
3)	Верно ли что, целые n и k имеют одинаковую четность.
'''
n, k = map(int,input('enter n, k:').split())
if n % 2 == k % 2:
    print(True)
else:
    print(False)
'''
4)	Напишите программу, которая выводит True если число Х кратно 3 и заканчивается на 5.
Число х вводится с клавиатуры.
'''
X = int(input('enter X:'))
if X % 3 == 0 and X % 10 == 5:
    print(True)
else:
    print(False)
'''
5)	Найти количество четных чисел среди заданных трех целых чисел.
В ответе вывести количество четных чисел.
'''
a, b, c = map(int,input('enter a, b, c:').split())
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print(3)
elif (a % 2 == 0 and b % 2 != 0 and c % 2 != 0) or (b % 2 == 0 and a % 2 != 0 and c % 2 != 0) or (c % 2 == 0 and b % 2 != 0 and a % 2 != 0):
    print(1)
elif (a % 2 == 0 and b % 2 == 0) or (c % 2 == 0 and b % 2 == 0) or (a % 2 == 0 and c % 2 == 0):
    print(2)

'''
6)	Дано двузначное число. Определить является ли сумма его цифр двузначным числом.
(Ответ: Да/Нет)
'''
x = int(input('enter x:'))
y = x//10 + x % 10
if 10 <= y <= 99:
    print('Да')
else:
    print('Нет')
'''
7)	Дано четырёхзначное число. Проверить, одинаковы ли все цифры в нём.
'''
x = int(input('enter x:'))
a = x // 1000
b = (x % 1000) // 100
c = (x % 100) // 10
d = x % 10
if a == b == c == d:
    print(True)
else:
    print(False)

    x = int(input('enter x:'))
    if x % 1111 == 0:
        print(True)
    else:
        print(False)


x = input('enter x:')
if x[0] == x[1] == x[2] == x[3]:
    print(True)
else:
    print(False)
'''
8)	Напишите программу, принимающую на вход год и выводящую "Високосный",
если в этом году действительно 366 дней, и "Не високосный" иначе. 
Год считается високосным, если его номер делится на 4, но не делится на 100 или же делится на 400.
'''
year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный')
else:
    print("Не високосный")

'''9)	Объяснить результат и вывести на экран результат логического выражения  T = S для заданных значений логических переменных a, b, c.
+   логическое сложение   (логическое «или») or 
•    логическое умножение (логическое «и») and
 ¯  логическое отрицание (логическое «не») not
'''
a = True
b = False
c = False
T = a and not (b or c)
print(T)
a = True
b = False
c = True
S = a and not b or a and c
print(S)
if T == S:
    print(T, '=', S)
else:
    print(T, 'не равно', S)


'''10) Поле  шахматной доски определяется парой натуральных чисел, каждое из которых не превосходит 8:
 первое – номер вертикали, второе – номер горизонтали. Заданы натуральные числа x1, y1, x2, y2.
a)	Определить, являются ли поля (x1, y1) и (x2, y2) одного  цвета?
b)	На поле (x1, y1) расположен ферзь. Угрожает ли он полю (x2, y2)?
c)	На поле (x1, y1) стоит ладья, на поле (x2, y2) – пешка. Определить, бьет ли ладья пешку,
пешка – ладью или фигуры не угрожают друг другу.
d)	На поле (x1, y1) стоит слон, на поле (x2, y2) – конь. Определить, бьет ли слон коня,
конь – слона или фигуры не угрожают друг другу.'''

#a
x1, y1 = map(int, input("введите координаты поля 1").split())
x2, y2 = map(int, input("введите координаты поля 2").split())
if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print('поля одного цвета')
    else:
        print('поля разных цыетов')
else:
     print("не корректно введены координаты поля")

#b
x1, y1 = map(int, input("введите координаты ферзя: ").split())
x2, y2 = map(int, input("введите координаты фигуры: ").split())
if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
    if x1 == x2 and y1 == y2:
        print("фигуры стоят на одной клетеке")
    elif x1 == x2 or y2 == y1:
        print('ферзь бъёт')
    elif (x1 - x2) * (x1 - x2) == (y1 - y2) * (y1 - y2):
        print('ферзь бьет')
    else:
        print('ферзь не угражает фигуре')
else:
    print("не корректно введены координаты фигур")

#c
x1, y1 = map(int, input("введите координаты ладьи: ").split())
x2, y2 = map(int, input("введите координаты пешки: ").split())
if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
    if x1 == x2 and y1 == y2:
        print("фигуры стоят на одной клетке")
    elif x1 == x2 or y2 == y1:
        print('ладья бъёт пешку')
    elif x2 + 1 == x1 or x2 - 1 == x1:
        print('пешка бьет ладью')
    else:
        print('фигуры не угражают друг другу')
else:
    print("не корректно введены координаты фигур")

#d
x1, y1 = map(int, input("введите координаты слона: ").split())
x2, y2 = map(int, input("введите координаты коня: ").split())
if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
    if x1 == x2 and y1 == y2:
        print("фигуры стоят на одной клетке")
    elif (x1 - x2) * (x1 - x2) == (y1 - y2) * (y1 -y2):
        print('слон бъёт коня')
    elif (x1 + 1 == x2 and y1 - 2 == y2) or (x1 + 1 == x2 and y1 + 2 == y2) or (x1 + 2 == x2 and y1 - 1 == y2) or (x1 + 2 == x2 and y1 + 1 == y2) or (x1 - 1 == x2 and y1 + 2 == y2) or (x1 - 1 == x2 and y1 - 2 == y2) or (x1 - 2 == x2 and y1 + 1 == y2) or (x1 - 2 == x2 and y1 - 1 == y2):
        print('конь бьет слона')
    else:
        print('фигуры не угражают друг другу')
else:
    print("не корректно введены координаты фигур")
