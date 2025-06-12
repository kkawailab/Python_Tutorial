from flask import Flask

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ルートURLへのルーティング
@app.route('/')
def hello_world():
    return 'Hello, Flask! これは最初のFlaskアプリケーションです。'

# 動的ルーティングの例
@app.route('/user/<name>')
def show_user(name):
    return f'こんにちは、{name}さん！'

# 複数のHTTPメソッドを受け付けるルート
@app.route('/about')
def about():
    return 'このサイトについて'

if __name__ == '__main__':
    # デバッグモードで起動（開発時のみ使用）
    app.run(debug=True, host='0.0.0.0', port=5000)