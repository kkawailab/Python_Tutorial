from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

# 基本的なルーティング
@app.route('/')
def index():
    return 'ホームページ'

# HTTPメソッドの指定
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f'{username}さん、ログインしました'
    return '''
    <form method="POST">
        <input type="text" name="username" placeholder="ユーザー名">
        <button type="submit">ログイン</button>
    </form>
    '''

# 変数ルール（型指定付き）
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'投稿ID: {post_id} の記事を表示'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'サブパス: {subpath}'

# JSONレスポンス
@app.route('/api/users')
def get_users():
    users = [
        {'id': 1, 'name': '田中太郎'},
        {'id': 2, 'name': '山田花子'}
    ]
    return jsonify(users)

# リダイレクト
@app.route('/old-page')
def old_page():
    return redirect(url_for('index'))

# エラーハンドリング
@app.errorhandler(404)
def page_not_found(e):
    return 'ページが見つかりません', 404

# URLの構築例
@app.route('/profile/<username>')
def profile(username):
    return f'{username}さんのプロフィール'

@app.route('/test-url')
def test_url():
    # url_forを使ってURLを生成
    return f'''
    <ul>
        <li><a href="{url_for('index')}">ホーム</a></li>
        <li><a href="{url_for('profile', username='tanaka')}">田中さんのプロフィール</a></li>
        <li><a href="{url_for('show_post', post_id=123)}">投稿123</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)