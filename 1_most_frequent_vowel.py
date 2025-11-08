class Solution(object):
    def maxFreqSum(self,s):
        vowels={}
        constant={}
        vowels_output=0
        constant_output=0
        vow=['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(s)):
            if s[i] in vow:
                if s[i] in vowels:
                    vowels[s[i]]+=1
                else:
                    vowels[s[i]]=1
            else:
                if s[i] in constant:
                    constant[s[i]]+=1
                else:
                    constant[s[i]]=1
            if s[i] in vowels and vowels[s[i]]>vowels_output:
                vowels_output=vowels[s[i]]
            if s[i] in constant and constant[s[i]]>constant_output:
                constant_output=constant[s[i]]
        return constant_output+vowels_output

stri="aeiaeia"
obj=Solution()
print(obj.maxFreqSum(stri))
