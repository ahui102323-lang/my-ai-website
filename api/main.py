import os
from flask import Flask, render_template, request, jsonify
import dashscope
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 1. 路径设置
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

# 2. 配置 API 密钥
dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# 3. 路由设置
@app.route('/')
def home():
    try:
        # 核心修正：补齐 HTML 模板可能需要的空变量，防止 'undefined' 报错
        return render_template('index.html', user=None, error=None)
    except Exception as e:
        return f"模板渲染发生错误: {str(e)}"

@app.route('/reflections')
def reflections():
    return render_template('reflections.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    try:
        user_input = request.json.get("question", "")
        # 这里预留了简单的 AI 逻辑
        answer = f"服务器已收到您的提问：'{user_input}'。目前连接正常！"
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"AI服务暂时无法访问: {str(e)}"})
