





# Ana sınıf WebPush
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
        print(f"{self.push_type} Push gönderildi!")


# Miras alan sınıflar
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

    def discountPrice(self):
        discount_price = self.price_info * (1 - self.discount_rate / 100)
        return discount_price


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self):
        # Stok bilgisi güncelleniyor: True ise False, False ise True yapılır.
        self.stock_info = not self.stock_info
        return self.stock_info


# Nesneler oluşturuluyor ve methodlar çağırılıyor

# TriggerPush nesnesi
trigger_push = TriggerPush("Web", True, 3, "2024-11-01", "2024-12-01", "TR", "Trigger", "HomePage")
trigger_push.send_push()

# BulkPush nesnesi
bulk_push = BulkPush("Mobile", False, 5, "2024-11-01", "2024-12-01", "EN", "Bulk", 5)
bulk_push.send_push()

# SegmentPush nesnesi
segment_push = SegmentPush("Web", True, 2, "2024-11-01", "2024-12-01", "EN", "Segment", "VIP Users")
segment_push.send_push()

# PriceAlertPush nesnesi ve indirimi hesaplama
price_alert_push = PriceAlertPush("App", True, 10, "2024-11-01", "2024-12-01", "EN", "PriceAlert", 1000, 20)
print(f"İndirimli Fiyat: {price_alert_push.discountPrice()}")
price_alert_push.send_push()

# InstockPush nesnesi ve stok güncellemesi
instock_push = InstockPush("Web", False, 3, "2024-11-01", "2024-12-01", "TR", "Instock", True)
print(f"Stok Durumu Güncellemesi: {instock_push.stockUpdate()}")
instock_push.send_push()
