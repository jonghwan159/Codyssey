# app.py
from flask import Flask, request, Response
import os
from io import BytesIO
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():
    text = "Hello, DevOps"
    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, lang=lang, tld="com").write_to_fp(fp)
    fp.seek(0)
    return Response(fp.getvalue(), mimetype='audio/mpeg')

if __name__ == "__main__":
    app.run('0.0.0.0', 5400)  # ← 포트 변경됨
