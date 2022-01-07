def programmerStrings(s):
    find_str = 'programmer'

    left_str = list(find_str)
    end_idx = 0

    for i in range(len(s)):
        if s[i] in left_str:
            left_str.pop(left_str.index(s[i]))
        if len(left_str) == 0:
            end_idx = i - 1
            break

    right_str = list(find_str)
    start_idx = 0

    for i in range(len(s) - 1, end_idx, -1):
        if s[i] in right_str:
            right_str.pop(right_str.index(s[i]))
        if len(right_str) == 0:
            start_idx = i
            break

    ans = start_idx - end_idx - 1

    return ans


print(programmerStrings('progxrammerrxproxgrammer'))
print(programmerStrings('hrhnbvyqlrsifkexomujijwuvaewaxkfljspxuiwspzleqbojulhxmxtunjmezmssjqovfmqnazmfdpawcuwdclpijjnvrkyljemydhyqczxjeybfcvolgfjgqnoneauxdidtprqjxvthfezmzrtvbwhzzzegwnwgwhhyttegaveamctinynnutuywrviiuzptfoqweulybzlwafmvkrniukrlakujregjmkmgrhyakinnuwtphqhxgshvbmisqtizuzyklctfsrisxwqcgrvljyenmjowrinryuyfwvksewtvxbldgwriaqbcdcvyirhczjdbhxrjjotayexlpexnbmglftzgkvjdvtxfmfuhoihbkfmfscwzmqjdbrpyvmhxkatzxplobjwdqukcnycmgebaibyyhihkimlqytrhgwxlehfplvxyzgjmjrrswnfwnnuopjzrdoarzfgbbaaeyzztqkvuzoxndgsczvaikaauqwfgbzhtaztuuxqjpptfrtfmhtihnyzcqvgffblsrnvyzbukiyftdkrhdacfddiodeximwftcwgblribvswsbpktntuewscylczrngqylbqvzrhzfjikpjcbzzxfmqzngtpvtwvhsdcsewmddwspqjasujxsfpwwgikablcitbwfizjjjuposnuvabsovcvnelwantesolvcdnwpdmnslesxlyrglexxbwsozupjeifeyfutqouzxjiafilwafubsftqgwcnhafivpasxvdgzyrrmyzgwylmqkrbhvynsgotraaipwxlkfhccxcvxthlthwoufdhnlmbtdlweneiuourfplbmkujwtconzxpiiydrncgcbapbvbedpomyetyxxfplrctilrcxukjnrbafqrbyknummakvvurtklsryflkwazkteokhpoidpqgeecdunajgmqagaxcfyyjvfdgmseblkhdfgtwzeocirmnkcvwlspjzqxlxwjwltxdaseypuoatniwqrknpfzizx'))
print(programmerStrings('programmerprogrammer'))
