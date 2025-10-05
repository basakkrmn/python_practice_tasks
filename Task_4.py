#Kullanıcıdan iki sayı alan ve
# bu sayıların toplamını, farkını, bölümünü, çarpımını hesaplayıp ekrana yazdıran bir program yazın.
# (Bölme işleminde sıfıra bölünme kontrolü yapınız.)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2 ==0:
      print("Invalid operation! Cannot divide by zero!")
      return None
    else:
        return n1/n2

def printing_the_calculation(n1,n2):
    print("Addition: ",add(n1,n2))
    print("Subtraction: ",subtract(n1,n2))
    print("Multiplication: ", multiply(n1,n2))
    division_result =round(divide(n1,n2),2)
    print("Division: ",division_result)


number_1 =int(input("Please enter the first number: \n"))
number_2 =int(input("Please enter the second number: \n"))

printing_the_calculation(number_1,number_2)

