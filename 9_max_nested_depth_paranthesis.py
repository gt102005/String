class Stack(object):
    def __init__(self):
        self.sizee=100
        self.arr=[0]*self.sizee
        self.head=-1
    def push(self,data):
        if self.head>self.sizee-1:
            return "stack overflow"
        self.head+=1
        self.arr[self.head]=data
    def pop(self):
        output=self.arr[self.head]
        self.head-=1
        return output
    def top(self):
        return self.arr[self.head]
    def empty(self):
        if self.head==-1:
            return True
        else:
            return False

class Solution(object):
    def maxDepth(self,s):
        stack=Stack()
        output=0
        for i in range(len(s)):
            temp=0
            if s[i]=='(':
                stack.push(s[i])
            else:
                x=i
                while s[x]==")" and stack.top()=="(" and x<len(s)-1:
                    stack.pop()
                    temp+=1
                    x+=1
            output=max(output,temp)
        return output

s="()(())((()()))()(((((((())))))))"
sol=Solution()
output=sol.maxDepth(s)
print(output)
