h,b,c,s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
volume = h*b*c*s/8/1024/1024
v = round(volume,1)
print(v,"MB")
