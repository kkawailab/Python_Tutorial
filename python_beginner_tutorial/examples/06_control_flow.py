# 06_control_flow.py - 制御フロー（条件分岐とループ）

# ===== if文（条件分岐） =====
print("=== if文（条件分岐） ===")

# 基本的なif文
age = 18
if age >= 20:
    print("成人です")
else:
    print("未成年です")

# elif を使った複数条件
score = 85
print(f"\n点数: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"成績: {grade}")

# 複数の条件を組み合わせる
temperature = 28
humidity = 65

print(f"\n温度: {temperature}℃, 湿度: {humidity}%")

if temperature >= 25 and humidity >= 60:
    print("蒸し暑いです")
elif temperature >= 25 and humidity < 60:
    print("暖かくて快適です")
elif temperature < 25 and humidity >= 60:
    print("涼しいけど湿度が高いです")
else:
    print("涼しくて快適です")

# 条件式（三項演算子）
is_weekend = True
message = "休日です" if is_weekend else "平日です"
print(f"\n{message}")

# ===== 比較演算子と論理演算子 =====
print("\n=== 比較演算子と論理演算子 ===")

x = 10
y = 20

# 比較演算子
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # 等しい
print(f"x != y: {x != y}")  # 等しくない
print(f"x < y: {x < y}")    # より小さい
print(f"x > y: {x > y}")    # より大きい
print(f"x <= y: {x <= y}")  # 以下
print(f"x >= y: {x >= y}")  # 以上

# 論理演算子
a = True
b = False
print(f"\na = {a}, b = {b}")
print(f"a and b: {a and b}")  # 両方True
print(f"a or b: {a or b}")    # どちらかTrue
print(f"not a: {not a}")      # 否定

# in演算子
fruits = ["りんご", "みかん", "ばなな"]
print(f"\n'りんご' in fruits: {'りんご' in fruits}")
print(f"'ぶどう' not in fruits: {'ぶどう' not in fruits}")

# ===== for文（繰り返し） =====
print("\n=== for文（繰り返し） ===")

# リストのループ
colors = ["赤", "青", "緑", "黄"]
print("色のリスト:")
for color in colors:
    print(f"  - {color}")

# range()を使ったループ
print("\n1から5まで:")
for i in range(1, 6):
    print(f"  {i}")

# インデックスと値を同時に取得
print("\nインデックスと値:")
for i, color in enumerate(colors):
    print(f"  {i}: {color}")

# 辞書のループ
person = {"name": "田中", "age": 25, "city": "東京"}
print("\n辞書のループ:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 複数のリストを同時にループ
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["東京", "大阪", "名古屋"]

print("\n複数リストの同時ループ:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} ({age}歳) - {city}在住")

# ===== while文 =====
print("\n=== while文 ===")

# 基本的なwhile文
count = 0
print("カウントアップ:")
while count < 5:
    print(f"  カウント: {count}")
    count += 1

# 条件付きwhile文
print("\n3の倍数を見つける:")
num = 1
found_count = 0
while found_count < 5:
    if num % 3 == 0:
        print(f"  {num}")
        found_count += 1
    num += 1

# ===== break と continue =====
print("\n=== break と continue ===")

# break文（ループを終了）
print("breakの例:")
for i in range(10):
    if i == 5:
        print("  5で終了")
        break
    print(f"  {i}")

# continue文（次の反復へスキップ）
print("\ncontinueの例（偶数をスキップ）:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}")

# ===== else節付きループ =====
print("\n=== else節付きループ ===")

# for-else
print("素数判定（for-else）:")
n = 17
for i in range(2, n):
    if n % i == 0:
        print(f"{n}は素数ではありません（{i}で割り切れる）")
        break
else:
    print(f"{n}は素数です")

# while-else
print("\nwhile-else の例:")
count = 0
while count < 3:
    print(f"  カウント: {count}")
    count += 1
else:
    print("  正常に終了しました")

# ===== ネストしたループ =====
print("\n=== ネストしたループ ===")

# 九九の表（一部）
print("九九の表（3×3）:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()  # 改行

# ===== 実用的な例 =====
print("\n=== 実用的な例 ===")

# 1. パスワード強度チェック
def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("8文字以上にしてください")
    
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("大文字を含めてください")
    
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("小文字を含めてください")
    
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("数字を含めてください")
    
    if any(c in "!@#$%^&*" for c in password):
        strength += 1
    else:
        feedback.append("特殊文字(!@#$%^&*)を含めてください")
    
    return strength, feedback

password = "Pass123!"
strength, feedback = check_password_strength(password)

print(f"パスワード: {password}")
print(f"強度: {'★' * strength}{'☆' * (5 - strength)} ({strength}/5)")
if feedback:
    print("改善点:")
    for item in feedback:
        print(f"  - {item}")

# 2. FizzBuzz問題
print("\nFizzBuzz（1-20）:")
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# 3. 数当てゲーム（シミュレーション）
import random

secret_number = random.randint(1, 10)
max_attempts = 3
attempts = 0

print(f"\n数当てゲーム（1-10の数を{max_attempts}回以内に当ててください）")

# シミュレーション用の推測値
guesses = [5, 7, secret_number]  # 3回目で正解するようにする

for guess in guesses:
    attempts += 1
    print(f"推測 {attempts}: {guess}")
    
    if guess == secret_number:
        print(f"正解！ {attempts}回目で当たりました！")
        break
    elif guess < secret_number:
        print("もっと大きい数です")
    else:
        print("もっと小さい数です")
    
    if attempts >= max_attempts:
        print(f"残念！正解は {secret_number} でした")
        break