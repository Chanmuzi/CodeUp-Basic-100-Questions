n = int(input())
result = 0
for x in range(1,n+1):
    if result < n:
        result += x
    else: break
print(result)
