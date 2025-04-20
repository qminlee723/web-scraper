from navigator import setup_driver, go_to_site, click_next_page
from scraper import scrape_page
from utils import save_to_csv, get_today_filename

def main():
    driver = setup_driver()
    go_to_site(driver)

    output_file = get_today_filename("튼튼머니_적립시설")
    save_to_csv(output_file, [["지역", "시설명", "주소", "연락처"]], mode="w")

    MAX_PAGE = 402
    for page in range(1, MAX_PAGE + 1):
        print(f"📄 페이지 {page} 처리 중...")
        page_data = scrape_page(driver)
        save_to_csv(output_file, page_data, mode="a")
        print(f"✅ 페이지 {page} 저장 완료 ({len(page_data)}개 항목)")

        if page < MAX_PAGE:
            if not click_next_page(driver, page):
                break

    driver.quit()
    print(f"🎉 전체 크롤링 완료! 저장된 파일명: {output_file}")

if __name__ == "__main__":
    main()
