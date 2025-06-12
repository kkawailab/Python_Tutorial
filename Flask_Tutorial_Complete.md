# Python Flask 完全チュートリアル

## 目次
1. [はじめに](#はじめに)
2. [環境構築](#環境構築)
3. [基本的なFlaskアプリケーション](#基本的なflaskアプリケーション)
4. [ルーティングの詳細](#ルーティングの詳細)
5. [テンプレートエンジン（Jinja2）](#テンプレートエンジンjinja2)
6. [フォーム処理](#フォーム処理)
7. [データベース連携](#データベース連携)
8. [まとめ](#まとめ)

## はじめに

Flaskは、Pythonで書かれた軽量なWebアプリケーションフレームワークです。「マイクロフレームワーク」と呼ばれ、必要最小限の機能から始めて、必要に応じて拡張していくことができます。

### Flaskの特徴
- シンプルで学習しやすい
- 拡張性が高い
- RESTful APIの構築が容易
- 大規模なコミュニティとエコシステム

## 環境構築

### 1. プロジェクトディレクトリの作成

```bash
mkdir flask_tutorial
cd flask_tutorial
```

### 2. 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 仮想環境の有効化（macOS/Linux）
source venv/bin/activate
```

### 3. 必要なパッケージのインストール

まず、`requirements.txt`ファイルを作成します：

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
WTForms==3.1.1
email-validator==2.1.0.post1
```

次に、パッケージをインストールします：

```bash
pip install -r requirements.txt
```

### 4. ディレクトリ構造の作成

```bash
mkdir -p templates/forms templates/db templates/partials templates/macros
mkdir -p static/css static/js
mkdir instance
```

## 基本的なFlaskアプリケーション

### app.py - 最初のFlaskアプリ

```python
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
```

### 実行方法

```bash
python app.py
```

ブラウザで以下のURLにアクセスして動作を確認：
- http://localhost:5000/ - Hello, Flask!が表示される
- http://localhost:5000/user/田中 - 動的ルーティングの確認
- http://localhost:5000/about - 静的ページの表示

### 解説

1. **`Flask(__name__)`**: Flaskアプリケーションのインスタンスを作成。`__name__`は現在のPythonモジュール名を渡します。

2. **`@app.route()`**: デコレータを使用してURLパスと関数を関連付けます。

3. **動的ルーティング**: `<name>`のような変数部分を含むURLパターンを定義できます。

4. **`debug=True`**: 開発時に便利な機能（自動リロード、詳細なエラー表示）を有効にします。

## ルーティングの詳細

### routes_example.py - 高度なルーティング

```python
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
```

### 実行と確認

```bash
python routes_example.py
```

以下のURLで各機能を確認：
- http://localhost:5000/login - GET/POSTメソッドの処理
- http://localhost:5000/post/123 - 整数型の動的ルート
- http://localhost:5000/api/users - JSON APIレスポンス
- http://localhost:5000/test-url - url_forによるURL生成

### ルーティングの重要概念

1. **HTTPメソッド**: `methods`パラメータでGET、POST、PUT、DELETEなどを指定
2. **変数ルール**: `<変数名>`で動的な値を受け取る。型指定も可能（int、float、path、uuid）
3. **url_for()**: ルート名から動的にURLを生成。URLの変更に強い
4. **エラーハンドラー**: 特定のHTTPステータスコードに対するカスタム処理

## テンプレートエンジン（Jinja2）

### テンプレートの基本構造

#### templates/base.html - ベーステンプレート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Flask チュートリアル{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">ホーム</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
            <li><a href="{{ url_for('contact') }}">お問い合わせ</a></li>
        </ul>
    </nav>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Flask チュートリアル</p>
    </footer>
</body>
</html>
```

#### templates/index.html - 子テンプレート

```html
{% extends "base.html" %}

{% block title %}ホーム - Flask チュートリアル{% endblock %}

{% block content %}
<h1>Flask チュートリアルへようこそ！</h1>

<h2>変数の表示</h2>
<p>こんにちは、{{ name }}さん！</p>
<p>現在の時刻: {{ current_time }}</p>

<h2>条件分岐</h2>
{% if user_logged_in %}
    <p>ログイン済みです</p>
{% else %}
    <p>ログインしてください</p>
{% endif %}

<h2>ループ処理</h2>
<ul>
    {% for item in items %}
        <li>{{ loop.index }}. {{ item }}</li>
    {% endfor %}
</ul>

<h2>フィルターの使用</h2>
<p>大文字に変換: {{ message|upper }}</p>
<p>文字数: {{ message|length }}文字</p>
<p>デフォルト値: {{ undefined_var|default('値が設定されていません') }}</p>
{% endblock %}
```

### template_example.py - テンプレートを使用するアプリケーション

```python
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
```

### Jinja2の主な機能

1. **テンプレートの継承**: `{% extends %}` と `{% block %}` で共通レイアウトを再利用
2. **変数の表示**: `{{ variable }}` で変数を出力
3. **制御構造**: `{% if %}`, `{% for %}` などの制御文
4. **フィルター**: `{{ variable|filter }}` でデータを変換
5. **マクロ**: 再利用可能なテンプレート関数
6. **インクルード**: 部分テンプレートの読み込み

## フォーム処理

### forms_example.py - WTFormsを使用したフォーム処理

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# WTFormsを使用したフォームクラス
class RegistrationForm(FlaskForm):
    username = StringField('ユーザー名', validators=[
        DataRequired(message='ユーザー名は必須です'),
        Length(min=3, max=20, message='3文字以上20文字以下で入力してください')
    ])
    email = StringField('メールアドレス', validators=[
        DataRequired(message='メールアドレスは必須です'),
        Email(message='有効なメールアドレスを入力してください')
    ])
    password = PasswordField('パスワード', validators=[
        DataRequired(message='パスワードは必須です'),
        Length(min=6, message='6文字以上で入力してください')
    ])
    confirm_password = PasswordField('パスワード確認', validators=[
        DataRequired(message='パスワード確認は必須です'),
        EqualTo('password', message='パスワードが一致しません')
    ])
    terms = BooleanField('利用規約に同意する', validators=[
        DataRequired(message='利用規約への同意が必要です')
    ])
    submit = SubmitField('登録')

class ContactForm(FlaskForm):
    name = StringField('お名前', validators=[DataRequired()])
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    subject = SelectField('件名', choices=[
        ('general', '一般的なお問い合わせ'),
        ('support', 'サポート'),
        ('feedback', 'フィードバック'),
        ('other', 'その他')
    ])
    message = TextAreaField('メッセージ', validators=[
        DataRequired(),
        Length(min=10, max=500)
    ])
    submit = SubmitField('送信')

@app.route('/')
def index():
    return render_template('forms/index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # フォームデータの処理（実際はデータベースに保存）
        flash(f'ユーザー {form.username.data} の登録が完了しました！', 'success')
        return redirect(url_for('index'))
    
    return render_template('forms/register.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        # フォームデータの処理
        flash('お問い合わせを受け付けました。', 'info')
        return redirect(url_for('contact'))
    
    return render_template('forms/contact.html', form=form)

@app.route('/simple-form', methods=['GET', 'POST'])
def simple_form():
    if request.method == 'POST':
        # 通常のフォーム処理（WTFormsを使わない場合）
        name = request.form.get('name')
        age = request.form.get('age')
        hobbies = request.form.getlist('hobbies')  # 複数選択の値を取得
        
        return render_template('forms/result.html', 
                             name=name, age=age, hobbies=hobbies)
    
    return render_template('forms/simple.html')

# ファイルアップロードの例
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルが選択されていません', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('ファイルが選択されていません', 'error')
            return redirect(request.url)
        
        if file:
            # ファイルの保存処理（実際は安全な方法で保存）
            filename = file.filename
            flash(f'ファイル {filename} がアップロードされました', 'success')
            return redirect(url_for('index'))
    
    return render_template('forms/upload.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### フォームテンプレートの例

#### templates/forms/register.html

```html
{% extends "base.html" %}

{% block title %}ユーザー登録 - Flask チュートリアル{% endblock %}

{% block content %}
<h1>ユーザー登録</h1>

<form method="POST" action="{{ url_for('register') }}" novalidate>
    {{ form.hidden_tag() }}
    
    <div class="form-group">
        {{ form.username.label }}
        {{ form.username(class="form-control") }}
        {% if form.username.errors %}
            <div class="error">
                {% for error in form.username.errors %}
                    <span>{{ error }}</span>
                {% endfor %}
            </div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.email.label }}
        {{ form.email(class="form-control") }}
        {% if form.email.errors %}
            <div class="error">
                {% for error in form.email.errors %}
                    <span>{{ error }}</span>
                {% endfor %}
            </div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.password.label }}
        {{ form.password(class="form-control") }}
        {% if form.password.errors %}
            <div class="error">
                {% for error in form.password.errors %}
                    <span>{{ error }}</span>
                {% endfor %}
            </div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.confirm_password.label }}
        {{ form.confirm_password(class="form-control") }}
        {% if form.confirm_password.errors %}
            <div class="error">
                {% for error in form.confirm_password.errors %}
                    <span>{{ error }}</span>
                {% endfor %}
            </div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.terms() }}
        {{ form.terms.label }}
        {% if form.terms.errors %}
            <div class="error">
                {% for error in form.terms.errors %}
                    <span>{{ error }}</span>
                {% endfor %}
            </div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.submit(class="btn btn-primary") }}
    </div>
