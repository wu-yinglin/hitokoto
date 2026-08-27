from flask import Flask, jsonify, request
import random, os

app = Flask(__name__)

# 修正路径：兼容本地和线上
TXT_PATH = os.path.join(os.path.dirname(__file__), 'hitokoto.txt')

with open(TXT_PATH, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(lines)
    if request.args.get('encode') == 'text':
        return text, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return jsonify({"code": 200, "hitokoto": text})
