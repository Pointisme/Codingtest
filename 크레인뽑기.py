def solution(board, moves):
    delta = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                delta.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(delta) > 1:
                    if delta[-1] == delta[-2]:
                        delta.pop(-1)
                        delta.pop(-1)
                        answer += 2
                break
    return answer