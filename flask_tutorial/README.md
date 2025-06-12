# Flask チュートリアル

このチュートリアルでは、Python Flaskの基本的な機能を学習できます。

## セットアップ

### 1. 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 仮想環境の有効化（macOS/Linux）
source venv/bin/activate
```

### 2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

## チュートリアルの内容

### 1. 基本的なFlaskアプリケーション（app.py）

最もシンプルなFlaskアプリケーションの例です。

```bash
python app.py
```

ブラウザで http://localhost:5000 にアクセスしてください。

### 2. ルーティングの例（routes_example.py）

様々なルーティングパターンを学習できます：
- 基本的なルート
- HTTPメソッドの指定
- 動的ルーティング
- JSONレスポンス
- リダイレクト
- エラーハンドリング

```bash
python routes_example.py
```

### 3. テンプレートの使用（template_example.py）

Jinja2テンプレートエンジンの使い方を学習できます：
- テンプレートの継承
- 変数の表示
- 条件分岐とループ
- フィルターの使用
- フラッシュメッセージ

```bash
python template_example.py
```

### 4. フォーム処理（forms_example.py）

WTFormsを使用したフォーム処理を学習できます：
- フォームの作成と検証
- フラッシュメッセージ
- ファイルアップロード

```bash
python forms_example.py
```

### 5. データベース連携（database_example.py）

SQLAlchemyを使用したデータベース操作を学習できます：
- モデルの定義
- CRUD操作
- リレーションシップ

```bash
python database_example.py
```

初回起動時は http://localhost:5000/init_db にアクセスしてサンプルデータを投入してください。

## ディレクトリ構造

```
flask_tutorial/
├── app.py                  # 基本的なFlaskアプリケーション
├── routes_example.py       # ルーティングの例
├── template_example.py     # テンプレートの例
├── forms_example.py        # フォーム処理の例
├── database_example.py     # データベース連携の例
├── requirements.txt        # 依存パッケージ
├── README.md              # このファイル
├── templates/             # HTMLテンプレート
│   ├── base.html
│   ├── index.html
│   ├── forms/
│   └── db/
├── static/                # 静的ファイル
│   ├── css/
│   └── js/
└── instance/             # インスタンス固有の設定やデータベース
```

## 学習のポイント

1. **基礎から始める**: まずは`app.py`から始めて、Flaskの基本的な仕組みを理解しましょう。

2. **段階的に学習**: 各ファイルは独立して実行できるので、一つずつ試してみてください。

3. **コードを読む**: 各ファイルにはコメントが含まれているので、コードの意味を理解しながら進めてください。

4. **実験する**: コードを変更して、どのように動作が変わるか試してみましょう。

## 参考リンク

- [Flask公式ドキュメント](https://flask.palletsprojects.com/)
- [Jinja2テンプレート](https://jinja.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [WTForms](https://wtforms.readthedocs.io/)