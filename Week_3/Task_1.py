import math
# Kullanıcıdan alınan n sayısına kadar Fibonacci serisi oluşturan bir generator fonksiyon yazın.
# Daha sonra bu serideki:
# Tek sayıları filtreleyin
# Kalan çift sayıların karekökünü alın
# Sonuçları lambda ve map ile işleyip liste olarak döndürün
# Örnek: n=10 → Fibonacci: [0,1,1,2,3,5,8,13,21,34]
# Çiftler: [0,2,8,34] → Karekök: [0.0, 1.41, 2.83, 5.83]

def fibonacci(n):
   first,second =0,1
   for count in range(n):
       yield first
       first,second=second,first+second


continue_number =int(input("How long should the Fibonacci series continue ? \n"))

fibonacci_series= list(fibonacci(continue_number))
print(f"Fibonacci series up to {continue_number}: {fibonacci_series}")

even_numbers= list(filter(lambda x: x%2 ==0,fibonacci_series))
print(f"Even numbers: {even_numbers}")

sqrt_numbers=list(map(lambda x: round(math.sqrt(x), 2), even_numbers ))
print(f"Square roots of even numbers: {sqrt_numbers}")





