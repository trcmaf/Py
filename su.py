import numpy as np

n = 10
all = [list(map(int, input().split())) for row in range(n)]
print(*all, sep='\n')
sum1 = 0

for i in range(all[0]):
    sum1 += all[i]
    if all[i] == 1:
