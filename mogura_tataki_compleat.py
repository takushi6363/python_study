import time
import random

def mogura(r):
    m = ""
    n = ""
    for i in range(8):
        ana = "."
        if i == r:
           ana = "○"
        m = m + " _" + ana + "_ "
        n = n + " [" + str(i) + "] "
    print(m)
    print(n)

print("＝＝＝＝＝＝＝ゲームスタート＝＝＝＝＝＝＝＝")
hit = 0
ts = time.time()
for i in range(10):
        r = random.randint(0,7)
        mogura(r)
        p = input("もぐらはどこ？")
        if p == str(r):
           print("Hit!")
           hit = hit + 1
        else:
          print("Miss")
t = int(time.time()-ts)
bonus = 0
if t < 60:
    bouns = 60 - t
print("＝＝＝＝＝＝＝＝ゲームエンド＝＝＝＝＝＝＝＝")
print("time",t, "sec")
print("hit",hit,"✖️ bouns",bouns)
print("score",hit*bouns)