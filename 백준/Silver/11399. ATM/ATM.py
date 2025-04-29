p = int(input()) # ATM에 줄을 선 사람 수
pi = list(map(int, input().split())) # 각 순서의 사람들이 돈을 인출하는데 걸리는 시간

pi.sort() # 돈을 인출하는데 걸리는 시간이 적은 순으로 정렬

min = 0
sum_min = 0

for i in range(p): 
    min += pi[i]
    sum_min += min

print(sum_min)
