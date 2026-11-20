T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 A가 짧은 쪽이 되도록 맞추기
    if N > M:
        A, B = B, A
        N, M = M, N

    answer = -float('inf')
    for start in range(M - N + 1):
        total = 0
        for i in range(N):
            total += A[i] * B[start + i]
        answer = max(answer, total)

    print(f'#{test_case} {answer}')