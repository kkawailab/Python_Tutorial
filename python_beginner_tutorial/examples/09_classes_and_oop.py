# 09_classes_and_oop.py - クラスとオブジェクト指向プログラミング

# ===== クラスの基本 =====
print("=== クラスの基本 ===")

# シンプルなクラス
class Dog:
    """犬を表すクラス"""
    
    # クラス変数（すべてのインスタンスで共有）
    species = "犬"
    
    # コンストラクタ（初期化メソッド）
    def __init__(self, name, age):
        # インスタンス変数
        self.name = name
        self.age = age
    
    # インスタンスメソッド
    def bark(self):
        return f"{self.name}が吠えています: ワンワン！"
    
    def info(self):
        return f"{self.name}は{self.age}歳の{self.species}です。"

# インスタンスの作成
dog1 = Dog("ポチ", 3)
dog2 = Dog("ハチ", 5)

print(dog1.info())
print(dog2.info())
print(dog1.bark())

# ===== アクセス修飾子 =====
print("\n=== アクセス修飾子 ===")

class Person:
    def __init__(self, name, age, salary):
        self.name = name          # パブリック
        self._age = age           # プロテクテッド（慣習的）
        self.__salary = salary    # プライベート（名前マングリング）
    
    def get_salary(self):
        """プライベート変数へのアクセサー"""
        return self.__salary
    
    def set_salary(self, new_salary):
        """プライベート変数へのセッター"""
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("給与は正の数である必要があります")

person = Person("田中", 30, 500000)
print(f"名前: {person.name}")  # OK
print(f"年齢: {person._age}")  # 動作するが推奨されない
# print(person.__salary)  # AttributeError
print(f"給与: {person.get_salary()}")

# ===== 継承 =====
print("\n=== 継承 ===")

# 基底クラス（親クラス）
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass  # サブクラスで実装
    
    def info(self):
        return f"{self.name}は{self.species}です。"

# 派生クラス（子クラス）
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "猫")  # 親クラスのコンストラクタを呼び出し
        self.age = age
    
    def make_sound(self):
        return "ニャー"
    
    def purr(self):
        return f"{self.name}がゴロゴロ言っています"

class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name, "鳥")
        self.can_fly = can_fly
    
    def make_sound(self):
        return "チュンチュン"
    
    def fly(self):
        if self.can_fly:
            return f"{self.name}が飛んでいます"
        else:
            return f"{self.name}は飛べません"

# 使用例
cat = Cat("タマ", 2)
bird = Bird("ピーちゃん")
penguin = Bird("ペンペン", can_fly=False)

print(cat.info())
print(f"{cat.name}: {cat.make_sound()}")
print(cat.purr())

print(f"\n{bird.name}: {bird.make_sound()}")
print(bird.fly())
print(penguin.fly())

# ===== 多重継承 =====
print("\n=== 多重継承 ===")

class Flyable:
    def fly(self):
        return "飛んでいます"

class Swimmable:
    def swim(self):
        return "泳いでいます"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "アヒル")
    
    def make_sound(self):
        return "ガーガー"

duck = Duck("ドナルド")
print(duck.info())
print(duck.fly())
print(duck.swim())
print(duck.make_sound())

# ===== ポリモーフィズム =====
print("\n=== ポリモーフィズム ===")

def animal_concert(animals):
    """異なる動物の鳴き声を出力"""
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

# 異なるクラスのインスタンスを同じように扱う
animals = [
    Cat("ミケ", 3),
    Bird("インコ"),
    Duck("カモ子")
]

animal_concert(animals)

# ===== 特殊メソッド（マジックメソッド） =====
print("\n=== 特殊メソッド ===")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """文字列表現"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """開発者向けの文字列表現"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """len()関数で使用"""
        return self.pages
    
    def __eq__(self, other):
        """等価比較"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):
        """小なり比較（ページ数で比較）"""
        return self.pages < other.pages

book1 = Book("Python入門", "山田太郎", 300)
book2 = Book("Python実践", "田中花子", 450)
book3 = Book("Python入門", "山田太郎", 300)

print(str(book1))  # __str__
print(repr(book2))  # __repr__
print(f"ページ数: {len(book1)}")  # __len__
print(f"book1 == book3: {book1 == book3}")  # __eq__
print(f"book1 < book2: {book1 < book2}")  # __lt__

# ===== プロパティ =====
print("\n=== プロパティ ===")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """摂氏温度のゲッター"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """摂氏温度のセッター"""
        if value < -273.15:
            raise ValueError("絶対零度以下にはできません")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """華氏温度（読み取り専用）"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"摂氏: {temp.celsius}°C")
print(f"華氏: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"更新後 - 摂氏: {temp.celsius}°C, 華氏: {temp.fahrenheit}°F")

# ===== クラスメソッドと静的メソッド =====
print("\n=== クラスメソッドと静的メソッド ===")

class DateUtils:
    @staticmethod
    def is_leap_year(year):
        """うるう年判定（静的メソッド）"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @classmethod
    def days_in_month(cls, year, month):
        """月の日数を返す（クラスメソッド）"""
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and cls.is_leap_year(year):
            return 29
        return days[month - 1]

print(f"2024年はうるう年: {DateUtils.is_leap_year(2024)}")
print(f"2024年2月の日数: {DateUtils.days_in_month(2024, 2)}日")

# ===== 実用的なクラスの例 =====
print("\n=== 実用的なクラスの例 ===")

class BankAccount:
    """銀行口座クラス"""
    
    # クラス変数
    bank_name = "Python銀行"
    account_count = 0
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance
        self.transaction_history = []
        BankAccount.account_count += 1
        self.account_number = f"ACC{BankAccount.account_count:04d}"
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        """入金"""
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"入金: ¥{amount:,}")
            return True
        return False
    
    def withdraw(self, amount):
        """出金"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_history.append(f"出金: ¥{amount:,}")
            return True
        return False
    
    def get_statement(self):
        """取引明細"""
        statement = f"\n{self.bank_name} - 口座番号: {self.account_number}\n"
        statement += f"口座名義: {self.owner}\n"
        statement += "取引履歴:\n"
        for transaction in self.transaction_history:
            statement += f"  - {transaction}\n"
        statement += f"現在の残高: ¥{self.__balance:,}"
        return statement

# 使用例
account1 = BankAccount("田中太郎", 10000)
account2 = BankAccount("山田花子", 5000)

account1.deposit(5000)
account1.withdraw(3000)
account1.deposit(10000)

print(account1.get_statement())
print(f"\n総口座数: {BankAccount.account_count}")