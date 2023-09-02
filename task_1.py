# https://github.com/YaDmitryE/py_lesson_7

# Введите строку без пробелов
string = input("Введите строку без пробелов: ")

# Сравниваем строку с её обратным порядком символов
if string == string[::-1]:
    print("yes")
else:
    print("no")
