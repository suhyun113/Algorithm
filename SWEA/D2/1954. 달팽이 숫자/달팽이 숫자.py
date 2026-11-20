T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    r, c, d = 0, 0, 0
    for num in range(1, N * N + 1):
        arr[r][c] = num
        
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 만약 칸이 밖이거나 이미 채워져 있다면 방향 바꾸기
        if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] != 0:
            d = (d + 1) % 4 # 더 작을때는 자기자신 반환
            nr = r + dr[d]
            nc = c + dc[d] 
        r, c = nr, nc # 조건 만족하면 이동 가능
        
    print(f'#{test_case}')
    for row in arr:
        print(*row)
            