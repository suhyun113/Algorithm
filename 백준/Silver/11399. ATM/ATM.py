N = int(input())
P = list(map(int, input().split()))

# 오름차순 정렬일 때 최솟값
P.sort()

result = 0
min_result = 0

for i in range(N):
    result += P[i]
    min_result += result

print(min_result)
