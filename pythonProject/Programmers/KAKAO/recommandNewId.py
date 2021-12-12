import string


def include(x, filter):
    return x in filter


def solution(new_id):
    special_char = ['-', '_', '.']
    filtering = list(string.ascii_lowercase) + list(string.digits) + special_char

    new_id = str.lower(new_id)

    new_id = "".join([x for x in new_id if include(x, filtering)])

    # new_id = new_id.filter(list(string.ascii_lowercase) + list(string.digits) + special_char)
    new_id += 's'
    for i, c in enumerate(new_id):
        if i <= len(new_id) - 1:
            while new_id[i] == '.' and new_id[i + 1] == '.':
                new_id = new_id[:i] + new_id[i + 1:]
    new_id = new_id[:-1]
    if new_id.startswith('.'):
        new_id = new_id[1:]

    if new_id.endswith('.'):
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[0:15]

    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = new_id + new_id[-1]

    return new_id


print(solution("....!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
