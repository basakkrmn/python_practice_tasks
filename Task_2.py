import string
# Programınız “Python, Guido van Rossum tarafından 1991 yılında geliştirilmiş bir programlama dilidir.
# Python, okunabilirliği ve basit sözdizimi ile öne çıkar.
# Dilin tasarım felsefesi, kod okunabilirliğini vurgular ve bu da onu yeni başlayanlar için ideal kılar.
# Python, web geliştirme, veri analizi, yapay zeka, bilimsel hesaplama ve otomasyon gibi birçok alanda kullanılır.
# Python'un geniş kütüphane ekosistemi, geliştiricilere güçlü araçlar sunar.
# Python topluluğu çok aktiftir ve sürekli olarak dilin gelişimine katkıda bulunur.
# Python programlama dilini öğrenmek, yazılım dünyasında birçok kapı açar.”
# bu metinde en çok geçen 3 kelimeyi bulsun. Tüm harfleri küçük yapsın ve noktalama işaretlerini temizlesin.

python_text="Python, Guido van Rossum tarafından 1991 yılında geliştirilmiş bir programlama dilidir.\
 Python, okunabilirliği ve basit sözdizimi ile öne çıkar. \
 Dilin tasarım felsefesi, kod okunabilirliğini vurgular ve bu da onu yeni başlayanlar için ideal kılar. \
 Python, web geliştirme, veri analizi, yapay zeka, bilimsel hesaplama ve otomasyon gibi birçok alanda kullanılır.\
 Python'un geniş kütüphane ekosistemi, geliştiricilere güçlü araçlar sunar.\
 Python topluluğu çok aktiftir ve sürekli olarak dilin gelişimine katkıda bulunur. \
 Python programlama dilini öğrenmek, yazılım dünyasında birçok kapı açar."

python_text=python_text.lower()

clean_text = ''.join([c for c in python_text if c not in string.punctuation])
words = clean_text.split()

words_number ={ }

for word in words:
    if word in words_number:
        words_number[word] +=1
    else:
        words_number[word]=1


words_number.items()
sorted_list = sorted(words_number.items(), key=lambda x: x[1], reverse=True)[:3]

for i in sorted_list:
    print(i)