</form>
{% endblock %}
```

### WTFormsの利点

1. **自動的な検証**: バリデーターによる入力値の自動検証
2. **CSRF保護**: Flask-WTFによる自動的なCSRF保護
3. **エラー処理**: エラーメッセージの統一的な管理
4. **再利用性**: フォームクラスの再利用が容易

## データベース連携

### database_example.py - SQLAlchemyを使用したデータベース操作

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# データベース設定
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "blog.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# データベースの初期化
db = SQLAlchemy(app)

# モデルの定義
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<Post {self.title}>'

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Tag {self.name}>'

# 多対多の関係のための中間テーブル
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

# データベースの作成
with app.app_context():
    db.create_all()

# ルート定義
@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('db/index.html', posts=posts)

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('db/users.html', users=all_users)

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('db/user_detail.html', user=user)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        # ユーザーの重複チェック
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        
        if existing_user:
            flash('ユーザー名またはメールアドレスが既に使用されています', 'error')
        else:
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('ユーザーが正常に追加されました', 'success')
            return redirect(url_for('users'))
    
    return render_template('db/add_user.html')

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = request.form['user_id']
        
        new_post = Post(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        
        flash('投稿が正常に追加されました', 'success')
        return redirect(url_for('index'))
    
    users = User.query.all()
    return render_template('db/add_post.html', users=users)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('db/post_detail.html', post=post)

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        
        flash('投稿が更新されました', 'success')
        return redirect(url_for('post_detail', post_id=post.id))
    
    return render_template('db/edit_post.html', post=post)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    
    flash('投稿が削除されました', 'info')
    return redirect(url_for('index'))

# カスタムフィルター
@app.template_filter('datetime')
def datetime_filter(datetime_obj):
    return datetime_obj.strftime('%Y年%m月%d日 %H:%M')

# サンプルデータの投入
@app.route('/init_db')
def init_db():
    # 既存のデータをクリア
    db.drop_all()
    db.create_all()
    
    # サンプルユーザーの作成
    users = [
        User(username='tanaka', email='tanaka@example.com'),
        User(username='yamada', email='yamada@example.com'),
        User(username='suzuki', email='suzuki@example.com')
    ]
    
    for user in users:
        db.session.add(user)
    
    db.session.commit()
    
    # サンプル投稿の作成
    posts = [
        Post(title='Flaskを始めました', 
             content='今日からFlaskの勉強を始めました。とても楽しいです！', 
             user_id=1),
        Post(title='データベース連携', 
             content='SQLAlchemyを使ってデータベースと連携する方法を学びました。', 
             user_id=1),
        Post(title='初めての投稿', 
             content='はじめまして。よろしくお願いします。', 
             user_id=2)
    ]
    
    for post in posts:
        db.session.add(post)
    
    db.session.commit()
    
    flash('サンプルデータが投入されました', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

### SQLAlchemyの主要概念

1. **モデル定義**: `db.Model`を継承してテーブルを定義
2. **カラム型**: Integer、String、Text、DateTime、Boolean など
3. **リレーションシップ**: 一対多、多対多の関係を定義
4. **クエリ**: `Model.query`を使用したデータベース操作
5. **セッション管理**: `db.session`でトランザクション管理

### CRUD操作の例

```python
# Create（作成）
new_user = User(username='new_user', email='new@example.com')
db.session.add(new_user)
db.session.commit()

