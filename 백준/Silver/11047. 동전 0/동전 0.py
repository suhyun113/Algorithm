N, K = map(int, input().split())
A = [int(input()) for __ in range(N)] # 동전의 가치
count = 0 # 동전 개수

A.sort(reverse=True)

# K원 만드는데 필요한 동전 개수의 최솟값
# 동전의 종류는 N
for coin in A:

    count += K // coin
    K %= coin

print(count)
