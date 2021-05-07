'''Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)=⎧⎩⎨⎪⎪1−(x+2)2,−x2,(x−2)2+1,при x≤−2при −2<x≤2при 2<x

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
Sample Input 1:

4.5

Sample Output 1:

7.25


Sample Input 2:

-4.5

Sample Output 2:

-5.25


Sample Input 3:

1

Sample Output 3:

-0.5
'''
# def f(x):
#     # put your python code here
#     if x<=-2:
#         f=1-(x+2)**2
#     elif x>-2 and x<=2:
#         f=-(x/2)
#     elif x>2:
#         f=(x-2)**2+1
#     return f
'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные
 значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного
  списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.'''

# def modify_list(l):
#     le = len(l)-1
#     i = le
#     while i!=-1:
#         if l[i]%2:
#             del l[i]
#         else:
#             l[i]=l[i]//2
#         i -=1
#     return
'''Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение по ключу 2⋅key.
Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''
#
# # не добавляйте кода вне функции
# def update_dictionary(d, key, value):
#     # put your python code here
#     if key in d:
#         d[key].append(value)
#         #print('ключ есть')
#     elif key is not d:
#         #d[2*key]=[]
#         if 2*key is d:
#             d[2*key].append(value)
#             #print('ключ 2*key уже есть')
#         elif (2*key is not d) and d.get(2*key)==None:
#             d[2*key]=[]
#             d[2*key].append(value)
#             #print('создание ключа и + новое значение списка')
#         elif (2*key is not d) and d.get(2*key)!=None:
#             d[2*key].append(value)
#             #print('создание ключа и + значение списка')
#     return
#
# # не добавляйте кода вне функции

'''Когда Антон прочитал «Войну и мир», ему стало интересно,
сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, 
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его 
повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным.

 Sample Input 1:

a aa abC aa ac abc bcd a

Sample Output 1:

a 2
aa 2
ac 1
abc 2
bcd 1


Sample Input 2:

a A a

Sample Output 2:

a 3
'''

# # put your python code here
# n='' #инициализация строки
# n = str(input())
# m = [] #инициализация списка
# m.append([str(s.lower()) for s in n.split()])
# d = {} #инициализация пустого словаря
# li, lj = len(m), len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p]+=1
#         else:
#             d[p] = 1
# for key,value in d.items():
#    print(key,value)

'''Имеется реализованная функция f(x), принимающая на вход целое число x, 
которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.

Функция вычисляется достаточно долго, ничего не выводит на экран, 
не пишет в файлы и зависит только от переданного аргумента x.

Напишите программу, которой на вход в первой строке подаётся число 
n — количество значений x, для которых требуется узнать значение 
функции f(x), после чего сами эти n значений, каждое на отдельной 
строке. Программа должна после каждого введённого значения аргумента 
вывести соответствующие значения функции f на отдельной строке. 

Для ускорения вычисления необходимо сохранять уже вычисленные значения
функции при известных аргументах.

Обратите внимание, что в этой задаче установлено достаточно сильное 
ограничение в две секунды по времени исполнения кода на тесте. 

 Sample Input:

5
5
12
9
20
12

Sample Output:

11
41
47
61
41'''

# # Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
# d = {}
# k = []
# n = int(input())
# for i in range(n):
#     x = int(input())
#     k.append(x)
# for j in range(0, len(k)):
#     key = k[j]
#     if key in d:
#         print(d[key])
#     elif key not in d:
#         p = k[j]
#         d[key] = f(p)
#         print(d.get(key))

'''Напишите программу, которая запускается 
из консоли и печатает значения всех переданных 
аргументов на экран (имя скрипта выводить не нужно).
Не изменяйте порядок аргументов при выводе.

Для доступа к аргументам командной строки программы 
подключите модуль sys и используйте переменную argv из этого модуля.

Пример работы программы:

> python3 my_solution.py arg1 arg2
arg1 arg2'''
# import sys
#
# s = ''
# s2 = ''
# for i in range(1, len(sys.argv)):
#     s = s + sys.argv[i] + ' '
# s2 = s
# print(s2, end=' ')
# digits = set('0123456789')
# i = 0
# multiplier = ''
# decrypted = ''
#
# with open('03_04_02_input.txt') as in_f_obj:
#     string = in_f_obj.readline().strip()
#
# char = string[i]
# i += 1
#
# while i < len(string):
#
#     while string[i] in digits:
#         multiplier += string[i]
#         i += 1
#         if i > (len(string) - 1):
#             break
#
#      # print(char * int(multiplier), end='')
#     decrypted += (char * int(multiplier))
#
#     multiplier = ''
#     if i > (len(string) - 1):
#         break
#     char = string[i]
#
#     i += 1
#
# with open('03_04_02_ouput.txt', 'w') as out_f_obj:
#     out_f_obj.write(decrypted)
# import re
#
# with open('dataset_3363_2 (2).txt', 'r+') as f:
#     a = re.split(r"(\d+)", f.readline())[:-1]
#     result = ''.join([y * int(x) for x, y in zip(a[1::2], a[::2])])
#     print(result)
#     f.seek(0)
#     f.write(result)
#
# dictionary = {}
#
# with open('03_04_03_input.txt') as in_f_obj:
#     for line in in_f_obj:
#         line = line.lower()
#         for word in line.split():
#             if word not in dictionary:
#                 dictionary[word] = 1
#             elif word in dictionary:
#                 dictionary[word] += 1
#
# max_quantity = 1
#
# for key, value in dictionary.items():
#     current_quantity = dictionary[key]
#     if current_quantity > max_quantity:
#         max_quantity = current_quantity
#         word_with_max_quantity = key
#
# with open('03_04_03_output.txt', 'w') as out_f_obj:
#     most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
#     out_f_obj.write(most_popular)

'''

#[STEPIK]
# Программирование на Python https://stepik.org/67
# 03_04_04 Файловый ввод/вывод

Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''
averages = []
marks_math = []
marks_phys = []
marks_rus = []
counter = 0
value01 = 0
value02 = 0
value03 = 0

with open('03_04_04_input.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.rstrip().split(';')
        student_average = ((int(line[1]) + int(line[2]) + int(line[3])) / 3)
        averages.append(student_average)
        marks_math.append(int(line[1]))
        marks_phys.append(int(line[2]))
        marks_rus.append(int(line[3]))
        counter += 1

with open('03_04_04_output.txt', 'w') as out_f_obj:
    for _ in averages:
        out_f_obj.write(str(_) + '\n')

    for _ in marks_math:
        value01 += int(_)
    for _ in marks_phys:
        value02 += int(_)
    for _ in marks_rus:
        value03 += int(_)
    average_math = value01 / counter
    average_phys = value02 / counter
    average_rus = value03 / counter

    out_f_obj.write(str(average_math) + ' ' + str(average_phys) + ' ' + str(average_rus))