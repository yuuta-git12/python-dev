
def fibonacci1(n):
    """
    フィボナッチ数列を求めるプログラム

    :param n: フィボナッチ数列の要素番号
    :return: フィボナッチ数列の要素番号nの値を返す
    n = 30の際の処理時間:0.660043344
    """
    if (n == 1) or (n == 2):
        return 1
    return fibonacci1(n - 2) + fibonacci1(n - 1)


memo = {1: 1, 2: 1}
def fibonacci2(n):
    """
    メモ化を使用したフィボナッチ数列を求めるプログラム
    :param n:
    :return:
    n = 30の際の処理時間:8.406900000001993e-05
    """
    if n in memo:
        return memo[n]
    # 辞書に登録されていない値は計算して辞書に登録する。
    memo[n] = fibonacci2(n-2) + fibonacci2(n-1)
    return memo[n]

def fibonacci3(n):
    """
    ループを使ったフィボナッチ数列を求めるプログラム
    :param n:
    :return:
    n = 30の際の処理時間:0.00014319299999998591
    """
    fib = [1,1]
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])

    return fib[n-1]