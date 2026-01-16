from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 你的个人信息（可以根据需要修改这里）
USER_INFO = {
    "name": "阿辉 (Ahui)",
    "role": "AI 探索者 / Python 初学者",
    "motto": "提问比答案更重要，用 AI 赋能成长。",
    "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" # 自动生成的头像
}

KNOWLEDGE_BASE = {
    "科学上网": "科学上网是接触全球 AI 资源的门票。通过合法合规的方式访问国际互联网，我们可以使用 ChatGPT, Gemini 等顶级工具。",
    "学习收获": "通过与 AI 交互，我意识到‘提问’比‘答案’更重要。活到老学到老在 AI 时代变得触手可及。",
    "网页搭建": "本网页使用 Python 的 Flask 框架搭建，体现了从小白到开发者的跨越。"
}

@app.route('/')
def home():
    return render_template('index.html', user=USER_INFO)

@app.route('/reflections')
def reflections():
    return render_template('reflections.html', user=USER_INFO)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', user=USER_INFO)

@app.route('/chat')
def chat_page():
    return render_template('chat.html', user=USER_INFO)

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_input = request.json.get("question", "")
    answer = "这是一个好问题！你可以尝试问我：科学上网、学习收获 或 网页搭建。"
    for key in KNOWLEDGE_BASE:
        if key in user_input:
            answer = KNOWLEDGE_BASE[key]
            break
    return jsonify({"answer": answer})

if __name__ == '__main__':
    # 只要这一行即可，Vercel 会自动寻找 app 对象
    app = Flask(__name__)