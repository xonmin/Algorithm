num_dict = {}


def init():
    num_dict['zero'] = '0'
    num_dict['one'] = '1'
    num_dict['two'] = '2'
    num_dict['three'] = '3'
    num_dict['four'] = '4'
    num_dict['five'] = '5'
    num_dict['six'] = '6'
    num_dict['seven'] = '7'
    num_dict['eight'] = '8'
    num_dict['nine'] = '9'


def solution(s):
    init()
    answer = []
    word = ''
    for i in s:
        if word in num_dict.keys():
            answer.append(num_dict[word])
            word = ''
        if i not in string.digits:
            word += i
        else:
            answer.append(i)

    if word != '':
        answer.append(num_dict[word])
    return int(''.join(answer))
