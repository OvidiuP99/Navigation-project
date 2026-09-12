from pages.test_pages import SullenClothing

def test_standard_tees(driver):
    page = SullenClothing(driver)
    page.open()
    page.close_popup()
    page.click_standard_tees()
    
    assert "STANDARD TEES" in page.get_title().upper()

def test_premium_tees(driver):
    page = SullenClothing(driver)
    page.open()
    page.close_popup()
    page.click_premium_tees()

    assert "PREMIUM TEES" in page.get_title().upper()

def test_longsleeves(driver):
    page = SullenClothing(driver)
    page.open()
    page.close_popup()
    page.click_longsleeves()

    assert "LONG SLEEVES" in page.get_title().upper()      

