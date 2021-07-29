#https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longestSubstring(s):
    start=maxlength =0
    used_char={}
    for i,val in enumerate(s):
        if val in used_char and start <= used_char[val]:
            start=used_char[val]+1
        else:
            maxlength=max(maxlength,i-start+1)

        used_char[val]=i
        ret_string=s[start:i+1]
    return maxlength,ret_string

print(longestSubstring('acab'))



