s=input()
x='.'
for i in s:
    if list(s).count(i)==1:
        x = i
        break

if x!='.':
    print(s.find(x))
else:
    print(-1)