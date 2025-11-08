class Solution(object):
    def reverseWords(self, s):
        output=""
        l=s.split()
        for i in range(len(l)-1,-1,-1):
            if i==0:
                output+=l[i]
            else:
                output+=l[i]+" "  
        return output

s1="  hello world  "
s2="a good   example"
sol=Solution()
output=sol.reverseWords(s2)
print(output)
print(len(output))

