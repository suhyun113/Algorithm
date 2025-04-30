N = int(input())
rope_W = [int(input()) for __ in range(N)] # 각 로프가 버틸 수 있는 최대 중량
W = 0
min_W = 0 # 각 경우에서 최솟값(기준)
max_W = 0 # 들어올릴 수 있는 물체의 최대 중량

rope_W.sort(reverse=True) # 내림차순으로 정렬(30, 20, 10)
for i in range(N):
    min_W = rope_W[i]
    W = min_W * (i + 1) # 로프 개수만큼 곱함
    max_W = max(W, max_W)
print(max_W)