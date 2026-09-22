# First commit: 2026-07-20
# Last commit: 2026-07-20
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import getpass
import time


# ==================================================
# 주소 설정/opt/crawler/login_amodify.py
# ==================================================

LOGIN_URL = (
    "https://sign.dcinside.com/login"
    "?s_url=https://www.dcinside.com/"
)

WRITE_URL = (
    "https://gall.dcinside.com/"
    "mgallery/board/modify/?id=catfiesta&no=57"
)


# ==================================================
# 1. 터미널에서 로그인 정보 입력
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
    # 8. 글쓰기 페이지 이동
    # ==================================================

    print()
    print("[7] 글쓰기 페이지 이동")

    driver.get(WRITE_URL)

    time.sleep(5)

    print("[8] 글쓰기 페이지 로딩 완료")
    print("현재 주소:", driver.current_url)
    print("페이지 제목:", driver.title)


    # ==================================================
    # 9. 제목 입력
    # ==================================================

    print()
    print("===== 제목 입력 =====")

    subject = driver.find_element(
        By.NAME,
        "subject"
    )

    subject.clear()
    subject.send_keys("battlecat")

    print(
        "제목 입력 완료:",
        subject.get_attribute("value")
    )


    # ==================================================
    # 10. HTML 모드 전환
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
    # 11. HTML 본문 입력
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
    html_area.send_keys("""<img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b2e62c3b56dc2c3c414d4600b7304882b4fc173c2dd99faf46412aa81c82276d1d1fbf339f59fadce55c6deedb6eaa2c9a4b8c65f8055c2905f1ee82d89f0c1e5a02e808189751491f47feca0ed6a98068adbd95d6555b6d5154cae29915d7ef855f7cf2612a889d5547fa47123b2690510d46770cfa162565b1302f1a4207b12e7950c2c"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/1287997"><b>파이파이</b></a></span><div style="font-size:33px;"><br></div><img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b296ec1be61c5c67542bf64a5b03fe6048bc953e11d578ab744087e916425e5bc1a19e5434d4b7a4a723b6a67980b6b7a1f4be4d44799c05687703d8b6c6dda323e9f10f5adbe70e59dec17db5f21930c4a3dbed238b1f21b8c0e3df52bab7e4a7716c2d51cc0d0b5d389bb05c08da65b3fd8006488ae56a3d3356dadbbc0dcea86eed4b3"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/1288249"><b>사쿠라</b></a></span><div style="font-size:33px;"><br></div><img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b2e66c1bf6dcec2ab2fa18f1f862f0fb4ce28f38dfbfaf2461ea02e4b733156ea478535b1bf2ee88221bc6fc1bbb2c2b8311d62989058a84723ea9ad66098a7a7bb19a4eb877893abb7d8e8869ab0f986ec9201693ac62b3a3fdc4bd13f993aa54634550f82514c46c13256181724c73c5645d900ab2ea7c40dcd092d9621fcb958f357b2"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/990255"><b>엠마</b></a></span><div style="font-size:33px;"><br></div><img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b2b67c0b46dc7c8b742ddbe8edff3f356a4e198871a45500ef6646bba25fee555a637f870a611e9ec85c6d5ef5a8588bf09311ecad866b47f65fae3240950901faf4382c4078549d4c40bb7f2521320c9ebef0f39ef298eb29dd58d9c3494812490a55c90ea4eef166c5689440f388c"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/1277076"><b>트릭시</b></a></span><div style="font-size:33px;"><br></div><img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b2962c0bf6fc7c8f4f7ffcb30ecbd144a22397c9150323d7beebce6d01ba1a343a59dfd33c21d9368b74957629a1e87512071c8ce039a09d115f95ede35035c47e3504003890c19d8aa65d184eddee6c56dc41d4802a00462711fe7bbbcaffeda2e9fc9a96f05236f4dfa4db723b7a4"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/1420112"><b>스탈</b></a></span><div style="font-size:33px;"><br></div><img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b2863c5be6ecfc5a2e66d161b293e82db37f6bb14bc3187616d148313b840b01601d4b3057ca70f860381f2c301791c557191ba260afdbc6563a63ec13e844a50586a089f2f7a2b3cb2af05013c1fa8c7d90767a8ba71a8c5e45af23dd2b9853f988dbda1165fc6f4f81f0c72435257"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/1230277"><b>왕녀</b></a></span><div style="font-size:33px;"><br></div><img src="https://dcimg3.dcinside.co.kr/viewimage.php?id=2ebcc420ecd72bb26f&no=24b0d769e1d32ca73fe784fa11d028316e90785a65405c690dfe698237454a1be33b5f5da9ff14725b2e60c9b16fc4c1b5f32fdb91c4e3342e0c6e1ccf215895961954f2bc296e929c59f3307f125cc23653d1b90d6d85fb1e645452f5c2bd944589d33fd0a3bcdbd07f6ab94a542e772e304229da2916791bc46857755b75c7680f22be3f541bd9e014b9ae2ec8f25a2c25ad137f1a8550"><br><span style="font-size: 22px;"><a href="https://m.dcinside.com/board/yavetwarch/1231038"><b>꼬꼬미1</b></a> / <a href="https://m.dcinside.com/board/yavetwarch/1422041"><b>2</b></a></span><div style="font-size:33px;"><br></div>

""")

    print(
        "HTML 입력 결과:",
        html_area.get_attribute("value")
    )


    # ==================================================
    # 12. 등록 전 스크린샷
    # ==================================================

    driver.save_screenshot(
        "login_post_before_submit.png"
    )

    print()
    print(
        "등록 전 스크린샷 저장 완료: "
        "login_post_before_submit.png"
    )


    # ==================================================
    # 13. 등록 버튼 찾기
    # ==================================================

    print()
    print("===== 등록 시도 =====")


    write_button = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn_blue.write"
    )

    print("등록 버튼 발견")
    print("버튼 텍스트:", write_button.text)
    print("표시 여부:", write_button.is_displayed())
    print("활성 여부:", write_button.is_enabled())


    # ==================================================
    # 14. 실제 등록 클릭
    # ==================================================

    print()
    print("등록 버튼 클릭")

    write_button.click()
    print("클릭 완료")

    time.sleep(10)


    # ==================================================
    # 15. 등록 결과 확인
    # ==================================================

    print()
    print("========== 등록 후 결과 ==========")

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
        body_text[:3000]
    )


    # ==================================================
    # 16. 등록 후 스크린샷
    # ==================================================

    driver.save_screenshot(
        "login_post_after_submit.png"
    )

    print()
    print(
        "등록 후 스크린샷 저장 완료: "
        "login_post_after_submit.png"
    )


finally:

    driver.quit()

    print()
    print("Chrome 종료")

