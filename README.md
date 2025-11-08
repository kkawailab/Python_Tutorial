# Python Tutorial Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

Pythonプログラミングの基礎から、データサイエンス、Web開発まで網羅する包括的な日本語チュートリアル集です。実践的なコード例と詳細な解説を通じて、Pythonのスキルを段階的に習得できます。

## 📚 チュートリアル一覧

### 1. Python初級チュートリアル
**ファイル**: [Python_Beginner_Tutorial_Complete.md](./Python_Beginner_Tutorial_Complete.md)

プログラミング初心者を対象とした、Pythonの基礎を学ぶための完全ガイドです。

**学習内容**:
- Hello World - 最初のプログラム
- 変数とデータ型（整数、浮動小数点、文字列、ブール値）
- 文字列操作とフォーマット
- リスト、タプル、辞書、セット
- 制御フロー（if文、for/whileループ）
- 関数の定義と使用
- モジュールとパッケージ
- クラスとオブジェクト指向プログラミング
- ファイル操作
- エラー処理と例外

**対象者**: プログラミング初心者、Python入門者

---

### 2. NumPy完全チュートリアル
**ファイル**: [NumPy_Tutorial_Complete.md](./NumPy_Tutorial_Complete.md)

科学計算とデータ処理の基盤となるNumPyライブラリを徹底的に学びます。

**学習内容**:
- NumPy配列（ndarray）の基礎
- 配列の作成と初期化（zeros, ones, arange, linspace等）
- 配列の操作とインデックス、スライシング
- 配列の演算（要素ごとの演算、行列演算）
- 配列の形状変換（reshape, transpose, flatten）
- 統計関数と集約（mean, sum, std等）
- ブロードキャスティング
- 線形代数（行列演算、固有値、逆行列）
- ファイル入出力
- 実践的な応用例（画像処理、データ前処理）

**対象者**: データサイエンス入門者、科学計算に興味がある方

---

### 3. Pandas完全チュートリアル
**ファイル**: [Pandas_Tutorial_Complete.md](./Pandas_Tutorial_Complete.md)

データ分析の最強ツールPandasを使いこなすための包括的なガイドです。

**学習内容**:
- Pandasのデータ構造（Series, DataFrame）
- データの読み込みと書き出し（CSV, Excel, JSON, SQL）
- データの選択とフィルタリング（loc, iloc, query）
- データの操作と変換（apply, map, replace）
- 欠損値の処理（fillna, dropna, interpolate）
- データの結合とマージ（merge, join, concat）
- グループ化と集計（groupby, pivot_table）
- 時系列データの処理
- データの可視化
- 高度なデータ操作（MultiIndex, カテゴリカルデータ）
- パフォーマンス最適化

**対象者**: データアナリスト、データサイエンティスト、ビジネスアナリスト

---

### 4. Matplotlib完全チュートリアル
**ファイル**: [Matplotlib_Tutorial_Complete.md](./Matplotlib_Tutorial_Complete.md)

Pythonで最も広く使われているグラフ描画ライブラリMatplotlibの完全ガイドです。

**学習内容**:
- 基本的なプロット（折れ線、散布図、棒グラフ）
- プロットのカスタマイズ（色、スタイル、マーカー、ラベル）
- 複数のグラフとサブプロット
- 様々なプロットタイプ（ヒストグラム、箱ひげ図、パイチャート、等高線図）
- 3Dプロット
- アニメーション
- スタイルとテーマ
- 画像の保存とエクスポート
- 実践的な応用例（データ可視化、科学プロット）
- パフォーマンスとベストプラクティス

**対象者**: データ可視化を学びたい方、レポート作成者

---

### 5. Seaborn完全チュートリアル
**ファイル**: [Seaborn_Tutorial_Complete.md](./Seaborn_Tutorial_Complete.md)

統計的データ可視化に特化した、美しく洗練されたグラフを簡単に作成できるSeabornライブラリのガイドです。

**学習内容**:
- 基本的なプロット（散布図、折れ線グラフ）
- カテゴリカルプロット（バーチャート、ボックスプロット、バイオリンプロット）
- 分布の可視化（ヒストグラム、KDE、ディストリビューションプロット）
- 回帰プロット
- ヒートマップと相関行列
- ペアプロットとファセットグリッド
- スタイルとカラーパレット
- 時系列データの可視化
- 高度な統計プロット
- 実践的な応用例とベストプラクティス

