# First commit: 2026-07-20
# Last commit: 2026-07-20
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import getpass
import time


LOGIN_URL = (
    "https://sign.dcinside.com/login"
    "?s_url=https://www.dcinside.com/"
)

WRITE_URL = (
    "https://gall.dcinside.com/"
    "mgallery/board/write/?id=catfiesta"
)


# ==================================================
# 1. 터미널에서 로그인 정보 입력/opt/crawler/login_test.py
# ==================================================

user_id = input("아이디 입력: ")
user_pw = getpass.getpass("비밀번호 입력: ")


# ==================================================
# 2. Chrome 설정
# ==================================================

options = Options()

options.binary_location = "/usr/bin/google-chrome"

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# 로그인 페이지 정상 표시를 위한 데스크톱 UA
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36"
)


driver = webdriver.Chrome(
    options=options
)


try:

    # ==================================================
    # 3. 로그인 페이지 접속
    # ==================================================

    print()
    print("[1] Chrome 실행 성공")

    driver.get(LOGIN_URL)

    print("[2] 로그인 페이지 접속")

    time.sleep(3)


    # ==================================================
    # 4. 아이디 입력
    # ==================================================

    id_input = driver.find_element(
        By.NAME,
        "user_id"
    )

    id_input.clear()
    id_input.send_keys(user_id)

    print("[3] 아이디 입력 완료")


    # ==================================================
    # 5. 비밀번호 입력
    # ==================================================

    pw_input = driver.find_element(
        By.NAME,
        "pw"
    )

    pw_input.clear()
    pw_input.send_keys(user_pw)

    print("[4] 비밀번호 입력 완료")


    # ==================================================
    # 6. 로그인 버튼 클릭
    # ==================================================

    login_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    print("[5] 로그인 버튼 발견")

    login_button.click()

    print("[6] 로그인 버튼 클릭 완료")

    time.sleep(7)


    # ==================================================
    # 7. 로그인 결과 확인
    # ==================================================

    print()
    print("========== 로그인 결과 ==========")

    print("현재 주소:", driver.current_url)
    print("페이지 제목:", driver.title)

    # ==================================================
    # 8. 같은 Chrome으로 글쓰기 페이지 이동
    # ==================================================

    print()
    print("[7] 글쓰기 페이지 이동")

    driver.get(WRITE_URL)

    time.sleep(5)

    print("[8] 글쓰기 페이지 로딩 완료")
    print("현재 주소:", driver.current_url)
    print("페이지 제목:", driver.title)
    print("HTML 크기:", len(driver.page_source))


    # ==================================================
    # 9. INPUT 조사
    # ==================================================

    print()
    print("========== INPUT 목록 ==========")

    inputs = driver.find_elements(
        By.TAG_NAME,
        "input"
    )

    print("INPUT 개수:", len(inputs))

    for i, element in enumerate(inputs, start=1):

        print(
            f"[{i}]",
            "type =", element.get_attribute("type"),
            "| name =", element.get_attribute("name"),
            "| id =", element.get_attribute("id"),
            "| value =", element.get_attribute("value")
        )


    # ==================================================
    # 10. TEXTAREA 조사
    # ==================================================

    print()
    print("========== TEXTAREA 목록 ==========")

    textareas = driver.find_elements(
        By.TAG_NAME,
        "textarea"
    )

    print("TEXTAREA 개수:", len(textareas))

    for i, element in enumerate(textareas, start=1):

        print(
            f"[{i}]",
            "name =", element.get_attribute("name"),
            "| id =", element.get_attribute("id"),
            "| class =", element.get_attribute("class"),
            "| 표시 =", element.is_displayed()
        )


    # ==================================================
    # 11. BUTTON 조사
    # ==================================================

    print()
    print("========== BUTTON 목록 ==========")

    buttons = driver.find_elements(
        By.TAG_NAME,
        "button"
    )

    print("BUTTON 개수:", len(buttons))

    for i, element in enumerate(buttons, start=1):

        print(
            f"[{i}]",
            "type =", element.get_attribute("type"),
            "| class =", element.get_attribute("class"),
            "| text =", element.text,
            "| 표시 =", element.is_displayed()
        )


    # ==================================================
    # 12. 우리가 특히 궁금한 요소 개별 확인
    # ==================================================

    print()
    print("========== 핵심 요소 확인 ==========")


    # 비밀번호 입력칸
    password_fields = driver.find_elements(
        By.NAME,
        "password"
    )

    print(
        "password 입력칸 개수:",
        len(password_fields)
    )


    # 제목 입력칸
    subject_fields = driver.find_elements(
        By.NAME,
        "subject"
    )

    print(
        "subject 입력칸 개수:",
        len(subject_fields)
    )


    # HTML 버튼
    html_buttons = driver.find_elements(
        By.XPATH,
        "//button[normalize-space()='HTML']"
    )

    print(
        "HTML 버튼 개수:",
        len(html_buttons)
    )


    # HTML 본문 입력창
    html_areas = driver.find_elements(
        By.CSS_SELECTOR,
        ".note-codable"
    )

    print(
        ".note-codable 개수:",
        len(html_areas)
    )


    # 등록 버튼
    write_buttons = driver.find_elements(
        By.CSS_SELECTOR,
        "button.btn_blue.btn_svc.write"
    )

    print(
        "등록 버튼 개수:",
        len(write_buttons)
    )


    # ==================================================
    # 13. 화면 텍스트 일부 출력
    # ==================================================

    print()
    print("========== 화면 텍스트 앞부분 ==========")

    body_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text

    print(body_text[:3000])


    # ==================================================
    # 14. 스크린샷 저장
    # ==================================================

    driver.save_screenshot(
        "logged_in_write_page.png"
    )

    print()
    print(
        "스크린샷 저장 완료: "
        "logged_in_write_page.png"
    )


finally:

    driver.quit()

    print()
    print("Chrome 종료")
