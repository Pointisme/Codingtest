def solution(record):
    actions=[]
    DB=dict()
    answer = []
    
    for i in record:
        info = i.split()
        action, userid = info[0],info[1]
        if action in ("Enter","Change"):
            name=info[2]
            DB[userid]=name
        actions.append((action,userid))

        for j in actions:
            action,userid = j[0],j[1]
            if action == 'Enter':
                answer.append(f'{DB[userid]}님이 들어왔습니다.')
            elif action == 'Leave':
                answer.append(f'{DB[userid]}님이 나갔습니다.')
    return answer

    