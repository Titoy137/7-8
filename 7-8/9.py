s = str(input())
m = str(input())
z = 0
n = len(s)
v = len(m)
x = (max(n, v) - min(n, v))
while z <= x:
    if n > v:
        print(s)
    if v > n:
        print(m)
    z += 1
