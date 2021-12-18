def getTheGroups(n, queryType, students1, students2):
    friends = set()
    rest = set()
    for i, q in enumerate(queryType):
        if q == 'Total':
            break
        s1, s2 = students1.pop(i), students2.pop(i)
        friends.add(s1)
        friends.add(s2)

    for s in students1:
        if s not in friends:
            rest.add(s)
    for s in students2:
        if s not in friends:
            rest.add(s)

    f_num = len(friends)
    r_num = len(rest)

    return f_num + r_num


print(getTheGroups(2, ['Total'], [1], [2]))
print(getTheGroups(3, ['Friend', 'Total'], [1, 2], [2, 3]))
print(getTheGroups(4, ['Friend','Friend', 'Total'], [1, 2,1], [2, 3,4]))