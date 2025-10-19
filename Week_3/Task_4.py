import math
# Kullanıcıdan bir sayı girmesini isteyen ve bu sayının  karekökünü hesaplayan bir program yazın.
# - Negatif sayı girilirse uygun hata mesajı verin
# - Sayı yerine metin girilirse uygun hata mesajı verin
# - Try-except blokları kullanın

user_input = input("Please enter a number: ")

try:
    number = float(user_input)  # for int or float
    if number >= 0:
        sqrt_number = math.sqrt(number)
        print(f"The square root of {number} is {sqrt_number:.2f}")
    else:
        print("Negative numbers are not allowed!")

except ValueError:
    print("Invalid input! Please enter a valid number.")

