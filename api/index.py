from flask import Flask, jsonify, request
import random, os, re

app = Flask(__name__)

TXT_PATH = os.path.join(os.path.dirname(__file__), 'hitokoto.txt')

# 按段落读取：以空行分隔，每个段落是一个"一段话"
with open(TXT_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 用两个及以上换行切分段落（兼容 Windows 的 \r\n）
paragraphs = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]

@app.route('/')
@app.route('/api/hitokoto')
def hitokoto():
    text = random.choice(paragraphs)
    mode = request.args.get('encode')

    if mode == 'text':
        # 纯文本模式：保留原始换行
        return text, 200, {'Content-Type': 'text/plain; charset=utf-8'}

    if mode == 'html' or request.args.get('html'):
        # 网页模式：换行转成 <br>，方便直接插入 HTML
        html = text.replace('\n', '<br>')
        return jsonify({"code": 200, "hitokoto": html})

    if mode == 'oneline':
        # 单行模式：多句压成一行（用空格连接）
        flat = ' '.join(text.split('\n'))
        return jsonify({"code": 200, "hitokoto": flat})

    # 默认 JSON：保留 \n 换行符
    return jsonify({"code": 200, "hitokoto": text})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
