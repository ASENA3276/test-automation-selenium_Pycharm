
#Soru 1:

#50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen doğru yanlış sayısına göre aldığı puanı hesaplayan programı yazınız.

#Ogrenci isimli bir sınıf tanımlayınız.

#Bu sınıfın içinde ogrenci_adi, ogrenci_soyadi, ogrenci_sinif’ı değişkenleri bulunacaktır. Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecektir.

#Soru diye bir sınıfınız olacaktır. Bu sınıfın net_sayisi ve hesapla isimli iki fonksiyon olacaktır.

#net_sayisi fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulacaktır.

#hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacaktır. Her net 2 puan olacak şekilde öğrenci bilgileri ve puanı console ekranında gösterilecektir.




# Öğrenci sınıfı tanımlanması için yazılan kod satırı.
class Ogrenci:
    def __init__(self, adi, soyadi, sinif):
        self.ogrenci_adi = adi
        self.ogrenci_soyadi = soyadi
        self.ogrenci_sinif = sinif

    def bilgileri_goster(self):
        print(f"Öğrenci Adı: {self.ogrenci_adi} {self.ogrenci_soyadi}")
        print(f"Sınıf: {self.ogrenci_sinif}")


# Soru sınıfı tatanımlanması için yazılan kod satırı.
class Soru:
    @staticmethod
    def net_sayisi(dogru_sayisi, yanlis_sayisi):
        # 4 yanlış bir doğruyu götürdüğünden bu matematiksel hesaplama eklendi.
        net = dogru_sayisi - (yanlis_sayisi // 4)
        return max(0, net)  # Negatif net olmaması için sıfırdan büyük değer döndürmemiz gerekiyor bu kısım onun için eklendi.

    @staticmethod
    def hesapla(net_sayisi):
        # Her net 2 puan olarak ayarlanıyor bu kısımda.
        return net_sayisi * 2


# Genel anlamda çalışma mantığının kurulduğu alan
def main():

    # Öğrenci bilgilerini alıyoruz klavye ile elimizle bilgileri girmemiz istenecek
    adi = input("Öğrenci Adı: ")
    soyadi = input("Öğrenci Soyadı: ")
    sinif = input("Öğrenci Sınıfı: ")

    # Öğrenci nesnesi oluşturuyoruz bunları karşı taraftan istiyoruz
    ogrenci = Ogrenci(adi, soyadi, sinif)

    # Soru bilgilerini alıyoruz kaç doğru kaç yanlış yapıldığını karşı taraftan istiyoruz. Hesaplamalar ona göre yapılacaktır.
    dogru_sayisi = int(input("Doğru sayısı: "))
    yanlis_sayisi = int(input("Yanlış sayısı: "))

    # Net sayısı ve puan hesaplama
    net = Soru.net_sayisi(dogru_sayisi, yanlis_sayisi)
    puan = Soru.hesapla(net)

    # Sonuçları gösteriyomek için ekrana yazdırma kısmı
    ogrenci.bilgileri_goster()
    print(f"Net Sayısı: {net}")
    print(f"Toplam Puan: {puan}")

if __name__ == "__main__":
    main()

