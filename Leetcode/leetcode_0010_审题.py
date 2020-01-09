"""
题目
给定一个字符串 s 和一个字符规律 p，实现支持 '.' 和 '*' 的正则表达式匹配

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。


分析
字符串匹配 - 动态规划

dp表结构
1. 当前p字符iP
2. 当前s字符iS

最优解结构
* 解 => dp[len(p)][] = 1

状态转移方程
dp[iP][iS]=
* p[iP] != * (. included)
    1. 0 if dp[iP-1][iS-1]==0
    2. 1 if p[iP]=='.'
    3. 1 if p[iP]==s[iS]
* p[iP] == *
`   1. 1 if p[iP-1]==s[iS] else 0

初始状态
设定第一行
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return True
        if not s: return False

        dp = [[s[i]==p[0] or p[0] == '.' for i in range(len(s))]]
        for iP in range(1,len(p)):
            dp.append([p[iP]=='*' and dp[iP-1][0]])
            for iS in range(1,len(s)):
                if p[iP] != '*':
                    dp[iP].append((p[iP]=='.' or p[iP]==s[iS]) and dp[iP-1][iS-1])
                else:
                    dp[iP].append(p[iP-1]==s[iS] and dp[iP-1][iS])
        return True in dp[-1]

print(Solution().isMatch('aab','c*a*b'))
