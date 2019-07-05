# 1. LeetCode勉強記録（Python_BinaryTree編）

- LeetCodeの勉強記録
    - BinaryTreeの問題
- その他詳細・雑感は[solutions[Python].md](https://github.com/kokokocococo555/LeetCodeMemo/blob/master/solutions%5BPython%5D.md)の冒頭参照

<!-- TOC -->

- [1. LeetCode勉強記録（Python_BinaryTree編）](#1-leetcode%E5%8B%89%E5%BC%B7%E8%A8%98%E9%8C%B2pythonbinarytree%E7%B7%A8)
  - [1.1. Easy](#11-easy)
    - [1.1.1. 100. Same Tree](#111-100-same-tree)
    - [1.1.2. 101. Symmetric Tree](#112-101-symmetric-tree)
    - [1.1.3. ▲104. Maximum Depth of Binary Tree](#113-%E2%96%B2104-maximum-depth-of-binary-tree)
    - [1.1.4. ▲107. Binary Tree Level Order Traversal II](#114-%E2%96%B2107-binary-tree-level-order-traversal-ii)
    - [1.1.5. ▲108. Convert Sorted Array to Binary Search Tree](#115-%E2%96%B2108-convert-sorted-array-to-binary-search-tree)
    - [1.1.6. ▲110. Balanced Binary Tree](#116-%E2%96%B2110-balanced-binary-tree)
    - [1.1.7. 111. Minimum Depth of Binary Tree](#117-111-minimum-depth-of-binary-tree)
    - [1.1.8. 112. Path Sum](#118-112-path-sum)
    - [1.1.9. ▲226. Invert Binary Tree](#119-%E2%96%B2226-invert-binary-tree)
    - [235. Lowest Common Ancestor of a Binary Search Tree](#235-lowest-common-ancestor-of-a-binary-search-tree)

<!-- /TOC -->

## 1.1. Easy

### 1.1.1. [100. Same Tree](https://leetcode.com/problems/same-tree/)

- 再帰的な方法で解こうとしたが、正解と異なる結果が出るケースがあり、うまくいかず
- Solutionその1も再帰的な方法
    - 最初に考えていたよりもっとシンプルな方法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### 1.1.2. [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

- rootの次で木を2つに分けて、rightを反転させた部分木がleftと同一か否かを判定すればOK
    - 100.の2つの木が同一か否かを判定する関数を利用（一部改変）
    - 再帰的な方法で解いた

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        def isMirrorSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return isMirrorSame(p.left, q.right) and isMirrorSame(p.right, q.left)
        
        return isMirrorSame(root.left, root.right)
```

### 1.1.3. ▲[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- 再帰的な方法で解いた
    - Discussionを見ると、自分の実装は無駄なif文が多いみたい
    - ただし、自分の最初の実装の方がかなり速い（無駄な計算をif文で省けている）
- ▲Discussionにはwhile文での解法もある（max()が不要）
    - 順番に降りていってカウントしている。分かりやすく、美しい解法。elegant!
    - 速い
    - https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34198/Python-multiple-solutions-recursion-level-order-using-stack-and-level-order-using-queue

```python
# 自力実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1+self.maxDepth(root.right)
        if root.left and not root.right:
            return 1+self.maxDepth(root.left)
        if root.left and root.right:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
```

```python
# もっとシンプル、しかし遅い（Discussionを参考に実装）
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
```

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [root]
        h = 0
        
        while stack:
            next_level = []
            while stack:
                top = stack[-1]
                stack = stack[:-1]
                if top.left:
                    next_level.append(top.left)
                if top.right:
                    next_level.append(top.right)
            stack = next_level
            h += 1
        return h
```

### 1.1.4. ▲[107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

- 104.で学んだwhile文での解法を援用
    - TreeNodeそのものを追加してしまうと木全体の値が保存されてしまうため、一部修正して使用
- ▲Discussionでは深さ優先探索(DFS)+stack/+再帰、幅優先探索(BFS)+queueの解法があった
    - 今処理している階層を記録しておく解法もあった
        - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue).
    - 自力実装したのはDFS+stackの一種

```python
# DFS+stack（自力実装）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        layer = [root]
        if not root:
            return []
        anser = [[root.val]]
        while layer:
            new_layer = []
            tmp_ans = []  # TreeNodeそのものを追加してしまうと木全体の値が保存されてしまうため
            while layer:
                new_root = layer[-1]
                layer = layer[:-1]
                if new_root.left:
                    new_layer.append(new_root.left)
                    tmp_ans.append(new_root.left.val)
                if new_root.right:
                    new_layer.append(new_root.right)
                    tmp_ans.append(new_root.right.val)
            layer = new_layer[::-1]
            if tmp_ans:
                anser.append(tmp_ans)
        return anser[::-1]
```

### 1.1.5. ▲[108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

- ▲試行錯誤したものの、分からなかった
- TreeNodeの作り方は分かった
- Discussionを見たところ、numsを真ん中で割って処理していく、という元々の方針は良かった
    - あとは実装力
    - シンプルなコード例では再帰的に処理していた

```python
# TreeNodeのつなげ方
tn = TreeNode(0)
tn.left = TreeNode(1)
tn = tn.left
tn.left = TreeNode(2)
tn = tn.left
......
```

```python
# Discussionを参考に実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = (len(nums)-1)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
```

### 1.1.6. ▲[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

- ▲試行錯誤したものの、分からなかった
- Discussionを見たところ、左右の子から親に上がる際に1を足していき、左右の子での差が1を超えてからは常に-1を返し続ける関数を定義して再帰している

```python
# Discussionを参考に実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            if left==-1:
                return -1
            
            right = check(root.right)
            if right==-1:
                return -1
            
            if abs(left-right)>1:
                return -1
            
            return 1+max(left, right)
            
        return check(root)!=-1
```

### 1.1.7. [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

- 104.で学んだwhile文での解法を援用
    - 遅い…
- Discussionにあった再帰的な方法だともう少し速い
    - https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36094/My-solution-in-python

```python
# 自力実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        h = 0
        while stack:
            next_level = []
            h += 1
            while stack:
                root = stack.pop()
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
                if not root.left and not root.right:
                    return h
            stack = next_level
```

```python
# Discussionのコードにコメントを付けただけ

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1  # 左右どちらかが存在しないため、単純に深さを得ることになっている
        return min(self.minDepth(root.right),self.minDepth(root.left))+1  # 左右のうち短い深さを得て自身を足す
```

### 1.1.8. [112. Path Sum](https://leetcode.com/problems/path-sum/)

- 再帰的な解法で実装した
    - そこそこ速い
    - メソッド内でもう1つ関数を定義しているが、Discussionにあった解法はもっとシンプルでエレガントだった
    - https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)
    - 速さは変わらない

```python
# 自力実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def sums(node, sum_ans, sum):
            if not node:
                return False
            sum_ans += node.val
            if sum_ans==sum and not node.left and not node.right:  # 木の途中でsumと一致してもTrueを返さないようにするため
                return True
            return sums(node.left, sum_ans, sum) or sums(node.right, sum_ans, sum)
        sum_ans = 0
        return sums(root, sum_ans, sum)
```

```python
# エレガントな実装（Discussionを参考に実装）
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val==sum and not root.left and not root.right:
                return True

        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

### 1.1.9. ▲[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

- Binary Treeのかなり基本的な問題
- 再帰的な方法で解いた
- ▲Solutionでは再帰的な方法、queueを使った幅優先探索が紹介されていた
    - 104.や107.のwhile文での解法も参考に

```python
# 自力実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.left or root.right:
            root.left, root.right = root.right, root.left
            if root.left:
                if root.left.left or root.left.right:
                    root.left = self.invertTree(root.left)
            if root.right:
                if root.right.left or root.right.right:
                    root.right = self.invertTree(root.right)
            return root
        else:
            return root
```

```python
# Solutionのコメントを参考にリファクタリング
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

### [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- binary search tree (BST) をたどってpまで行く
    - その際に通ってきたノードの値をリストに保存していく
    - 同様にqまで行く
    - 各ノードの値がリストに存在する場合、答えを更新し続ける
    - qにたどり着いたら答えを返す
- Solutionでは再帰的な方法と反復的な方法が紹介されていた
    - 要はpとqが左右に分かれる、もしくはpまたはqがもう片方の親になるノードを見つければよい
        - elegant!
    - p, qともに現在のノードの右にある場合、右の部分木に先延ばし
    - p, qともに現在のノードの左にある場合、左の部分木に先延ばし
    - それ以外（pとqが左右に分かれる、もしくはpまたはqがもう片方の親になる）の場合、現在のノードが答え

```python
# 自力実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lis = []
        head = root
        # pを探索
        while True:
            lis.append(root.val)
            if root.val==p.val:
                break
            if root.val<p.val:
                root = root.right
            elif p.val<root.val:
                root = root.left

        # qを探索
        while True:
            if head.val in lis:
                ans = head
            if head.val==q.val:
                return ans
            if head.val<q.val:
                head = head.right
            elif q.val<head.val:
                head = head.left
```

```python
# 再帰的な方法（Solutionを参考に実装）
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rv = root.val
        pv = p.val
        qv = q.val
        if rv<pv and rv<qv:
            return self.lowestCommonAncestor(root.right, p, q)  # p, qともにrootの右にある場合、右の部分木に探索を先送りする
        elif pv<rv and qv<rv:
            return self.lowestCommonAncestor(root.left, p, q)  # p, qともにrootの左にある場合、左の部分木に探索を先送りする
        else:
            return root
```

```python
# 反復的な方法（Solutionを参考に実装）
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv = p.val
        qv = q.val
        while root:
            rv = root.val
            if rv<pv and rv<qv:
                root = root.right
            elif pv<rv and qv<rv:
                root = root.left
            else:
                return root
```