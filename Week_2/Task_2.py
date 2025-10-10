#İç içe for döngüleri kullanarak 1’den 10’a kadar olan sayıların çarpım tablosunu oluşturan
# bir program yazın. Her sayının 1’den 10’a kadar olan çarpımlarını ekrana yazdırın.
# Çıktı düzenli ve okunaklı olmalıdır.

# Başlık satırı
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n" + "-"*44)

# Çarpım tablosu
for i in range(1, 11):
    print(f"{i:2} |", end="")  # Satır başı
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()  # Yeni satıra geç

#for number in range(1,11):
#  for num in range(1,11):
#    print(f"{number} x {num} = {number*num}") basitçe kod bu şekilde