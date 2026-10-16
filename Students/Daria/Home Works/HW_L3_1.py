number = input("Input first number:")
operation = input("Input operation (+ or -):")

match operation:
    case "+":
        print(int(number) + int(input("Input second number:")))
    case "-":
        print( int(number) - int(input("Input second number:")))



