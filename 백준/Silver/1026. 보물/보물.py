N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0
A.sort() # 오름차순 정렬 0 1 1 1 6
B.sort(reverse=True) # 내림차순 정렬 8 7 3 2 1

# S의 값을 가장 작게 만들고 싶음
for i in range(N):
    S += (A[i] * B[i])
print(S)