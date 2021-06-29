import time

t = time.localtime()

print(t)
d = time.strftime("%Y/%m/%d %A",t)
h = time.strftime("%H:%M:%S ,t")
print(d)
print(h)

import datetime
n = datetime.datetime.now()
print(n)
print("時を取り出す",n.hour)
print("分を取り出す",n.minute)
print("秒を取り出す",n.second)

