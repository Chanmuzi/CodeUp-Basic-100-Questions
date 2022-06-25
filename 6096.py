d = []
for i in range(19):
      d.append([])  # d라는 리스트에 공백 리스트 19개 생성

for i in range(19):
      a = input().split()
      for j in range(19):
            d[i].append(int(a[j]))  # a를 통해 입력받은 값들을 d의 공백 리스트에 각각 하나씩 추가(총 19번)   

n = int(input())
for i in range(n) :
  x, y = input().split()
  x = int(x)
  y = int(y)
  for j in range(19):
        if d[x-1][j] == 1:
              d[x-1][j] = 0
        else: d[x-1][j] = 1 # 입력받은 정수는 인덱스 숫자와 맞추기 위해 1을 빼주어야 한다
  for k in range(19):
        if d[k][y-1] == 1:
              d[k][y-1] = 0
        else: d[k][y-1] = 1

for i in range(19) :
  for j in range(19) : 
    print(d[i][j], end=' ')    # 공백을 두고 한 줄로 출력
  print() # 줄바꿈이 빠지면 오답 처리된다
