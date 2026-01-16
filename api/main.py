from flask import Flask, render_template, request, jsonify
import os
import dashscope
from dashscope import Generation
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 这里的路径指定非常关键：因为 main.py 在 api 文件夹内，
# 它需要告诉 Flask 去上一层目录 (..) 寻找 templates 和 static 文件夹
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


# AI 问答的后端接口
@app.route('/ask', methods=['POST'])
def ask_ai():
    user_input = request.json.get("question", "")

    # 简单的关键词匹配模拟逻辑
    answer = "这是一个好问题！关于这个，我的建议是继续保持好奇心。你可以尝试问我：科学上网、学习收获 或 网页搭建。"

    for key in KNOWLEDGE_BASE:
        if key in user_input:
            answer = KNOWLEDGE_BASE[key]
            break

    return jsonify({"answer": answer})

# 在 Vercel 环境中，不需要 app.run()，Vercel 会自动处理入口