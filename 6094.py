n = int(input())
k = input().split()

d = []  # 공백 리스트 생성
for i in k:
    i = int(i)
    d.append(i) # 입력 받은 값들을 공백 리스트에 추가

print(min(d))
