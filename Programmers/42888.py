'''
오픈채팅방 
'''

def solution(record):
    answer = []
    user_info = {}

    for msg in record:
        msg_info = msg.split()
        # leave인 경우는 제외하고 가장 최근 이름 저장
        if len(msg_info) == 3:
            method, id, name = msg_info
            user_info[id] = name

    for msg in record:
        msg_info = msg.split()
        if msg_info[0] == "Enter":
            answer.append(user_info[msg_info[1]] + "님이 들어왔습니다.")
        elif msg_info[0] == "Leave":
            answer.append(user_info[msg_info[1]] + "님이 나갔습니다.")

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))