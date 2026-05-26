
#Soru 2:

#Insan isimli bir sınıf tanımlayınız.

#Bütün constructor parametreleri default değerlere sahip olacak, default contructor (__init__) içinde belirlenecektir.

#Bu değerler; ad, soyad, yas, ulke, sehir olacaktır.Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacaktır.

#kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le döndürülecektir.

#yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecektir.

#Bu classtan belirtilen bilgileri içeren bir nesne tanımlayınız.

#Tanımlanan nesneye yetenek ekleyiniz. (Bisiklete binmek, Python vs.)

#kisi_bilgileri fonksiyonu ile bu bilgileri console ekranında gösteriniz.

# Insan sınıfı tanımlanıyor
class Insan:
    def __init__(self, ad="Ahmet", soyad="Yılmaz", yas=30, ulke="Türkiye", sehir="İstanbul"):
        #  gerekli olan nitelikleri tanımlamak için eklendi.
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        # Boş bir yetenekler listesi oluşturuldu.
        self.yetenekler = []

    def kisi_bilgileri(self):
        # Kişinin bilgilerini return ile  döndürme
        return {
            "Ad": self.ad,
            "Soyad": self.soyad,
            "Yaş": self.yas,
            "Ülke": self.ulke,
            "Şehir": self.sehir,
            "Yetenekler": self.yetenekler
        }

    def yetenek_ekle(self, yetenek):
        # Yetenek eklemek için gerekli alan
        self.yetenekler.append(yetenek)


# Insan sınıfından bir adet nesne oluşturuyoruz
kisi = Insan()

# Yetenek ekleme adımı
kisi.yetenek_ekle("Bisiklete binmek")
kisi.yetenek_ekle("Python")

# Kişi bilgilerini gösterme yani ekrana yazdırmak için gerekli alan.
kisi_bilgileri = kisi.kisi_bilgileri()
for bilgi, deger in kisi_bilgileri.items():
    print(f"{bilgi}: {deger}")