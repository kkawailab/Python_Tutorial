# 04_lists_and_tuples.py - リストとタプル

# ===== リストの基本 =====
print("=== リストの基本 ===")

# リストの作成
fruits = ["りんご", "みかん", "ばなな"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Python", 3.14, True, None]
empty_list = []

print(f"果物リスト: {fruits}")
print(f"数値リスト: {numbers}")
print(f"混合リスト: {mixed}")
print(f"空のリスト: {empty_list}")

# リストの長さ
print(f"\nリストの長さ: {len(fruits)}")

# ===== インデックスとスライス =====
print("\n=== インデックスとスライス ===")

languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]

# インデックスアクセス
print(f"最初の要素: {languages[0]}")
print(f"最後の要素: {languages[-1]}")
print(f"3番目の要素: {languages[2]}")

# スライス
print(f"最初の3つ: {languages[:3]}")
print(f"2番目から4番目: {languages[1:4]}")
print(f"最後の2つ: {languages[-2:]}")
print(f"1つ飛ばし: {languages[::2]}")

# ===== リストの変更 =====
print("\n=== リストの変更 ===")

colors = ["赤", "青", "緑"]
print(f"元のリスト: {colors}")

# 要素の変更
colors[1] = "黄"
print(f"要素変更後: {colors}")

# 要素の追加
colors.append("紫")  # 末尾に追加
print(f"append後: {colors}")

colors.insert(1, "オレンジ")  # 指定位置に挿入
print(f"insert後: {colors}")

colors.extend(["黒", "白"])  # 複数要素を追加
print(f"extend後: {colors}")

# 要素の削除
colors.remove("黄")  # 値を指定して削除
print(f"remove後: {colors}")

deleted = colors.pop()  # 最後の要素を削除して返す
print(f"pop後: {colors} (削除された要素: {deleted})")

deleted = colors.pop(0)  # インデックスを指定して削除
print(f"pop(0)後: {colors} (削除された要素: {deleted})")

# del文での削除
del colors[1]
print(f"del後: {colors}")

# リストのクリア
colors_copy = colors.copy()
colors_copy.clear()
print(f"clear後: {colors_copy}")

# ===== リストのメソッド =====
print("\n=== リストのメソッド ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# カウント
print(f"数値リスト: {numbers}")
print(f"1の出現回数: {numbers.count(1)}")
print(f"5の出現回数: {numbers.count(5)}")

# インデックスの検索
print(f"最初の5のインデックス: {numbers.index(5)}")

# ソート
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"昇順ソート: {numbers_copy}")

numbers_copy.sort(reverse=True)
print(f"降順ソート: {numbers_copy}")

# sorted()関数（元のリストは変更しない）
sorted_numbers = sorted(numbers)
print(f"sorted()使用: {sorted_numbers}")
print(f"元のリスト: {numbers}")

# 反転
numbers_copy = numbers.copy()
numbers_copy.reverse()
print(f"反転: {numbers_copy}")

# ===== リスト内包表記 =====
print("\n=== リスト内包表記 ===")

# 基本的なリスト内包表記
squares = [x**2 for x in range(1, 6)]
print(f"1-5の平方数: {squares}")

# 条件付きリスト内包表記
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"1-10の偶数: {even_numbers}")

# 文字列操作
words = ["python", "java", "javascript", "ruby"]
upper_words = [word.upper() for word in words]
print(f"大文字変換: {upper_words}")

# 条件分岐を含む
numbers = [1, 2, 3, 4, 5]
result = ["偶数" if x % 2 == 0 else "奇数" for x in numbers]
print(f"偶数奇数判定: {result}")

# ===== タプルの基本 =====
print("\n=== タプルの基本 ===")

# タプルの作成
tuple1 = (1, 2, 3)
tuple2 = "a", "b", "c"  # 括弧なしでもOK
single_tuple = (1,)  # 要素が1つの場合はカンマが必要
empty_tuple = ()

print(f"タプル1: {tuple1}")
print(f"タプル2: {tuple2}")
print(f"単一要素タプル: {single_tuple}")
print(f"空のタプル: {empty_tuple}")

# タプルは変更不可（イミュータブル）
coordinates = (10, 20)
print(f"座標: {coordinates}")
# coordinates[0] = 30  # エラー！

# タプルのアンパック
x, y = coordinates
print(f"x = {x}, y = {y}")

# 複数の値を返す関数でよく使われる
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [5, 2, 8, 1, 9]
minimum, maximum = get_min_max(nums)
print(f"最小値: {minimum}, 最大値: {maximum}")

# ===== リストとタプルの相互変換 =====
print("\n=== リストとタプルの相互変換 ===")

list_data = [1, 2, 3, 4, 5]
tuple_data = tuple(list_data)
print(f"リスト→タプル: {tuple_data}")

back_to_list = list(tuple_data)
print(f"タプル→リスト: {back_to_list}")

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
    print(row)

# 要素へのアクセス
print(f"\n2行3列目の要素: {matrix[1][2]}")

# 転置行列
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("\n転置行列:")
for row in transposed:
    print(row)

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 成績データの処理
students = [
    ("田中", 85),
    ("山田", 92),
    ("佐藤", 78),
    ("鈴木", 88),
    ("高橋", 95)
]

# 成績順にソート
students.sort(key=lambda x: x[1], reverse=True)
print("成績順位:")
for i, (name, score) in enumerate(students, 1):
    print(f"{i}位: {name} - {score}点")

# 平均点の計算
scores = [score for name, score in students]
average = sum(scores) / len(scores)
print(f"\n平均点: {average:.1f}点")

# 合格者のリスト（80点以上）
passed = [name for name, score in students if score >= 80]
print(f"合格者: {passed}")