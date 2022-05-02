J = ['a','b','d']
S = ['a','a','b','c','c','d','f','d']

J = input()
S = input()

N = len(J)
M = len(S)
count = 0
for i in range(N):
	for y in range(M):
		if J[i]==S[y]:
			count += 1
print(count)