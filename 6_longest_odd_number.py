class Solution(object):
        def largestOddNumber(self, num):
            num_len=len(num)
            str_to_num=int(num)
            while str_to_num:
                if str_to_num%2!=0:
                    return str_to_num
                else:
                    str_to_num=str_to_num//10
            return ''


num = "52"
sol=Solution()
output=sol.largestOddNumber(num)
print(output)