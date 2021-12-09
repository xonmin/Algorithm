def solution(record):
    answer = []
    user_name = {}
    act_list = []
    transform_eng = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    for info in record:
        info_split = info.split()
        if info_split[0] == "Leave":
            act, id = info_split[0], info_split[1]
            act_list.append([id, act])
        elif info_split[0] == "Enter":
            act, id, nickname = info_split[0], info_split[1], info_split[2]
            user_name[id] = nickname
            act_list.append([id, act])
        if info_split[0] == 'Change':
            id, nickname = info_split[1], info_split[2]
            user_name[id] = nickname

    for id, act in act_list:
        answer.append("".join([user_name.get(id), "님이 ", transform_eng.get(act)]))

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
