from flask import Flask, render_template, request, jsonify
import os
import dashscope
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 显式指定路径，确保 Vercel 能在 api 目录的上一级找到网页文件
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

# 配置 API 密钥
dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# 模拟的 AI 知识库
KNOWLEDGE_BASE = {
    "科学上网": "科学上网是接触全球 AI 资源的门票。通过合法合规的方式访问国际互联网，我们可以使用 ChatGPT, Gemini 等顶级工具。",
    "学习收获": "通过与 AI 交互，我意识到‘提问’比‘答案’更重要。活到老学到老在 AI 时代变得触手可及。",
    "网页搭建": "本网页使用 Python 的 Flask 框架搭建，体现了从小白到开发者的跨越。"
}

@app.route('/')
def home():
    return render_template('index.html')

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
    user_input = request.json.get("question", "")
    answer = "这是一个好问题！你可以尝试问我：科学上网、学习收获 或 网页搭建。"
    
    for key in KNOWLEDGE_BASE:
        if key in user_input:
            answer = KNOWLEDGE_BASE[key]
            break
            
    return jsonify({"answer": answer})
