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