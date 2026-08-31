from flask import Flask, jsonify, request
import random, os, re

app = Flask(__name__)

TXT_PATH = os.path.join(os.path.dirname(__file__), 'hitokoto.txt')

# 按段落读取
with open(TXT_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

paragraphs = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]

@app.route('/')
@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(paragraphs)
    mode = request.args.get('encode')

    if mode == 'text':
        # 前面加了一个 \n ← 改动点
        return '\n' + text, 200, {'Content-Type': 'text/plain; charset=utf-8'}

    if mode == 'html' or request.args.get('html'):
        html = text.replace('\n', '<br>')
        # 前面加了一个 <br> ← 改动点
        return jsonify({"code": 200, "hitokoto": '<br>' + html})

    # 前面加了一个 \n ← 改动点
    return jsonify({"code": 200, "hitokoto": '\n' + text})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
