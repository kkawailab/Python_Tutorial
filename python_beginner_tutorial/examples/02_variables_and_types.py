# 02_variables_and_types.py - 変数とデータ型

# ===== 変数の基本 =====
# 変数の宣言と代入
name = "田中太郎"
age = 25
height = 170.5
is_student = True

print("名前:", name)
print("年齢:", age)
print("身長:", height, "cm")
print("学生:", is_student)

# 変数の型を確認
print("\n型の確認:")
print("nameの型:", type(name))
print("ageの型:", type(age))
print("heightの型:", type(height))
print("is_studentの型:", type(is_student))

# ===== 数値型 =====
print("\n=== 数値型 ===")

# 整数（int）
integer_num = 100
negative_num = -50
binary_num = 0b1010  # 2進数
octal_num = 0o12     # 8進数
hex_num = 0xFF       # 16進数

print(f"整数: {integer_num}")
print(f"負の数: {negative_num}")
print(f"2進数 0b1010 = {binary_num}")
print(f"8進数 0o12 = {octal_num}")
print(f"16進数 0xFF = {hex_num}")

# 浮動小数点数（float）
float_num = 3.14159
scientific = 1.23e-4  # 科学的記数法

print(f"\n浮動小数点数: {float_num}")
print(f"科学的記数法: {scientific}")

# 複素数（complex）
complex_num = 3 + 4j
print(f"複素数: {complex_num}")
print(f"実部: {complex_num.real}, 虚部: {complex_num.imag}")

# ===== 文字列型 =====
print("\n=== 文字列型 ===")

# 文字列の作成
single_quote = 'シングルクォート'
double_quote = "ダブルクォート"
triple_quote = '''複数行の
文字列を
書くことができます'''

print(single_quote)
print(double_quote)
print(triple_quote)

# 文字列の結合
first_name = "太郎"
last_name = "田中"
full_name = last_name + " " + first_name
print(f"フルネーム: {full_name}")

# 文字列の長さ
text = "Python programming"
print(f"'{text}'の長さ: {len(text)}")

# ===== ブール型 =====
print("\n=== ブール型 ===")

is_sunny = True
is_raining = False

print(f"晴れている: {is_sunny}")
print(f"雨が降っている: {is_raining}")

# ブール値の演算
print(f"晴れていて雨が降っていない: {is_sunny and not is_raining}")

# ===== None型 =====
print("\n=== None型 ===")

result = None
print(f"result: {result}")
print(f"resultの型: {type(result)}")

# ===== 型変換 =====
print("\n=== 型変換 ===")

# 文字列から数値へ
str_num = "123"
int_from_str = int(str_num)
float_from_str = float(str_num)

print(f"文字列 '{str_num}' → 整数 {int_from_str}")
print(f"文字列 '{str_num}' → 浮動小数点数 {float_from_str}")

# 数値から文字列へ
num = 456
str_from_num = str(num)
print(f"数値 {num} → 文字列 '{str_from_num}'")

# 浮動小数点数から整数へ（切り捨て）
float_val = 3.7
int_from_float = int(float_val)
print(f"浮動小数点数 {float_val} → 整数 {int_from_float}")

# ===== 変数の命名規則 =====
print("\n=== 変数の命名規則 ===")

# 良い変数名の例
user_name = "山田"
user_age = 30
MAX_SIZE = 100  # 定数は大文字
_private_var = "プライベート"

# Pythonの予約語は使えない
# class = "クラス"  # エラー
# def = "定義"      # エラー

print("良い変数名の例:")
print(f"user_name: {user_name}")
print(f"user_age: {user_age}")
print(f"MAX_SIZE: {MAX_SIZE}")

# ===== 複数代入 =====
print("\n=== 複数代入 ===")

# 複数の変数に同時に代入
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# 値の交換
a, b = 5, 10
print(f"交換前: a={a}, b={b}")
a, b = b, a
print(f"交換後: a={a}, b={b}")

# 同じ値を複数の変数に代入
p = q = r = 0
print(f"p={p}, q={q}, r={r}")