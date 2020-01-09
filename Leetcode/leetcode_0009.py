from math import log
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        lg=int(log(x, 10))+1
        split = lg//2-1
        left = x//10**(split+ 1+ (0 if lg%2 == 0 else 1))
        right = x%10**(split+1)
        while split>=0:
            if left//10**split != right%10:
                return False
            split, left, right = split-1, left%10**split, right//10
        return True

print(Solution().isPalindrome(1))