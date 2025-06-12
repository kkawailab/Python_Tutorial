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