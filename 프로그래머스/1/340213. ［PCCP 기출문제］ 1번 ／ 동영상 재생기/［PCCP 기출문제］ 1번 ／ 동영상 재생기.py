def solution(video_len, pos, op_start, op_end, commands):
    # 문자열 시간 "mm:ss"를 초 단위로 변경
    def time_to_sec(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    
    # 초 단위를 문자열 시간 "mm:ss"로 변경(출력 위함)
    def sec_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
    
    video_len_sec = time_to_sec(video_len)
    cur_pos = time_to_sec(pos)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)
    
    # 오프닝 건너뛰기
    if (op_start_sec <= cur_pos <= op_end_sec):
        cur_pos = op_end_sec
        
    # 명령어 처리
    for command in commands:
        if (command == "prev"):
            cur_pos = max(0, cur_pos - 10)
        elif (command == "next"):
            cur_pos = min(video_len_sec, cur_pos + 10)
            
        # 이동 후 오프닝 범위면 건너뛰기
        if op_start_sec <= cur_pos < op_end_sec:
            cur_pos = op_end_sec
            
    return sec_to_time(cur_pos)