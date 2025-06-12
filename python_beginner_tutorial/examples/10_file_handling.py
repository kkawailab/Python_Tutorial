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