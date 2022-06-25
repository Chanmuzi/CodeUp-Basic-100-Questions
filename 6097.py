h,w = input().split() # h는 세로, w는 가로
h = int(h)
w = int(w)

crossList = []
for i in range(h):
      crossList.append([])    
      for j in range(w):
            crossList[i].append(int(0))   # 가로, 세로 개수를 곱한 격자판 생성

n = int(input()) # 막대의 개수
for i in range(n):
      l,d,x,y = input().split() # 막대의 길이, 방향, 좌표
      l = int(l)
      d = int(d)
      x = int(x)
      y = int(y)
      
      if d == 0: # 가로
            for k in range(l):
                  crossList[x-1][y-1+k] = 1     # l의 값만큼 가로에 있는 칸을 1로 바꿔준다
      else:       #세로
            for k in range(l):
                  crossList[x-1+k][y-1] = 1     # l의 값만큼 세로에 있는 칸을 1로 바꿔준다

for m in range(h):
      for n in range(w):
            print(crossList[m][n],end=' ')
      print()     # 줄바꿈
