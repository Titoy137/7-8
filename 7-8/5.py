s = str(input())
x = 0
while x <= len(s):
    if s[-1] == s[x]:
        print(x)
    x += 1
