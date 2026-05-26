import selenium

# Soru 1:

# 3 tane parametre alan bolunen_sayi_bulma isimli bir fonksiyon tanımlayınız.
#
# Bu fonsiyon; min_sayi, max_sayi, bolen_sayi isimli parametreleri alsın.
#
# Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak, min_sayi ve max_sayi aralığındaki bolen_sayi değerine bölünen sayıları tam_bolunenler adlı bir diziye atayıp, listelesin.
#
# tam_bolunenler dizisi ile min_sayi ve max_sayi arasındaki değerlerin sayısını return ile döndürsün.


#  parametreleri içeren fonksiyonun tanımlandığı adım
def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):

    tam_bolunenler = []  # Bölünen sayıları depolamak için oluşturulan bir dize yada liste denilebilir.

    # min_sayi ile max_sayi arasındaki sayılar üzerinde sürekli dönmesi gereken sayacın tanımlandığı adım.
    for sayi in range(min_sayi, max_sayi + 1): #sürekli 1 sayı arttırarak sayacın ilerlemesi gerektiğinin tanımlandığı kısım.
        if sayi % bolen_sayi == 0:  # Bölünebilme kontrolünün sağlandığı adım.
            tam_bolunenler.append(sayi)

    # Girilen sayıların arasındaki sayıların tam bölünenlerini ve tam bölünenlerin kaç adet olduğunu veren kod adımı.
    return (
        tam_bolunenler, len(tam_bolunenler))



# Bu kısıma istenilen değerler girilerek kod çalıştırılabilir.
deneme = bolunen_sayi_bulma(100, 150, 3)  # 100 ile 150 arasında 3'e bölünen sayıları bulalım

print(deneme)
