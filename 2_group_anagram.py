class Solution(object):
    def fun(self,a,b):
        a=list(a)
        b=list(b)
        for i in b:
            if i in a:
                pass
            else:
                return False
        return True

    def groupAnagrams(self, strs):
        output=[]
        for i in range(len(strs)):
            temp=[strs[i]]
            for j in range(len(strs)):
                if self.fun(strs[j],strs[i]) and j!=i:
                    temp.append(strs[j])
            output.append(temp)
        return output



input=['eat', 'tea', 'ate','tan', 'nat', 'bat']
obj=Solution()
print(obj.groupAnagrams(input))
