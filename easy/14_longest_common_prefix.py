

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ''
        word = strs[0]
        for i in range(1, len(word)+1):
            counter = 1
            for j in range(1, len(strs)):
                if word[0:i] != strs[j][0:i]:
                    counter = 0
            if counter == 1:
                common_prefix = word[0:i]
            else:
                break
        # * невнимательно прочитал задание и искал префикс сдвигающимся 
        # * слайсом по всей длине слова, а не только в его начале
        # common_prefix = ''
        # min_len_string = ''
        # for i in range(0, len(strs)):
        #     if len(strs[i]) < len(min_len_string) or min_len_string == '':
        #         min_len_string = strs[i]
        # for i in range(0, len(min_len_string)):
        #     for j in range(len(min_len_string), i, -1):
        #         counter = 1
        #         for x in range(len(strs)):
        #             if min_len_string[i:j] not in strs[x]:
        #                 counter = 0
        #         if counter == 1 and len(min_len_string[i:j]) > len(common_prefix):
        #             common_prefix = min_len_string[i:j]
        return common_prefix
        