def largestMagical(binString):
    # 1의 수는 반드시 0의 수보다 적지않아야함
    # subsequence 1과 0의 수는 같아야함
    ans = ""

    def chk(string):
        if string == '':
            return True
        zero = 0
        one = 0
        for s in string:
            if s == '1':
                one += 1
            elif s == '0':
                zero += 1
            if zero > one:
                return False
        else:
            if zero == one:
                return True

            return False

    ans = ''
    for i in range(len(binString) - 1):
        for j in range(i + 1, len(binString)):
            if chk(binString[i:j]):
                if chk(binString[:i] + binString[j:]):
                    # print("경우의 수 ")
                    # print(binString[i:j]+binString[:i] + binString[j:])
                    # print(binString[:i] + binString[j:]+ binString[i:j])
                    # print(binString[:i]+ binString[i:j]+ binString[j:])
                    ans = max(ans, binString[i:j] + binString[:i] + binString[j:])
                    ans = max(ans, binString[:i] + binString[j:] + binString[i:j])
                    ans = max(ans, binString[:i] + binString[i:j] + binString[j:])

    return ans


print(largestMagical('1101001100'))
print(largestMagical('11011000'))
