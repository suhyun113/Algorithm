def solution(diffs, times, limit):
    n = len(diffs) # 퍼즐의 개수
    
    # 주어진 숙련도 level로 퍼즐 풀 수 있는지 판단
    def is_possible(level):
        total_time = 0
        for i in range(n):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1] if i > 0 else 0
            
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += (time_cur + time_prev) * mistakes + time_cur
                
            if total_time > limit:
                return False # 제한 시간 초과
        return True # 제한 시간 내에 완료 가능
    
    # 이분 탐색
    left = 1
    right = max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            # 주어진 level로 가능하다면,
            answer = mid
            # 가능하면서 최솟값 찾기
            right = mid - 1
        else:
            # 주어진 level로 불가능 -> 더 큰 값
            left = mid + 1
    return answer
            
            