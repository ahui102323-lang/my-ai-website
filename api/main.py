import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import dashscope
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

dashscope.api_key = os.getenv('ALIYUN_API_KEY')

# --- 完美修复：解决日志中的 404 图标报错 ---
@app.route('/favicon.ico')
@app.route('/favicon.png')
def favicon():
    # 告诉浏览器：如果找不到图标，就去 static/images 目录找，或者干脆忽略
    return send_from_directory(os.path.join(app.root_path, '../static/images'),
                               'ai.png', mimetype='image/png')

def safe_render(template_name):
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
        # 这里你可以对接真正的 dashscope.Generation.call(...)
        return jsonify({"answer": f"AI 已就绪！您说的是：{user_input}"})
    except Exception as e:
        return jsonify({"answer": f"错误: {str(e)}"})
