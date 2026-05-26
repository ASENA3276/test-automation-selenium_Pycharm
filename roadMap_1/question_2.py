
#Soru 2:

#sayi_atama ve sayi_okunusu isimli 2 tane fonksiyon tanımlayınız.

#Bu fonksiyonlardan sayi_atama fonksiyonu 2 basamaklı bir sayıyı parametre olarak alsın ve fonksiyon içinde bu değer bir değişkene atansın.

#Daha sonra sayi_atama fonksiyonu içinde sayi_okunusu isimli fonksiyon çağırılarak değişkene atanan sayının okunuşu string olarak verilsin.

#sayi_atama fonksiyonu 2 basamaktan daha az yada daha fazla sayıyı kabul etmeyecektir.


#Tüm rakamların nasıl okunduğunun tanımlandığı kod satırı.
def sayi_okunusu(sayi):
    birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    onlar_basamagi = sayi // 10  # Sayının onlar basamağının tanımlanması
    birler_basamagi = sayi % 10  # Sayının birler basamağının tanımlanması


    okunus = f"{onlar[onlar_basamagi]} {birler[birler_basamagi]}".strip()
    return okunus

def sayi_atama(sayi):
    # Sayının 2 basamaklı olup olmadığını kontrol etmek için yazılan adım
    if 10 <= sayi <= 99:
        okunus = sayi_okunusu(sayi)
        print(f"Sayı: {sayi}, Okunuşu: {okunus}")
    else:
        print("Lütfen 2 basamaklı bir sayı giriniz.")

#Okunuşunu merak ettiğiniz sayıyı aşağıya girinizz.
sayi_atama(8997)