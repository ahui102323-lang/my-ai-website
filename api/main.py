import os
from flask import Flask, render_template, request, jsonify
import dashscope
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# 定义一个通用的安全渲染函数
def safe_render(template_name):
    # 强制传入 user=None，解决 HTML 里的 {{ user }} 报错问题
    return render_template(template_name, user=None)

@app.route('/')
def home():
    return safe_render('index.html')

@app.route('/reflections')
def reflections():
    return safe_render('reflections.html')

@app.route('/gallery')
def gallery():
    return safe_render('gallery.html')

@app.route('/chat')
def chat_page():
    return safe_render('chat.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    try:
        user_input = request.json.get("question", "")
        return jsonify({"answer": f"已收到消息：{user_input}，AI 模块准备就绪！"})
    except Exception as e:
        return jsonify({"answer": f"错误: {str(e)}"})
