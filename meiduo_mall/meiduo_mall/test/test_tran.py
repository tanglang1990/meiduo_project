
a = 100
b = 100

def transfer(count):
    global a
    global b
    if a < count:
        print('a的余额不足')
    else:
        a -= count
        b += count
        print('a的余额:' + str(a))
        print('b的余额:' + str(b))

transfer(50)
transfer(100)
