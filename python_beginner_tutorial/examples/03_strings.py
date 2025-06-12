# 03_strings.py - 文字列の操作

# ===== 文字列の作成と基本操作 =====
print("=== 文字列の作成と基本操作 ===")

# 文字列の作成
text1 = "Python"
text2 = 'プログラミング'
text3 = """複数行の
文字列"""

# 文字列の結合
combined = text1 + " " + text2
print(f"結合: {combined}")

# 文字列の繰り返し
repeated = "Python! " * 3
print(f"繰り返し: {repeated}")

# ===== 文字列のインデックスとスライス =====
print("\n=== インデックスとスライス ===")

text = "Python Programming"

# インデックス（0から始まる）
print(f"最初の文字: {text[0]}")
print(f"最後の文字: {text[-1]}")
print(f"5番目の文字: {text[4]}")

# スライス
print(f"最初の6文字: {text[0:6]}")
print(f"7文字目以降: {text[7:]}")
print(f"最後の11文字: {text[-11:]}")
print(f"2文字おきに取得: {text[::2]}")
print(f"逆順: {text[::-1]}")

# ===== 文字列メソッド =====
print("\n=== 文字列メソッド ===")

sample = "  Hello, Python World!  "

# 大文字・小文字変換
print(f"大文字: {sample.upper()}")
print(f"小文字: {sample.lower()}")
print(f"先頭のみ大文字: {sample.capitalize()}")
print(f"単語の先頭を大文字: {sample.title()}")
print(f"大小文字入れ替え: {sample.swapcase()}")

# 空白の処理
print(f"両端の空白削除: '{sample.strip()}'")
print(f"左端の空白削除: '{sample.lstrip()}'")
print(f"右端の空白削除: '{sample.rstrip()}'")

# 文字列の検索
text = "Python is awesome. Python is powerful."
print(f"\n'Python'の位置: {text.find('Python')}")
print(f"'Python'の最後の位置: {text.rfind('Python')}")
print(f"'Python'の出現回数: {text.count('Python')}")
print(f"'awesome'を含む: {'awesome' in text}")
print(f"'Python'で始まる: {text.startswith('Python')}")
print(f"'powerful.'で終わる: {text.endswith('powerful.')}")

# 文字列の置換
replaced = text.replace("Python", "Programming")
print(f"\n置換後: {replaced}")

# 文字列の分割と結合
words = text.split()
print(f"\n単語に分割: {words}")

csv_data = "りんご,みかん,ばなな,ぶどう"
fruits = csv_data.split(",")
print(f"カンマで分割: {fruits}")

# リストを文字列に結合
joined = " - ".join(fruits)
print(f"結合: {joined}")

# ===== 文字列のフォーマット =====
print("\n=== 文字列のフォーマット ===")

name = "田中"
age = 25
height = 170.5

# f文字列（Python 3.6以降推奨）
print(f"{name}さんは{age}歳で、身長は{height}cmです。")

# format()メソッド
print("{}さんは{}歳で、身長は{}cmです。".format(name, age, height))
print("{0}さんは{1}歳です。{0}さんの身長は{2}cmです。".format(name, age, height))
print("{n}さんは{a}歳で、身長は{h}cmです。".format(n=name, a=age, h=height))

# %演算子（古い方法）
print("%sさんは%d歳で、身長は%.1fcmです。" % (name, age, height))

# 数値のフォーマット
price = 1234.567
print(f"\n価格: ¥{price:,.2f}")  # カンマ区切り、小数点以下2桁
print(f"パーセント: {0.856:.1%}")  # パーセント表示
print(f"2進数: {42:b}")  # 2進数
print(f"16進数: {255:x}")  # 16進数

# 幅指定と配置
print(f"\n右寄せ: '{name:>10}'")
print(f"左寄せ: '{name:<10}'")
print(f"中央寄せ: '{name:^10}'")
print(f"0埋め: {age:05d}")

# ===== エスケープシーケンス =====
print("\n=== エスケープシーケンス ===")

print("改行\n新しい行")
print("タブ\t区切り")
print("バックスラッシュ\\")
print("シングルクォート\'とダブルクォート\"")
print("キャリッジリターン\rで先頭に戻る")

# raw文字列
path = r"C:\Users\name\Documents\file.txt"
print(f"Windowsパス: {path}")

# ===== 文字列の判定 =====
print("\n=== 文字列の判定 ===")

# 数字の判定
num_str = "12345"
alpha_str = "abcde"
alnum_str = "abc123"
space_str = "   "

print(f"'{num_str}'.isdigit(): {num_str.isdigit()}")
print(f"'{alpha_str}'.isalpha(): {alpha_str.isalpha()}")
print(f"'{alnum_str}'.isalnum(): {alnum_str.isalnum()}")
print(f"'{space_str}'.isspace(): {space_str.isspace()}")

# 大文字・小文字の判定
upper_str = "HELLO"
lower_str = "hello"
title_str = "Hello World"

print(f"\n'{upper_str}'.isupper(): {upper_str.isupper()}")
print(f"'{lower_str}'.islower(): {lower_str.islower()}")
print(f"'{title_str}'.istitle(): {title_str.istitle()}")

# ===== Unicode文字列 =====
print("\n=== Unicode文字列 ===")

emoji = "Python 🐍 プログラミング 💻"
print(emoji)
print(f"文字数: {len(emoji)}")

# 文字のUnicodeコードポイント
char = "あ"
print(f"'{char}'のコードポイント: {ord(char)}")
print(f"コードポイント12354の文字: {chr(12354)}")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# メールアドレスの検証（簡易版）
email = "user@example.com"
if "@" in email and email.count("@") == 1:
    username, domain = email.split("@")
    if username and domain and "." in domain:
        print(f"{email} は有効なメールアドレスの形式です")

# 文字列の正規化
user_input = "  Python Programming  "
normalized = user_input.strip().lower().replace(" ", "_")
print(f"正規化: '{user_input}' → '{normalized}'")