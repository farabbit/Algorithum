# Leetcode

## 题目

### [leetcode_0001](./leetcode_0001.py)
两数之和

* 哈希表优化搜索速度 O(n)-> O(1) - 消耗内存，换取速度
* Python: 使用字典模拟哈希表

### [leetcode_0015](./leetcode_0015.py)
三数之和

对于无序输入，且与值大小有关的题，可考虑排序后处理

python
* ```a[len(a)-1:len(a)]``` 替代 ```a[-1]``` 可避免index out of range
* ```__hash__与__eq__```使用hash(id(self))计算哈希值，或判断相等性
  ```python
  def __hash__(self):
    return hash(id(self))

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return hash(id(self))==hash(id(other))
    else:
      return False
  ```
* practice: UnorderedTuple
```python
class UnorderedTuple(tuple):
  def __hash__(self):
      return super().__hash__(tuple(sorted(self)))

  def __eq__(self, other):
      if isinstance(other, self.__class__):
          return self.__hash__()==other.__hash__()
      else:
          return False
```

### [leetcode_0002](./leetcode_0002.py)
两数相加 - 倒序链表

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

### [leetcode_0003](leetcode_0003.py)
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

### [leetcode_0690](leetcode_0690.py)
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

### [leetcode_0100](leetcode_0100.py)
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

### [leetcode_0310](./leetcode_0310.py) *REDO*
最小高度树 -> 树的重心

树形图：从外向内剥洋葱，逐次去掉度为1的节点

python
* set
  * ```setDict = collections.defaultdict(set)``` - 默认set字典，省去set初始化，可以直接```setDict[i] |= {t}```
  * ```setA |= {t}, setA -= {t}```
  * ```setA.pop()```随机取值

### [leetcode_0671](./leetcode_0671.py) *REDO*
二叉树中第二小的节点

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

### leetcode 202 快乐树 [Happy Number](https://leetcode-cn.com/problems/happy-number/) *REDO*

[leetcode_0202.py](./leetcode_1282.py)

尾递归
* 尾递归从最后开始计算, 每递归一次就算出相应的结果, 也就是说, 函数调用出现在调用者函数的尾部, 因为是尾部, 所以**没有必要去保存任何局部变量**. 直接让被调用的函数返回时越过调用者。尾递归**把当前的运算结果（或路径）放在参数里传给下层函数**，深层函数所面对的不是越来越简单的问题，而是越来越复杂的问题，因为参数里带有前面若干步的运算路径。

快慢指针
* 可以用于发现循环

python
* 循环内外都返回值bool时，可以分析条件判断结果，合并返回值

```python
def v2(n):
    history = {1}
    while n not in history:
        summ = sum(int(i)**2 for i in (str(n)))
        history.add(n)
        n=summ
    return n==1
```

### leetcode 258 [Add Digits](https://leetcode-cn.com/problems/add-digits/comments/)
各位相加
> 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

时间复杂度O(1) => 有公式解

python
* tail recursion
```python
def addDigits(num: int) -> int:
    return addDigits(sum(int(i) for i in str(num))) if num > 9 else num
```
