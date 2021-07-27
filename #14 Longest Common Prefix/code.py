class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = 200
        for i in strs:
            if len(i) < min_str:
                min_str = len(i)
        otpt = ''
        for i in range(min_str):
            temp_letter = strs[0][i]
            temp_iterator_list = []
            for str_iter in strs:
                temp_iterator_list.append(str_iter[i])
            if all(j == temp_letter for j in temp_iterator_list):
                otpt = otpt + temp_letter
            else:
                break
        return(otpt)