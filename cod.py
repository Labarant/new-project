print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225


num1 = int(input('Введите первое число '))
num2 = int(input('Введите второе число '))
rev = ''
rev2 =''
summ_rev = ''
print()
while(num1 > 0):
  dig = num1 % 10
  rev += str(dig)
  num1 = num1 // 10
print("Первое число в обратном порядке:", int(rev))
while(num2 > 0):
  dig = num2 % 10
  rev2 += str(dig)
  num2 = num2 // 10
print("Второе число в обратном порядке:", int(rev2))
print()
summ = int(rev) + int(rev2)
print('Сумма', summ)
while(summ > 0):
  dig = summ % 10
  summ_rev  += str(dig)
  summ = summ // 10

print('Сумма наоборот', summ_rev )  
