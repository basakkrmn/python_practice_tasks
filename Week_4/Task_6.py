import math
from datetime import datetime, timedelta
# Personel Yönetim Sistemi (Advanced OOP)
# Şirket personel yönetimi için gelişmiş sistem. Farklı personel türleri için inheritance kullanacak.
# Personel base class: ad, soyad, maas, departman, ise_baslama_tarihi (datetime)
# zam_hesapla methodu: datetime ile kıdem hesaplayıp zam oranı belirleyecek
# izin_hesapla methodu: datetime.timedelta ile çalışılan gün sayısına göre izin hesaplayacak
# Yonetici subclass: Ek olarak sorumlu_oldugu_kisiler listesi ve bonus hesaplama
# Gelistirici subclass: Teknoloji stack listesi ve proje bazlı prim hesaplama
# __eq__ methodu: İki personelin maaşlarını karşılaştıracak
# __gt__ methodu: Hangi personelin daha uzun süredir çalıştığını kontrol edecek.
# Örnek:
# personel1 = Yonetici("Mehmet", "Demir", 20000, "IT", "2020-03-15")
# personel2 = Gelistirici("Zeynep", "Kaya", 15000, "Yazılım", "2021-06-20")
# print(f"Kıdem: {personel1 > personel2}")  # __gt__ test
# print(f"Zam oranı: {personel1.zam_hesapla()}")

class Personel:
    def __init__(self, ad, soyad, maas, departman, ise_baslama_tarihi):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman

        if isinstance(ise_baslama_tarihi, str):
            self.ise_baslama_tarihi = datetime.strptime(ise_baslama_tarihi, "%Y-%m-%d")
        else:
            self.ise_baslama_tarihi = ise_baslama_tarihi

    def __str__(self):
        return f"{self.ad} {self.soyad} - {self.departman} - Maaş: {self.maas} TL"

    def calisma_suresi_gun(self):
        bugun = datetime.now()
        fark = bugun - self.ise_baslama_tarihi
        return fark.days

    def zam_hesapla(self):
        gun = self.calisma_suresi_gun()
        yil = gun // 365

        if yil < 1:
            oran = 0.05
        elif yil < 3:
            oran = 0.10
        else:
            oran = 0.20

        return oran

    def izin_hesapla(self):
        gun = self.calisma_suresi_gun()
        yil = gun // 365

        if yil < 1:
            izin_gun = 10
        elif yil < 5:
            izin_gun = 14
        else:
            izin_gun = 20

        return timedelta(days=izin_gun)

    def __eq__(self, diger):
        return self.maas == diger.maas

    def __gt__(self, diger):
        return self.ise_baslama_tarihi < diger.ise_baslama_tarihi


class Yonetici(Personel):
    def __init__(self, ad, soyad, maas, departman, ise_baslama_tarihi, sorumlu_oldugu_kisiler=None):
        super().__init__(ad, soyad, maas, departman, ise_baslama_tarihi)
        self.sorumlu_oldugu_kisiler = sorumlu_oldugu_kisiler or []

    def bonus_hesapla(self):
        kisi_sayisi = len(self.sorumlu_oldugu_kisiler)
        bonus = kisi_sayisi * 500
        return bonus


class Gelistirici(Personel):
    def __init__(self, ad, soyad, maas, departman, ise_baslama_tarihi, teknoloji_stack=None):
        super().__init__(ad, soyad, maas, departman, ise_baslama_tarihi)
        self.teknoloji_stack = teknoloji_stack or []

    def prim_hesapla(self, proje_sayisi):
        temel_prim = 1000
        ekstra = len(self.teknoloji_stack) * 100
        toplam_prim = proje_sayisi * (temel_prim + ekstra)
        return toplam_prim


if __name__ == "__main__":
    personel1 = Yonetici("Mehmet", "Demir", 20000, "IT", "2020-03-15", sorumlu_oldugu_kisiler=["A", "B", "C"])
    personel2 = Gelistirici("Zeynep", "Kaya", 15000, "Yazılım", "2021-06-20", teknoloji_stack=["Python", "Django"])

    print(personel1)
    print(personel2)
    print()

    # __gt__ testi: hangisi daha kıdemli?
    print(f"Kıdem: {personel1 > personel2}")  # True/False

    # zam oranı
    zam_orani1 = personel1.zam_hesapla()
    print(f"{personel1.ad} için zam oranı: {zam_orani1*100:.0f}%")

    zam_orani2 = personel2.zam_hesapla()
    print(f"{personel2.ad} için zam oranı: {zam_orani2*100:.0f}%")

    # izin hesaplama
    print(f"{personel1.ad} izin günleri: {personel1.izin_hesapla()} gün")
    print(f"{personel2.ad} izin günleri: {personel2.izin_hesapla()} gün")

    # bonus/prim
    print(f"{personel1.ad} bonusu: {personel1.bonus_hesapla():.2f} TL")
    print(f"{personel2.ad} 3 proje primi: {personel2.prim_hesapla(3):.2f} TL")

    # eşit maaş kontrolü
    print(f"Maaşlar eşit mi? {personel1 == personel2}")

    # örnek: zam uygulamak istersen
    zam_tutari = personel1.maas * zam_orani1
    print(f"{personel1.ad} zam sonrası maaşı: {personel1.maas + zam_tutari:.2f} TL")
