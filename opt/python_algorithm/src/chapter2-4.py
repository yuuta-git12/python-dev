"""2進数を10進数に変換する処理
"""
n = '10010'
result = 0
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i - 1))
print(result)


"""10進数を2真数に変換する処理
"""
a = 18
print(bin(a))

"""2進数を10進数に変換する処理
"""
b = '10010'
print(int(b, 2))


"""Pythonでのビット反転・論理積・論理和・左シフト・右シフトの処理
"""
val_a = 0b10010
print(bin(val_a), 'のビット反転', bin(~val_a))

val_b = 0b11001
print(bin(val_a), 'と', bin(val_b), 'の論理積', bin(val_a & val_b))

print(bin(val_a), 'と', bin(val_b), 'の論理和', bin(val_a | val_b))

print(bin(val_a), 'の1ビット左シフト', bin(val_a << 1))

print(bin(val_b), 'の2ビット右シフト', bin(val_b >> 2))