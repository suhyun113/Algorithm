def solution(bandage, health, attacks):
    t, x, y = bandage
    cur_health = health # 현재 체력
    combo = 0 # 연속 성공 시간
    
    # 공격 정보
    attack_map = {time: damage for time, damage in attacks}
    
    # 생존 시간
    total_time = attacks[-1][0] # 마지막 공격 시간
    
    for time in range(1, total_time + 1):
        if time in attack_map:
            # 공격을 당한 경우
            cur_health -= attack_map[time]
            if cur_health <= 0:
                return -1 # 죽음
            combo = 0 # 연속 성공 시간 초기화
        else:
            # 공격을 당하지 않은 경우
            cur_health += x
            combo += 1
            
            if combo == t:
                cur_health += y
                combo = 0 # 연속 성공 시간 초기화
                
            if cur_health > health:
                cur_health = health
    
    return cur_health