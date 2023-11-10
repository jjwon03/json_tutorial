# A very simple Flask Hello World app for you to get started with...
"안녕하세요? 만나서 만나서 정말 정말 정말 반갑습니다!"
# {"안녕하세요?": 1,
#  "만나서": 2,
#  "정말": 3,
#  "반갑습니다!":1}
from flask import Flask
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '안녕 안녕 반가워 반가워 반가워 반가워 고양이 고양이 고양이 냐옹 나옹 '
    counter = dict(Counter(user_string))
    result = json.dumps(counter)
    return result