import time
import chapter2

"""
素数を求めるメソッド
is_prime()とget_prime()の処理時間の比較を
スクリプト 

引数を100000で実行した場合の結果
is_prime()処理時間:0.434652664
get_prime()処理時間:0.15991669900000005
"""

start = time.perf_counter()
for i in range(100000):
    result = chapter2.is_prime(i)
print('is_prime()処理時間:{}'.format(time.perf_counter() - start))

start = time.perf_counter()
chapter2.get_prime(100000)
print('get_prime()処理時間:{}'.format(time.perf_counter() - start))