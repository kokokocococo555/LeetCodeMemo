# 1. LeetCode勉強記録（Python_LinkedList編）_Easy

- LeetCodeの勉強記録
    - LinkedListの問題
    - Easy編
- その他詳細・雑感は[solutions[Python].md](https://github.com/kokokocococo555/LeetCodeMemo/blob/master/solutions%5BPython%5D.md)の冒頭参照


<!-- TOC -->

- [1. LeetCode勉強記録（Python_LinkedList編）_Easy](#1-leetcode%E5%8B%89%E5%BC%B7%E8%A8%98%E9%8C%B2pythonlinkedlist%E7%B7%A8easy)
  - [1.1. Easy](#11-easy)
    - [1.1.1. ▲21. Merge Two Sorted Lists](#111-%E2%96%B221-merge-two-sorted-lists)
    - [1.1.2. ▲83. Remove Duplicates from Sorted List](#112-%E2%96%B283-remove-duplicates-from-sorted-list)
    - [1.1.3. 141. Linked List Cycle](#113-141-linked-list-cycle)
    - [1.1.4. ▲160. Intersection of Two Linked Lists](#114-%E2%96%B2160-intersection-of-two-linked-lists)
    - [1.1.5. 203. Remove Linked List Elements](#115-203-remove-linked-list-elements)
    - [1.1.6. ▲206. Reverse Linked List](#116-%E2%96%B2206-reverse-linked-list)
    - [1.1.7. ▲234. Palindrome Linked List](#117-%E2%96%B2234-palindrome-linked-list)
    - [237. Delete Node in a Linked List](#237-delete-node-in-a-linked-list)

<!-- /TOC -->
## 1.1. Easy
### 1.1.1. ▲[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

- リストであれば
    - 両方のリストから先頭から順に数をpop
    - 数同士を比較し、小さい方を新しいリストに追加
    - 大きい方は残したまま小さかった方のリストから次の数をpop
    - どちらかのリストが空になるまで繰り返す
    - 残ったリストの要素を新しいリストに結合
    - この機能を2つのcntを使用することで実現
- しかしリストではなくListNodeというClassを使用しているため、len()やスライシングが使えない
- ▲Discussionを見ると再帰的なコードが書けるっぽい（要復習）
- 再帰ではなく、上述の元アイデアをListNodeに落とし込んだ解法が上がっていたため、ListNodeの挙動を参考にして実装
  - [python3 24ms beats 100%
  ](https://leetcode.com/problems/merge-two-sorted-lists/discuss/200801/python3-24ms-beats-100)

```python
# リストならうまく動きそうなバージョン（自力実装）
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cnt1=0
        cnt2=0
        l = []
        while cnt1<len(l1) and cnt2<len(l2):
            # 数を比較
            if l1[cnt1]<=l2[cnt2]:
                l.append(l1[cnt1])
                cnt1 += 1
            else:
                l.append(l2[cnt2])
                cnt2 += 1
        # 残った要素を結合
        if cnt1==len(l1):
            l.extend(l2[cnt2:])
        else:
            l.extend(l1[cnt1:])

        return l

```

```python
# ListNodeで動いたバージョン（Discussionを参考に実装）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        # 最初のインデックスを覚えておく
        head = l
        while l1 and l2:
            # 小さい値を持つ方のリストを連結する
            # 連結の後、連結されたリストのインデックスを1つ送る
            if l1.val<=l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
                
            # 作成リストのインデックスを次へ送る
            # 値を残して次以降が上書きされるように
            l = l.next

        # 最後に残ったリストを連結する
        if l1:
            l.next = l1
        else:
            l.next = l2

        # 覚えておいた最初のインデックスの次以降を出力
        # 最初のインデックスは0を指すため
        return head.next
```

### 1.1.2. ▲[83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

- リストノードの扱いに納得がいっていないため、うまく実装できない
- ▲リストノードの扱い能力を測る基本的な問題とのこと
    - Solutionを見ると、最初に考えた方針はよかった

```python
# Solutionを参考に実装
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = head
        while ans!=None and ans.next!=None:
            if ans.val==ans.next.val:
                ans.next = ans.next.next
            else:
                ans = ans.next
        return head
```

### 1.1.3. [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

- 値の一致を基準にすると、無限ループかたまたま同じ数列が繰り返されているだけなのかの判別ができない
- 1度通った値を変更しておくことで、次にその値に当たった場合はループしているということが分かる
    - たまたまリスト内にその値が存在しないように注意しなければならない
    - 今回は数値がvalに含まれるため、文字列ならたまたま存在することはない、しかも2つ連続では存在しないだろうという判断
- Solutionではメモリアドレスを保存する方法、2つのポインタを使用する方法が紹介されている

```python
# 自力実装

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        while True:
            if head.val=="cycle" and head.next.val=="cycle":
                return True
            if head.next:
                head.val = "cycle"
                head = head.next
            else:
                return False
```

```python
# Solutionを参考に実装
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while True:
            if slow==fast:
                return True
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
```

### 1.1.4. ▲[160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

- 元のインプットを破壊しないように、といった指示がある
- 解法を思いつかなかった
- Solutionではブルートフォース、メモリアドレス、2つのポインタを使った解法が紹介されていた
    - ▲2つのポインタでの解法、本当にこれでコーナーケース含めてうまく処理できるのかどうか納得いっていないので復習が必要

```python
# Two Pointers（Solutionを参考に実装）

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB
        while pa!=pb:
            pa = headB if pa==None else pa.next
            pb = headA if pb==None else pb.next
        return pa
```

### 1.1.5. [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

- 試行錯誤の末、正解にたどり着いた
    - `head = head.next.next`ではうまくいかないと気づくまで時間がかかった
    - 条件分岐が多い解法になってしまった
- Discussionの[記事](https://leetcode.com/problems/remove-linked-list-elements/discuss/158651/Simple-Python-solution-with-explanation-(single-pointer-dummy-head).)では先頭にダミーを作成することでシンプルなコードを実現していた
    - elegant!
- その他のDiscussionでは自力で実装したコードと似た発想での解法が紹介されていた

```python
# 自力実装

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # リストの長さが0, 1の場合
        if not head:
            return head
        if not head.next:
            if head.val==val:
                return None
            else:
                return head

        # 先頭からvalが続く場合
        while head.val==val:
            head = head.next
            if not head:
                return None

        # 解答のために先頭を記録
        ans = head

        while head:
            # 次の値がvalの場合、飛ばして次の次に接続する
            while head.next and head.next.val==val:
                head.next = head.next.next
            head = head.next

        return ans
```

### 1.1.6. ▲[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

- ListNodeを前から順にスキャンして値をリストに保存していく
    - リストの逆順に新しいListNodeを作成していく
- Solutionではループな方法と再帰的な方法が解説されていた
    - ▲ループな方法、紙に書いてなんとか理解できるけど、これを思いつくのは今の自分では無理そう...

```python
# 自力実装

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        ans = ListNode(lis[-1])
        cur = ans
        for t in lis[::-1][1:]:
            cur.next = ListNode(t)
            cur = cur.next
        return ans
```

```python
# Solutionを参考に実装
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        c = head
        while c:
            c.next, p, c = p, c, c.next
        return p
```

### 1.1.7. ▲[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

- ひとまずは上の条件を無視して、リストを作成して逆順と同一になるかどうか判定して実装
- 処理速度O(n), 使用メモリO(1)での実装を要求されている
    - 解法思いつかず
- Discussionではfast（1個飛ばし）, slow（順番）の2つのカーソルを使用
    - 使用メモリはO(1)ではなくO(n)？
        - Discussionのコメントにも同様の疑問があり、その返事に'I think rev is not really created. We are updating the list nodes' next values in place.'とあった
        - https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space/220392
    - Linked Listの最後から作っていくrevをslowに合わせて作成し、fastが最後まで行った段階で前半半分を逆順にしたrevも完成する
    - あとは作成したrevと、後半の頭にあるslowとを順に比較していき、revが無事最後まで行けばTrue
    - ▲Linked Listが後ろからも作成できることは覚えておくべき

```python
# 自力実装（条件無視）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        return lis==lis[::-1]
```

```python
# Discussionを参考に実装
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        s = f = head
        while f and f.next:
            f = f.next.next
            rev, rev.next, s = s, rev, s.next
        if f:
            s = s.next
        while rev and rev.val==s.val:
            rev = rev.next
            s = s.next
        return not rev
```

### [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

- headとnodeの2の引数が必要そうな設問なのに、コードでは引数がnodeのみ
- Solutionを見ると、削除すべきノードとしてnodeが与えられている
    - コード上で`node.val`, `node.next.val`の値を確認することで確かめられた
    - Down voteが大量についている

```python
# Solutionを参考に実装

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
