try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе числоЖ "))

    result = num1 / num2
    print(f"Результат деления: {result}")

except ValueError:
    print("Ошибка! Вы ввели не число. Пожалуйста, вводите только цифры.")

except ZeroDivisionError:
    print("Ошибка! На ноль делить нельзя.")
