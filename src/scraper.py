import time
from bs4 import BeautifulSoup

def scrape_page(driver):
    time.sleep(2)  # 페이지 로딩 대기
    soup = BeautifulSoup(driver.page_source, "html.parser")
    rows = soup.select("tr")

    page_data = []
    for row in rows:
        mcons = row.select("div.mCont")
        if mcons:
            values = [m.text.strip() for m in mcons]
            if values:
                page_data.append(values)
    return page_data
