# Brute approach O(n^2) time complexity
def rotate(s,k):
    output=''
    temp=k%len(s)
    l=len(s)-temp
    for i in range(len(s)):
        if i>=l:
            output+=s[i]
    for i in range(l):
        output+=s[i]
    return output
s='abcde'
k=7
output=rotate(s,k)
print(output)


# optimal way O(n) time complexity
def rotate(s, k):
    k = k % len(s)            
    return s[len(s)-k:] + s[:len(s)-k]    
s = "abcde"
k = 7
print(rotate(s, k))  
