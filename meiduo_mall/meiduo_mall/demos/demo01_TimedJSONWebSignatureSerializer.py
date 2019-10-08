from itsdangerous import TimedJSONWebSignatureSerializer as Serialzier, BadSignature, SignatureExpired

# TimedJSONWebSignatureSerializer
# Timed : 时效
# JSON ：处理的是类似json的数据
# Signature ： 签名， 会进行加密的处理
# Serializer ： 序列化，是可逆的

secret_key = '123456'
expires_in = 5
s = Serialzier(secret_key, expires_in)
access_token = s.dumps({'uid': 1})
access_token = access_token.decode()

# 正常情况
s1 = Serialzier(secret_key, expires_in)
try:
    result = s1.loads(access_token)
except BadSignature:
    print('签名异常')
else:
    print('正常情况：')
    print(result)

# 模拟别人不知道秘钥想解密 access_token
s1 = Serialzier('1234567', expires_in)
try:
    result = s1.loads(access_token)
except BadSignature:
    print('签名异常')
else:
    print(result)

# 模拟别人尝试伪造 access_token，但伪造错了
s1 = Serialzier(secret_key, expires_in)
try:
    result = s1.loads(access_token + '1')
except BadSignature:
    print('签名异常')
else:
    print(result)

# 模拟过期
import time

time.sleep(6)
s1 = Serialzier(secret_key, expires_in)
try:
    result = s1.loads(access_token)
except SignatureExpired:
    print('签名已过期')
else:
    print(result)
