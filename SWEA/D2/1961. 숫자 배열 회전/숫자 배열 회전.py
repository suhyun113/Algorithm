# 90도로 시계방향 회전한 새 배열 만들기 함수
def rotate(arr, N):
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[i][j] = arr[N - 1 - j][i]
    return new

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    rotate90 = rotate(arr, N)
    rotate180 = rotate(rotate90, N)
    rotate270 = rotate(rotate180, N)
    
    print(f'#{test_case}')
    for i in range(N):
        a = ''.join(map(str, rotate90[i]))
        b = ''.join(map(str, rotate180[i]))
        c = ''.join(map(str, rotate270[i]))        
        print(a, b, c)
        