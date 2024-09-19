from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

# 平文（plain text）
pt = bytes_to_long(b"sayonara")

# 公開鍵の生成
p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 6557

# 秘密鍵の生成
phi = (p-1)*(q-1)
d = pow(e,-1,phi)

# 暗号化
ct = pow(pt, e, n)
print(long_to_bytes(ct))

# 復号
pt = pow(ct, d, n)
print(long_to_bytes(pt))

