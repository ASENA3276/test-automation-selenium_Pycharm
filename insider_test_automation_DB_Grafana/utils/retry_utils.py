import time  # Bekleme için gerekli

def retry(action, retries=3, delay=2):
    """
    Belirtilen action'ı retry mekanizması ile çalıştırır
    :param action: Çalıştırılacak fonksiyon
    :param retries: Kaç kez denenecek
    :param delay: Denemeler arası bekleme süresi
    """
    for attempt in range(retries):  # Retry sayısı kadar dene
        try:
            return action()  # Fonksiyonu çalıştır
        except Exception as e:  # Hata alırsa
            if attempt == retries - 1:  # Son deneme ise
                raise e  # Hatayı fırlat
            time.sleep(delay)  # Bekle ve tekrar dene