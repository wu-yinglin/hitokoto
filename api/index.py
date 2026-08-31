from flask import Flask, jsonify, request
import random, os, re

app = Flask(__name__)

TXT_PATH = os.path.join(os.path.dirname(__file__), 'hitokoto.txt')

with open(TXT_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

paragraphs = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]

def add_blank_before_dot(text):
    """只在每个 ▪ 前面加一个空行"""
    result = text.replace('▪', '\n\n▪')
    return result.lstrip('\n')   # 去掉开头的空行

@app.route('/')
@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(paragraphs)
    mode = request.args.get('encode')

    if mode == 'text':
        return add_blank_before_dot(text), 200, {'Content-Type': 'text/plain; charset=utf-8'}

    if mode == 'html' or request.args.get('html'):
        html = add_blank_before_dot(text).replace('\n\n', '<br><br>').replace('\n', '<br>')
        return jsonify({"code": 200, "hitokoto": html})

    return jsonify({"code": 200, "hitokoto": add_blank_before_dot(text)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
