a,b,c = input().split()
d = [int(a),int(b),int(c)]
for i in d:
    if i % 2 == 0:
        print('even')
    else: print('odd')
