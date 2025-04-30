from os import remove

N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
S = 0

A.sort() # 오름차순 재배열
B_sorted = sorted(B, reverse=True) # 내림차순으로 재배열한 B

for i in range(N):
    S += A[i] * B_sorted[i]

print(S)