import os
from flask import Flask, render_template, request, jsonify
import dashscope
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# --- 核心路径修正（解决 500 错误的杀手锏） ---
# 获取当前 main.py 所在的 api 目录
base_dir = os.path.dirname(os.path.abspath(__file__))
# 定位到 api 文件夹的上一层（项目根目录）
root_dir = os.path.abspath(os.path.join(base_dir, '..'))

app = Flask(__name__, 
            template_folder=os.path.join(root_dir, 'templates'), 
            static_folder=os.path.join(root_dir, 'static'))

# 配置 API 密钥（确保 Vercel 设置中 Key 名为 ALIYUN_API_KEY）
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
    try:
        user_input = request.json.get("question", "")
        answer = "这是一个好问题！你可以尝试问我：科学上网、学习收获 或 网页搭建。"
        
        for key in KNOWLEDGE_BASE:
            if key in user_input:
                answer = KNOWLEDGE_BASE[key]
                break
                
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"出错啦：{str(e)}"})

# Vercel 不需要 app.run()
