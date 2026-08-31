from flask import Flask, jsonify, request
import random, os, re

app = Flask(__name__)

TXT_PATH = os.path.join(os.path.dirname(__file__), 'hitokoto.txt')

with open(TXT_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

paragraphs = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]

BLANK_LINE = '\u3000'   # 全角空格行：固件不会丢弃

def add_blank_before_dot(text):
    result = text.replace('▪', '\n' + BLANK_LINE + '\n▪')
    return result.lstrip('\n')

@app.route('/')
@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(paragraphs)
    mode = request.args.get('encode')

    if mode == 'text':
        return add_blank_before_dot(text), 200, {'Content-Type': 'text/plain; charset=utf-8'}

    if mode == 'html' or request.args.get('html'):
        html = add_blank_before_dot(text).replace('\n', '<br>')
        return jsonify({"code": 200, "hitokoto": html})

    return jsonify({"code": 200, "hitokoto": add_blank_before_dot(text)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
