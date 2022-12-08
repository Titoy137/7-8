s = str(input())
if s[0:3] == 'abc':
    s=s.replace('abc', 'www')
    print(s)
else:
    print(s, 'zzz')
