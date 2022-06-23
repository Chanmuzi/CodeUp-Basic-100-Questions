a = int(input())
b = 0
while b < a:
    for i in range(1,a+1):
        b += i
        if b >= a: break
    print(i)
