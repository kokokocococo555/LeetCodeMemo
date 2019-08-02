# 1. LeetCode勉強記録（Python_LinkedList編）_Easy

- LeetCodeの勉強記録
    - LinkedListの問題
    - Medium編
- その他詳細・雑感は[solutions[Python].md](https://github.com/kokokocococo555/LeetCodeMemo/blob/master/solutions%5BPython%5D.md)の冒頭参照


<!-- TOC -->

- [1. LeetCode勉強記録（Python_LinkedList編）_Easy](#1-leetcode%E5%8B%89%E5%BC%B7%E8%A8%98%E9%8C%B2pythonlinkedlist%E7%B7%A8easy)
  - [1.1. Medium](#11-medium)
    - [1.1.1. 2. Add Two Numbers](#111-2-add-two-numbers)

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