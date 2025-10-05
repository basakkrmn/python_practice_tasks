#	Kullanıcı kayıt ve giriş sistemi oluşturun.
#•	Kullanıcı adı en az 3 karakter olmalı.
#•	 Şifre en az 6 karakter ve en az 1 rakam içermeli.
#•	E-mail’de “@” işareti olmalı.
#•	Yaş 13’ten büyük olmalı.
# Tüm koşullar sağlanıyorsa True, değilse False döndürsün.

print("---Welcome to the login and register system---")
print("Please follow the rules to register: ")
print("1. Username must be at least 3 characters long.")
print("2. Password must be at least 6 characters long and contain at least 1 number.")
print("3. Email must contain the '@' symbol.")
print("4. Age must be greater than 13.\n")


username = input("Please enter your username: \n")
password = input("Please enter your password: \n")
email = input("Please enter your email: \n")
user_age = int(input("Please enter your age: \n"))


valid_username = len(username) >= 3
valid_password = len(password) >= 6 and any(char.isdigit() for char in password)
valid_email = "@" in email
valid_age = user_age > 13


if not valid_username:
    print("Username must be at least 3 characters!")
if not valid_password:
    print("Password must be at least 6 characters and contain at least 1 number!")
if not valid_email:
    print("Email must contain '@' symbol!")
if not valid_age:
    print("You must be older than 13!")


validation = valid_username and valid_password and valid_email and valid_age


if validation:
    print("\nRegistration successful!")
else:
    print("\nInvalid situation, please try again.")

print("Validation status:", validation)


