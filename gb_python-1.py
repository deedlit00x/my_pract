# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

a = 1
b = 2
str1 = input("Введите первую строку ")
str2 = input("Введите вторую строку ")
num1 = int(input("Введите первое число "))
num2 = int(input("Введите второе число "))

print("a = ", a, "b = ", b)
print(f'Введеные значения - {str1}, {num1}, {str2}, {num2}')

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите время в секундах "))
h = time // 3600
m = (time - h * 3600) // 60
s = time - (h * 3600 + m * 60)

print(f'чч:мм:сс: {h} : {m} : {s}')


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input("Введите число: "))
tmp = str(num)
tmpOne = int(str(num) + str(num))
tmpTwo = int(str(num) + str(num) + str(num))
sumTotal = (num + tmpOne + tmpTwo)

print(f'Сумма чисел {num} + {tmpOne} + {tmpTwo} = {sumTotal}')
# можно записать в одну строку без создания доп переменных.
# sumTotal = (num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = abs(int(input("Введите целое положительное число: ")))
n_max = n % 10

while n >= 0:
    n = n // 10
    if n % 10 > n_max:
        n_max = n % 10
    elif n > 9:
        continue
    else:
        print(f'Максимальное цифра в числе {n_max}')
        break

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = int(input("Введите прибыль "))
costs = int(input("Введите издержки "))

if profit > costs:
    print(
        f"Фирма работает в плюс. Рентабельность выручки составила {profit / costs:.1f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(
        f"прибыль в расчете на одного сторудника составила {profit / workers:.0f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:

# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

distance = int(input("Введите результаты пробежки первого дня в км: "))
desired_distance = int(input("Введите общий желаемый результат в км: "))
day = 1

print(f'результат пробежки {day}-го дня равен {distance}')
while distance < desired_distance:
    distance *= 1.1
    day += 1
    print(f'результат пробежки {day}-го дня равен {round(distance, 2)}')
print(f'Вы достигнете требуемых показателей на {day} день')
