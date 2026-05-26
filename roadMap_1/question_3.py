
# Kullanıcının girdiği vize1, vize2, final notlarına göre harf notunu hesaplayınız.
#
# -vize1 toplam notun %30'una etki edecektir.
#
# -vize2 toplam notun %30'una etki edecektir.
#
# -final toplam notun %40'ına etki edecektir.
#
# Bu değerler 0-100 arası kabul edilmelidir!

#Notlar için fonsiyon tanımlamasının yapıldığı kod satırı.
def harf_notu_hesapla(vize1, vize2, final):
    if not (0 <= vize1 <= 100 and 0 <= vize2 <= 100 and 0 <= final <= 100): # Sınav puanlarının 0 ile 100 arasında olması gerektiğinin yazıldığı kod satırı.
        return "Lütfen notlar 0 ile 100 arasında olmalıdır." # Fonsiyonu döndürmek için return kullanılıyor.

    toplam_not = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40) #Sınavların nor ortalamasına ne kadar etki ettiğinin ayarlandığı kod satırı.

    #Alınan notların karşılığında hangi harf notunun geçerli olduğunun tanımlanması.

    if toplam_not >= 90:
        return "AA"
    elif toplam_not >= 85:
        return "BA"
    elif toplam_not >= 80:
        return "BB"
    elif toplam_not >= 75:
        return "CB"
    elif toplam_not >= 70:
        return "CC"
    elif toplam_not >= 65:
        return "DC"
    elif toplam_not >= 60:
        return "DD"
    elif toplam_not >= 55:
        return "FD"
    else:
        return "FF"


# Lütfen Vize1 Vize2 ve Final sınav notlarınızı giriniz.

print(harf_notu_hesapla(90,72,30))