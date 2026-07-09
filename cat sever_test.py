root@crawler:~# cat sever_test.py
from flask import Flask, request
from regex_test import extract_images
from nickdate_test import extract_nickdate
from concurrent.futures import ThreadPoolExecutor
import time

app = Flask(__name__)


@app.route("/extract", methods=["POST"])
def extract():

    data = request.get_json()

    if not data or "url" not in data:
        return {
            "success": False,
            "message": "URL 없음"
        }

    url = data["url"]

    try:
        start = time.time()

        images = extract_images(url)

        print(
            f"[시간] extract_images : "
            f"{time.time() - start:.2f}초",
            flush=True
        )

        return {
            "success": True,
            "images": images
        }

    except Exception as e:
        print(
            f"[오류] {e}",
            flush=True
        )

        return {
            "success": False,
            "message": str(e)
        }


@app.route("/extract-info", methods=["POST"])
def extract_info():

    data = request.get_json()

    if not data or "urls" not in data:
        return {
            "success": False,
            "message": "URL 목록 없음"
        }

    urls = data["urls"]

    try:
        start = time.time()

        # 날짜/작성자 추출 작업을 최대 4개씩 병렬 처리
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(
                executor.map(
                    extract_nickdate,
                    urls
                )
            )

        print(
            f"[시간] extract_nickdate : "
            f"{time.time() - start:.2f}초",
            flush=True
        )

        return {
            "success": True,
            "results": results
        }

    except Exception as e:
        print(
            f"[오류] {e}",
            flush=True
        )

        return {
            "success": False,
            "message": str(e)
        }


@app.route("/")
def home():
    return "Server OK"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
root@crawler:~#
