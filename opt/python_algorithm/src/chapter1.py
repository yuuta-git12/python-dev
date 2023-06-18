data = [i if i% 2 ==0 else 0 for i in range(10)]
print(data)

data1 = [i for i in range(10) if i% 2 ==0]
print(data1)

"問題1"
x = 3

def calc(x):
    x += 4
    return x

print(x)
print(calc(x))
print(x)

"問題2"
a = [3]

def calc(a):
    a[0] += 4
    return a

print(a)
print(calc(a))
print(a)

"問題3"
a = [3]

def calc(a):
    a = [4]
    return a

print(a)
print(calc(a))
print(a)