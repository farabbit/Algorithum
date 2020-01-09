class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 1
        # 先前值
        pre = 1
        # 递减长度
        des_num = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if des_num > 0:
                    # 求和公式
                    res += ((1 + des_num) * des_num) // 2
                    # 递减长度比先前值大,所以我们要把先前值补充
                    if pre <= des_num: res += (des_num - pre + 1)
                    pre = 1
                    des_num = 0
                if ratings[i] == ratings[i - 1]:
                    pre = 1
                else:
                    pre += 1
                res += pre
            else:
                des_num += 1
        # print(des_num)
        if des_num > 0:
            res += ((1 + des_num) * des_num) // 2
            if pre <= des_num: res += (des_num - pre + 1)
        return res

print(Solution().candy([1,2,3,4,2,1,4,1]))