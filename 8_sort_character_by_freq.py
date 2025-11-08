class Solution(object):
    def frequencySort(self, s):
        temp={}
        output=''
        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]]=1
            else:
                temp[s[i]]+=1
        for i in range(len(temp)):
            temp_max_key=''
            temp_max_val=-1
            for i,j in temp.items():
                if j>temp_max_val:
                    temp_max_key=i
                    temp_max_val=j
            output+=temp_max_key*temp_max_val
            temp[temp_max_key]=-1
        return output

                        
        
      
s="tree"
sol=Solution()
output=sol.frequencySort(s)
print(output)

