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
    - [1.1.10. 235. Lowest Common Ancestor of a Binary Search Tree](#1110-235-lowest-common-ancestor-of-a-binary-search-tree)
    - [1.1.11. ▲257. Binary Tree Paths](#1111-%E2%96%B2257-binary-tree-paths)
    - [1.1.12. 404. Sum of Left Leaves](#1112-404-sum-of-left-leaves)
    - [1.1.13. ▲429. N-ary Tree Level Order Traversal](#1113-%E2%96%B2429-n-ary-tree-level-order-traversal)
    - [1.1.14. ▲437. Path Sum III](#1114-%E2%96%B2437-path-sum-iii)
  - [1.2. Medium](#12-medium)
    - [1.2.1. 94. Binary Tree Inorder Traversal](#121-94-binary-tree-inorder-traversal)
    - [1.2.2. 95. Unique Binary Search Trees II](#122-95-unique-binary-search-trees-ii)
    - [1.2.3. 96. Unique Binary Search Trees](#123-96-unique-binary-search-trees)
    - [1.2.4. ▲98. Validate Binary Search Tree](#124-%E2%96%B298-validate-binary-search-tree)
    - [1.2.5. ▲113. Path Sum II](#125-%E2%96%B2113-path-sum-ii)

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

### 1.1.10. [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

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

### 1.1.11. ▲[257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

- リストとしての扱いがうまくいかず、断念
- ▲DiscussionではDFS, BFSでの方法が紹介されていた
- DFSではstackに`(node, "list")`のタプルを積んでいって、nodeとリストを同時に処理していく方法が取られていた
- DFSでは再帰的な方法も取られていた
    - returnしなければ関数から脱出しないため、順にleftとrightを処理できる点が盲点だった

```python
# DFS, stack（Discussionをコピー）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
```

```python
# DFS, recursive（Discussionをコピー）
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)
```

### 1.1.12. [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)

- 再帰で解いた
- DiscussionではDFSも

```python
# 自力実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            if root.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return root.left.val
        elif root.left:
            if root.right:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left)
        elif not root.left:
            if root.right:
                return self.sumOfLeftLeaves(root.right)
            else:
                return 0
```

```python
# Discussionを参考にリファクタリング
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
```

### 1.1.13. ▲[429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

- DFS?で解いた
- ▲問題の建て付け的にはBFSそのもの
- DiscussionでもBFSで解かれていた

```python
# 自力実装
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        if not root.children:
            return [[root.val]]
        ans = []
        tmp = []
        stack = [[root]]
        while stack:
            tmp = []
            tmp_children = []
            children = stack.pop(0)
            while children:
                node = children.pop(0)
                tmp.append(node.val)
                tmp_children.extend(node.children)
            if tmp:
                ans.append(tmp)
            if tmp_children:
                stack.append(tmp_children)
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            # q = [child for node in q for child in node.children if child]  # これを書き下すと以下のfor文になる
            # ---ここから---
            tmp, q = q, []
            for node in tmp:
                for child in node.children:
                    if child:
                        q.append(child)
            # ---ここまで---
        return ret
```

### 1.1.14. ▲[437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

- ちょっとよく分からない
- ▲Discussionではブルートフォース（再帰的方法）とキャッシュを使った方法が紹介されていた
    - 要復習
    - 再帰的な方法ではtarget引数にtarget-valを入れることで、合計状態を次に伝えている
- 112., 113.も参考に

```python
# Discussionをコピペしてコメントを付与

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.numOfPaths = 0
        self.dfs(root, sum)
        return self.numOfPaths
    
    def dfs(self, node, target):
        """
        始点を下っていきながらtest()を順次実行していく
        """
        if node is None:
            return 
        self.test(node, target)
        # targetをval分だけ減らしてツリーを下っていく
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    def test(self, node, target):
        """
        targetをval分だけ減らしながらツリーを下り、途中でsumに合致すればカウントを増やす
        """
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
```

## 1.2. Medium

### 1.2.1. [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

- そもそも問題の意図が分からない

### 1.2.2. [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)

- 分からない

### 1.2.3. [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)

- 分からない

### 1.2.4. ▲[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

- 上の方の値を覚えておいて、左の木だとより小さく、右の木だとより大きく、という処理をうまく実装できなかった
- ▲Solutionを見るととても簡潔
- DFSによる実装も分かりやすい

```python
# Solutionを参考に実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidSubBST(root, float("-inf"), float("inf"))
        
    def isValidSubBST(self, root, minval, maxval):
        if not root:
            return True
        
        val = root.val
        if val <= minval or val >= maxval:
            return False

        if not self.isValidSubBST(root.right, val, maxval):
            return False
        if not self.isValidSubBST(root.left, minval, val):
            return False
        return True
```


### 1.2.5. ▲[113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

- 再帰で解こうとしたものの、うまく引数が初期化されず断念
- ▲Discussionを見ると、pathへの追加を引数の中で行う、sumからvalを引いていく（これも引数の中で）、といった点がポイントっぽい
  - BFSやDFSでもなのでBFS, DFSの練習問題に適している
  - https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)

```python
# Discussionを参考に実装

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
    
        def pathSumSub(node, path, s, ans):
            if not node.left and not node.right:
                if node.val == s:
                    path.append(node.val)
                    ans.append(path)

            if node.left:
                pathSumSub(node.left, path + [node.val], s - node.val, ans)
            if node.right:
                pathSumSub(node.right, path + [node.val], s - node.val, ans)
                
        pathSumSub(root, [], s, ans)
        return ans
```
