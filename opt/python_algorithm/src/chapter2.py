import sys
import math

# 2.2 FizzBuzzを実装する
def fizzbuzz(start=1, end=100):
    for i in range(start, end):
        if (i % 3 == 0) and (i % 5 == 0):  # if i % 15 == 0:
            print("FizzBuzz", end="\n")
        elif i % 3 == 0:
            print("Fizz", end="\n")
        elif i % 5 == 0:
            print("Buzz", end="\n")
        else:
            print(i, end="\n")


# 2.3 自動販売機のお釣り計算
def vending_machine():
    input_price = input('insert:')
    if not input_price.isdecimal():
        print('整数を入力してください。')
        sys.exit()

    product_price = input('product:')
    if not product_price.isdecimal():
        print('整数を入力してください。')
        sys.exit()

    change = int(input_price) - int(product_price)
    if change < 0:
        print('金額が不足しています。')
        sys.exit()

    print(change)
    coin = [5000,1000,500,100,10,5,1]

    for i in coin:
        # num = change // i
        # change %= i
        num,change = divmod(change,i)
        print('{}:{}枚'.format(i,num))

# 10進数の数字を任意の基数の数字に変換するメソッド
def convert1(from_num, base_num = 2):
    result = ''

    while from_num > 0:
        result = str(from_num % base_num) + result
        from_num //= base_num
    print(result)

# 2進数の数字を10進数の数字に変換するメソッド
def convert2(from_num):

    num_str = str(from_num)
    result = 0
    for i in range(len(num_str)):
        result += int(num_str[i]) * 2**(len(num_str)-i-1)
    print(result)


# 素数を求めるメソッド 与えられた値が素数ならTrue、素数でないならFalse
# 与えられた値をその値の平方根までの範囲で割り切れる値がないか検索する。
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 素数を求めるメソッド 与えられた値が素数ならTrue、素数でないならFalse
# エラトステネスの篩を使用した場合
def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    # 奇数のリストを作成
    # data = [i for i in range(0,n) if not i % 2 == 0]
    data = [i + 1 for i in range(2, n, 2)]
    while limit > data[0]:
        prime.append(data[0])
        # 割り切れない値だけを取り出す
        data = [j for j in data if j % data[0] != 0]

    return prime + data


