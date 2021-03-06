# Задача 1. Тайны археологии


# Что нужно сделать

# Археолог Ирина в последней экспедиции нашла древнюю глиняную табличку с числами 114 12 14 10605 4907 450. Ирина предположила, что это шифр, который можно расшифровать с помощью компьютерной программы.

# Помогите Ирине — напишите программу, которая будет выводить на экран числа, соответствующие следующему условию: они чётные и делятся на три. Для подходящих чисел программа выводит сообщение «Число подходит». Для неподходящих под условие — «Число не подходит».

# print('Задача 1. Тайны археологии\n')

# for num in 114, 12, 14, 10605, 4907, 450:
#   if num % 2 == 0 and num % 3 != 0:
#     print('Число подходит: ', num)
#   else:
#     print('Число не подходит: ', num)
    

# Задача 2. Должники


# Что нужно сделать

# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой номер. У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт нам номер с отрицательным значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя, то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.

# print('Задача 2. Должники\n')

# pos_num = 0

# for num in range(10):
#   user_num = int(input('Введите число: '))
#   if user_num % 2 == 0 and user_num > 0:
#     # print('Число {} положительное и больше 0\n'.format(user_num))
#     pos_num += 1
# print('Одновременно четных и положительных чисел: ', pos_num)


# Задача 3. Посчитай чужую зарплату...


# Что нужно сделать

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу, которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев и выводит на экран среднюю зарплату за год.


# print('Задача 3. Посчитай чужую зарплату...\n')

# user_salary = 0

# for num in range(1, 13):
#   user_num = int(input('Введите зарплату сотрудника за месяц №: {} '.format(num)))
#   user_salary += user_num
# user_salary = user_salary // 12
# print('Средняя зарплата содруника за год составляет {} рублей'.format(user_salary))

# Задача 4. С заботой о природе


# Что нужно сделать

# Огромный заповедник поделён на большое количество секторов. Все сектора пронумерованы. Вы устроились на работу лесничим и отвечаете за группу секторов с номерами 30–35.

# В ваши обязанности входит:

#     следить за тем, чтобы посетителей в каждом секторе было не больше десяти;
#     фиксировать количество нарушений этого правила.

# Напишите программу, которая для каждого сектора запрашивает текущее количество людей в нём, и если оно больше десяти, то фиксирует нарушение. В конце выведите количество нарушений.


# Пример:

# Людей в 30-м секторе: 7

# Всё спокойно.

# Людей в 31-м секторе: 11

# Нарушение! Слишком много людей в секторе!

# Людей в 32-м секторе: 100

# Нарушение! Слишком много людей в секторе!

# Людей в 33-м секторе: 10

# Всё спокойно.

# Людей в 34-м секторе: 0

# Всё спокойно.

# Людей в 35-м секторе: 1

# Всё спокойно.

# Количество нарушений: 2


# print('Задача 4. С заботой о природе\n')
 
# count = 0

# for num in range(30, 36):
#   guest_count = int(input('Введите кол-во посетителей: '))
#   if guest_count > 10:
#     count += 1
#     print('Людей в {} секторе: {}\nНарушение! Слишком много людей в секторе!'.format(num, guest_count))
#   else:
#     print('Людей в {} секторе: {}\nВсё спокойно.'.format(num, guest_count))

# print('Количество нарушений: {}'.format(count))

# Задача 5. Факториал


# Что нужно сделать

# Мы всё ближе и ближе подбираемся к серьёзной математике. Одна из классических задач — задача на нахождение факториала числа. И в будущем мы с ней ещё встретимся.


# Дано натуральное число n. Напишите программу, которая находит n! (n-факториал).


# Запись n! означает следующее:


# n! = 1 * 2 * 3 * 4 * 5 * … * n


# Пример:

# Введите число: 5

# Факториал числа 5 равен 120

# print('Задача 5. Факториал\n')
 
# n = int(input('Введите число: '))
# factorial = 1

# for num in range(2, n + 1):
#     factorial *= num
    
# print('факториал числа {}: {}'.format(n, factorial))

# Задача 6. Успеваемость в классе


# Что нужно сделать

# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. Напишите программу, которая получает список оценок — N чисел — и выводит на экран сообщение о том, кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

# print('Задача 6. Успеваемость в классе\n')
 
# n = int(input('Введите кол-во учеников: '))
# five_count = 0
# four_count = 0
# third_count = 0

# for num in range(1, n + 1):
#     est = int(input('введите оценку ученика № {}: '.format(num)))
#     if est == 5: 
#       five_count +=1
#     elif est == 4: 
#       four_count +=1
#     elif est == 3: 
#       third_count +=1
      
# if five_count > four_count and five_count > third_count:
#   print('Сегодня больше отличников')
# elif five_count < four_count and four_count > third_count: 
#   print('Сегодня больше хорошистов')
# else:
#   print('Сегодня больше троечников')

# Задача 7. Отрезок


# Что нужно сделать

# Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.

# print('Задача 7. Отрезок\n')
 
# start_num = int(input('Введите начало отрезка'))
# finish_num = int(input('Введите конец отрезка'))
# count = 0
# summ = 0

# for num in range (start_num, finish_num + 1):
#   if num % 3 == 0:
#     summ += num
#     count += 1
    
# print(summ / count )

# Задача 8. Замечательные числа


# Что нужно сделать

# Напишите программу, которая находит и выводит все двузначные числа, которые равны утроенному произведению своих цифр. К таким относятся, например, 15 и 24.

# print('Задача 8. Замечательные числа\n')

# for num in range(10, 100):
#   n = (((num // 10 % 10) * (num % 10)) * 3)
#   if n == num:
#     print(n)

# Задача 9. ...Теперь можно посчитать и свою


# Что нужно сделать

# Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно, а не зря ли она работает столько времени на одном месте? Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.

# Пользователь вводит десять чисел. Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

# print('Задача 9. ...Теперь можно посчитать и свою\n')

# prev_sal = (int(input('Введите свою зарплату за первый месяц: ')))
# sal_pos = 0
# sal_neg = 0
# sal_not = 0

# for i in range(2, 10 + 1):
#   user_num = int(input('Введите свою зарплату за {} месяц: '.format(i)))
#   if user_num > prev_sal:
#     sal_pos += 1
#   elif user_num < prev_sal:
#     sal_neg += 1
#   else:
#     sal_not += 1

#   prev_sal = user_num

# print('за данный год , зарплата возросла {} раз, колебалась падением {} раз, а также {} раз осталась неизменной'.format(sal_pos, sal_neg, sal_not))

# Задача 10. Пропавшая карточка


# Что нужно сделать

# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Напишите программу, которая поможет найти потерянную карточку, если номера оставшихся известны. Найдите её, зная номера оставшихся карточек.

# Введите число карточек — N.

# Затем последовательно введите N – 1 номера оставшихся карточек

# Правильно:

# if a > 1:

#   b = 3

# else:

#   b = 5


# Неправильно:

# If a > 1:

#   b = 3

# else:

#     b = 5
    
    
    
# print('Задача 10.\n')
 
# user_num = int(input('Введите размер колоды: '))
# user_count = 0

# for num in range(user_num + 1):
#   user_count += num

# for n in range(user_num - 1):
#   user_answer = int(input('Введите номера оставшихся карточек: '))
#   user_count -= user_answer

# print('номер потерянной карточки: {}'.format(user_count))