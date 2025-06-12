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