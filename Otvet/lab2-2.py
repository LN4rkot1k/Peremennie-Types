# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python
number = 9
print(type(number))   # Вывод типа переменной number
float_number = 9.0
# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
bool_number = False
str_number = '9'
print(type(bool_number), type(str_number))
# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

print(int(bool_number))
print(int(str_number))
print(float(bool_number))
print(float(str_number))
print(str(bool_number))
print(str(str_number), "\n")
print(int(float_number), "\n", type(int(float_number)))