m_num = int(input())

measures = []

inputs = input()

for i in range(m_num):
    measures.append(int(inputs.split()[i]))

measures.sort(reverse=True)
ans = measures[0] * measures[-1]

print(ans)