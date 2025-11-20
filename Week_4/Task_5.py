import random
import math
from datetime import datetime
import time
from collections import Counter
# Quiz Uygulaması (Collections + Random)
# Zamanlı quiz uygulaması. Soruları rastgele seçmeli, süre tutmalı ve detaylı rapor oluşturmalı.
# soru_bankasi:  Soru, cevap, zorluk seviyesi içeren sözlük
# soru_sec methodu: random.sample ile belirtilen sayıda rastgele soru seçecek
# quiz_baslat methodu: time.time ile süre başlatacak.
# cevap_kontrol methodu: collections.Counter ile doğru/yanlış istatistiği tutacak.
# rapor_olustur methodu: datetime ile detaylı quiz raporu oluşturacak.
# puan_hesapla methodu: math modülü ile zorluk katsayılarına göre puan hesaplayacak.

class Quiz:
    def __init__(self):
        self.soru_bankasi = [
            {"soru": "Harry'nin Hogwarts’taki ilk yılının sonunda yok edilen taş hangisiydi?",
             "cevap": "felsefe taşı", "zorluk": "kolay"},

            {"soru": "Harry'nin baykuşunun adı nedir?",
             "cevap": "hedwig", "zorluk": "kolay"},

            {"soru": "Harry'nin Hogwarts'ta bağlı olduğu bina hangisidir?",
             "cevap": "gryffindor", "zorluk": "kolay"},

            {"soru": "Hogwarts’ın bulunduğu büyü okulu nedir?",
             "cevap": "hogwarts", "zorluk": "kolay"},

            {"soru": "Harry Potter evrenindeki büyücü hapishanesinin adı nedir?",
             "cevap": "azkaban", "zorluk": "orta"},

            {"soru": "Zümrüdüanka Yoldaşlığı’nın lideri kimdir?",
             "cevap": "dumbledore", "zorluk": "orta"},

            {"soru": "Hermione’nin kedisinin adı nedir?",
             "cevap": "crookshanks", "zorluk": "orta"},

            {"soru": "Lord Voldemort’un gerçek adı nedir?",
             "cevap": "tom riddle", "zorluk": "orta"},

            {"soru": "Harry’nin asasının çekirdeği hangi maddedendir?",
             "cevap": "anka tüyü", "zorluk": "zor"},

            {"soru": "Dumbledore'un kız kardeşinin adı nedir?",
             "cevap": "ariana", "zorluk": "zor"},

            {"soru": "Hermione'nin zaman döndürücüyü kullandığı mahkûm kimdi?",
             "cevap": "sirius black", "zorluk": "zor"},

            {"soru": "Voldemort’un ilk hortkuluk yaptığı nesne nedir?",
             "cevap": "güncesi", "zorluk": "zor"},
        ]

        self.istatistik = Counter()
        self.cevap_kayitlari = []
        self.son_sure = None
        self.son_puan = 0

    def soru_sec(self, adet):
        return random.sample(self.soru_bankasi, adet)

    def cevap_kontrol(self, kullanici_cevabi, dogru_cevap):
        kullanici_cevabi = kullanici_cevabi.strip().lower()
        dogru_cevap = dogru_cevap.strip().lower()

        if kullanici_cevabi == dogru_cevap:
            self.istatistik["dogru"] += 1
            return True
        else:
            self.istatistik["yanlis"] += 1
            return False

    def puan_hesapla(self):
        katsayilar = {
            "kolay": 1,
            "orta": 1.5,
            "zor": 2
        }

        puan = 0

        for kayit in self.cevap_kayitlari:
            if kayit["dogru_mu"]:
                z = kayit["zorluk"]
                puan += 10 * katsayilar.get(z, 1)

        return math.floor(puan)

    def rapor_olustur(self):
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dogru = self.istatistik["dogru"]
        yanlis = self.istatistik["yanlis"]
        toplam = len(self.cevap_kayitlari)
        basari_orani = (dogru / toplam * 100) if toplam > 0 else 0

        satirlar = []
        satirlar.append("--- Harry Potter Quiz Raporu ---")
        satirlar.append(f"Tarih: {tarih}")
        satirlar.append(f"Süre: {self.son_sure:.2f} saniye")
        satirlar.append(f"Toplam Soru: {toplam}")
        satirlar.append(f"Doğru: {dogru}  Yanlış: {yanlis}")
        satirlar.append(f"Başarı Oranı: {basari_orani:.1f}%")
        satirlar.append(f"Puan: {self.son_puan}")
        satirlar.append("")
        satirlar.append("Detaylı Cevaplar:")

        for i, kayit in enumerate(self.cevap_kayitlari, 1):
            durum = "Doğru" if kayit["dogru_mu"] else "Yanlış"
            satirlar.append(
                f"{i}. {kayit['soru']} (Zorluk: {kayit['zorluk']}) -> "
                f"Doğru: {kayit['dogru_cevap']} | Sen: {kayit['kullanici_cevabi']} [{durum}]"
            )

        return "\n".join(satirlar)

    def quiz_baslat(self, soru_sayisi=5):
        self.cevap_kayitlari.clear()
        self.istatistik.clear()

        sorular = self.soru_sec(soru_sayisi)

        print(f"{soru_sayisi} soruluk Harry Potter quizi başlıyor...\n")
        time.sleep(0.5)

        baslangic = time.time()

        for soru in sorular:
            print("Soru:", soru["soru"])
            cevap = input("Cevabınız: ")

            dogru_mu = self.cevap_kontrol(cevap, soru["cevap"])

            self.cevap_kayitlari.append({
                "soru": soru["soru"],
                "dogru_cevap": soru["cevap"],
                "kullanici_cevabi": cevap,
                "zorluk": soru["zorluk"],
                "dogru_mu": dogru_mu
            })

            print("Doğru!" if dogru_mu else "Yanlış!", "\n")

        bitis = time.time()
        self.son_sure = bitis - baslangic
        self.son_puan = self.puan_hesapla()

        print("\nQuiz Tamamlandı!\n")
        print(self.rapor_olustur())


if __name__ == "__main__":
    quiz = Quiz()
    quiz.quiz_baslat(soru_sayisi=5)



