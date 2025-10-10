# Range fonksiyonunu kullanarak;
# a)	1’den 100’e kadar olan çift sayıların toplamını bulun.
# b)	50’den geriye doğru 40’a kadar olan sayıları yazdırın.

print("---Task A---")
sum_even =0
numbers=range(2,101,2)
for number in numbers:
    sum_even += number

print(f"The sum of even numbers 1 to 100 is : {sum_even}")

print("---Task B---")
back_number = range(50,40,-1)

print("Numbers from 50 down to 40:", list(back_number))

