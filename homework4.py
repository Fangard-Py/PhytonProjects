# Организация программы
my_string = input("Привет, как мне к Вам обращаться? ")
number = len(my_string)
print(number)

# Работа с методами строк
my_string = input("Привет, как мне к Вам обращаться? ")

print("Привет,", my_string.upper())
print("Привет,", my_string.lower())
print("Привет,", my_string[0])
print("Привет,", my_string[-1])

my_string = input("Привет, Как Мне К Вам Обращаться? ".replace(' ', ''))
