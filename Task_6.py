#Bir akıllı ev sisteminde, oturma odası sıcaklığı her saat başı ölçülüyor ve kaydediliyor.
# Başlangıç sıcaklıkları: (22.5, 23.1, 21.8, 19.5, 18.9, 20.2, 22.7, 24.3, 25.6, 26.2, 25.8,
# 24.9, 23.7, 22.4, 21.1, 20.8, 19.9, 18.7, 19.2, 20.5, 21.9, 23.3, 22.8, 21.5).
# İstenen işlemler:
#•	Konfor Analizi: İdeal oda sıcaklığı 20-24 derece arasıdır. Bu aralıkta olmayan saatleri bulun.
#•	Enerji Tüketim Uyarısı: 25 derece üzeri sıcaklıklarda klima, 18 derece altında ısıtıcı çalışıyor. İkisi için de ayrı ayrı çalışan saat sayısını bulun.
#•	Gün içindeki en yüksek ve en düşük sıcaklık arasındaki farkı hesaplayın.
#•	Günlük ortalama sıcaklığı hesaplayın.

temperatures = [22.5, 23.1, 21.8, 19.5, 18.9, 20.2, 22.7, 24.3, 25.6, 26.2, 25.8,
24.9, 23.7, 22.4, 21.1, 20.8, 19.9, 18.7, 19.2, 20.5, 21.9, 23.3, 22.8, 21.5]

print("--- Comfort Analysis ---")
for hour, temp in enumerate(temperatures):
    if not 20 <= temp <= 24:
        print(f"Hour {hour}: {temp}°C - Out of comfort range!")

print("\n--- Energy Consumption Warning ---")
air_conditioning_count = 0
heater_count = 0
for temp in temperatures:
    if temp > 25:
        air_conditioning_count += 1
    if temp < 18:
        heater_count += 1
print(f"Air conditioner working hours: {air_conditioning_count}")
print(f"Heater working hours: {heater_count}")

print("\n--- Temperature Difference During the Day ---")
max_temp = max(temperatures)
min_temp = min(temperatures)
temp_diff = round(max_temp - min_temp, 2)
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")
print(f"Difference: {temp_diff}°C")

print("\n--- Average Temperature ---")
average_temp = round(sum(temperatures) / len(temperatures), 2)
print(f"Average Temperature: {average_temp}°C")