# Read（読み取り）
all_users = User.query.all()
user = User.query.get(1)  # IDで取得
user = User.query.filter_by(username='tanaka').first()

# Update（更新）
user = User.query.get(1)
user.email = 'newemail@example.com'
db.session.commit()

# Delete（削除）
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

## スタイルシート

### static/css/style.css

```css
/* 基本スタイル */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
    color: #333;
}

/* ナビゲーション */
nav {
    background-color: #333;
    padding: 1rem 0;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
}

nav li {
    margin: 0 1rem;
}

nav a {
    color: white;
    text-decoration: none;
    transition: color 0.3s;
}

nav a:hover {
    color: #ddd;
}

/* メインコンテンツ */
main {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    min-height: 500px;
    padding: 2rem;
}

/* 見出し */
h1, h2, h3 {
    color: #333;
    margin-top: 0;
}

h1 {
    border-bottom: 2px solid #333;
    padding-bottom: 0.5rem;
}

/* フォーム */
.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

.form-group input[type="checkbox"] {
    width: auto;
    margin-right: 0.5rem;
}

/* ボタン */
.btn, button {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #333;
    color: white;
    text-decoration: none;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-right: 0.5rem;
}

.btn:hover, button:hover {
    background-color: #555;
}

.btn-primary {
    background-color: #007bff;
}

.btn-primary:hover {
    background-color: #0056b3;
}

.btn-secondary {
    background-color: #6c757d;
}

.btn-secondary:hover {
    background-color: #5a6268;
}

.btn-danger {
    background-color: #dc3545;
}

.btn-danger:hover {
    background-color: #c82333;
}

/* アラート */
.alert {
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 4px;
}

.alert-success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.alert-error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.alert-info {
    background-color: #d1ecf1;
    color: #0c5460;
    border: 1px solid #bee5eb;
}

/* エラーメッセージ */
.error {
    color: #dc3545;
    font-size: 0.875rem;
    margin-top: 0.25rem;
}

/* 投稿 */
.post {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
}

.post h2 {
    margin-bottom: 0.5rem;
}

.post-meta {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.post-content {
    margin: 1.5rem 0;
    line-height: 1.8;
}

/* テーブル */
.users-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

.users-table th,
.users-table td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

.users-table th {
    background-color: #f8f9fa;
    font-weight: bold;
}

/* アクション */
.actions {
    margin: 1rem 0;
}

.form-actions {
    margin-top: 1.5rem;
}

/* フッター */
footer {
    text-align: center;
    padding: 2rem 0;
    color: #666;
    background-color: #f8f9fa;
}

/* インフォボックス */
.info-box {
    background-color: #e9ecef;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
}

/* レスポンシブ */
@media (max-width: 768px) {
    main {
        margin: 1rem;
        padding: 1rem;
    }
    
    nav ul {
        flex-direction: column;
        align-items: center;
    }
    
    nav li {
        margin: 0.5rem 0;
    }
}
```

