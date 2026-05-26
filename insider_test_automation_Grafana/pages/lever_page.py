from pages.base_page import BasePage

class LeverPage(BasePage):

    def verify_lever_page(self):
        assert "lever.co" in self.get_current_url()  # Lever sayfa kontrol