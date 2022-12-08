s = list(map(int, input(). split()))
m = len(s)
t = 1
if m >= 6:
    print(s[0],s[1],s[2],s[-3],s[-2],s[-1])
else:
    for t in range(m):
        print(s[0])
        t += 1
