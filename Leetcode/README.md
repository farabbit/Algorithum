# Leetcode

## 题目

### leetcode_0001
两数之和

[leetcode_0001.py](./leetcode_0001.py)

* 哈希表优化搜索速度 O(n)-> O(1) - 消耗内存，换取速度
* Python: 使用字典模拟哈希表

### leetcode_0002
两数相加 - 倒序链表

[leetcode_0002.py](./leetcode_0002.py)

None, 0对象与符号if, and, or
* None与0对象都是False -> 如vector(0,0,0)
* 多个值中，若同时有None与0对象，不便判断，可以使None变为0对象
* or与and 返回值为**使其停止**的值, 可用于获取此特殊值 （同时也符合boolean值）
  * 若全符合条件，返回最后一个值；若有不符合条件的，返回第一个不符合条件的值
* 例：确定a, b, c中有且只有一个不为None(或0对象)，使其.val值自增1
  * (a and b and c).val += 1
