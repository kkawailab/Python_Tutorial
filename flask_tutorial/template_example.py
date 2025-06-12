from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # フラッシュメッセージ用

@app.route('/')
def index():
    # テンプレートに渡すデータ
    context = {
        'name': 'ゲスト',
        'current_time': datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),
        'user_logged_in': False,
        'items': ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS'],
        'message': 'flaskは素晴らしいフレームワークです'
    }
    return render_template('index.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
def user_profile(username):
    # ユーザー情報（実際はデータベースから取得）
    user = {
        'username': username,
        'email': f'{username}@example.com',
        'joined_date': '2024年1月1日',
        'posts': [
            {'title': 'Flaskを始めました', 'date': '2024年1月5日'},
            {'title': 'テンプレートの使い方', 'date': '2024年1月10日'},
            {'title': 'データベース連携', 'date': '2024年1月15日'}
        ]
    }
    return render_template('user_profile.html', user=user)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # フラッシュメッセージ
        flash(f'{name}さん、お問い合わせありがとうございます！', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# カスタムフィルターの例
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

# コンテキストプロセッサー（すべてのテンプレートで使える変数を定義）
@app.context_processor
def inject_globals():
    return {
        'site_name': 'Flask チュートリアル',
        'current_year': datetime.now().year
    }

if __name__ == '__main__':
    app.run(debug=True)