import os
from flask import Flask, render_template, request, jsonify
import dashscope
from dotenv import load_dotenv

# 1. 环境初始化
load_dotenv()

# 2. 强力路径定位：无论服务器在哪运行，都强制指向根目录
# 获取 main.py 所在文件夹 (api)
current_api_dir = os.path.dirname(os.path.abspath(__file__))
# 获取根目录 (api 的上一层)
project_root = os.path.abspath(os.path.join(current_api_dir, '..'))

# 3. 实例化 Flask，明确指定模板和静态文件位置
app = Flask(__name__, 
            template_folder=os.path.join(project_root, 'templates'), 
            static_folder=os.path.join(project_root, 'static'))

# 4. 配置 API 密钥 (确保 Vercel 环境变量名完全一致)
dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# 5. 模拟知识库
KNOWLEDGE_BASE = {
    "科学上网": "科学上网是接触全球 AI 资源的门票。通过合法合规的方式访问国际互联网，我们可以使用 ChatGPT, Gemini 等顶级工具。",
    "学习收获": "通过与 AI 交互，我意识到‘提问’比‘答案’更重要。活到老学到老在 AI 时代变得触手可及。",
    "网页搭建": "本网页使用 Python 的 Flask 框架搭建，体现了从小白到开发者的跨越。"
}

# --- 路由设置 ---

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"错误：找不到 index.html。请确认 templates 文件夹在根目录。报错详情: {str(e)}"

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
        return jsonify({"answer": f"AI 对话服务暂时不可用：{str(e)}"})

# Vercel 部署不需要 app.run()
