class Solution(object):
    def longestCommonPrefix(self, strs):
        output=""
        if len(strs)<1:
            return output
        length_of_min=len(min(strs))
        i=0
        while i<length_of_min:
            is_true=False
            x=0
            while x<len(strs):
                if strs[x][i]==strs[0][i] and strs[x][i]:
                    is_true=True
                    x+=1
                else:
                    return output
            if is_true:
                output+=strs[0][i]
            i+=1
        return output
strs =  ["dog","racecar","car"]
sol=Solution()
output=sol.longestCommonPrefix(strs)
print(output)

        