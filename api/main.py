import os
from flask import Flask, render_template, request, jsonify
import dashscope
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 1. 强制使用 Vercel 最兼容的路径配置
# 在 Vercel 的 api 运行环境中，使用相对路径 '../' 来定位根目录下的文件夹
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

# 2. 配置 API 密钥
dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# 3. 简单的路由设置（确保不产生变量冲突）
@app.route('/')
def home():
    try:
        # 只要 index.html 存在，这行就能成功
        return render_template('index.html')
    except Exception as e:
        return f"模板渲染错误: {str(e)}"

@app.route('/reflections')
def reflections():
    return render_template('reflections.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

# 4. AI 问答接口
@app.route('/ask', methods=['POST'])
def ask_ai():
    try:
        # 即使 AI 还没完全调通，也要确保接口不崩
        user_input = request.json.get("question", "")
        return jsonify({"answer": f"收到你的消息：{user_input}。目前服务器连接正常！"})
    except Exception as e:
        return jsonify({"answer": f"接口异常: {str(e)}"})
