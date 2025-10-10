#Kullanıcının yaşına ve gelirine göre kredi başvurusu değerlendiren program yazın.
#•	Yaş 18-65 arası ve gelir 5000’den fazla: “Kredi onaylandı.”
#•	Yaş 18-65 arası ve gelir 5000’den az: “Geliriniz yetersiz.”
#•	Yaş 65’ten büyük: “Yaşınız kredi için uygun değil.”

print("---Credit Application System---")
print("Please note the rules for credit approval:")
print("1. If your age is less than 18, you are not eligible for credit.")
print("2. If your age is between 18 and 65 and your income is greater than 5000, your credit will be approved.")
print("3. If your age is between 18 and 65 and your income is 5000 or less, your income is insufficient.")
print("4. If your age is over 65, you are not eligible for credit.\n")


user_age=int(input("Please enter your age: \n"))
user_income=float(input("Please enter your income: \n"))

if  not 18 <= user_age <= 65:
    print("You are not eligible for credit.")
else:
   if user_income >5000:
       print("Your credit will be approved.")
   else:
       print("Your income is insufficient.")


