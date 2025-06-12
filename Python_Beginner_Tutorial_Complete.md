# Python初級チュートリアル完全版

## 目次
1. [はじめに](#はじめに)
2. [Hello World - 最初のプログラム](#hello-world)
3. [変数とデータ型](#変数とデータ型)
4. [文字列操作](#文字列操作)
5. [リストとタプル](#リストとタプル)
6. [辞書とセット](#辞書とセット)
7. [制御フロー](#制御フロー)
8. [関数](#関数)
9. [モジュールとパッケージ](#モジュールとパッケージ)
10. [クラスとオブジェクト指向](#クラスとオブジェクト指向)
11. [ファイル操作](#ファイル操作)
12. [エラー処理](#エラー処理)

## はじめに

このチュートリアルは、Pythonプログラミングの基礎を学ぶための包括的なガイドです。プログラミング初心者でも理解できるよう、基本概念から実践的な例まで段階的に説明します。

### 必要な環境
- Python 3.7以上
- テキストエディタまたはIDE（VSCode、PyCharmなど推奨）

### チュートリアルの使い方
各セクションには実行可能なコード例が含まれています。コードをコピーして実行し、結果を確認しながら学習を進めてください。

---

## 1. Hello World - 最初のプログラム {#hello-world}

### 基本的な出力

```python
# 01_hello_world.py - Hello World と基本的な出力

# ===== 最も基本的なプログラム =====
print("Hello, World!")

# ===== 日本語での出力 =====
print("こんにちは、Python！")

# ===== 複数行の出力 =====
print("Pythonプログラミングへようこそ！")
print("これから一緒に学んでいきましょう。")
print("楽しいプログラミングの世界が待っています！")

# ===== print関数の様々な使い方 =====
print()  # 空行を出力

# 複数の値を出力
print("名前:", "田中太郎")
print("年齢:", 25, "歳")

# セパレータ（区切り文字）の指定
print("りんご", "バナナ", "オレンジ", sep=" | ")
print("2024", "12", "25", sep="-")

# 改行なしで出力（endパラメータ）
print("処理中", end="")
print("...", end="")
print("完了！")

# ===== エスケープシーケンス =====
print("\n特殊文字の使い方:")
print("改行: line1\nline2")
print("タブ: column1\tcolumn2\tcolumn3")
print("引用符: \"ダブルクォート\" と \'シングルクォート\'")
print("バックスラッシュ: C:\\Users\\name\\Documents")

# ===== 文字列のフォーマット =====
name = "Python"
version = 3.9
print(f"\n{name} バージョン {version} を使用しています")

# ===== コメントの重要性 =====
# これは単一行コメントです
# プログラムの説明や注意事項を書きます

"""
これは複数行コメント（ドキュメント文字列）です。
関数やクラスの説明に使用したり、
長い説明が必要な場合に使います。
"""

# プログラムの終了メッセージ
print("\n最初のPythonプログラムが完了しました！🎉")
```

### 実行方法
```bash
python 01_hello_world.py
```

### 学習ポイント
- `print()`関数は画面に文字を表示する最も基本的な関数
- 日本語も問題なく表示可能
- `sep`パラメータで区切り文字を指定
- `end`パラメータで行末文字を指定
- エスケープシーケンスで特殊文字を表現

---

## 2. 変数とデータ型 {#変数とデータ型}

### 基本的なデータ型

```python
# 02_variables_and_types.py - 変数とデータ型

# ===== 変数の基本 =====
print("=== 変数の基本 ===")

# 変数の代入
message = "Hello, Python!"
number = 42
pi = 3.14159
is_active = True

print(f"メッセージ: {message}")
print(f"数値: {number}")
print(f"円周率: {pi}")
print(f"アクティブ状態: {is_active}")

# 変数の再代入
number = 100
print(f"\n更新後の数値: {number}")

# ===== データ型 =====
print("\n=== データ型 ===")

# 整数（int）
age = 25
year = 2024
temperature = -5

print(f"整数の例: {age}, {year}, {temperature}")

# 浮動小数点数（float）
height = 170.5
weight = 65.3
percentage = 0.85

print(f"小数の例: {height}, {weight}, {percentage}")

# 文字列（str）
name = "田中太郎"
city = '東京'  # シングルクォートも使用可能
multiline = """これは
複数行の
文字列です"""

print(f"文字列の例: {name}, {city}")
print(f"複数行文字列:\n{multiline}")

# ブール値（bool）
is_student = True
is_married = False

print(f"ブール値の例: {is_student}, {is_married}")

# None（値がないことを表す）
result = None
print(f"None値: {result}")

# ===== 型の確認 =====
print("\n=== 型の確認 ===")

print(f"'Hello'の型: {type('Hello')}")
print(f"42の型: {type(42)}")
print(f"3.14の型: {type(3.14)}")
print(f"Trueの型: {type(True)}")
print(f"Noneの型: {type(None)}")

# ===== 型変換 =====
print("\n=== 型変換 ===")

# 文字列を数値に変換
str_number = "123"
int_number = int(str_number)
print(f"文字列'{str_number}'を整数に変換: {int_number}")

# 数値を文字列に変換
num = 456
str_num = str(num)
print(f"数値{num}を文字列に変換: '{str_num}'")

# 小数と整数の相互変換
float_num = 3.7
int_from_float = int(float_num)  # 小数点以下切り捨て
print(f"小数{float_num}を整数に変換: {int_from_float}")

int_val = 5
float_from_int = float(int_val)
print(f"整数{int_val}を小数に変換: {float_from_int}")

# ===== 変数名のルール =====
print("\n=== 変数名のルール ===")

# 良い変数名の例
user_name = "山田"
age_in_years = 30
is_valid_email = True
MAX_SIZE = 100  # 定数は大文字

print("良い変数名の例:")
print(f"  user_name: {user_name}")
print(f"  age_in_years: {age_in_years}")
print(f"  is_valid_email: {is_valid_email}")
print(f"  MAX_SIZE: {MAX_SIZE}")

# 使用できない変数名の例（コメントで説明）
# 1age = 25  # 数字で始まる変数名はエラー
# my-name = "太郎"  # ハイフンは使用不可
# class = "A"  # 予約語は使用不可

# ===== 動的型付け =====
print("\n=== 動的型付け ===")

# Pythonは動的型付け言語
variable = 100
print(f"初期値: {variable}, 型: {type(variable)}")

variable = "文字列に変更"
print(f"変更後: {variable}, 型: {type(variable)}")

variable = [1, 2, 3]
print(f"再変更: {variable}, 型: {type(variable)}")

# ===== 算術演算 =====
print("\n=== 算術演算 ===")

a = 10
b = 3

print(f"加算: {a} + {b} = {a + b}")
print(f"減算: {a} - {b} = {a - b}")
print(f"乗算: {a} * {b} = {a * b}")
print(f"除算: {a} / {b} = {a / b}")
print(f"整数除算: {a} // {b} = {a // b}")
print(f"剰余: {a} % {b} = {a % b}")
print(f"べき乗: {a} ** {b} = {a ** b}")

# ===== 複合代入演算子 =====
print("\n=== 複合代入演算子 ===")

count = 0
print(f"初期値: {count}")

count += 5
print(f"+=5 後: {count}")

count -= 2
print(f"-=2 後: {count}")

count *= 3
print(f"*=3 後: {count}")

count //= 2
print(f"//=2 後: {count}")
```

### 学習ポイント
- Pythonの基本的なデータ型：int、float、str、bool、None
- 変数は型宣言不要（動的型付け）
- `type()`関数で型を確認
- 型変換関数：`int()`、`float()`、`str()`など
- 変数名は英数字とアンダースコアのみ使用可能

---

## 3. 文字列操作 {#文字列操作}

### 文字列の基本操作

```python
# 03_strings.py - 文字列の操作

# ===== 文字列の作成 =====
print("=== 文字列の作成 ===")

# さまざまな引用符の使い方
single = 'シングルクォート'
double = "ダブルクォート"
triple_single = '''複数行の
文字列を
書けます'''
triple_double = """こちらも
複数行の文字列
です"""

print(single)
print(double)
print(triple_single)
print(triple_double)

# ===== 文字列の連結 =====
print("\n=== 文字列の連結 ===")

first_name = "太郎"
last_name = "田中"

# + 演算子で連結
full_name = last_name + " " + first_name
print(f"フルネーム: {full_name}")

# 複数の文字列を連結
greeting = "こんにちは、" + full_name + "さん！"
print(greeting)

# ===== 文字列の繰り返し =====
print("\n=== 文字列の繰り返し ===")

star = "★"
line = "-"

print(star * 5)
print(line * 20)

# ===== 文字列のインデックスとスライス =====
print("\n=== インデックスとスライス ===")

text = "Python Programming"

# インデックス（0から始まる）
print(f"最初の文字: {text[0]}")
print(f"最後の文字: {text[-1]}")
print(f"3番目の文字: {text[2]}")

# スライス [開始:終了:ステップ]
print(f"\n最初の6文字: {text[0:6]}")
print(f"7文字目以降: {text[7:]}")
print(f"最後の11文字: {text[-11:]}")
print(f"1文字おき: {text[::2]}")
print(f"逆順: {text[::-1]}")

# ===== 文字列のメソッド =====
print("\n=== 文字列のメソッド ===")

sample = "  Hello, Python World!  "

# 大文字・小文字変換
print(f"大文字: {sample.upper()}")
print(f"小文字: {sample.lower()}")
print(f"タイトルケース: {sample.title()}")

# 空白の除去
print(f"前後の空白除去: '{sample.strip()}'")
print(f"左側の空白除去: '{sample.lstrip()}'")
print(f"右側の空白除去: '{sample.rstrip()}'")

# 文字列の置換
replaced = sample.replace("Python", "プログラミング")
print(f"置換後: {replaced}")

# 文字列の分割
words = sample.strip().split()
print(f"単語に分割: {words}")

csv_data = "りんご,バナナ,オレンジ"
fruits = csv_data.split(",")
print(f"カンマで分割: {fruits}")

# 文字列の結合
joined = " - ".join(fruits)
print(f"結合: {joined}")

# ===== 文字列の検索 =====
print("\n=== 文字列の検索 ===")

text = "Python is easy. Python is powerful."

# 含まれているかチェック
print(f"'Python'が含まれている: {'Python' in text}")
print(f"'Java'が含まれている: {'Java' in text}")

# 位置を検索
print(f"'Python'の最初の位置: {text.find('Python')}")
print(f"'Python'の最後の位置: {text.rfind('Python')}")
print(f"'Python'の出現回数: {text.count('Python')}")

# 開始・終了のチェック
print(f"'Python'で始まる: {text.startswith('Python')}")
print(f"'powerful.'で終わる: {text.endswith('powerful.')}")

# ===== 文字列のフォーマット =====
print("\n=== 文字列のフォーマット ===")

name = "山田"
age = 25
height = 170.5

# f-string（推奨）
print(f"{name}さんは{age}歳で、身長は{height}cmです。")

# format()メソッド
print("{}さんは{}歳で、身長は{}cmです。".format(name, age, height))

# % 演算子（古い方法）
print("%sさんは%d歳で、身長は%.1fcmです。" % (name, age, height))

# 数値のフォーマット
price = 1234.567
print(f"\n価格のフォーマット:")
print(f"  通常: {price}")
print(f"  小数点2桁: {price:.2f}")
print(f"  カンマ区切り: {price:,.2f}")
print(f"  パーセント: {0.85:.1%}")

# ===== エスケープ文字 =====
print("\n=== エスケープ文字 ===")

print("改行を含む文字列:\nこれは新しい行です")
print("タブを含む文字列:\t列1\t列2\t列3")
print("引用符: \"ダブル\" と \'シングル\'")
print("バックスラッシュ: C:\\Users\\Documents")

# raw文字列（エスケープを無効化）
path = r"C:\Users\Documents\file.txt"
print(f"raw文字列: {path}")

# ===== 文字列の判定 =====
print("\n=== 文字列の判定 ===")

# 数値判定
print("'123'.isdigit():", "123".isdigit())
print("'123.45'.isdigit():", "123.45".isdigit())

# アルファベット判定
print("'Hello'.isalpha():", "Hello".isalpha())
print("'Hello123'.isalpha():", "Hello123".isalpha())

# 英数字判定
print("'Hello123'.isalnum():", "Hello123".isalnum())
print("'Hello 123'.isalnum():", "Hello 123".isalnum())

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# メールアドレスの簡易バリデーション
email = "user@example.com"
is_valid = "@" in email and email.count("@") == 1 and "." in email.split("@")[1]
print(f"{email} は有効: {is_valid}")

# 文字列のクリーニング
user_input = "  HELLO world  \n"
cleaned = user_input.strip().lower()
print(f"クリーニング前: '{user_input}'")
print(f"クリーニング後: '{cleaned}'")

# パスワードの強度チェック
password = "Pass123!"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*" for c in password)
is_strong = all([has_upper, has_lower, has_digit, has_special, len(password) >= 8])
print(f"\nパスワード '{password}' の強度:")
print(f"  大文字: {has_upper}")
print(f"  小文字: {has_lower}")
print(f"  数字: {has_digit}")
print(f"  特殊文字: {has_special}")
print(f"  強度: {'強' if is_strong else '弱'}")
```

### 学習ポイント
- 文字列は不変（immutable）なデータ型
- インデックスとスライスで部分文字列を取得
- 豊富な文字列メソッドで様々な操作が可能
- f-stringが最も推奨される文字列フォーマット方法
- 文字列の検索、置換、分割、結合などの基本操作

---

## 4. リストとタプル {#リストとタプル}

### リストの操作

```python
# 04_lists_and_tuples.py - リストとタプル

# ===== リストの基本 =====
print("=== リストの基本 ===")

# リストの作成
fruits = ["りんご", "バナナ", "オレンジ"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True]
empty_list = []

print(f"フルーツ: {fruits}")
print(f"数値: {numbers}")
print(f"混合: {mixed}")
print(f"空のリスト: {empty_list}")

# リストの要素にアクセス
print(f"\n最初の要素: {fruits[0]}")
print(f"最後の要素: {fruits[-1]}")
print(f"2番目の要素: {fruits[1]}")

# ===== リストの変更 =====
print("\n=== リストの変更 ===")

# 要素の変更
fruits[1] = "ぶどう"
print(f"変更後: {fruits}")

# 要素の追加
fruits.append("メロン")
print(f"append後: {fruits}")

fruits.insert(1, "いちご")
print(f"insert後: {fruits}")

# 要素の削除
removed = fruits.pop()  # 最後の要素を削除
print(f"pop後: {fruits}, 削除された要素: {removed}")

fruits.remove("ぶどう")  # 特定の要素を削除
print(f"remove後: {fruits}")

# ===== リストのスライス =====
print("\n=== リストのスライス ===")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"元のリスト: {numbers}")
print(f"最初の3つ: {numbers[:3]}")
print(f"3番目から6番目: {numbers[2:6]}")
print(f"最後の3つ: {numbers[-3:]}")
print(f"1つおき: {numbers[::2]}")
print(f"逆順: {numbers[::-1]}")

# ===== リストの操作 =====
print("\n=== リストの操作 ===")

# リストの連結
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"連結: {combined}")

# リストの繰り返し
repeated = [0] * 5
print(f"繰り返し: {repeated}")

# リストの長さ
print(f"fruitsの長さ: {len(fruits)}")

# 要素の存在確認
print(f"'りんご'は含まれている: {'りんご' in fruits}")
print(f"'パイナップル'は含まれている: {'パイナップル' in fruits}")

# ===== リストのメソッド =====
print("\n=== リストのメソッド ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"元のリスト: {numbers}")

# ソート
numbers.sort()
print(f"昇順ソート後: {numbers}")

numbers.sort(reverse=True)
print(f"降順ソート後: {numbers}")

# その他のメソッド
print(f"最小値: {min(numbers)}")
print(f"最大値: {max(numbers)}")
print(f"合計: {sum(numbers)}")
print(f"1の出現回数: {numbers.count(1)}")
print(f"5のインデックス: {numbers.index(5)}")

# ===== リスト内包表記 =====
print("\n=== リスト内包表記 ===")

# 基本的なリスト内包表記
squares = [x**2 for x in range(10)]
print(f"0-9の二乗: {squares}")

# 条件付きリスト内包表記
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"偶数の二乗: {even_squares}")

# 文字列処理
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"大文字変換: {upper_words}")

# ===== タプルの基本 =====
print("\n=== タプルの基本 ===")

# タプルの作成
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)  # 要素が1つの場合はカンマが必要
empty_tuple = ()

print(f"座標: {coordinates}")
print(f"RGB: {rgb}")
print(f"単一要素: {single}")

# タプルの要素にアクセス
x, y = coordinates  # アンパック
print(f"x = {x}, y = {y}")

# タプルは不変（変更不可）
# coordinates[0] = 30  # これはエラーになる

# ===== リストとタプルの変換 =====
print("\n=== リストとタプルの変換 ===")

# リストからタプル
list_data = [1, 2, 3, 4, 5]
tuple_data = tuple(list_data)
print(f"リストをタプルに: {tuple_data}")

# タプルからリスト
tuple_data = (10, 20, 30)
list_data = list(tuple_data)
print(f"タプルをリストに: {list_data}")

# ===== ネストしたリスト =====
print("\n=== ネストしたリスト ===")

# 2次元リスト（行列）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("行列:")
for row in matrix:
    print(f"  {row}")

# 要素にアクセス
print(f"\n要素[1][2]: {matrix[1][2]}")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. 成績の集計
scores = [85, 92, 78, 95, 88, 76, 90]
average = sum(scores) / len(scores)
above_average = [score for score in scores if score > average]

print(f"成績: {scores}")
print(f"平均点: {average:.1f}")
print(f"平均以上の成績: {above_average}")

# 2. データのフィルタリング
products = [
    ("りんご", 100),
    ("バナナ", 80),
    ("オレンジ", 120),
    ("ぶどう", 300),
    ("メロン", 500)
]

cheap_products = [(name, price) for name, price in products if price < 150]
print(f"\n150円未満の商品: {cheap_products}")

# 3. リストの重複削除
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(f"\n重複削除前: {numbers}")
print(f"重複削除後: {unique_numbers}")

# 4. zip関数の使用
names = ["田中", "山田", "佐藤"]
ages = [25, 30, 28]
cities = ["東京", "大阪", "名古屋"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}さん（{age}歳）は{city}に住んでいます")
```

### 学習ポイント
- リストは可変（mutable）、タプルは不変（immutable）
- リストは`[]`、タプルは`()`で作成
- インデックスとスライスで要素にアクセス
- リスト内包表記で簡潔にリストを作成
- `zip()`関数で複数のリストを同時に処理

---

## 5. 辞書とセット {#辞書とセット}

### 辞書とセットの操作

```python
# 05_dictionaries_and_sets.py - 辞書とセット

# ===== 辞書の基本 =====
print("=== 辞書の基本 ===")

# 辞書の作成
person = {
    "name": "田中太郎",
    "age": 25,
    "city": "東京",
    "hobbies": ["読書", "映画鑑賞", "料理"]
}

# 別の作成方法
scores = dict(math=85, english=92, science=78)

# 空の辞書
empty_dict = {}

print(f"人物情報: {person}")
print(f"成績: {scores}")

# ===== 辞書の要素にアクセス =====
print("\n=== 辞書の要素にアクセス ===")

# キーでアクセス
print(f"名前: {person['name']}")
print(f"年齢: {person['age']}")

# get()メソッド（キーが存在しない場合のデフォルト値）
print(f"職業: {person.get('job', '未設定')}")
print(f"趣味: {person.get('hobbies')}")

# ===== 辞書の変更 =====
print("\n=== 辞書の変更 ===")

# 値の変更
person['age'] = 26
print(f"年齢を更新: {person['age']}")

# 新しいキーと値の追加
person['email'] = 'tanaka@example.com'
person['job'] = 'エンジニア'
print(f"更新後: {person}")

# 要素の削除
del person['email']
print(f"emailを削除後: {person}")

# pop()メソッド
removed_job = person.pop('job', 'デフォルト値')
print(f"削除された職業: {removed_job}")

# ===== 辞書のメソッド =====
print("\n=== 辞書のメソッド ===")

# すべてのキー、値、アイテム
print(f"キー: {list(person.keys())}")
print(f"値: {list(person.values())}")
print(f"アイテム: {list(person.items())}")

# 辞書の更新
update_data = {"age": 27, "phone": "090-1234-5678"}
person.update(update_data)
print(f"update後: {person}")

# ===== 辞書のループ処理 =====
print("\n=== 辞書のループ処理 ===")

# キーでループ
print("キーでループ:")
for key in person:
    print(f"  {key}: {person[key]}")

# キーと値でループ
print("\nキーと値でループ:")
for key, value in person.items():
    print(f"  {key} -> {value}")

# ===== ネストした辞書 =====
print("\n=== ネストした辞書 ===")

company = {
    "name": "テック株式会社",
    "employees": {
        "001": {"name": "田中", "department": "開発"},
        "002": {"name": "山田", "department": "営業"},
        "003": {"name": "佐藤", "department": "人事"}
    },
    "locations": ["東京", "大阪", "名古屋"]
}

print(f"会社名: {company['name']}")
print(f"従業員002: {company['employees']['002']}")
print(f"拠点: {company['locations']}")

# ===== セットの基本 =====
print("\n=== セットの基本 ===")

# セットの作成
fruits = {"りんご", "バナナ", "オレンジ"}
numbers = set([1, 2, 3, 3, 4, 4, 5])  # 重複は自動的に削除される
empty_set = set()  # 空のセット

print(f"フルーツ: {fruits}")
print(f"数値（重複削除）: {numbers}")

# ===== セットの操作 =====
print("\n=== セットの操作 ===")

# 要素の追加
fruits.add("ぶどう")
print(f"add後: {fruits}")

# 要素の削除
fruits.remove("バナナ")  # 要素がない場合はエラー
fruits.discard("メロン")  # 要素がなくてもエラーにならない
print(f"削除後: {fruits}")

# ===== セットの集合演算 =====
print("\n=== セットの集合演算 ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"セットA: {set_a}")
print(f"セットB: {set_b}")

# 和集合
union = set_a | set_b
print(f"和集合 (A ∪ B): {union}")

# 積集合
intersection = set_a & set_b
print(f"積集合 (A ∩ B): {intersection}")

# 差集合
difference = set_a - set_b
print(f"差集合 (A - B): {difference}")

# 対称差集合
symmetric_diff = set_a ^ set_b
print(f"対称差集合 (A △ B): {symmetric_diff}")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. 在庫管理システム
inventory = {
    "りんご": {"price": 100, "stock": 50},
    "バナナ": {"price": 80, "stock": 100},
    "オレンジ": {"price": 120, "stock": 30}
}

print("在庫一覧:")
for item, info in inventory.items():
    total_value = info["price"] * info["stock"]
    print(f"  {item}: 単価{info['price']}円, 在庫{info['stock']}個, 総額{total_value}円")

# 2. ユーザー管理
users = {
    "user001": {
        "name": "田中太郎",
        "email": "tanaka@example.com",
        "roles": {"admin", "user"}
    },
    "user002": {
        "name": "山田花子",
        "email": "yamada@example.com",
        "roles": {"user"}
    }
}

# 管理者権限を持つユーザーを検索
print("\n管理者ユーザー:")
for user_id, user_info in users.items():
    if "admin" in user_info["roles"]:
        print(f"  {user_id}: {user_info['name']}")

# 3. 単語の出現回数をカウント
text = "python is easy python is powerful python is versatile"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\n単語の出現回数: {word_count}")

# 4. 重複データの検出
data = ["apple", "banana", "apple", "orange", "banana", "grape"]
unique_data = list(set(data))
duplicates = []

for item in set(data):
    if data.count(item) > 1:
        duplicates.append(item)

print(f"\n元のデータ: {data}")
print(f"重複を除いたデータ: {unique_data}")
print(f"重複していた要素: {duplicates}")

# ===== 辞書内包表記 =====
print("\n=== 辞書内包表記 ===")

# 基本的な辞書内包表記
squares = {x: x**2 for x in range(5)}
print(f"数値と二乗: {squares}")

# 条件付き辞書内包表記
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"偶数の二乗: {even_squares}")

# リストから辞書を作成
names = ["田中", "山田", "佐藤"]
ages = [25, 30, 28]
name_age_dict = {name: age for name, age in zip(names, ages)}
print(f"名前と年齢: {name_age_dict}")
```

### 学習ポイント
- 辞書はキーと値のペアで構成される可変のデータ構造
- セットは重複を許さない要素の集合
- 辞書は`{}`または`dict()`、セットは`{}`または`set()`で作成
- 辞書の要素には`[]`または`get()`メソッドでアクセス
- セットは集合演算（和、積、差など）が可能

---

## 6. 制御フロー {#制御フロー}

### 条件分岐とループ

```python
# 06_control_flow.py - 制御フロー（条件分岐とループ）

# ===== if文 =====
print("=== if文 ===")

# 基本的なif文
age = 20
if age >= 18:
    print("成人です")

# if-else文
score = 75
if score >= 80:
    print("合格です")
else:
    print("不合格です")

# if-elif-else文
temperature = 28
if temperature < 0:
    print("とても寒い")
elif temperature < 10:
    print("寒い")
elif temperature < 20:
    print("涼しい")
elif temperature < 30:
    print("快適")
else:
    print("暑い")

# ===== 条件式の詳細 =====
print("\n=== 条件式の詳細 ===")

# 比較演算子
x = 10
y = 5
print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")

# 論理演算子
age = 25
has_license = True

if age >= 18 and has_license:
    print("\n運転できます")

rain = False
umbrella = True

if rain or umbrella:
    print("傘の準備OK")

if not rain:
    print("晴れています")

# ===== 三項演算子 =====
print("\n=== 三項演算子 ===")

age = 20
status = "成人" if age >= 18 else "未成年"
print(f"年齢{age}歳: {status}")

# ===== for文 =====
print("\n=== for文 ===")

# リストの要素をループ
fruits = ["りんご", "バナナ", "オレンジ"]
for fruit in fruits:
    print(f"フルーツ: {fruit}")

# range()を使ったループ
print("\n1から5まで:")
for i in range(1, 6):
    print(f"  {i}")

# インデックスと値を同時に取得
print("\nインデックス付き:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# 辞書のループ
person = {"name": "田中", "age": 25, "city": "東京"}
print("\n辞書のループ:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ===== while文 =====
print("\n=== while文 ===")

# 基本的なwhile文
count = 0
while count < 5:
    print(f"カウント: {count}")
    count += 1

# 条件を満たすまでループ
total = 0
num = 1
while total < 100:
    total += num
    num += 1
print(f"\n1から{num-1}までの合計が{total}で100を超えました")

# ===== break文とcontinue文 =====
print("\n=== break文とcontinue文 ===")

# break文（ループを抜ける）
print("break文の例:")
for i in range(10):
    if i == 5:
        print("  5で終了")
        break
    print(f"  {i}")

# continue文（次の繰り返しへ）
print("\ncontinue文の例（奇数をスキップ）:")
for i in range(10):
    if i % 2 == 1:
        continue
    print(f"  {i}")

# ===== else節付きループ =====
print("\n=== else節付きループ ===")

# for-else
print("素数判定:")
for num in [7, 8, 9]:
    for i in range(2, num):
        if num % i == 0:
            print(f"  {num}は素数ではありません")
            break
    else:
        print(f"  {num}は素数です")

# while-else
count = 0
while count < 3:
    print(f"カウント: {count}")
    count += 1
else:
    print("正常に終了しました")

# ===== ネストしたループ =====
print("\n=== ネストしたループ ===")

# 九九の表（一部）
print("九九の表（3x3）:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j:2d}", end="  ")
    print()  # 改行

# ===== リスト内包表記との組み合わせ =====
print("\n=== リスト内包表記との組み合わせ ===")

# 条件付きリスト内包表記
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"偶数: {evens}")

# ネストしたリスト内包表記
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"行列: {matrix}")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. パスワード検証
def validate_password(password):
    if len(password) < 8:
        return False, "パスワードは8文字以上必要です"
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if not has_upper:
        return False, "大文字を含める必要があります"
    if not has_lower:
        return False, "小文字を含める必要があります"
    if not has_digit:
        return False, "数字を含める必要があります"
    
    return True, "パスワードは有効です"

passwords = ["Pass123!", "password", "PASSWORD123", "Pass"]
for pwd in passwords:
    valid, message = validate_password(pwd)
    print(f"{pwd}: {message}")

# 2. メニューシステム
print("\n簡単なメニューシステム:")
menu_items = {
    "1": "ファイルを開く",
    "2": "ファイルを保存",
    "3": "設定",
    "4": "終了"
}

# シミュレーション（実際の入力の代わり）
user_choices = ["1", "2", "4"]
for choice in user_choices:
    if choice in menu_items:
        print(f"選択: {menu_items[choice]}")
        if choice == "4":
            print("プログラムを終了します")
            break
    else:
        print("無効な選択です")

# 3. 数当てゲーム（シンプル版）
import random

target = random.randint(1, 10)
max_attempts = 3
attempts = 0

print(f"\n数当てゲーム（1-10の数を{max_attempts}回以内に当ててください）")
# シミュレーション用の推測値
guesses = [5, 7, target]

for guess in guesses:
    attempts += 1
    print(f"推測{attempts}: {guess}")
    
    if guess == target:
        print(f"正解！ {attempts}回目で当たりました")
        break
    elif guess < target:
        print("もっと大きい数です")
    else:
        print("もっと小さい数です")
    
    if attempts >= max_attempts:
        print(f"残念！正解は{target}でした")
        break
```

### 学習ポイント
- `if-elif-else`で条件分岐を実装
- `for`文でシーケンスの要素を反復処理
- `while`文で条件が真の間ループを継続
- `break`でループを抜け、`continue`で次の反復へ
- ループにも`else`節を付けられる（正常終了時に実行）

---

## 7. 関数 {#関数}

### 関数の定義と使用

```python
# 07_functions.py - 関数

# ===== 関数の基本 =====
print("=== 関数の基本 ===")

# シンプルな関数
def greet():
    print("こんにちは！")

# 関数の呼び出し
greet()

# 引数を持つ関数
def greet_with_name(name):
    print(f"こんにちは、{name}さん！")

greet_with_name("田中")
greet_with_name("山田")

# 戻り値を持つ関数
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# ===== 引数の種類 =====
print("\n=== 引数の種類 ===")

# デフォルト引数
def introduce(name, age=20, city="東京"):
    print(f"{name}さん（{age}歳）は{city}に住んでいます。")

introduce("田中")  # デフォルト値を使用
introduce("山田", 25)  # ageを指定
introduce("佐藤", 30, "大阪")  # すべて指定

# キーワード引数
print("\nキーワード引数:")
introduce(name="鈴木", city="名古屋", age=28)  # 順序を変えて指定

# 可変長引数（*args）
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"\n合計: {sum_all(1, 2, 3)}")
print(f"合計: {sum_all(1, 2, 3, 4, 5)}")

# キーワード可変長引数（**kwargs）
def print_info(**info):
    print("\n情報:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="高橋", age=35, job="エンジニア", hobby="読書")

# ===== 関数の高度な使い方 =====
print("\n=== 関数の高度な使い方 ===")

# 複数の戻り値
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(nums)
print(f"リスト {nums} の最小値: {minimum}, 最大値: {maximum}")

# 関数内関数（ネストした関数）
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(f"\n5を加える関数: {add_five(3)} = 5 + 3")

# ===== ラムダ関数 =====
print("\n=== ラムダ関数 ===")

# 基本的なラムダ関数
square = lambda x: x ** 2
print(f"3の二乗: {square(3)}")

# リストのソートで使用
students = [
    {"name": "田中", "score": 85},
    {"name": "山田", "score": 92},
    {"name": "佐藤", "score": 78}
]

# scoreでソート
students.sort(key=lambda x: x["score"], reverse=True)
print("\n成績順:")
for student in students:
    print(f"  {student['name']}: {student['score']}点")

# map()関数との組み合わせ
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"\n元のリスト: {numbers}")
print(f"二乗: {squared}")

# filter()関数との組み合わせ
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数のみ: {even_numbers}")

# ===== デコレータ =====
print("\n=== デコレータ ===")

# シンプルなデコレータ
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello(name):
    return f"hello, {name}!"

print(say_hello("python"))  # HELLO, PYTHON!

# 実行時間を計測するデコレータ
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}の実行時間: {end - start:.6f}秒")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "完了"

result = slow_function()

# ===== ジェネレータ =====
print("\n=== ジェネレータ ===")

# シンプルなジェネレータ
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

print("1から5まで:")
for num in count_up_to(5):
    print(f"  {num}")

# フィボナッチ数列のジェネレータ
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nフィボナッチ数列（最初の10個）:")
fib_nums = list(fibonacci(10))
print(fib_nums)

# ===== 実用的な関数の例 =====
print("\n=== 実用的な関数の例 ===")

# 1. バリデーション関数
def validate_email(email):
    """簡易的なメールアドレスのバリデーション"""
    if "@" not in email:
        return False, "＠マークがありません"
    
    parts = email.split("@")
    if len(parts) != 2:
        return False, "＠マークが複数あります"
    
    username, domain = parts
    if not username:
        return False, "ユーザー名が空です"
    
    if "." not in domain:
        return False, "ドメインが不正です"
    
    return True, "有効なメールアドレスです"

emails = ["user@example.com", "invalid.email", "@example.com", "user@@example.com"]
print("メールアドレスのバリデーション:")
for email in emails:
    is_valid, message = validate_email(email)
    print(f"  {email}: {message}")

# 2. 再帰関数（階乗）
def factorial(n):
    """n!を計算する"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\n5! = {factorial(5)}")

# 3. 高階関数
def apply_operation(numbers, operation):
    """リストの各要素に操作を適用"""
    return [operation(x) for x in numbers]

nums = [1, 2, 3, 4, 5]
print(f"\n元のリスト: {nums}")
print(f"二乗: {apply_operation(nums, lambda x: x**2)}")
print(f"2倍: {apply_operation(nums, lambda x: x*2)}")
print(f"文字列化: {apply_operation(nums, str)}")

# 4. メモ化（キャッシュ）を使った効率化
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    """メモ化されたフィボナッチ数"""
    if n < 2:
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

print(f"\nフィボナッチ数（メモ化）:")
for i in range(10):
    print(f"  F({i}) = {fibonacci_memo(i)}")

# 5. エラーハンドリングを含む関数
def safe_divide(a, b):
    """安全な除算"""
    try:
        result = a / b
        return True, result
    except ZeroDivisionError:
        return False, "ゼロで除算はできません"
    except TypeError:
        return False, "数値以外は計算できません"

test_cases = [(10, 2), (10, 0), (10, "2")]
print("\n安全な除算:")
for a, b in test_cases:
    success, result = safe_divide(a, b)
    if success:
        print(f"  {a} ÷ {b} = {result}")
    else:
        print(f"  {a} ÷ {b}: エラー - {result}")
```

### 学習ポイント
- `def`キーワードで関数を定義
- 引数はデフォルト値、可変長引数、キーワード引数など様々な形式
- `return`で値を返す（複数の値も可能）
- ラムダ関数で簡潔な関数を定義
- デコレータで関数を拡張
- ジェネレータでメモリ効率的な反復処理

---

## 8. モジュールとパッケージ {#モジュールとパッケージ}

### モジュールのインポートと作成

```python
# 08_modules.py - モジュールとパッケージ

# ===== 標準ライブラリのインポート =====
print("=== 標準ライブラリのインポート ===")

# import文の基本
import math
print(f"円周率: {math.pi}")
print(f"平方根: {math.sqrt(16)}")

# from ... import文
from datetime import datetime, date, timedelta
now = datetime.now()
print(f"\n現在時刻: {now}")
print(f"今日の日付: {date.today()}")
print(f"1週間後: {date.today() + timedelta(days=7)}")

# エイリアス（別名）を使ったインポート
import random as rnd
print(f"\nランダムな数（1-10）: {rnd.randint(1, 10)}")

# ===== よく使う標準モジュール =====
print("\n=== よく使う標準モジュール ===")

# os モジュール
import os
print(f"現在のディレクトリ: {os.getcwd()}")
print(f"環境変数PATH: {os.environ.get('PATH', 'Not found')[:50]}...")

# sys モジュール
import sys
print(f"\nPythonバージョン: {sys.version.split()[0]}")
print(f"プラットフォーム: {sys.platform}")

# json モジュール
import json
data = {"name": "田中", "age": 25, "hobbies": ["読書", "映画"]}
json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(f"\nJSON形式:\n{json_string}")

# re モジュール（正規表現）
import re
text = "私のメールアドレスは user@example.com です。"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = re.search(email_pattern, text)
if email:
    print(f"\n見つかったメールアドレス: {email.group()}")

# collections モジュール
from collections import Counter, defaultdict
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"\n単語の出現回数: {dict(word_count)}")

# ===== 自作モジュール =====
print("\n=== 自作モジュールの例 ===")

# my_math.py という名前で以下の内容を保存すると仮定
my_math_content = '''
"""数学関連のユーティリティ関数"""

def add(a, b):
    """2つの数を加算"""
    return a + b

def multiply(a, b):
    """2つの数を乗算"""
    return a * b

def factorial(n):
    """階乗を計算"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

PI = 3.14159
E = 2.71828
'''

# 実際の使用例（ファイルがあると仮定）
# from my_math import add, multiply, PI
# result = add(5, 3)
# print(f"5 + 3 = {result}")

print("自作モジュールの構造例:")
print(my_math_content)

# ===== パッケージの構造 =====
print("\n=== パッケージの構造例 ===")

package_structure = """
my_package/
    __init__.py
    math_utils.py
    string_utils.py
    data/
        __init__.py
        csv_handler.py
        json_handler.py
"""

print("パッケージのディレクトリ構造:")
print(package_structure)

# ===== __name__ == "__main__" の使い方 =====
print("\n=== __name__ == '__main__' の使い方 ===")

script_example = '''
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    # このスクリプトが直接実行された時のみ実行される
    print("電卓プログラム")
    result = add(10, 5)
    print(f"10 + 5 = {result}")

if __name__ == "__main__":
    main()
'''

print("スクリプトとモジュールの両方で使える例:")
print(script_example)

# ===== モジュールの検索パス =====
print("\n=== モジュールの検索パス ===")
print("Pythonがモジュールを検索するパス:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"  {i}. {path}")
print("  ...")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. 設定ファイルモジュール
config_example = '''
# config.py
DATABASE = {
    "host": "localhost",
    "port": 5432,
    "name": "myapp",
    "user": "admin"
}

API_KEYS = {
    "weather": "your-api-key",
    "maps": "another-api-key"
}

DEBUG = True
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
'''

print("1. 設定ファイルの例:")
print(config_example)

# 2. ユーティリティモジュール
utils_example = '''
# utils.py
import re
from datetime import datetime

def validate_email(email):
    """メールアドレスのバリデーション"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_date(date_obj, format_string="%Y年%m月%d日"):
    """日付のフォーマット"""
    return date_obj.strftime(format_string)

def generate_id():
    """ユニークなIDを生成"""
    from uuid import uuid4
    return str(uuid4())
'''

print("\n2. ユーティリティモジュールの例:")
print(utils_example)

# 3. データ処理モジュール
data_processor_example = '''
# data_processor.py
import csv
import json

class DataProcessor:
    @staticmethod
    def read_csv(filename):
        """CSVファイルを読み込んでリストで返す"""
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    @staticmethod
    def write_json(data, filename):
        """データをJSONファイルに保存"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
'''

print("\n3. データ処理モジュールの例:")
print(data_processor_example)

# ===== インポートのベストプラクティス =====
print("\n=== インポートのベストプラクティス ===")

best_practices = """
1. 標準ライブラリ → サードパーティ → 自作モジュールの順でインポート
2. アルファベット順に並べる
3. from ... import * は避ける（名前空間の汚染を防ぐ）
4. 循環インポートを避ける
5. 相対インポートよりも絶対インポートを推奨

例：
# 良い例
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

from myapp.utils import helper
from myapp.models import User

# 避けるべき例
from module import *  # 何がインポートされるか不明確
"""

print(best_practices)
```

### 学習ポイント
- `import`文でモジュールをインポート
- `from ... import`で特定の要素のみインポート
- `as`でエイリアス（別名）を設定
- 標準ライブラリには便利なモジュールが多数存在
- 自作モジュールで機能を整理・再利用

---

## 9. クラスとオブジェクト指向 {#クラスとオブジェクト指向}

### オブジェクト指向プログラミング

```python
# 09_classes_and_oop.py - クラスとオブジェクト指向プログラミング

# ===== クラスの基本 =====
print("=== クラスの基本 ===")

# シンプルなクラス
class Dog:
    """犬を表すクラス"""
    
    # クラス変数（すべてのインスタンスで共有）
    species = "犬"
    
    # コンストラクタ（初期化メソッド）
    def __init__(self, name, age):
        # インスタンス変数
        self.name = name
        self.age = age
    
    # インスタンスメソッド
    def bark(self):
        return f"{self.name}が吠えています: ワンワン！"
    
    def info(self):
        return f"{self.name}は{self.age}歳の{self.species}です。"

# インスタンスの作成
dog1 = Dog("ポチ", 3)
dog2 = Dog("ハチ", 5)

print(dog1.info())
print(dog2.info())
print(dog1.bark())

# ===== アクセス修飾子 =====
print("\n=== アクセス修飾子 ===")

class Person:
    def __init__(self, name, age, salary):
        self.name = name          # パブリック
        self._age = age           # プロテクテッド（慣習的）
        self.__salary = salary    # プライベート（名前マングリング）
    
    def get_salary(self):
        """プライベート変数へのアクセサー"""
        return self.__salary
    
    def set_salary(self, new_salary):
        """プライベート変数へのセッター"""
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("給与は正の数である必要があります")

person = Person("田中", 30, 500000)
print(f"名前: {person.name}")  # OK
print(f"年齢: {person._age}")  # 動作するが推奨されない
# print(person.__salary)  # AttributeError
print(f"給与: {person.get_salary()}")

# ===== 継承 =====
print("\n=== 継承 ===")

# 基底クラス（親クラス）
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass  # サブクラスで実装
    
    def info(self):
        return f"{self.name}は{self.species}です。"

# 派生クラス（子クラス）
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "猫")  # 親クラスのコンストラクタを呼び出し
        self.age = age
    
    def make_sound(self):
        return "ニャー"
    
    def purr(self):
        return f"{self.name}がゴロゴロ言っています"

class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name, "鳥")
        self.can_fly = can_fly
    
    def make_sound(self):
        return "チュンチュン"
    
    def fly(self):
        if self.can_fly:
            return f"{self.name}が飛んでいます"
        else:
            return f"{self.name}は飛べません"

# 使用例
cat = Cat("タマ", 2)
bird = Bird("ピーちゃん")
penguin = Bird("ペンペン", can_fly=False)

print(cat.info())
print(f"{cat.name}: {cat.make_sound()}")
print(cat.purr())

print(f"\n{bird.name}: {bird.make_sound()}")
print(bird.fly())
print(penguin.fly())

# ===== 多重継承 =====
print("\n=== 多重継承 ===")

class Flyable:
    def fly(self):
        return "飛んでいます"

class Swimmable:
    def swim(self):
        return "泳いでいます"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "アヒル")
    
    def make_sound(self):
        return "ガーガー"

duck = Duck("ドナルド")
print(duck.info())
print(duck.fly())
print(duck.swim())
print(duck.make_sound())

# ===== ポリモーフィズム =====
print("\n=== ポリモーフィズム ===")

def animal_concert(animals):
    """異なる動物の鳴き声を出力"""
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

# 異なるクラスのインスタンスを同じように扱う
animals = [
    Cat("ミケ", 3),
    Bird("インコ"),
    Duck("カモ子")
]

animal_concert(animals)

# ===== 特殊メソッド（マジックメソッド） =====
print("\n=== 特殊メソッド ===")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """文字列表現"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """開発者向けの文字列表現"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """len()関数で使用"""
        return self.pages
    
    def __eq__(self, other):
        """等価比較"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):
        """小なり比較（ページ数で比較）"""
        return self.pages < other.pages

book1 = Book("Python入門", "山田太郎", 300)
book2 = Book("Python実践", "田中花子", 450)
book3 = Book("Python入門", "山田太郎", 300)

print(str(book1))  # __str__
print(repr(book2))  # __repr__
print(f"ページ数: {len(book1)}")  # __len__
print(f"book1 == book3: {book1 == book3}")  # __eq__
print(f"book1 < book2: {book1 < book2}")  # __lt__

# ===== プロパティ =====
print("\n=== プロパティ ===")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """摂氏温度のゲッター"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """摂氏温度のセッター"""
        if value < -273.15:
            raise ValueError("絶対零度以下にはできません")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """華氏温度（読み取り専用）"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"摂氏: {temp.celsius}°C")
print(f"華氏: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"更新後 - 摂氏: {temp.celsius}°C, 華氏: {temp.fahrenheit}°F")

# ===== クラスメソッドと静的メソッド =====
print("\n=== クラスメソッドと静的メソッド ===")

class DateUtils:
    @staticmethod
    def is_leap_year(year):
        """うるう年判定（静的メソッド）"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @classmethod
    def days_in_month(cls, year, month):
        """月の日数を返す（クラスメソッド）"""
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and cls.is_leap_year(year):
            return 29
        return days[month - 1]

print(f"2024年はうるう年: {DateUtils.is_leap_year(2024)}")
print(f"2024年2月の日数: {DateUtils.days_in_month(2024, 2)}日")

# ===== 実用的なクラスの例 =====
print("\n=== 実用的なクラスの例 ===")

class BankAccount:
    """銀行口座クラス"""
    
    # クラス変数
    bank_name = "Python銀行"
    account_count = 0
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance
        self.transaction_history = []
        BankAccount.account_count += 1
        self.account_number = f"ACC{BankAccount.account_count:04d}"
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        """入金"""
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"入金: ¥{amount:,}")
            return True
        return False
    
    def withdraw(self, amount):
        """出金"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_history.append(f"出金: ¥{amount:,}")
            return True
        return False
    
    def get_statement(self):
        """取引明細"""
        statement = f"\n{self.bank_name} - 口座番号: {self.account_number}\n"
        statement += f"口座名義: {self.owner}\n"
        statement += "取引履歴:\n"
        for transaction in self.transaction_history:
            statement += f"  - {transaction}\n"
        statement += f"現在の残高: ¥{self.__balance:,}"
        return statement

# 使用例
account1 = BankAccount("田中太郎", 10000)
account2 = BankAccount("山田花子", 5000)

account1.deposit(5000)
account1.withdraw(3000)
account1.deposit(10000)

print(account1.get_statement())
print(f"\n総口座数: {BankAccount.account_count}")
```

### 学習ポイント
- クラスは`class`キーワードで定義
- `__init__`メソッドでインスタンスを初期化
- 継承により既存クラスを拡張
- 特殊メソッドでPythonの組み込み関数と連携
- `@property`デコレータでゲッター/セッターを実装

---

## 10. ファイル操作 {#ファイル操作}

### ファイルの読み書き

```python
# 10_file_handling.py - ファイル操作

import os
import json
import csv
from datetime import datetime

# ===== ファイルの読み書き基本 =====
print("=== ファイルの読み書き基本 ===")

# テキストファイルへの書き込み
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Pythonでファイル操作を学んでいます。\n")
    f.write("これは2行目です。\n")
    f.write("3行目を書き込みました。")

print("sample.txtを作成しました")

# テキストファイルの読み込み
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"\nファイル全体の内容:\n{content}")

# 1行ずつ読み込む
print("\n1行ずつ読み込み:")
with open("sample.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"  {line_num}: {line.strip()}")

# ===== ファイルモード =====
print("\n=== ファイルモード ===")

# 追記モード
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("\n追記された行です。")

# readlines()を使った読み込み
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"行数: {len(lines)}")
    print(f"最後の行: {lines[-1].strip()}")

# ===== バイナリファイルの操作 =====
print("\n=== バイナリファイルの操作 ===")

# バイナリデータの書き込み
data = bytes([0x50, 0x79, 0x74, 0x68, 0x6F, 0x6E])  # "Python"
with open("binary_data.bin", "wb") as f:
    f.write(data)

# バイナリデータの読み込み
with open("binary_data.bin", "rb") as f:
    binary_content = f.read()
    print(f"バイナリデータ: {binary_content}")
    print(f"デコード結果: {binary_content.decode('utf-8')}")

# ===== CSVファイルの操作 =====
print("\n=== CSVファイルの操作 ===")

# CSVファイルの書き込み
students = [
    ["名前", "年齢", "成績"],
    ["田中太郎", 20, 85],
    ["山田花子", 22, 92],
    ["佐藤次郎", 21, 78]
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("students.csvを作成しました")

# CSVファイルの読み込み
print("\nCSVファイルの内容:")
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# DictReaderを使った読み込み
print("\nDictReaderを使用:")
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['名前']} ({row['年齢']}歳): {row['成績']}点")

# ===== JSONファイルの操作 =====
print("\n=== JSONファイルの操作 ===")

# 辞書データの準備
data = {
    "users": [
        {
            "id": 1,
            "name": "田中太郎",
            "email": "tanaka@example.com",
            "active": True
        },
        {
            "id": 2,
            "name": "山田花子",
            "email": "yamada@example.com",
            "active": False
        }
    ],
    "updated_at": datetime.now().isoformat()
}

# JSONファイルへの書き込み
with open("users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("users.jsonを作成しました")

# JSONファイルの読み込み
with open("users.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(f"\n読み込んだデータ:")
    print(f"ユーザー数: {len(loaded_data['users'])}")
    for user in loaded_data['users']:
        status = "アクティブ" if user['active'] else "非アクティブ"
        print(f"  {user['name']}: {status}")

# ===== ファイルとディレクトリの操作 =====
print("\n=== ファイルとディレクトリの操作 ===")

# 現在のディレクトリ
current_dir = os.getcwd()
print(f"現在のディレクトリ: {current_dir}")

# ファイルの存在確認
if os.path.exists("sample.txt"):
    print("sample.txtは存在します")
    print(f"  サイズ: {os.path.getsize('sample.txt')}バイト")
    print(f"  絶対パス: {os.path.abspath('sample.txt')}")

# ディレクトリの作成
if not os.path.exists("temp_dir"):
    os.makedirs("temp_dir")
    print("\ntemp_dirを作成しました")

# ファイルの移動/名前変更
if os.path.exists("sample.txt"):
    os.rename("sample.txt", "temp_dir/renamed_sample.txt")
    print("ファイルを移動しました")

# ディレクトリ内のファイル一覧
print("\ntemp_dir内のファイル:")
for item in os.listdir("temp_dir"):
    item_path = os.path.join("temp_dir", item)
    if os.path.isfile(item_path):
        print(f"  ファイル: {item}")
    else:
        print(f"  ディレクトリ: {item}")

# ===== with文を使わない方法（推奨されない） =====
print("\n=== with文を使わない方法（参考） ===")

# 手動でファイルを開いて閉じる
f = open("manual_file.txt", "w", encoding="utf-8")
try:
    f.write("手動でファイルを管理")
finally:
    f.close()  # 必ず閉じる

print("※ with文を使うことを推奨します")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. ログファイルの作成
def write_log(message, filename="app.log"):
    """タイムスタンプ付きでログを記録"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

write_log("アプリケーションが起動しました")
write_log("ユーザーがログインしました")
write_log("処理が完了しました")

print("ログファイルを作成しました")

# 2. 設定ファイルの読み書き
config = {
    "app_name": "MyPythonApp",
    "version": "1.0.0",
    "settings": {
        "debug": True,
        "max_connections": 100,
        "timeout": 30
    }
}

# 設定を保存
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

# 設定を読み込んで更新
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)
    
loaded_config["settings"]["debug"] = False
loaded_config["version"] = "1.0.1"

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(loaded_config, f, indent=2)

print("\n設定ファイルを更新しました")

# 3. データのバックアップ
import shutil

def backup_file(source, backup_dir="backups"):
    """ファイルをタイムスタンプ付きでバックアップ"""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)
    backup_name = f"{name}_{timestamp}{ext}"
    backup_path = os.path.join(backup_dir, backup_name)
    
    shutil.copy2(source, backup_path)
    return backup_path

if os.path.exists("config.json"):
    backup_path = backup_file("config.json")
    print(f"\nバックアップを作成: {backup_path}")

# ===== クリーンアップ =====
print("\n=== クリーンアップ ===")

# 作成したファイルを削除
files_to_remove = [
    "binary_data.bin",
    "students.csv",
    "users.json",
    "manual_file.txt",
    "app.log",
    "config.json"
]

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"削除: {file}")

# ディレクトリの削除
if os.path.exists("temp_dir"):
    shutil.rmtree("temp_dir")
    print("削除: temp_dir/")

if os.path.exists("backups"):
    shutil.rmtree("backups")
    print("削除: backups/")

print("\nクリーンアップ完了")
```

### 学習ポイント
- `with`文でファイルを安全に開閉
- テキストファイルは`encoding="utf-8"`を指定
- CSVは`csv`モジュール、JSONは`json`モジュールを使用
- `os`モジュールでファイルシステムを操作
- 常に例外処理を考慮したファイル操作を心がける

---

## 11. エラー処理 {#エラー処理}

### 例外処理とエラーハンドリング

```python
# 11_error_handling.py - エラー処理と例外

# ===== 基本的な例外処理 =====
print("=== 基本的な例外処理 ===")

# try-except文
try:
    result = 10 / 0
except ZeroDivisionError:
    print("エラー: ゼロで除算することはできません")

# 複数の例外を処理
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"エラー: '{value}'は整数に変換できません")
        return None
    except TypeError:
        print(f"エラー: 型が不正です")
        return None

print(f"\n変換結果: {safe_convert('123')}")
print(f"変換結果: {safe_convert('abc')}")
print(f"変換結果: {safe_convert(None)}")

# ===== 例外の詳細情報 =====
print("\n=== 例外の詳細情報 ===")

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except IndexError as e:
    print(f"エラーの種類: {type(e).__name__}")
    print(f"エラーメッセージ: {str(e)}")

# 複数の例外を同時にキャッチ
try:
    value = input("数値を入力してください（デモのため'abc'を使用）: ")
    value = 'abc'  # デモ用
    num = int(value)
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"入力エラー: {e}")

# ===== else節とfinally節 =====
print("\n=== else節とfinally節 ===")

def read_file_safely(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f"エラー: ファイル '{filename}' が見つかりません")
        return None
    except PermissionError:
        print(f"エラー: ファイル '{filename}' への読み取り権限がありません")
        return None
    else:
        # エラーが発生しなかった場合のみ実行
        print("ファイルの読み取りに成功しました")
        return content
    finally:
        # エラーの有無に関わらず必ず実行
        if file:
            file.close()
            print("ファイルをクローズしました")

# 存在しないファイルを読み込もうとする
read_file_safely("non_existent_file.txt")

# ===== 例外の再発生 =====
print("\n=== 例外の再発生 ===")

def process_data(data):
    try:
        # データ処理のシミュレーション
        if not data:
            raise ValueError("データが空です")
        return data.upper()
    except ValueError:
        print("データ処理中にエラーが発生しました")
        raise  # 例外を再発生させる

try:
    process_data("")
except ValueError as e:
    print(f"上位でキャッチ: {e}")

# ===== カスタム例外 =====
print("\n=== カスタム例外 ===")

class ValidationError(Exception):
    """バリデーションエラー用のカスタム例外"""
    pass

class AgeValidationError(ValidationError):
    """年齢バリデーション用の例外"""
    def __init__(self, age, message="年齢が不正です"):
        self.age = age
        self.message = f"{message}: {age}"
        super().__init__(self.message)

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("年齢は整数である必要があります")
    if age < 0:
        raise AgeValidationError(age, "年齢は0以上である必要があります")
    if age > 150:
        raise AgeValidationError(age, "年齢が現実的ではありません")
    return True

# カスタム例外のテスト
test_ages = [25, -5, 200, "30"]

for age in test_ages:
    try:
        validate_age(age)
        print(f"年齢 {age} は有効です")
    except AgeValidationError as e:
        print(f"年齢エラー: {e}")
    except TypeError as e:
        print(f"型エラー: {e}")

# ===== アサーション =====
print("\n=== アサーション ===")

def calculate_average(numbers):
    assert len(numbers) > 0, "リストが空です"
    assert all(isinstance(n, (int, float)) for n in numbers), "数値以外が含まれています"
    return sum(numbers) / len(numbers)

try:
    print(f"平均: {calculate_average([1, 2, 3, 4, 5])}")
    print(f"平均: {calculate_average([])}")  # AssertionError
except AssertionError as e:
    print(f"アサーションエラー: {e}")

# ===== コンテキストマネージャーでのエラー処理 =====
print("\n=== コンテキストマネージャー ===")

class DatabaseConnection:
    def __enter__(self):
        print("データベースに接続しました")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"エラーが発生しました: {exc_value}")
            print("ロールバックを実行します")
        else:
            print("コミットを実行します")
        print("データベース接続を閉じました")
        return False  # 例外を伝播させる

# 正常なケース
print("正常なケース:")
with DatabaseConnection() as db:
    print("データを処理中...")

# エラーが発生するケース
print("\nエラーケース:")
try:
    with DatabaseConnection() as db:
        print("データを処理中...")
        raise ValueError("データが不正です")
except ValueError:
    print("エラーを処理しました")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. 堅牢な入力処理
def get_user_input(prompt, validator=None, max_attempts=3):
    """ユーザー入力を取得し、バリデーションを行う"""
    for attempt in range(max_attempts):
        try:
            # デモ用の入力値
            if attempt == 0:
                value = "abc"  # 最初は無効な値
            else:
                value = "25"   # 2回目は有効な値
            
            print(f"\n{prompt} (入力値: {value})")
            
            if validator:
                value = validator(value)
            return value
        except Exception as e:
            remaining = max_attempts - attempt - 1
            if remaining > 0:
                print(f"エラー: {e}")
                print(f"残り{remaining}回入力できます")
            else:
                print("最大試行回数に達しました")
                raise

# 使用例
try:
    age = get_user_input("年齢を入力してください:", int)
    print(f"入力された年齢: {age}")
except:
    print("有効な入力が得られませんでした")

# 2. リトライ機能付き関数
import time
import random

def retry(max_attempts=3, delay=1):
    """リトライデコレータ"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"試行 {attempt + 1} 失敗: {e}")
                        print(f"{delay}秒後にリトライします...")
                        time.sleep(delay)
                    else:
                        print(f"すべての試行が失敗しました")
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_network_call():
    """不安定なネットワーク呼び出しのシミュレーション"""
    if random.random() < 0.7:  # 70%の確率で失敗
        raise ConnectionError("ネットワークエラー")
    return "成功！"

print("\n不安定な処理のリトライ:")
try:
    result = unstable_network_call()
    print(f"結果: {result}")
except ConnectionError:
    print("最終的に失敗しました")

# 3. ログ機能付きエラーハンドラ
import logging
from datetime import datetime

# ログの設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_errors(func):
    """エラーをログに記録するデコレータ"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"{func.__name__}でエラー発生: {e}")
            raise
    return wrapper

@log_errors
def risky_operation(x, y):
    """エラーが発生する可能性のある処理"""
    if y == 0:
        raise ValueError("ゼロ除算は許可されていません")
    return x / y

print("\nログ機能付きエラー処理:")
try:
    result = risky_operation(10, 0)
except ValueError:
    print("エラーがログに記録されました")

# ===== エラー処理のベストプラクティス =====
print("\n=== エラー処理のベストプラクティス ===")

best_practices = """
1. 具体的な例外をキャッチする（Exception は最後の手段）
2. エラーメッセージは分かりやすく具体的に
3. finally節でリソースのクリーンアップを行う
4. 適切なログを残す
5. ユーザーフレンドリーなエラーメッセージを表示
6. エラーを握りつぶさない（適切に処理または再発生）
7. カスタム例外は基底例外クラスから継承
"""

print(best_practices)
```

### 学習ポイント
- `try-except`で例外をキャッチして処理
- `else`節は例外が発生しなかった場合に実行
- `finally`節は必ず実行される（クリーンアップ用）
- カスタム例外クラスで独自のエラー型を定義
- デコレータでエラー処理を共通化

---

## まとめ

このチュートリアルでは、Pythonプログラミングの基礎から応用まで幅広くカバーしました。

### 学習した内容
1. **基本構文**: 変数、データ型、演算子
2. **データ構造**: リスト、タプル、辞書、セット
3. **制御構造**: 条件分岐、ループ
4. **関数**: 定義、引数、戻り値、デコレータ
5. **モジュール**: インポート、パッケージ構造
6. **オブジェクト指向**: クラス、継承、ポリモーフィズム
7. **ファイル操作**: テキスト、CSV、JSON
8. **エラー処理**: 例外処理、カスタム例外

### 次のステップ
- より高度なPythonライブラリ（NumPy、Pandas、Matplotlib）を学習
- Webフレームワーク（Django、Flask）でWebアプリケーション開発
- データサイエンスや機械学習への応用
- 実際のプロジェクトでコードを書いて経験を積む

### 参考リソース
- [Python公式ドキュメント](https://docs.python.org/ja/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- オンラインコミュニティやフォーラムでの質問と学習

プログラミングは実践が重要です。このチュートリアルで学んだ内容を基に、自分のプロジェクトを作成してみてください。Happy Coding! 🐍