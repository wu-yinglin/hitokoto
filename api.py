from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# 启动时读取一次，避免每次请求都读磁盘
with open('hitokoto.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(lines)
    # 支持纯文本模式 ?encode=text
    if request.args.get('encode') == 'text':
        return text, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return jsonify({
        "code": 200,
        "hitokoto": text
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
