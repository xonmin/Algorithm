def solution(n, words):
    answer = []

    al_word = [words[0]]
    for i in range(1,len(words)):

        if words[i] in al_word:
            return [(i % n) + 1, (i // n)+1 ]
        elif words[i][0] != al_word[-1][-1]:

            return [(i % n) + 1, (i // n)+1]
        else:
            al_word.append(words[i])

    return [0,0]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
