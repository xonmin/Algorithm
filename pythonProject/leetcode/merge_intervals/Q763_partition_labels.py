from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        letter_dict = {}
        for i in range(len(s)):
            letter_dict[s[i]] = [i, i] if s[i] not in letter_dict else [min(letter_dict[s[i]][0], i),
                                                                        max(letter_dict[s[i]][1], i)]

        for k in letter_dict:
            if not answer:
                answer.append(k)
            else:
                insert = False
                for a in answer:
                    if letter_dict[k][0] <= letter_dict[a][1] and letter_dict[k][1] >= letter_dict[a][0]:
                        letter_dict[a][0] = min(letter_dict[k][0], letter_dict[a][0])
                        letter_dict[a][1] = max(letter_dict[k][1], letter_dict[a][1])
                        insert = True
                        break
                if not insert:
                    answer.append(k)

        for i in range(len(answer)):
            answer[i] = letter_dict[answer[i]][1] - letter_dict[answer[i]][0] + 1

        return answer


if __name__ == '__main__':
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
