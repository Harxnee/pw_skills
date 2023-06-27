n=int(input())
l = []
for i in range(n):
    l.append(int(input()))
x = l.count(0)
for i in range(x):
    l.remove(0)

for i in range(x):
    l.append(0)



print(l)