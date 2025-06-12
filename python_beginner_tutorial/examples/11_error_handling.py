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