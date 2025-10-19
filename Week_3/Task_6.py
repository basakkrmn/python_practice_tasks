# Bir isim listesindeki tüm isimleri büyük harfe çeviren ve başına "Sayın " ekleyen bir program yazın.
# Örnek: ["ali", "ayşe", "mehmet"] → ["Sayın ALİ", "Sayın AYŞE", "Sayın MEHMET"]
# - Lambda ve map kullanın
# - Kullanıcıdan virgülle ayrılmış isimler alın

user_input = input("Enter names separated by commas: ")

names = user_input.split(",")

format_name = lambda name: "Sayın " + name.upper()

formatted_names = list(map(format_name, names))

print(formatted_names)

