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

# 3. 路由设置 - 为每个页面补齐基础变量，防止 undefined 报错
@app.route('/')
def home():
    return render_template('index.html', user=None)

@app.route('/reflections')
def reflections():
    # 补齐子页面可能需要的变量
    return render_template('reflections.html', user=None)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', user=None)

@app.route('/chat')
def chat_page():
    return render_template('chat.html', user=None)

# 4. AI 问答接口
@app.route('/ask', methods=['POST'])
def ask_ai():
    try:
        user_input = request.json.get("question", "")
        # 这里是简单的 AI 逻辑
        answer = f"连接成功！您输入的是：'{user_input}'。目前 AI 助手已准备就绪。"
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"AI服务暂时无法访问: {str(e)}"})
