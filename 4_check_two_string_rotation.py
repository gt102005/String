class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal) or len(s)==0:
            return False
        return goal in s+s

s = "abcde"
goal = "cdeab"
sol=Solution()
output=sol.rotateString(s,goal)
print(output)