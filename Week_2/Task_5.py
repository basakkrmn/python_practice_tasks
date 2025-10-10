# Verilen 2 listeyi zip fonksiyonu ile birleştirerek index ve değerleri birlikte yazdırın.
# [“Ali”, ”Ayşe”, ”Mehmet”, ”Zeynep”]
# [25, 30, 35, 28]

names= ["Ali","Ayşe","Mehmet","Zeynep"]
ages =[25, 30, 35, 28]

for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index} - {name} is {age} years old")
