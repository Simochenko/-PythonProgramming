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
# '''
# averages = []
# marks_math = []
# marks_phys = []
# marks_rus = []
# counter = 0
# value01 = 0
# value02 = 0
# value03 = 0
#
# with open('03_04_04_input.txt') as in_f_obj:
#     for line in in_f_obj:
#         line = line.rstrip().split(';')
#         student_average = ((int(line[1]) + int(line[2]) + int(line[3])) / 3)
#         averages.append(student_average)
#         marks_math.append(int(line[1]))
#         marks_phys.append(int(line[2]))
#         marks_rus.append(int(line[3]))
#         counter += 1
#
# with open('03_04_04_output.txt', 'w') as out_f_obj:
#     for _ in averages:
#         out_f_obj.write(str(_) + '\n')
#
#     for _ in marks_math:
#         value01 += int(_)
#     for _ in marks_phys:
#         value02 += int(_)
#     for _ in marks_rus:
#         value03 += int(_)
#     average_math = value01 / counter
#     average_phys = value02 / counter
#     average_rus = value03 / counter
#
#     out_f_obj.write(str(average_math) + ' ' + str(average_phys) + ' ' + str(average_rus))


# 03_06_02 Установка дополнительных модулей

'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям). 
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.
'''
# import requests
#
# with open('03_06_02_input.txt') as in_f_obj:
#     url = in_f_obj.read().strip()
#
# r = requests.get(url)
# counter = 0
#
# for line in r.text.splitlines():
#     counter += 1
#
# # Цикл выше можно заменить более простой конструкцией
# # print(len(r.text.splitlines()))
#
# with open('03_06_02_output.txt', 'w') as out_f_obj:
#     out_f_obj.write(str(counter))


# 03_06_03 Установка дополнительных модулей

'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''
# import requests
#
# url_pattern = 'https://stepik.org/media/attachments/course67/3.6.3/'
#
# with open('03_06_03_input.txt') as in_f_obj:
#     url = in_f_obj.read().strip()
#
# counter = 0
#
# while True:
#     r = requests.get(url)
#     if 'We' in str(r.text.strip()):
#         break
#     url = url_pattern + str(r.text.strip())
# # print(str(counter) + ' ' + url)
# # counter += 1
#
# text = r.text.strip()
#
# with open('03_06_03_output.txt', 'w') as out_f_obj:
#     out_f_obj.write(text)


# 03_07_01 Задачи по материалам недели

'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''
#
# n = int(input())
# x_list = [input().split(';') for x in range(n)]
# vs = [(x[0], x[2]) for x in x_list]
# import itertools
# clubs = set(itertools.chain.from_iterable(vs))
# res = {club:[0, 0, 0, 0, 0] for club in clubs}
# for kom1, gol1, kom2, gol2 in x_list:
#     res[kom1][0] += 1
#     res[kom2][0] += 1
#     if int(gol1) > int(gol2):
#         res[kom1][1] += 1
#         res[kom1][4] += 3
#         res[kom2][3] += 1
#     elif int(gol1) < int(gol2):
#         res[kom2][1] += 1
#         res[kom2][4] += 3
#         res[kom1][3] += 1
#     elif int(gol1) == int(gol2):
#         res[kom1][2] += 1
#         res[kom1][4] += 1
#         res[kom2][2] += 1
#         res[kom2][4] += 1
# for club in clubs:
#     print('{}:{}'.format(club, ' '.join(map(str, res[club]))))


# 03_07_02 Задачи по материалам недели

'''
Дополнительная
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то
 странным набором звуков. 
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. 
заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и 
теперь нуждаются в помощи: 
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
 одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
  после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
 которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac
Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
'''

# string = str(input())
# cipher = str(input())
#
# message_to_cipher = str(input())
# cipher_to_message = str(input())
# ciphered_message = ''
# unciphered_message = ''
#
# encryption = {}
#
# # Наполняем шифровальный словарь
# for i in range(len(string)):
#     encryption[string[i]] = cipher[i]
#
# # Зашифровываем сообщение по наполненному словарю
# for i in range(len(message_to_cipher)):
#     for key in encryption.keys():
#         if message_to_cipher[i] == key:
#             ciphered_message += encryption[key]
#
# # Расшифровываем сообщение по наполненному словарю
# for i in range(len(cipher_to_message)):
#     for key, value in encryption.items():
#         if cipher_to_message[i] == value:
#             unciphered_message += key
#
# print(ciphered_message)
# print(unciphered_message)

# 03_07_03 Задачи по материалам недели

'''
Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.
Через стандартный ввод подаётся следующая структура: первой строкой — количество dd записей в списке известных слов, после передаётся  dd строк с одним словарным словом на строку, затем — количество ll строк текста, после чего — ll строк текста.
Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:
aab
aba
c
aaa
'''

# d = int(input())
# # words = []
# words = set()
# # unknow_words = []
# unknow_words = set()
#
# for _ in range(d):
#     # words.append(input().lower())
#     words.add(input().lower())
#
# l = int(input())
#
# for _ in range(l):
#     string = input().lower().split()
#
#     for i in range(len(string)):
#         if string[i] not in words:
#             # unknow_words.append(string[i])
#             unknow_words.add(string[i])
#
# for word in unknow_words:
#     print(word)

# 03_07_04 Задачи по материалам недели

'''
Группа биологов в институте биоинформатики завела себе черепашку.
После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.
Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.
Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего nn строк с самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты целочисленные.
Sample Input:
4
север 10
запад 20
юг 30
восток 40
Sample Output:
20 -20
'''

# n = int(input())
# movement = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
#
#
# for _ in range(n):
#     direction = input().split()
#     if direction[0] in movement:
#         movement[direction[0]] += int(direction[1])
#
# x = movement['восток'] - movement['запад']
# y = movement['север'] - movement['юг']
#
# print(x, y)


# 03_07_05 Задачи по материалам недели

'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

# class_rawinfo = {}
# #new_heights = 0
# #new_students = 0
# class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
# #class_info = []
#
# with open('03_07_05_input.txt') as in_f_obj:
# 	for line in in_f_obj:
# 		#print(line)
# 		string = line.rstrip().split('\t')
# 		#print(string)
# #n = int(input())
# #for _ in range(n):
# 	#string = input().split('	')
# 		if string[0] not in class_rawinfo:
# 			class_rawinfo[string[0]] = [int(string[2]), 1]
# 		elif string[0] in class_rawinfo:
# 			heights = class_rawinfo[string[0]][0] + int(string[2])
# 			students = class_rawinfo[string[0]][1] + 1
# 			class_rawinfo[string[0]] = [heights, students]
#
# for k, v in class_rawinfo.items():
# 	#print(k, str(v[0] / v[1]))
# 	#list.pop([int(k)-1])
# 	class_info[int(k)-1] = v[0] / v[1]
# 	#print(class_rawinfo)
# 	#print(class_info)
#
# with open('03_07_05_output.txt', 'w') as out_f_obj:
# 	for i in range(len(class_info)):
# 		#print(i+1, str(class_info[i]))
# 		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
# 		#print(output)
# 		out_f_obj.write(output)