# 1. LeetCode勉強記録（Python_LinkedList編）_Easy

- LeetCodeの勉強記録
    - LinkedListの問題
    - Medium編
- その他詳細・雑感は[solutions[Python].md](https://github.com/kokokocococo555/LeetCodeMemo/blob/master/solutions%5BPython%5D.md)の冒頭参照


<!-- TOC -->

- [1. LeetCode勉強記録（Python_LinkedList編）_Easy](#1-leetcode%E5%8B%89%E5%BC%B7%E8%A8%98%E9%8C%B2pythonlinkedlist%E7%B7%A8easy)
  - [1.1. Medium](#11-medium)
    - [1.1.1. 2. Add Two Numbers](#111-2-add-two-numbers)
    - [1.1.2. ▲19. Remove Nth Node From End of List](#112-%E2%96%B219-remove-nth-node-from-end-of-list)
    - [1.1.3. ▲24. Swap Nodes in Pairs](#113-%E2%96%B224-swap-nodes-in-pairs)
    - [1.1.4. 61. Rotate List](#114-61-rotate-list)
    - [1.1.5. 82. Remove Duplicates from Sorted List II](#115-82-remove-duplicates-from-sorted-list-ii)
    - [86. Partition List](#86-partition-list)

<!-- /TOC -->

## 1.1. Medium

### 1.1.1. [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

- テストケースに引っかかりつつ、バグを修正していくことで回答できた

```python
# 自力実装

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        head = ans
        adv = 0
        while l1 and l2:
            sum_of_dig = l1.val+l2.val+adv
            tmp = sum_of_dig%10
            adv = sum_of_dig//10
            ans.next = ListNode(tmp)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            if l1:
                ll = l1
            elif l2:
                ll = l2
            while ll:
                sum_of_dig = ll.val+adv
                tmp = sum_of_dig%10
                adv = sum_of_dig//10
                ans.next = ListNode(tmp)
                ans = ans.next
                ll = ll.next
        if adv>0:
            ans.next = ListNode(adv)
        return head.next
```

```python
# Solutionを参考にリファクタリング
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        head = ans
        carry = 0
        while l1 or l2:
            if l1:
                x = l1.val
                l1 = l1.next
            elif not l1:
                x = 0
            if l2:
                y = l2.val
                l2 = l2.next
            elif not l2:
                y = 0
            sum_of_dig = x+y+carry
            carry = sum_of_dig//10
            ans.next = ListNode(sum_of_dig%10)
            ans = ans.next
        if carry>0:
            ans.next = ListNode(carry)
        return head.next
```

### 1.1.2. ▲[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

- 最初に一度全リストをスキャンして長さを得る
- その後、改めてリストを辿っていって、指定の位置のノードを飛ばして繋げる
- ▲Solutionでは長さを得るためのスキャンを無しにして、代わりにnの差がある2つのポインタを使用している

```python
# 自力実装

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt = 0
        tmp = head
        while tmp:
            cnt += 1
            tmp = tmp.next
        if cnt==1:
            return None
        ans = head
        ret = ans
        for i in range(cnt-1):
            if i>=cnt-n:
                ans.val = ans.next.val
            if i==cnt-2:
                ans.next = None
            ans = ans.next
        return ret
```

```python
# Solutionを参考に実装
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, dummy
        for _ in range(n+1):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
```

### 1.1.3. ▲[24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

- 方針は立ったが、実装はできず
    1. ペアの前のノード(後ろから2n番目)を最後尾にもってくる
    2. ペアの後ろ以降のノード(後ろから2n-1番目)を、その中の先頭から順に最後尾にもってくる
    3. 2.を2n-2回繰り返す
    4. 1~3を`2n<len(head)`の間、繰り返す
- ▲Discussionを見ると、自分が難しく考えすぎていたことが分かる
    - 処理を追っても理解しきれず

### 1.1.4. [61. Rotate List](https://leetcode.com/problems/rotate-list/)

- 愚直に実装した
- テストケースに引っかかってばかりだった
    - テストケース作成の重要さが分かった
- Discussionでは2つのリストを使用して同時に処理していた

```python
# 自力実装

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k==0:
            return head
        n = 0
        head2 = head
        while head2:
            n += 1
            head2 = head2.next
        if k%n==0:
            return head
        m = n-k%n
        head3 = head
        for _ in range(m-1):
            head3 = head3.next
        ans = head3.next
        while head3.next:
            head3 = head3.next
        head3.next = head
        for _ in range(m):
            head3 = head3.next
        head3.next = None
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k==0:
            return head
        n = 1
        head2 = head
        while head2.next:
            n += 1
            head2 = head2.next
        if k%n==0:
            return head

        m = n-k%n
        head3 = head
        for _ in range(m-1):
            head3 = head3.next
        head2.next, head3.next, ans = head, None, head3.next
        return ans
```

### 1.1.5. [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

- 惜しいところまでいっている気がするが、実装しきれていない

```python
# Discussionを写経
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336/Python-in-place-solution-with-dummy-head-node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val==head.next.val:
                while head and head.next and head.val==head.next.val:
                    head.next = head.next.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
            
        return dummy.next
```

### [86. Partition List](https://leetcode.com/problems/partition-list/)

- 実装が分からん
- Solutionでは2つのリストを新たに作成して最後に結合していた

```python
# Solutionを写経

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val<x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
            
        after.next = None
        before.next = after_head.next
        
        return before_head.next
```