# Отримання числа від користувача
number = int(input("Введіть число: "))

# Перемноження цифр, поки число не стане менше або дорівнювати 9
while number > 9:
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10
    number = product

print(number)





