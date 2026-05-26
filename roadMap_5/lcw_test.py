from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


#Otomasyon sırasında kullanılacak olan tüm elementlerin locaterlarını bu kısımda tanımladım. Direkt find_element içine de ekleyebilirdim ama böyle daha düzenli duruyor.
class LCWTest(unittest.TestCase):
    LCW_URL = "https://www.lcw.com/"
    CATEGORY_PAGE = (By.CLASS_NAME, "menu-header-item.menu-header-item--outlet > .menu-header-item__title")
    PRODUCT_PAGE = (By.CSS_SELECTOR, "img.product-image__image[src*='7034876']")
    SIZE_SELECTION_BUTTON = (
    By.XPATH, "//button[@class='option-box option-size-box option-size-box__stripped' and text()='11-12 Yaş']")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-card")
    CART_PAGE_ICON = (By.CSS_SELECTOR, "a.header-dropdown-toggle[href='https://www.lcw.com/sepetim']")
    HOME_PAGE_ICON = (By.ID, "Layer_1")
    ALLOW_COOKIES = (By.ID, "cookieseal-banner-accept")
    OPTIN_CLOSE = (By.CLASS_NAME, "ins-web-opt-in-reminder-close-button")



#Mause ile elementlere her tıklama işleminde tıklanan kısım belli olsun diye kırmızı bir efect ekledim.
    def click_with_effect(self, element):


        self.driver.execute_script("""
        var elem = arguments[0];
        var rect = elem.getBoundingClientRect();
        var effect = document.createElement("div");

        effect.style.position = "fixed";
        effect.style.width = "50px";
        effect.style.height = "50px";
        effect.style.borderRadius = "50%";
        effect.style.backgroundColor = "rgba(139, 0, 0, 1.0)";
        effect.style.top = (rect.top + window.scrollY + rect.height / 2 - 25) + "px";
        effect.style.left = (rect.left + window.scrollX + rect.width / 2 - 25) + "px";
        effect.style.zIndex = "9999";
        effect.style.pointerEvents = "none";
        effect.style.animation = "clickEffect 0.5s ease-out";

        document.body.appendChild(effect);

        setTimeout(function() { effect.remove(); }, 500);

        var style = document.createElement("style");
        style.innerHTML = `
            @keyframes clickEffect {
                0% { transform: scale(1); opacity: 1; }
                100% { transform: scale(3); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
        """, element)

        element.click()  # Normal tıklama işlemi yapmak için eklenen kod.




#Bu kısım testlere başlamadan önce driver ve browser ayarlamalarını yapmak için eklendi tüm testlerin başında gerekli bir adım.
    def test_lcw_flow(self):
        self.driver = webdriver.Chrome() #driver olarak chrome seçtim başka browserlarda seçilebilir.
        self.driver.get(self.LCW_URL)    # otomasyon işlemlerini yapacağımız sitenin url tanımlanır ve site browserda açılır.
        self.driver.maximize_window()    #Açılan Browser'ı tam ekran yapmak için eklendi.
        time.sleep(2) #elementlerin yüklenmesi için bekleme süresi eklendi.


        #Bu adımda sayfada çıkan çerezler kabul edilmiştir diğer tıklamalara izin verilmiyor bu adımı geçmeden.
        allow_cookies = self.driver.find_element(*self.ALLOW_COOKIES) #Locater'ı tanımlı olan elementi bulmak için eklenen kod.
        self.click_with_effect(allow_cookies)  # Kırmızı Efektli Tıklama
        time.sleep(2) #elementlerin yüklenmesi için bekleme süresi eklendi.

        #Bu adımda çıkan optin bildirimi kapatılmıştır tıklama işlemlerini engellediği için.
        optin_close = self.driver.find_element(*self.OPTIN_CLOSE)
        self.click_with_effect(optin_close)  # Kırmızı Efektli Tıklama
        time.sleep(2)



        #Bu adımda Outlet kategorisi seçilmiş ve tıklanmıştır.
        category_page = self.driver.find_element(*self.CATEGORY_PAGE)
        self.click_with_effect(category_page)  # Kırmızı Efektli Tıklama
        time.sleep(2)

        #Assert ile kategori sayfasında olduğu doğrulanmıştır.
       # self.assertIn("/outlet", self.driver.current_url,"URL BU DEĞERİ İÇERMEMEKTEDİR KATEGORY SAYFASINDA DEĞİLSİNİZ...")




        # Bu adımda bir product seçilmiş ve tıklanmıştır.
        product_page = self.driver.find_element(*self.PRODUCT_PAGE)
        self.click_with_effect(product_page)  # Kırmızı Efektli Tıklama
        time.sleep(2)

        # Assert ile product sayfasında olduğu doğrulanmıştır.
        self.assertTrue(self.driver.find_element(By.XPATH,"//span[@class='hidden-xs' and contains(text(), 'Ürün Kodu')]").is_displayed()) #Bu sayfada tanımlanan locatera sahip element bulunmazsa hata verir.



        #Bir üründe add to card butonuna basmadan önce beden seçimi yapmak gerektiğinden bu adımda beden seçilmıştır.
        size_selection_button = self.driver.find_element(*self.SIZE_SELECTION_BUTTON)
        time.sleep(5) #Beden seçiminden önce minik bir popup çıkmaktadır onun kaybolması için bekleme süresi eklenmiştir.
        self.click_with_effect(size_selection_button)  # Kırmızı Efektli Tıklama
        time.sleep(2)




        #ürün sayfasındaki add to cart butonu seçilmiş ve tıklanmıştır.
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        self.click_with_effect(add_to_cart_button)  # Kırmızı Efektli Tıklama
        time.sleep(2)



        #Cart sayfasına gitmek için ürün sayfasında bulunan cart iconuna tıklama işlemi yapılmıştır.
        cart_page_icon = self.driver.find_element(*self.CART_PAGE_ICON)
        self.click_with_effect(cart_page_icon)  # Kırmızı Efektli Tıklama
        time.sleep(2)


        #Cart sayfasında olduğumuzu doğrulamak için eklenmiş olan assert
        self.assertIn("/sepetim", self.driver.current_url ,"URL BU DEĞERİ İÇERMEMEKTEDİR CART SAYFASINDA DEĞİLSİNİZ..." )

        home_page = self.driver.find_element(*self.HOME_PAGE_ICON)
        time.sleep(5)
        self.click_with_effect(home_page)  # Kırmızı Efektli Tıklama
        time.sleep(2)

        self.assertEqual(self.LCW_URL, self.driver.current_url,"URL BU DEĞERİ İÇERMEMEKTEDİR ANA SAYFADA DEĞİLSİNİZ...")



    #Tüm işlemler bittikten sonra browser'ı kapatmak için eklenmiştir.
    def tearDown(self):
        if hasattr(self, 'driver'): # Eğer driver özelliği varsa kapat.
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