**対象者**: 統計分析やデータ探索を行う方、データサイエンティスト

---

### 6. Flask完全チュートリアル
**ファイル**: [Flask_Tutorial_Complete.md](./Flask_Tutorial_Complete.md)

軽量でシンプルなWebアプリケーションフレームワークFlaskを使ったWeb開発の完全ガイドです。

**学習内容**:
- Flaskの基本とアプリケーション構造
- 環境構築と仮想環境の設定
- ルーティングとHTTPメソッド
- テンプレートエンジン（Jinja2）
- フォーム処理とバリデーション
- データベース連携（SQLite, SQLAlchemy）
- RESTful APIの構築
- セッション管理とクッキー
- ユーザー認証
- デプロイメント

**対象者**: Web開発初心者、API開発者、Webアプリケーション開発者

---

## 🚀 使い方

### 必要な環境
- Python 3.7以上
- pip（Pythonパッケージマネージャー）
- テキストエディタまたはIDE（VSCode、PyCharm、Jupyter Notebook等を推奨）

### インストール

各チュートリアルで使用するライブラリのインストール:

```bash
# NumPyのインストール
pip install numpy

# Pandasのインストール
pip install pandas

# Matplotlibのインストール
pip install matplotlib

# Seabornのインストール
pip install seaborn

# Flaskのインストール
pip install flask

# すべてをまとめてインストール
pip install numpy pandas matplotlib seaborn flask
```

### 学習の進め方

1. **初心者の方**: まず[Python初級チュートリアル](./Python_Beginner_Tutorial_Complete.md)から始めて、Pythonの基礎を固めましょう。

2. **データサイエンスに興味がある方**:
   - [NumPy](./NumPy_Tutorial_Complete.md) → [Pandas](./Pandas_Tutorial_Complete.md) → [Matplotlib](./Matplotlib_Tutorial_Complete.md) → [Seaborn](./Seaborn_Tutorial_Complete.md)の順で学習することをお勧めします。

3. **Web開発に興味がある方**:
   - Python基礎を学んだ後、[Flask](./Flask_Tutorial_Complete.md)に進みましょう。

4. **実践的な学習**:
   - 各チュートリアルには実行可能なコード例が豊富に含まれています。
   - コードをコピーして実際に実行し、結果を確認しながら学習を進めてください。
   - コードを改変して実験することで、理解が深まります。

---

## 📖 各チュートリアルの特徴

### 実践的なコード例
すべてのチュートリアルには、すぐに実行できるコード例が含まれています。コピー＆ペーストで動作するため、学習がスムーズです。

### 詳細な解説
各概念について、初心者にも分かりやすい詳細な解説を提供しています。

### 段階的な学習
基礎から応用まで、段階的に難易度が上がる構成になっています。

### 日本語での丁寧な説明
すべてのチュートリアルが日本語で書かれており、日本人学習者に最適化されています。

---

## 🎯 学習ロードマップ

```
Python初心者
    ↓
Python初級チュートリアル
    ↓
    ├─→ データサイエンスコース
    │       ↓
    │   NumPy → Pandas → Matplotlib → Seaborn
    │
    └─→ Web開発コース
            ↓
        Flask → (応用)
```

---

## 🤝 貢献

このリポジトリへの貢献を歓迎します！バグ報告、機能提案、プルリクエストなど、お気軽にどうぞ。

---

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](./LICENSE)ファイルをご覧ください。

---

## 🔗 関連リンク

- [公式Webサイト](http://kklab.mobi/Python_Tutorial/)
- [Python公式ドキュメント](https://docs.python.org/ja/3/)
- [NumPy公式ドキュメント](https://numpy.org/doc/)
- [Pandas公式ドキュメント](https://pandas.pydata.org/docs/)
- [Matplotlib公式ドキュメント](https://matplotlib.org/)
- [Seaborn公式ドキュメント](https://seaborn.pydata.org/)
- [Flask公式ドキュメント](https://flask.palletsprojects.com/)

---

## 📧 お問い合わせ

質問や提案がある場合は、GitHubのIssuesページからお気軽にご連絡ください。

---

**Happy Learning! 🎉**
