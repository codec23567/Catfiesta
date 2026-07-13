(venv) root@crawler:/opt/crawler# cat login_modify_actual.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


LOGIN_URL = (
    "https://sign.dcinside.com/login"
    "?s_url=https://www.dcinside.com/"
)


def modify_post(
    user_id,
    user_pw,
    modify_url,
    html
):

    options = Options()

    options.binary_location = "/usr/bin/google-chrome"

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)

    try:

        # ============================================
        # 로그인
        # ============================================

        driver.get(LOGIN_URL)

        time.sleep(3)

        id_input = driver.find_element(
            By.NAME,
            "user_id"
        )

        id_input.clear()
        id_input.send_keys(user_id)
        pw_input = driver.find_element(
            By.NAME,
            "pw"
        )

        pw_input.clear()
        pw_input.send_keys(user_pw)

        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        )

        login_button.click()

        time.sleep(7)


        # ============================================
        # 수정 페이지 이동
        # ============================================

        driver.get(modify_url)

        time.sleep(5)


        # ============================================
        # HTML 모드
        # ============================================

        html_button = driver.find_element(
            By.XPATH,
            "//button[normalize-space()='HTML']"
        )

        html_button.click()

        time.sleep(2)


        # ============================================
        # 본문 교체
        # ============================================

        html_area = driver.find_element(
            By.CSS_SELECTOR,
            ".note-codable"
        )

        html_area.clear()
        html_area.send_keys(html)


        # ============================================
        # 수정 버튼
        # ============================================

        write_button = driver.find_element(
            By.CSS_SELECTOR,
            "button.btn_blue.write"
        )

        write_button.click()

        time.sleep(3)

        return {
            "success": True
        }


    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


    finally:

        driver.quit()
(venv) root@crawler:/opt/crawler#
