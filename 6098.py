a = [[] for _ in range(10)]   # 공백 리스트로 구성된 리스트 a 생성

for i in range(10):
      b = input().split()
      for j in range(10):
            a[i].append(int(b[j]))  # 입력받은 값들로 리스트 a 채우기
            
a[1][1] = 9 # 시작점은 항상 (2,2)

x = int(1)
y = int(1)  # (2,2) 좌표를 인덱스로 접근할 수 있도록 행,열 인덱스를 1로 설정

while True:
      if a[x][y+1] == 0:      # 오른쪽 칸이 0이라면
            a[x][y+1] = int(9)
            y += 1            # 무조건 오른쪽으로 이동한다
      elif a[x][y+1] == 1:    # 오른쪽 칸이 1일 때
            if a[x+1][y] == 0:      # 아래쪽 칸이 0이라면
                  a[x+1][y] = int(9)
                  x += 1            # 아래로 이동한다
            elif a[x+1][y] == 1: break#아래쪽 칸이 1이라면 끝낸다
            else: # 아래쪽 칸이 2라면
                  a[x+1][y] = int(9)
                  break
      else: # 오른쪽 칸이 2라면
            a[x][y+1] = int(9)
            break      

for m in range(10):
      for n in range(10):
            print(a[m][n],end=' ')  # 모든 리스트 요소 출력 및 띄어쓰기
      print()     # 줄바꿈
