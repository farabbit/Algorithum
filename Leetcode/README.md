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

* [ ] recursive
* [ ] 流程式

Python
None, 0对象与符号if, and, or
* None与0对象都是False -> 如vector(0,0,0)
* 多个值中，若同时有None与0对象，不便判断，可以使None变为0对象
* or与and 返回值为**使其停止**的值, 可用于获取此特殊值 （同时也符合boolean值）
  * 若全符合条件，返回最后一个值；若有不符合条件的，返回第一个不符合条件的值
* 例：确定a, b, c中有且只有一个不为None(或0对象)，使其.val值自增1
  * (a and b and c).val += 1

### leetcode_0003
无重复最长字串

**滑动窗口算法（Sliding Window）**：在循环中，使用两个变量记录窗口的边界
* 使用边界变量访问边界值，监控进出窗口的值
* 使用字典/数组/集合记录窗口内的内容（无序）

### [leetcode_0011](leetcode_0011.py) *REDO*
盛水最多的容器

* 首尾双指针 -> 获取最值时，若能够处理好外部点与内部点之间的关系，可使用首尾双指针

### [leetcode_0013](leetcode_0013.py)
罗马数字转整数

python
* 简单的循环叠加可以用```return sum(i*2 for i in range(i))```代替

### leetcode_0690
员工的重要性

树搜索

广度优先 比 深度优先 速度快：没有回溯步骤
深度优先 比 广度优先 内存小：不用保存整个树
Python
* 字典推导：{e.i:e for e in employees}
* 队列：
  * q=queue.Queue()
  * q.put(), q.get()
  * q.isEmpty()

### leetcode_0100
相同的树-树遍历

深度优先范式-递归
```python
def DFS(t):
    if reachExit: return
    return DFS(t.left) and DFS(t.mid) and DFS(t.right)
```

广度优先范式-队列
```python
def BFS(t):
    import queue
    q = queue.Queue()
    result = 0
    q.put(t)
        while not t.empty():
            if reachExit: return # or continue
            result ++
            q.put(t.left)
            q.put(t.mid)
            q.put(t.right)
        return result
```

### leetcode_0310 *REDO*
最小高度树 -> 树的重心

[leetcode_0310.py](./leetcode_0310.py)

树形图：从外向内剥洋葱，逐次去掉度为1的节点

python
* set
  * ```setDict = collections.defaultdict(set)``` - 默认set字典，省去set初始化，可以直接```setDict[i] |= {t}```
  * ```setA |= {t}, setA -= {t}```
  * ```setA.pop()```随机取值

### leetcode_0671 *REDO*
二叉树中第二小的节点

[leetcode_0671.py](./leetcode_0671.py)

* 多重情况分支时，使用多个简单的if，往往比把情况叠加更简洁
* 可以不那么急着返回值

### [leetcode_0273](./leetcode_0273.py) *REDO 好好看好好学*

python
1. enumerate(iterable, start)
  * example: enumerate('abcd', 2): (2, 'a'), (3, 'b'), (4, 'c'), (5, 'd')
2. ```a[-1:0]= '', [] or ()```
3. 从字符串中去掉空格' '：.split(), 加上空格：' '.join()

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            if num < 20:
                return to19[num - 1:num] # a[-1:0] = '' <-> -1~0 not exist
            if num < 100:
                return [tens[num // 10 - 2]] + helper(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ["Hundred"] + helper(num % 100)
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):
                if num < 1000 ** (p + 1):
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        return " ".join(helper(num)) or "Zero"
```

### [leetcode_1282](./leetcode_1282.py) *REDO 好好看好好学*

python
* 循环：在函数体构造数据结构
* 列表推导：在返回值解包数据结构
* dd = collectionl.defaultdict(list) -> ```dd[i].append()```

```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        resultDic = collections.defaultdict(list)
        for i,size in enumerate(groupSizes):
            resultDic[size].append(i)
        return [lst[i:i+size] for size, lst in resultDic.items() for i in range(0,len(lst),size)]
```
