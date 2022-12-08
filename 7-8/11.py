s = list(map(str, input().split()))
m = len(s)
if m > 10:
    print(s[0:5])
else:
    v = 12 - m
    b = 'o'
    for i in range(v):
        s.append(b)
    print(''.join(s))
