#モンテカルロ法で円周率
import numpy as np

times = 10000000

x = 0.0
y = 0.0
pi = 0.0
count = 0


#  点をばらまく
for i in range(1, times):
    x = np.random.rand()
    y = np.random.rand()
    
    # 点が円の中に入っているか
    if(x**2 + y**2 < 1.0):
        count += 1

# 円の中に入っている点の割合から円周率計算
pi = 4.0 * count / times
print(pi)
