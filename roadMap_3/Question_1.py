
# Ana sınıf
class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        if self.optin:
            print(f"{self.push_type} Push gönderildi!")
        else:
            print(f"{self.push_type} Push gönderilemedi, kullanıcı opt-in onayı vermedi. User'ın Op-tin ayarlarını kontrol edebilirsiniz.")

# Web Push clasına bağlı birçok alt class oluşturuldu bu kısımda. Bu oluşturulan classlar gönderilecek olan push türlerini tanımlamak için oluşturulmuştur.
class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page

class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date

class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, price_info, discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discount_price(self):
        discounted_price = self.price_info * (1 - self.discount_rate)
        return discounted_price

class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stock_update(self):
        self.stock_info = not self.stock_info
        return self.stock_info

# Nesneleri oluşturma ve test etmek için ıoluşturulan kısımdır. Burada tüm push türleri için mevcut durum bilgileri girilir ve daha sonra bu bilgilere gçre push gönderimi yapılırd.
trigger_push = TriggerPush("iOS", True, 5, "2024-12-08", "2024-12-31", "EN", "Trigger", "CartPage")
trigger_push.send_push()

bulk_push = BulkPush("Android", True, 10, "2024-12-08", "2024-12-31", "EN", "Bulk", 20241201)
bulk_push.send_push()

segment_push = SegmentPush("Web", False, 7, "2024-12-08", "2024-12-31", "TR", "Segment", "PremiumUsers")
segment_push.send_push()

price_alert_push = PriceAlertPush("iOS", True, 5, "2024-12-08", "2024-12-31", "TR", "PriceAlert", 85, 0.5)
print(f"İndirimli fiyat: {price_alert_push.discount_price()}")
price_alert_push.send_push()

instock_push = InstockPush("Web", False, 3, "2024-12-08", "2024-12-31", "EN", "Instock", False)
print(f"Stok güncel durumu: {instock_push.stock_update()}")
instock_push.send_push()


#NOTLARRRR
#Ana Sınıf (WebPush):

#Ana özellikleri içeriyor: platform, optin, global_frequency_capping, start_date, end_date, language, push_type.
#send_push metodu, kullanıcının opt-in durumuna göre push gönderip göndermeyeceğini belirtiyor.
#Alt Sınıflar:

#TriggerPush: trigger_page ek özelliği içeriyor.
#BulkPush: send_date ek özelliği içeriyor.
#SegmentPush: segment_name ek özelliği içeriyor.
#PriceAlertPush: price_info ve discount_rate özelliklerini alıyor ve discount_price metoduyla indirimli fiyatı hesaplıyor.
#InstockPush: stock_info özelliğine sahip ve stock_update metodu ile stok bilgisini güncelliyor.
