# Составить функцию, которая напечатает 40 любых символов.
# Вариант 20

def generate_random_string(num):
    x = input("Введите случайный символ: ")
    print(str(x) * num)

generate_random_string(40)