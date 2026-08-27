from flask import Flask, jsonify, request
import random, os

app = Flask(__name__)

# txt 就放在同目录下的 api 文件夹里
TXT_PATH = os.path.join(os.path.dirname(__file__), 'hitokoto.txt')

with open(TXT_PATH, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

@app.route('/')
@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(lines)
    if request.args.get('encode') == 'text':
        return text, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return jsonify({"code": 200, "hitokoto": text})

# 注意：这里不要写 app.run()！Vercel 会自己处理启动