## 実践的な演習

### 演習1: 基本的なWebアプリケーション

1. `app.py`を実行して、基本的なルーティングを確認
2. 新しいルートを追加して、自己紹介ページを作成
3. 動的ルーティングを使用して、複数の製品情報を表示

### 演習2: テンプレートの活用

1. `template_example.py`を実行
2. 新しいテンプレートを作成して、商品一覧ページを作成
3. テンプレートの継承を使用して、統一的なデザインを適用

### 演習3: フォームの実装

1. `forms_example.py`を実行
2. アンケートフォームを新規作成
3. フォームバリデーションを追加

### 演習4: データベース操作

1. `database_example.py`を実行
2. `/init_db`にアクセスしてサンプルデータを投入
3. 新しいモデル（カテゴリーなど）を追加
4. CRUD操作を実装

## トラブルシューティング

### よくある問題と解決方法

1. **ImportError: No module named 'flask'**
   ```bash
   pip install flask
   ```

2. **TemplateNotFound エラー**
   - templatesディレクトリが正しい場所にあるか確認
   - ファイル名のスペルミスをチェック

3. **データベースエラー**
   ```python
   with app.app_context():
       db.create_all()
   ```

4. **CSRF token missing**
   - フォームに `{{ form.hidden_tag() }}` を追加
   - SECRET_KEYが設定されているか確認

## セキュリティのベストプラクティス

1. **SECRET_KEYの管理**
   ```python
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
   ```

2. **SQLインジェクション対策**
   - SQLAlchemyのORMを使用
   - 生のSQLクエリは避ける

3. **XSS対策**
   - Jinja2の自動エスケープ機能を活用
   - `{{ variable|safe }}` は信頼できるデータのみに使用

4. **CSRF対策**
   - Flask-WTFのCSRF保護を有効化

## デプロイメント

### 本番環境への準備

1. **設定の分離**
   ```python
   class Config:
       SECRET_KEY = os.environ.get('SECRET_KEY')
       SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
   
   class DevelopmentConfig(Config):
       DEBUG = True
   
   class ProductionConfig(Config):
       DEBUG = False
   ```

2. **WSGIサーバーの使用**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **環境変数の設定**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   ```

## まとめ

このチュートリアルでは、Flaskの基本的な機能から実践的な使い方まで学習しました：

1. **基本的なアプリケーション構造**: ルーティング、ビュー関数
2. **テンプレートエンジン**: Jinja2による動的なHTML生成
3. **フォーム処理**: WTFormsによる安全なフォーム処理
4. **データベース連携**: SQLAlchemyによるORM
5. **静的ファイルの管理**: CSS、JavaScript、画像ファイル

### 次のステップ

1. **認証機能の追加**: Flask-Loginを使用したユーザー認証
2. **RESTful API**: Flask-RESTfulを使用したAPI開発
3. **非同期処理**: Celeryを使用したバックグラウンドタスク
4. **テスト**: pytestを使用した自動テスト
5. **デプロイ**: Heroku、AWS、Google Cloud Platformへのデプロイ

### 参考資料

- [Flask公式ドキュメント](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [WTForms Documentation](https://wtforms.readthedocs.io/)

このチュートリアルを通じて、Flaskを使用した Web アプリケーション開発の基礎を習得できました。実際のプロジェクトでは、これらの知識を組み合わせて、より複雑で実用的なアプリケーションを構築することができます。