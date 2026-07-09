root@crawler:~# cat selenium_post_test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


WRITE_URL = "https://gall.dcinside.com/mgallery/board/write/?id=catfiesta"

CHROME_PATH = "/root/chrome-linux64/chrome"

DRIVER_PATH = (
    "/root/.cache/selenium/chromedriver/"
    "linux64/138.0.7204.183/chromedriver"
)


# ==================================================
# Chrome 설정
# ==================================================

options = Options()

options.binary_location = CHROME_PATH

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")


service = Service(DRIVER_PATH)

driver = webdriver.Chrome(
    service=service,
    options=options
)


try:

    # ==================================================
    # 1. 글쓰기 페이지 열기
    # ==================================================

    print("[1] 크롬 실행 성공")

    driver.get(WRITE_URL)

    print("[2] 글쓰기 페이지 접속")

    time.sleep(5)

    print("[3] 페이지 로딩 완료")
    print("현재 주소:", driver.current_url)
    print("페이지 제목:", driver.title)


    # ==================================================
    # 2. 제목 입력
    # ==================================================

    print()
    print("===== 제목 입력 =====")

    subject = driver.find_element(
        By.NAME,
        "subject"
    )

    subject.clear()
    subject.send_keys("hello")

    print(
        "제목 입력 완료:",
        subject.get_attribute("value")
    )


    # ==================================================
    # 3. 비밀번호 입력
    # ==================================================

    print()
    print("===== 비밀번호 입력 =====")

    password = driver.find_element(
        By.NAME,
        "password"
    )

    password.clear()
    password.send_keys("1234")

    print("비밀번호 입력 완료")


    # ==================================================
    # 4. HTML 모드 전환
    # ==================================================

    print()
    print("===== HTML 모드 =====")

    html_button = driver.find_element(
        By.XPATH,
        "//button[normalize-space()='HTML']"
    )

    print("HTML 버튼 발견")

    html_button.click()

    print("HTML 버튼 클릭 완료")

    time.sleep(2)


    # ==================================================
    # 5. 실제 HTML 입력창에 본문 입력
    # ==================================================

    print()
    print("===== 본문 입력 =====")

    html_area = driver.find_element(
        By.CSS_SELECTOR,
        ".note-codable"
    )

    print("HTML 입력창 발견")
    print("표시 여부:", html_area.is_displayed())

    html_area.clear()
    html_area.send_keys("siuuuuuuu")

    print(
        "HTML 입력 결과:",
        html_area.get_attribute("value")
    )


    # ==================================================
    # 6. 등록 전 스크린샷
    # ==================================================

    driver.save_screenshot(
        "before_submit.png"
    )

    print()
    print("등록 전 스크린샷 저장 완료")


    # ==================================================
    # 7. 등록 버튼 찾기
    # ==================================================

    print()
    print("===== 등록 시도 =====")

    write_button = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn_blue.btn_svc.write"
    )

    print("등록 버튼 발견")
    print("버튼 텍스트:", write_button.text)
    print("표시 여부:", write_button.is_displayed())
    print("활성 여부:", write_button.is_enabled())


    # ==================================================
    # 8. 실제 등록 클릭
    # ==================================================

    print()
    print("등록 버튼 클릭")

    write_button.click()

    print("클릭 완료")

    # 등록 처리 대기
    time.sleep(10)


    # ==================================================
    # 9. 결과 확인
    # ==================================================

    print()
    print("===== 등록 후 결과 =====")

    print(
        "현재 주소:",
        driver.current_url
    )

    print(
        "페이지 제목:",
        driver.title
    )


    body_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text


    print()
    print("===== 화면 텍스트 앞부분 =====")

    print(
        body_text[:2000]
    )


    # ==================================================
    # 10. 결과 스크린샷
    # ==================================================

    driver.save_screenshot(
        "after_submit.png"
    )

    print()
    print(
        "결과 스크린샷 저장 완료: "
        "after_submit.png"
    )


finally:

    driver.quit()

    print()
    print("크롬 종료")

root@crawler:~#
