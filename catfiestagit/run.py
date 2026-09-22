# First commit: 2026-07-20
# Last commit: 2026-07-21
import json
import os
import requests

from login_modify_actual import modify_post
from login_modify_normal import modify_normal_post
from nickdate_test import extract_nickdate

print("GitHub Actions 시작")

mode = os.environ["INPUT_MODE"]
user_id = os.environ["INPUT_ID"]
user_pw = os.environ["INPUT_PW"]
modify_url = os.environ["INPUT_URL"]
html = os.environ["INPUT_HTML"]
text = os.environ["INPUT_TEXT"]

if mode == "html":

    result = modify_post(
        user_id=user_id,
        user_pw=user_pw,
        modify_url=modify_url,
        html=html
    )

elif mode == "text":

    result = modify_normal_post(
        user_id=user_id,
        user_pw=user_pw,
        modify_url=modify_url,
        text=text
    )

elif mode == "extract_info":

    urls = json.loads(os.environ.get("INPUT_URLS", "[]"))

    result = [extract_nickdate(url) for url in urls]

    response = requests.post(
        os.environ["GAS_WEBAPP_URL"],
        json={
            "secret": os.environ["GAS_SECRET"],
            "sheet": os.environ.get("INPUT_SHEET", ""),
            "results": result
        },
        timeout=30
    )

    response.raise_for_status()
    print(response.text)

else:
    raise ValueError(f"Unknown mode: {mode}")

print(result)
print("INPUT_SHEET =", os.environ.get("INPUT_SHEET"))
print("GAS_WEBAPP_URL =", os.environ.get("GAS_WEBAPP_URL"))
