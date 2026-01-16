import os
from flask import Flask, render_template, request, jsonify
import dashscope
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# --- 核心改动：使用 Vercel 最兼容的路径写法 ---
# 在 Vercel 中，api 文件夹内的函数运行时，根目录通常被映射为当前执行环境
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

# 配置 API 密钥
dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# 模拟知识库
KNOWLEDGE_BASE = {
    "科学上网": "科学上网是接触全球 AI 资源的门票。",
    "学习收获": "我意识到‘提问’比‘答案’更重要。",
    "网页搭建": "本网页使用 Python 的 Flask 框架搭建。"
}

@app.route('/')
def home():
    try:
        # 如果还是找不到，尝试直接返回 template 名
        return render_template('index.html')
    except Exception as e:
        # 这里会显示更具体的错误信息，帮我们做最后判断
        return f"当前运行路径: {os.getcwd()}，错误详情: {str(e)}"

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
        answer = "你可以尝试问我：科学上网、学习收获 或 网页搭建。"
        for key in KNOWLEDGE_BASE:
            if key in user_input:
                answer = KNOWLEDGE_BASE[key]
                break
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"AI服务暂不可用: {str(e)}"})
