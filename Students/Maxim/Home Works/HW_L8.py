try:
    n_1 = int(input("Enter first number: "))
    n_2 = int(input("Enter second number: "))

    print(f'Result is: {n_1 / n_2:.2f}')
except ValueError:
    print("Input only numbers")
except ZeroDivisionError:
    print("U cant devide by zero")
