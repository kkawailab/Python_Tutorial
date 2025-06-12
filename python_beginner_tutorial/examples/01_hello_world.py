# 01_hello_world.py - Pythonの最初のプログラム

# 最も基本的な出力
print("Hello, World!")
print("こんにちは、Python！")

# 複数の値を出力
print("私の名前は", "太郎", "です")

# 区切り文字を指定
print("りんご", "みかん", "ばなな", sep=", ")

# 改行を制御
print("1行目", end=" ")
print("同じ行に続きます")

# 空行を出力
print()

# 複数行の文字列
print("""これは
複数行の
文字列です""")

# エスケープシーケンス
print("改行→\n新しい行")
print("タブ→\tタブで区切られた")
print("引用符→\"ダブルクォート\"と\'シングルクォート\'")

# raw文字列（エスケープシーケンスを無効化）
print(r"C:\Users\name\Documents")

# 文字列の繰り返し
print("=" * 50)
print("Pythonの学習を始めましょう！")
print("=" * 50)