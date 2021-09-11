def solution(id_list, report, k):
    answer = []

    ban_count = {i: 0 for i in id_list}
    report_mail = [0 for i in id_list]  # result

    # 중복 제거
    report = set(report)
    report = list(report)

    for repo in report:
        reporter, subject = repo.split()
        if subject in ban_count:  # 리포트에 신고 접수가 있으면
            ban_count[subject] += 1

    for repo in report:
        reporter, subject = repo.split()
        if ban_count.get(subject) >= k:
            idx = id_list.index(reporter)
            report_mail[idx] +=1

    answer = report_mail

    #print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)