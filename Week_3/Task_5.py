import math
# Dört işlem yapan bir hesap makinesi fonksiyonu yazın.
# - Toplama, çıkarma, çarpma, bölme işlemleri
# - Kullanıcıdan işlem tipi ve sayıları input ile alın
# - Bölme işleminde sıfıra bölme hatasını try-except ile yakalayın
# - Geçersiz işlem girilirse uygun mesaj verin
# - Lambda ifadeleri kullanarak işlemleri tanımlayın


def calculator():
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y

    operation = input("Enter operation (+, -, *, /): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            try:
                result = divide(num1, num2)
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                result = None
        else:
            print("Invalid operation!")
            result = None

        if result is not None:
            print(f"The result of {num1} {operation} {num2} is {result}")

    except ValueError:
        print("Invalid input! Please enter a number.")



if __name__ == "__main__":
    calculator()


