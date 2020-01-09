"""longest substring without repeating"""

def maxSubString(s):
    maxLen = start = 0
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            if start <= dic[s[i]]:
                start = dic[s[i]]+1
            else:
                dic[s[i]] = i
                maxLen = max(maxLen, dic[s[i]]-start+1)
        else:
            dic[s[i]] = i
            maxLen = max(maxLen, dic[s[i]]-start+1)
    return maxLen
