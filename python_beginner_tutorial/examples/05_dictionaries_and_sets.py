# 05_dictionaries_and_sets.py - 辞書と集合

# ===== 辞書の基本 =====
print("=== 辞書の基本 ===")

# 辞書の作成
person = {
    "name": "田中太郎",
    "age": 25,
    "city": "東京",
    "hobbies": ["読書", "映画鑑賞", "プログラミング"]
}

# 別の作成方法
scores = dict(math=85, english=92, science=78)
empty_dict = {}

print(f"人物情報: {person}")
print(f"成績: {scores}")
print(f"空の辞書: {empty_dict}")

# ===== 値へのアクセス =====
print("\n=== 値へのアクセス ===")

# キーを使ったアクセス
print(f"名前: {person['name']}")
print(f"年齢: {person['age']}")
print(f"趣味: {person['hobbies']}")

# get()メソッド（キーが存在しない場合のデフォルト値）
print(f"職業: {person.get('job', '未設定')}")
print(f"電話: {person.get('phone')}")  # None

# ===== 辞書の変更 =====
print("\n=== 辞書の変更 ===")

# 値の更新
person["age"] = 26
print(f"年齢更新後: {person['age']}")

# 新しいキーと値の追加
person["email"] = "tanaka@example.com"
person["job"] = "エンジニア"
print(f"追加後: {person}")

# update()メソッドで複数の更新
person.update({
    "phone": "090-1234-5678",
    "city": "大阪"
})
print(f"update後: {person}")

# 要素の削除
del person["phone"]
print(f"del後のキー: {list(person.keys())}")

removed_value = person.pop("email", None)
print(f"pop後: 削除された値 = {removed_value}")

# ===== 辞書のメソッド =====
print("\n=== 辞書のメソッド ===")

# キー、値、アイテムの取得
print(f"すべてのキー: {list(person.keys())}")
print(f"すべての値: {list(person.values())}")
print(f"すべてのアイテム: {list(person.items())}")

# キーの存在確認
print(f"'name'キーは存在する: {'name' in person}")
print(f"'salary'キーは存在する: {'salary' in person}")

# 辞書のコピー
person_copy = person.copy()
person_copy["name"] = "山田花子"
print(f"元の辞書の名前: {person['name']}")
print(f"コピーの名前: {person_copy['name']}")

# 辞書のクリア
temp_dict = {"a": 1, "b": 2}
print(f"クリア前: {temp_dict}")
temp_dict.clear()
print(f"クリア後: {temp_dict}")

# ===== 辞書の反復処理 =====
print("\n=== 辞書の反復処理 ===")

product = {
    "name": "ノートPC",
    "price": 98000,
    "brand": "TechCorp",
    "specs": {
        "cpu": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD"
    }
}

# キーでループ
print("キーでループ:")
for key in product:
    print(f"  {key}")

# キーと値でループ
print("\nキーと値でループ:")
for key, value in product.items():
    print(f"  {key}: {value}")

# ネストした辞書へのアクセス
print(f"\nCPU: {product['specs']['cpu']}")
print(f"RAM: {product['specs']['ram']}")

# ===== 辞書内包表記 =====
print("\n=== 辞書内包表記 ===")

# 基本的な辞書内包表記
squares = {x: x**2 for x in range(1, 6)}
print(f"平方数の辞書: {squares}")

# 条件付き辞書内包表記
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数の平方数: {even_squares}")

# リストから辞書を作成
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"名前の長さ: {name_lengths}")

# ===== 集合の基本 =====
print("\n=== 集合の基本 ===")

# 集合の作成
fruits_set = {"りんご", "みかん", "ばなな", "りんご"}  # 重複は自動的に削除
numbers_set = set([1, 2, 3, 2, 1, 4])  # リストから作成
empty_set = set()  # 空の集合

print(f"果物セット: {fruits_set}")
print(f"数値セット: {numbers_set}")
print(f"空のセット: {empty_set}")

# ===== 集合の操作 =====
print("\n=== 集合の操作 ===")

# 要素の追加と削除
colors = {"赤", "青", "緑"}
print(f"元の集合: {colors}")

colors.add("黄")
print(f"add後: {colors}")

colors.remove("青")  # 要素がない場合はエラー
print(f"remove後: {colors}")

colors.discard("紫")  # 要素がなくてもエラーにならない
print(f"discard後: {colors}")

# ===== 集合演算 =====
print("\n=== 集合演算 ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"集合A: {set_a}")
print(f"集合B: {set_b}")

# 和集合
union = set_a | set_b  # または set_a.union(set_b)
print(f"和集合 (A ∪ B): {union}")

# 積集合
intersection = set_a & set_b  # または set_a.intersection(set_b)
print(f"積集合 (A ∩ B): {intersection}")

# 差集合
difference = set_a - set_b  # または set_a.difference(set_b)
print(f"差集合 (A - B): {difference}")

# 対称差集合
symmetric_diff = set_a ^ set_b  # または set_a.symmetric_difference(set_b)
print(f"対称差 (A △ B): {symmetric_diff}")

# 部分集合の判定
subset = {1, 2, 3}
print(f"{subset} は {set_a} の部分集合: {subset.issubset(set_a)}")
print(f"{set_a} は {subset} の上位集合: {set_a.issuperset(subset)}")

# ===== 集合内包表記 =====
print("\n=== 集合内包表記 ===")

# 基本的な集合内包表記
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(f"1-10の偶数集合: {even_set}")

# 文字列から重複を除いた文字集合
text = "programming"
unique_chars = {char for char in text}
print(f"'{text}'の文字集合: {unique_chars}")

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. 成績管理システム
students_data = {
    "S001": {
        "name": "田中太郎",
        "scores": {"数学": 85, "英語": 92, "理科": 78},
        "club": "プログラミング部"
    },
    "S002": {
        "name": "山田花子",
        "scores": {"数学": 90, "英語": 88, "理科": 95},
        "club": "科学部"
    },
    "S003": {
        "name": "佐藤次郎",
        "scores": {"数学": 75, "英語": 80, "理科": 82},
        "club": "プログラミング部"
    }
}

# 各生徒の平均点を計算
print("生徒の平均点:")
for student_id, data in students_data.items():
    scores = data["scores"].values()
    average = sum(scores) / len(scores)
    print(f"{data['name']}: {average:.1f}点")

# 2. 重複の除去
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(list_with_duplicates))
print(f"\n重複除去前: {list_with_duplicates}")
print(f"重複除去後: {unique_list}")

# 3. 共通の要素を見つける
python_users = {"Alice", "Bob", "Charlie", "David"}
java_users = {"Bob", "David", "Eve", "Frank"}
javascript_users = {"Alice", "Charlie", "Eve", "George"}

# すべての言語を使うユーザー
all_languages = python_users & java_users & javascript_users
print(f"\nすべての言語を使うユーザー: {all_languages}")

# Pythonだけを使うユーザー
python_only = python_users - java_users - javascript_users
print(f"Pythonだけを使うユーザー: {python_only}")

# 少なくとも2つの言語を使うユーザー
at_least_two = (python_users & java_users) | (python_users & javascript_users) | (java_users & javascript_users)
print(f"少なくとも2つの言語を使うユーザー: {at_least_two}")

# 4. 単語の出現頻度をカウント
text = "Python is great. Python is powerful. Python is easy to learn."
words = text.lower().replace(".", "").split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\n単語の出現頻度:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}回")