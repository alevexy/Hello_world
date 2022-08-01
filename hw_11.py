# 1. Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных 9 классах (9а, 9б, 9в, 9м, 9ф и т. п.).
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
# б) в школе появился новый класс.
# в) в школе был расформирован (удален) другой класс.
# г) Вычислите общее количество учащихся 9 классов в школе.
# school = {'9a': 21, '9b': 19, '9c': 23}
# school['9b'] = 16
# school['9d'] = 17
# del school['9c']
# print(school)
# print(sum(school.values()))
# 2. Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для введённого слова вывести его синоним или написать что его нет.

# d = {'красивый': 'прекрасный', 'ошибка': 'неудача'}
#
# while True:
#     k = input('введите слово:')
#     if k in d:
#         if k == 'красивый':
#             print(d['красивый'][:])
#         elif k == 'ошибка':
#             print(d['ошибка'][:])
#     elif k == 'выход':
#         print('выход')
#         break
#     else:
#         print('синонима нет')

# 3. Коля устал запоминать телефонные номера и заказал у Вас программу, которая заменила бы ему телефонную книгу.
# Коля может послать программе два вида запросов: строку, содержащую имя контакта и его номер,
# разделенные пробелом, или просто имя контакта. В первом случае программа должна добавить в книгу новый номер,
# во втором – вывести номер контакта. Ввод происходит до символа точки.
# Если введенное имя уже содержится в списке контактов, необходимо перезаписать номер.
# Sample Input:
# Ben 89001234050
# Alice 210-220
# Alice
# Alice 404-502
# Ben
# Nick +4(908)273-22-42
# Nick
# Alice
# Robert 51234047129
# .
# Sample Output:
# 210-220
# 89001234050
# +4(908)273-22-42
# 404-502


# 4. Стремясь стать программистом, важно не только постоянно учиться, но и понимать язык,
# на котором говорят Ваши коллеги. Чтобы систематизировать знания, Вы решили написать программу,
# которая составляет маленький словарь из сленговых выражений.
# Программа принимает на вход строки до символа точки, состоящие из понятий и их определений,
# разделенных знаком тире.
# После заполнения словаря программе передается натуральное число m – количество запросов,
# а затем m строк, каждая из которых представляет собой одно понятие.
# Если это понятие есть в словаре, необходимо вывести его определение, в обратном случае – "Не найдено".
#
# Sample Input:
# DNS – компьютерная система для получения, хранения и обработки информации о доменных именах
# Интрасеть – это замкнутая внутренняя сеть какой-либо организации, работающая по Интернет-протоколу TCP/IP
# Фича – недокументированная дополнительная возможность, фишка
# Мейнфрейм – большой компьютер, имеющий высокую вычислительную мощность
# .
# 4
# Бэкап
# Фича
# Линуксоид
# DNS
# Sample Output:
# Не найдено
# недокументированная дополнительная возможность, фишка
# Не найдено
# компьютерная система для получения, хранения и обработки информации о доменных именах
#
#

# Дополнительные задачи:
# 5. Когда Антон прочитал «Войну и мир», ему стало интересно,
# сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы,
# которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого
# уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество".
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3
#
#
# 6. Коля понял, что у многих из его знакомых есть несколько телефонных номеров
# и нельзя хранить только один из них. Он попросил доработать Вашу программу так,
# чтобы можно было добавлять к существующему контакту новый номер или даже несколько номеров,
# которые передаются через запятую.
#
#  По запросу телефонного номера должен выводиться весь список номеров в порядке добавления,
#  номера должны разделяться запятой. Если у контакта нет телефонных номеров,
#  должна выводиться строка "Не найдено".
# Sample Input:
# Ben 89001234050, +70504321009
# Alice 210-220
# Alice
# Alice 404-502, 894-005, 439-095
# Nick +16507811251
# Ben
# Alex +4(908)273-22-42
# Alice
# Nick
# Robert 51234047129, 92174043215
# Alex
# Robert
#
# Sample Output:
# 210-220
# 89001234050, +70504321009
# 210-220, 404-502, 894-005, 439-095
# +16507811251
# +4(908)273-22-42
# 51234047129, 92174043215
#


