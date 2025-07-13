from flask import Flask, request, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64
from datetime import datetime
import traceback
app = Flask(__name__)

# 지원 언어 목록
VALID_LANGS = ['ko', 'en', 'ja', 'es']

@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    audio = None

    if request.method == "POST":
        text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", "ko")

        # 입력 검증
        if not text:
            error = "⚠️ 텍스트를 입력하세요."
        elif lang not in VALID_LANGS:
            error = "⚠️ 지원되지 않는 언어입니다."
        else:
            try:
                # gTTS 변환
                tts = gTTS(text=text, lang=lang, tld="com")
                fp = BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)

                # base64 인코딩
                audio = base64.b64encode(fp.read()).decode("utf-8")

                # 로그 저장
                with open("input_log.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} | lang={lang} | text={text}\n")

            except Exception as e:
                error = "⚠️ 음성 변환 중 오류가 발생했습니다."

    return render_template("index.html", error=error, audio=audio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
