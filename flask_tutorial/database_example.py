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