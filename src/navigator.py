from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def go_to_site(driver):
    driver.get("https://nfa.kspo.or.kr/spoint/selectSpointFacility.kspo")

def click_next_page(driver, current_page):
    wait = WebDriverWait(driver, 10)
    try:
        next_page_str = str(current_page + 1)
        next_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//a[contains(@onclick, \"pageinfo('{next_page_str}')\")]")))
        next_button.click()
        return True
    except Exception as e:
        print(f"❌ 페이지 {current_page+1} 이동 실패: {e}")
        return False
