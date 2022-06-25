n = int(input())
a = input().split()

d = []  # 공백 리스트 생성
for i in a:
    i = int(i)
    d.append(i) # 입력 받은 값들을 공백 리스트에 추가

d.reverse() # 리스트 뒤집기
for i in d:
    print(i,end=" ")
