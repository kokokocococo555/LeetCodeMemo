# 1. LeetCode勉強記録（Python編）_Medium

- LeetCodeの勉強記録
    - Medium編
- 自力で実装したコードの他にも、Solution, Discussionに投稿されている内容等を参照し、自分でも実装してみる
- 復習が必要な問題には▲をつけている
- 使用言語は`Python`

<!-- TOC -->

- [1. LeetCode勉強記録（Python編）_Medium](#1-leetcode%E5%8B%89%E5%BC%B7%E8%A8%98%E9%8C%B2python%E7%B7%A8medium)
  - [1.1. Medium](#11-medium)
    - [1.1.1. ▲3. Longest Substring Without Repeating Characters](#111-%E2%96%B23-longest-substring-without-repeating-characters)
    - [1.1.2. ▲5. Longest Palindromic Substring](#112-%E2%96%B25-longest-palindromic-substring)
    - [1.1.3. 6. ZigZag Conversion](#113-6-zigzag-conversion)
    - [1.1.4. 8. String to Integer (atoi)](#114-8-string-to-integer-atoi)
    - [1.1.5. ▲11. Container With Most Water](#115-%E2%96%B211-container-with-most-water)
    - [1.1.6. 12. Integer to Roman](#116-12-integer-to-roman)
    - [1.1.7. ▲15. 3Sum](#117-%E2%96%B215-3sum)
    - [1.1.8. 16. 3Sum Closest](#118-16-3sum-closest)
    - [1.1.9. ▲17. Letter Combinations of a Phone Number](#119-%E2%96%B217-letter-combinations-of-a-phone-number)
    - [1.1.10. ▲18. 4Sum](#1110-%E2%96%B218-4sum)
    - [1.1.11. 22. Generate Parentheses](#1111-22-generate-parentheses)
    - [1.1.12. ▲29. Divide Two Integers](#1112-%E2%96%B229-divide-two-integers)
    - [1.1.13. 31. Next Permutation](#1113-31-next-permutation)
    - [1.1.14. 33. Search in Rotated Sorted Array](#1114-33-search-in-rotated-sorted-array)
    - [1.1.15. 34. Find First and Last Position of Element in Sorted Array](#1115-34-find-first-and-last-position-of-element-in-sorted-array)
    - [1.1.16. 36. Valid Sudoku](#1116-36-valid-sudoku)
    - [1.1.17. ▲39. Combination Sum](#1117-%E2%96%B239-combination-sum)
    - [1.1.18. 40. Combination Sum II](#1118-40-combination-sum-ii)
    - [1.1.19. ▲43. Multiply Strings](#1119-%E2%96%B243-multiply-strings)
    - [1.1.20. 46. Permutations](#1120-46-permutations)
    - [1.1.21. 47. Permutations II](#1121-47-permutations-ii)
    - [1.1.22. 48. Rotate Image](#1122-48-rotate-image)
    - [1.1.23. 49. Group Anagrams](#1123-49-group-anagrams)
    - [1.1.24. ▲50. Pow(x, n)](#1124-%E2%96%B250-powx-n)
    - [1.1.25. 54. Spiral Matrix](#1125-54-spiral-matrix)
    - [1.1.26. ▲55. Jump Game](#1126-%E2%96%B255-jump-game)
    - [1.1.27. 56. Merge Intervals](#1127-56-merge-intervals)
    - [1.1.28. ▲59. Spiral Matrix II](#1128-%E2%96%B259-spiral-matrix-ii)
    - [1.1.29. 60. Permutation Sequence](#1129-60-permutation-sequence)
    - [1.1.30. 62. Unique Paths](#1130-62-unique-paths)
    - [1.1.31. 63. Unique Paths II](#1131-63-unique-paths-ii)
    - [1.1.32. 64. Minimum Path Sum](#1132-64-minimum-path-sum)
    - [1.1.33. 71. Simplify Path](#1133-71-simplify-path)
    - [1.1.34. 73. Set Matrix Zeroes](#1134-73-set-matrix-zeroes)
    - [1.1.35. 74. Search a 2D Matrix](#1135-74-search-a-2d-matrix)
    - [1.1.36. ▲75. Sort Colors](#1136-%E2%96%B275-sort-colors)
    - [1.1.37. 77. Combinations](#1137-77-combinations)

<!-- /TOC -->

## 1.1. Medium

### 1.1.1. ▲[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- 二重ループになってしまって良くはないものの、解くことはできた
- ▲Solutionではsliding windowで解いていた
    - ちょっとだけ二分探索に似ている気がする

```python
# 自力実装
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            dic = {}
            j = i
            while j<len(s) and not s[j] in dic:
                dic[s[j]] = 1
                j += 1
            if ans<len(dic):
                ans = len(dic)
        return ans
```

```python
# Solutionを参考に実装
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0
        n = len(s)
        dic = {}
        while l<n and r<n:
            if s[r] not in dic:
                dic[s[r]] = 1
                r += 1
                ans = max(ans, r-l)
            else:
                del dic[s[l]]
                l += 1
        return ans
```

```python
# Solutionを参考に実装（さらに最適化）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        n = len(s)
        dic = {}
        for r in range(n):
            if s[r] in dic:
                l = max(l, dic[s[r]])
            ans = max(ans, r-l+1)
            dic[s[r]] = r+1
        return ans
```

### 1.1.2. ▲[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

- 3.を参考にwindowをずらしながら検証していった
- ▲Solutionでは、各文字を中心として左右に範囲を広げていき、どこまでが回文になっているかを順次確認していく方法などが採られていた
- Manacher's AlgorithmだとO(n)らしい
    - [文字列の頭良い感じの線形アルゴリズムたち２ - あなたは嘘つきですかと聞かれたら「YES」と答えるブログ](https://snuke.hatenablog.com/entry/2014/12/02/235837)

```python
# 自力実装
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s

        n = len(s)
        while n>0:
            i = 0
            j = i+n
            while j<=len(s):
                if s[i]==s[j-1]:
                    if s[i:j]==s[i:j][::-1]:
                        return s[i:j]
                i += 1
                j += 1
            n -= 1
```

```python
# Solutionを参考に実装
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s

        start = end = 0
        for i in range(len(s)):
            leng1 = self.subPalindrome(s, i, i)  # 奇数の回文
            leng2 = self.subPalindrome(s, i, i+1)  # 偶数の回文
            leng = max(leng1, leng2)
            if leng>end-start:
                start = i-((leng-1)//2)
                end = i+(leng//2)

        return s[start:end+1]


    def subPalindrome(self, s, start, end):
        while start>=0 and end<len(s) and s[start]==s[end]:
            start -= 1
            end += 1
        return end-start-1
```

### 1.1.3. [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/submissions/)

- 実際に文字を並び替えて1つ1つのインデックスを確認した
- Solutionも似たような感じだった

```python
# 自力実装
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ans =""
        cnt = 0
        while cnt*2*(numRows-1)<len(s):
            ans += s[cnt*2*(numRows-1)]
            cnt += 1
        for i in range(1, numRows-1):
            cnt = 0
            while cnt*2*(numRows-1)-i<len(s):
                if cnt>0:
                    ans += s[cnt*2*(numRows-1)-i]
                if cnt*2*(numRows-1)+i<len(s):
                    ans += s[cnt*2*(numRows-1)+i]
                cnt += 1
        cnt = 0
        while cnt*2*(numRows-1)+numRows-1<len(s):
            ans += s[cnt*2*(numRows-1)+numRows-1]
            cnt += 1

        return ans
```

```python
# Solutionを参考にリファクタリング
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ans =""
        for i in range(numRows):
            cnt = 0
            while cnt*2*(numRows-1)-i<len(s):
                if cnt>0 and i!=0:
                    ans += s[cnt*2*(numRows-1)-i]
                if cnt*2*(numRows-1)+i<len(s) and i!=numRows-1:
                    ans += s[cnt*2*(numRows-1)+i]
                cnt += 1

        return ans
```

### 1.1.4. [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

- 条件を満たすようにif文、while文を使用
- Discussionも似た感じ。正規表現を使っている解法もあった

```python
# 自力実装
class Solution:
    def myAtoi(self, s: str) -> int:
        dic = {}
        for i in range(48, 59):
            dic[chr(i)] = 0

        p = 0
        ans = ""
        while p<len(s) and s[p]==" ":
            p += 1
        if p<len(s) and (s[p]=="-" or s[p]=="+"):
            ans += s[p]
            p += 1
        while p<len(s) and s[p] in dic:
            ans += s[p]
            p += 1

        if ans=="" or ans=="-" or ans=="+":
            return 0
        else:
            return min(max(int(ans), -2**31), 2**31-1)
```

### 1.1.5. ▲[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

- windowをずらしていく方法で実装したが、TLE
    - 2重ループになっていたから仕方ない
- ▲Solutionでは左右からポインタを狭めていく方法をとっていた
    - 似たようなことは考えたが、考えきれなかった

```python
# Solutionを参考に実装
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            s = min(height[l], height[r])*(r-l)
            ans = max(ans, s)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return ans
```

### 1.1.6. [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

- できるだけ条件分岐が少なくなるようにした
- Solutionでは4, 9といった場合のRomanも使用していた

```python
# 自力実装
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "",  # dummy
            10000: "",  # dummy
        }
        dig = 0
        ans = ""
        while num>0:
            n = num%10
            num = num//10
            if n==4 or n==9:
                ans = dic[1*(10**dig)]+dic[(n+1)*(10**dig)]+ans
            else:
                ans = dic[5*(10**dig)]*(n//5)+dic[1*(10**dig)]*(n%5)+ans
            dig += 1
        return ans
```

```python
# Solutionを参考に実装
class Solution:
    def intToRoman(self, num: int) -> str:
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""
        for s, n in zip(strs, nums):
            ans += s*(num//n)
            num %= n
        return ans
```

### 1.1.7. ▲[15. 3Sum](https://leetcode.com/problems/3sum/)

- 3重ループに工夫を加えたものの、TLE
- ▲Discussionでは2つ目のループと3つ目のループを融合し、O(N**2)で抑えている
    - 合計値の正負に応じて左右から範囲を狭めていく

```python
# 自力実装（TLE）
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        u_nums = list(set(nums))
        p1, p2, p3 =0, 0, 0
        ans = []
        while p1<n-2 and nums[p1]<=0:
            if p1==0 or nums[p1-1]!=nums[p1]:
                p2 = p1+1
                p2flg = True
                while p1<p2 and p2<n-1:
                    if p2flg==True:
                        p3 = n-1
                        while p2<p3 and p3<n:
                            if nums[p1]+nums[p2]+nums[p3]<=0:
                                if nums[p1]+nums[p2]+nums[p3]==0:
                                    ans.append([nums[p1], nums[p2], nums[p3]])
                                p3 = p2-1
                            else:
                                p3 -= 1
                    p2n = nums[p2]
                    p2 += 1
                    p2flg = nums[p2]!=p2n
            p1 += 1
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for p1 in range(n-2):
            if p1>0 and nums[p1-1]==nums[p1]:
                continue
            l, r = p1+1, n-1
            while l<r:
                sum3 = nums[p1]+nums[l]+nums[r]
                if sum3<0:
                    l += 1
                elif 0<sum3:
                    r -= 1
                else:
                    ans.append([nums[p1], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l += 1
                    while l<r and nums[r-1]==nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans
```

### 1.1.8. [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

- 15.を応用した

```python
# 自力実装
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                n_sum = nums[i]+nums[l]+nums[r]
                if n_sum==target:
                    return n_sum
                elif abs(n_sum-target)<diff:
                    diff = abs(n_sum-target)
                    ret = n_sum

                if n_sum-target<0:
                    l += 1
                else:
                    r -= 1
        return ret
```

### 1.1.9. ▲[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

- for文を組み合わせて実装
- ▲Solutionによると、[`backtracking`](https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%83%E3%82%AF%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0)というアルゴリズムがあるらしい
    - 再帰呼び出しの深さ優先探索の一種

```python
# 自力実装
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dic ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ret = [x for x in dic[digits[0]]]
        for i in digits[1:]:
            tmp1 = []
            tmp2 = []
            for st in ret:
                tmp1 = [st+x for x in dic[i]]
                tmp2.extend(tmp1)
                ret = tmp2
        return ret
```

```python
# Solutionを参考に実装(backtrack)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        DIC ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(combination, next_digits):
            if len(next_digits)==0:
                ret.append(combination)
            else:
                for x in DIC[next_digits[0]]:
                    backtrack(combination+x, next_digits[1:])

        ret = []
        backtrack("", digits)
        return ret
```

### 1.1.10. ▲[18. 4Sum](https://leetcode.com/problems/4sum/)

- 解けなかった
- ▲Discussionでは2Sum問題に分解して解いていた
    - 要復習

```python
# https://leetcode.com/problems/4sum/discuss/128591/Easy-to-understand-python-Solution をコピー
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 in d:
                    d[sum2].append((i,j))
                else:
                    d[sum2] = [(i,j)]

        result = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:
                    for (k,l) in list2:
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)
```

### 1.1.11. [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

- 妥当な`()`になる条件を考えたりもしたが、うまいことケースを列挙しつつ計算量を抑える方法が思いつかず、断念
- Solutionでは`backtracking`が使用されていた
    - 木構造的に再帰が進んでいく

```python
# Solutionを写経
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s="", l=0, r=0):
            if len(s)==2*n:
                ans.append(s)
                return
            if l<n:
                backtrack(s+"(", l+1, r)
            if r<l:
                backtrack(s+")", l, r+1)

        backtrack()
        return ans
```

### 1.1.12. ▲[29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

- 掛け算、割り算、modを使用せずに商を求める
- 引き算を繰り返す方法だとTLE
- ▲Discussionではビットシフト`<<`を使用して引き算の試行を高速化していた
    - 1bitシフトすると値が2倍になる

```python
# Solutionを参考に実装
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend*divisor>=0:
            c = 1
        else:
            c = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        while dividend>=divisor:
            tmp, i = divisor, 1
            while dividend>=tmp:
                dividend -= tmp
                ret += i
                i <<= 1  # ビットシフト
                tmp <<= 1  # ビットシフト
        return min(max(c*ret, -2147483648), 2147483647)  # overflow対策
```

### 1.1.13. [31. Next Permutation](https://leetcode.com/problems/next-permutation/)

- 複雑な処理が必要そうでさっぱり分からん
- Solution
    - 終端から`a[i-1]<a[i]`となる`a[i-1]`を見つける
    - `a[i:]`の中で`a[i-1]`より大きい最小の値`a[j]`と`a[i-1]`を交換
    - `a[i:]`を昇順に並べ替え
    - という手順

```python
# Solution(Java)を写経(Python)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return
        elif len(nums)==2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        
        p = len(nums)-2
        while 0<=p and nums[p]>=nums[p+1]:
            p -= 1
        if p>=0:
            p2 = len(nums)-1
            while 0<=p2 and nums[p2]<=nums[p]:
                p2 -= 1
            self.swap(nums, p, p2)
        self.reverse(nums, p+1)

    def reverse(self, nums, start):
        i = start
        j = len(nums)-1
        while i<j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
```

### 1.1.14. [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- ずれた数だけ補正し、通常の二分探索のように解いた
- Discussionでは、切れ目の前後どちらかをtargetに応じて-Inf, Infに置換した上で二分探索を行う方法や、`nums[l], nums[m], nums[r], target`の値の大小でうまくl, rを更新していく方法も紹介されていた
    - elegant!

```python
# 自力実装
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n==0:
            return -1
        if n==1:
            return 0 if nums[0]==target else -1
        p = n-1
        cnt = 1
        while cnt<n and nums[p-1]<=nums[p]:
            p -= 1
            cnt += 1
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            m2 = m-cnt
            if nums[m2]==target:
                return m2 if m2>=0 else m2+n
            elif nums[m2]<target:
                l = m+1
            elif nums[m2]>target:
                r = m-1
        return -1
```

### 1.1.15. [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

- 2回二分探索を行う

```python
# 自力実装
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans1 = -1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                if m==0 or (m>0 and nums[m-1]<nums[m]):
                    ans1 = m
                    break
                else:
                    r = m-1
            elif nums[m]<target:
                l = m+1
            elif nums[m]>target:
                r = m-1

        if ans1==-1:
            return [-1, -1]

        l = ans1
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                if m==len(nums)-1 or (m<len(nums)-1 and nums[m]<nums[m+1]):
                    ans2 = m
                    break
                else:
                    l = m+1
            elif nums[m]<target:
                l = m+1
            elif nums[m]>target:
                r = m-1

        return [ans1, ans2]
```

### 1.1.16. [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

- 9個の数字が条件を満たすかどうかを判定するメソッドを作成
- 行、列、3*3の3種類それぞれのリストを作成し、判定用メソッドを適用
- Discussionでは、`zip`や`set`を活用したシンプルな実装がなされていた
    - https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution

```python
# 自力実装
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # columns
        col_board = [[] for _ in range(9)]
        # 9*9
        nine_board = [[] for _ in range(9)]
        for i in range(len(board)):
            lis = board[i]
            # rows
            if not self.isValid(lis):
                return False

            for j in range(len(lis)):
                # columns
                col_board[j].append(lis[j])
                # 9*9
                idx = (i//3)+((j//3)*3)
                nine_board[idx].append(lis[j])
        # columns
        for col in col_board:
            # print(col)
            if not self.isValid(col):
                return False
        # 9*9
        for nine in nine_board:
            # print(nine)
            if not self.isValid(nine):
                return False
            
        return True


    def isValid(self, lis):
        dic = {}
        for i in lis:
            if i!=".":
                dic[i] = dic.get(i, 0)+1
                # print(dic[i])
                if dic[i]==2:
                    return False
        return True
```

### 1.1.17. ▲[39. Combination Sum](https://leetcode.com/problems/combination-sum/)

- 重複あり、使用個数の指定なしで合計値がtargetになる要素の組をすべて求める
- 方針すら思い浮かばないため、Discussionを見た
- DFSとDPで解かれていた
- ▲DFSは再帰で全ケースを確認、targetを超えた際には枝切り
- DPはうまく動かず...

```python
# DFS（Discussionを写経）
# https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans
    
    def dfs(self, nums, target, idx, path, ans):
        if target<0:
            return
        elif target==0:
            ans.append(path)
            return
        for i in range(idx, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], ans)
```

### 1.1.18. [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

- 39.のDFSを少し修正
- Discussionによると、`if i > start and nums[i] == nums[i - 1]: continue`で重複を防いでいた

```python
# 自力実装
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans
    
    
    def dfs(self, nums, target, idx, path, ans):
        if target<0:
            return
        if target==0:
            if not path in ans:
                ans.append(path)
            return
        for i in range(idx, len(nums)):
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ans)
```

```python
# Discussionを参考に実装
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans
    
    
    def dfs(self, nums, target, idx, path, ans):
        if target<0:
            return
        if target==0:
            ans.append(path)
            return
        for i in range(idx, len(nums)):
            if i>idx and nums[i]==nums[i-1]:  # 重複を防ぐ
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ans)
```


### 1.1.19. ▲[43. Multiply Strings](https://leetcode.com/problems/multiply-strings/)

- 文字列で与えられる数値の積を計算する
- ただしビルトイン関数を用いて直接計算したり数値型に直したりしてはいけない
- 何をすればよいのか分からず
- ▲Discussionでは1桁ずつ積を計算し、掛け算の筆算を再現していた
    - リストを用意して計算する方法は繰り上がりの扱いも楽そうで、応用が利きそう

```python
# Discussionを写経
# https://leetcode.com/problems/multiply-strings/discuss/17615/Simple-Python-solution-18-lines
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0]*(len(num1)+len(num2))
        pos = len(product)-1
        for n1 in reversed(num1):
            tmp = pos
            for n2 in reversed(num2):
                product[tmp] += int(n1)*int(n2)
                product[tmp-1] += product[tmp]//10
                product[tmp] %= 10
                tmp -= 1
            pos -= 1
        p = 0
        while p<len(product)-1 and product[p]==0:
            p += 1
        return "".join(map(str, product[p:]))
```

### 1.1.20. [46. Permutations](https://leetcode.com/problems/permutations/)

- 39.を応用して再帰（backtracking）で解いた
- `nums`はそのまま`.pop(x)`するとグローバルに反映されるため、`.copy()`してから`.pop(x)`すること
- `path`は`path.append(x)`するとグローバルに変更が伝播してしまうため、再帰の引数で`path+[x]`とすること
- Discussionもbacktracking

```python
# 自力実装
class Solution:
    def permute(self, nums):
        ans = []
        self.backtracking(nums, [], ans)
        return ans

    def backtracking(self, nums, path, ans):
        if not nums:
            ans.append(path)
            return

        for i in range(len(nums)):
            tmp = nums.copy()
            x = tmp.pop(i)
            self.backtracking(tmp, path+[x], ans)
```

### 1.1.21. [47. Permutations II](https://leetcode.com/problems/permutations-ii/)

- 46.とほぼ同じ

```python
# 自力実装
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtracking(nums, [], ans)
        return ans

    def backtracking(self, nums, path, ans):
        if not nums:
            if not path in ans:
                ans.append(path)
            return

        for i in range(len(nums)):
            tmp = nums.copy()
            x = tmp.pop(i)
            self.backtracking(tmp, path+[x], ans)
```

### 1.1.22. [48. Rotate Image](https://leetcode.com/problems/rotate-image/)

- 4箇所をそれぞれで同時に置換する
- Discussionではone-linerの解法`matrix[:] = zip(*matrix[::-1])`が紹介されていたが、まだよく分かっていない
- 他にも、`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`で転置し、各行内を逆順にすれば90°回転する、という方法も

```python
# 自力実装
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ni = len(matrix)
        nj = len(matrix[0])
        for i in range(ni//2+1):
            for j in range(i, nj-i-1):
                matrix[i][j], matrix[j][nj-i-1], matrix[ni-i-1][nj-j-1], matrix[ni-j-1][i] = \
                matrix[ni-j-1][i], matrix[i][j], matrix[j][nj-i-1], matrix[ni-i-1][nj-j-1]
```

### 1.1.23. [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

- ソートした文字列を辞書のキーに据え、キーとの一致を確認した
- Solutionによると、文字列のソートではなく文字数のカウントだともっと速くなる（文字列ソートは`KlogK`だが文字数カウントは`K`なので）

```python
# 自力実装
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            tmp = dic.get(sorted_s, [])
            tmp.append(s)
            dic[sorted_s] = tmp
        return dic.values()
```

### 1.1.24. ▲[50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

- 普通にループしようとするとTLE
- ビットシフトか？
- ▲Discussionではビットシフトを利用した方法、再帰的な方法が採られていた

```python
# Discussionをコピペ
# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:  # 2進数で1が立っている桁に来た際にpowにxを掛ける=最終的にxのn乗になる
                pow *= x
            x *= x  # 2進数の桁とx**yのyとを一致させる
            n >>= 1
        return pow
```

### 1.1.25. [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

- 上辺、右辺、下辺、左辺の4段階に分けて処理
- 処理終了の条件が`if not matrix`だと`matrix=[[]]`の場合に終了しないため、注意
- Solutionも似たような感じ

```python
# 自力実装
class Solution:
    def spiralOrder(self, matrix):
        ans = []
        while matrix and matrix[0]:
            # 先頭行をpop（順方向）
            tmp = matrix.pop(0)
            ans.extend(tmp)
            if not matrix or not matrix[0]:
                return ans

            # 最終列をpop（順方向）
            for i in range(len(matrix)):
                tmp = matrix[i].pop(-1)
                ans += [tmp]
            if not matrix or not matrix[0]:
                return ans

            # 最終行をpop（逆方向）
            tmp = matrix.pop(-1)
            tmp.reverse()
            ans.extend(tmp)
            if not matrix or not matrix[0]:
                return ans

            # 先頭列をpop（逆方向）
            tmp = []
            for i in range(len(matrix)):
                tmp.append(matrix[i].pop(0))
            tmp.reverse()
            ans.extend(tmp)
        return ans
```

### 1.1.26. ▲[55. Jump Game](https://leetcode.com/problems/jump-game/)

- 後ろから順に確認していき、0の際にその前の場所で0を飛び越えられるかどうかを確認
- 1あれば順に次に行けるため、0の場合のみを考えればよい
- 0が連続した場合も「後ろの0を飛び越えられない値」と見なせるため、1以上の値と同様に扱ってよい
- ▲SolutionではDPの手順が解説されている
    - 自分で実装したコードはstep4の貪欲法のようなもの
    - Solutionではさらに最適化された貪欲法が紹介されていた

```python
# 自力実装
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True

        p = len(nums)-2
        while p>=0:
            if nums[p]>0:
                p -= 1
            else:
                cnt = 1
                p -= 1
                while p>=0 and nums[p]<=cnt:
                    p -= 1
                    cnt += 1
                if p==-1:
                    return False
        return True
```

### 1.1.27. [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

- 各区間を含む最大・最小値を更新していく
- Solutionではグラフを作成してbrute forceで解く方法と、ソートして前から順に比較していく方法が紹介されていた

```python
# 自力実装
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        p = 0
        n = len(intervals)
        while p<n:
            start = intervals[p][0]
            end = intervals[p][1]
            while p<n-1 and end>=intervals[p+1][0]:
                start = min(start, intervals[p+1][0])
                end = max(end, intervals[p+1][1])
                p += 1
            ans.append([start, end])
            p += 1
        return ans
```

### 1.1.28. ▲[59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

- 実装方法分からず
- ▲Discussionでは、インデックスの増加を制御して実装していた

```python
# Discussionを参考に実装
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        r, c, dr, dc = 0, 0, 0, 1
        for k in range(n**2):
            ans[r][c] += k+1
            if ans[(r+dr)%n][(c+dc)%n]:
                dr, dc = dc, -dr
            r += dr
            c += dc
        return ans
```

### 1.1.29. [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

- backtrackingで実装したところ、コードテストではうまくいくものの、提出するとTLEになる
- Discussionによると、与えられているkを活用する
    - [参考](https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation)

```python
# 自力実装（TLE）
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        perm = ""
        lis = []

        def backtracking(nums, perm, n):
            if n==0:
                lis.append(perm)
            else:
                for i in range(n):
                    tmp = nums.copy()
                    x = tmp.pop(i)
                    backtracking(tmp, perm+str(x), n-1)

        backtracking(nums, perm, n)
        return lis[k-1]
```

```python
# Discussionを写経
# https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        perm = ""
        k -= 1
        while n>0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))  # k/階乗の商, 余りを返す
            perm += str(nums.pop(index))

        return perm
```

### 1.1.30. [62. Unique Paths](https://leetcode.com/problems/unique-paths/submissions/)

- よくある問題なので`((m-1)+(n-1))!/((m-1)!*(n-1)!)`で計算した
- DiscussionではDPでの回答が紹介されていた
    - 前のマスまでのルート数を足し合わせていく

```python
# 自力実装
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ((m-1)+(n-1))!/((m-1)!*(n-1)!)
        m2 = math.factorial(m-1)
        n2 = math.factorial(n-1)
        mn2 = math.factorial(m+n-2)
        return int(mn2/(m2*n2))
```

```python
# Discussionを参考に実装
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        route = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                route[i][j] = route[i-1][j]+route[i][j-1]
        return route[-1][-1]
```

### 1.1.31. [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

- 62.問のDPを応用
- 1行目、1列目に障害物がある場合に手間取った
- Solutionも1行目・1列目に前処理をしてDPを用いるという同様な回答

```python
# 自力実装
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        og = obstacleGrid
        r = len(og)
        c = len(og[0])
        for i in range(r):
            for j in range(c):
                if og[i][j]==1:
                    og[i][j] = 0
                else:
                    og[i][j] = 1

        flg = 0
        for j in range(c):
            if og[0][j]==0:
                flg = 1
            if flg==1:
                og[0][j] = 0

        flg = 0
        for i in range(r):
            if og[i][0]==0:
                flg = 1
            if flg==1:
                og[i][0] = 0

        for i in range(1, r):
            for j in range(1, c):
                if og[i][j]!=0:
                    og[i][j] = og[i-1][j]+og[i][j-1]
                    
        return og[-1][-1]
```

### 1.1.32. [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

- 分からず
- DiscussionではDPで解いていた
- 1行目、1列目の累積和をまずとって、あとは上・左のminとの和をとっていく

```python
# Discussionを参考に実装
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i-1][0]+grid[i][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j-1]+grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
```

### 1.1.33. [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

- 文字列を'/'で区切ってリスト化し、流れに沿って文字列を変換していく

```python
# 自力実装
class Solution:
    def simplifyPath(self, path: str) -> str:
        # // -> /
        ans = path.split("/")
        p = 0
        while p<len(ans):
            if ans[p]=="." or ans[p]=="":
                ans.pop(p)
            # /a/b/.. -> /a
            elif ans[p]==".." and p>0:
                ans.pop(p)
                ans.pop(p-1)
                p -= 1
            # /a/b/../../../.. -> /
            elif ans[p]==".." and p==0:
                ans.pop(p)
            else:
                p += 1
        ans = "/".join(ans)
        return "/"+ans
```

### 1.1.34. [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- メモリをO(1)で実装せよというお題
- O(m*n)ならできたが、分からず
- 多次元のリストは値だけコピーする際には`copy.deepcopy(list)`とする
    - `list.copy()`や`list[:]`では参照を渡すだけ
- Solutionを見ると、該当する行・列の値を一旦0ではなくダミーの値`-1`などに置換しておき、最後にダミーの値を0に置換し直すという方法が採られていた
    - これなら0にした要素が影響を及ぼすことなく処理できる
    - ただし計算量が多い
- SolutionではメモリO(1)に加え、計算量も抑えた方法として、最初の行・列をフラグとして利用する方法が採られていた

```python
# 自力実装
import copy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = copy.deepcopy(matrix)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                # print(i, j)
                # print(mat)
                # print(matrix)
                if mat[i][j]==0:
                    for iall in range(m):
                        matrix[iall][j] = 0
                    for jall in range(n):
                        matrix[i][jall] = 0
```

```python
# Solutionを参考に実装
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0]==0:
                is_col = True
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0

        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j] = 0

        if is_col:
            for i in range(m):
                matrix[i][0] = 0
```

### 1.1.35. [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

- 二分探索を2回行った
- Discussionでは1つのリストと見なし、二分探索1回で終わらせていた

```python
# 自力実装
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        if r==0:
            return False
        c = len(matrix[0])
        if c==0:
            return False
        f1, l1 = 0, r-1
        r_ans = -1
        while f1<=l1:
            m1 = (f1+l1)//2
            if matrix[m1][0]<=target and matrix[m1][c-1]>=target:
                r_ans = m1
                break
            elif matrix[m1][0]<target:
                f1 = m1+1
            elif matrix[m1][0]>target:
                l1 = m1-1
        if r_ans==-1:
            return False

        f2, l2 = 0, c-1
        while f2<=l2:
            m2 = (f2+l2)//2
            if matrix[r_ans][m2]==target:
                return True
            elif matrix[r_ans][m2]<target:
                f2 = m2+1
            else:
                l2 = m2-1
        return False
```

```python
# Discussionを参考に実装
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        if r==0:
            return False
        c = len(matrix[0])
        if c==0:
            return False
        f1, l1 = 0, r*c-1
        while f1<=l1:
            m1 = (f1+l1)//2
            if matrix[m1//c][m1%c]==target:
                return True
            elif matrix[m1//c][m1%c]<target:
                f1 = m1+1
            elif matrix[m1//c][m1%c]>target:
                l1 = m1-1
        return False
```

### 1.1.36. ▲[75. Sort Colors](https://leetcode.com/problems/sort-colors/)

- 2回スキャンではなく、1周で完了せよというお題
- ポインタを3つ使用し、前から順に2なら後ろの方と、1なら0の中で一番後ろのものと入れ替えていく実装
- ▲Discussionの実装はよりスマート

```python
# 自力実装
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2, p3 = 0, len(nums)-1, len(nums)-1
        while p1<p3:
            if nums[p1]==2:
                nums[p1], nums[p3] = nums[p3], nums[p1]
                p3 -= 1
            elif nums[p1]==1:
                while p1<p2 and nums[p2]!=0:
                    p2 -= 1
                if p1<p2:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p2 -= 1
                else:
                    p1 += 1
            else:
                p1 += 1
```

```python
# Discussionを参考に実装
# https://leetcode.com/problems/sort-colors/discuss/26479/AC-Python-in-place-one-pass-solution-O(n)-time-O(1)-space-no-swap-no-count
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 2
            if tmp<=1:
                nums[p1] = 1
                p1 += 1
            if tmp==0:
                nums[p0] = 0
                p0 += 1
```

### 1.1.37. [77. Combinations](https://leetcode.com/problems/combinations/)

- backtrackingで実装した
- Discussionではbacktrackingの他にも再帰、順次でのコード例もあった

```python
# 自力実装
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(first, last, k, ktmp, path):
            for i in range(first, last+k+1):
                if ktmp==0:
                    ans.append(path)
                    return
                elif i<=n:
                    backtrack(i+1, n, k, ktmp-1, path+[i])
        
        backtrack(1, n, k, k, [])
        return ans
```

```python
# Discussionを参考にリファクタリング
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(first, last, k, path):
            if k==0:
                ans.append(path)
                return
            for i in range(first, last+1):
                backtrack(i+1, n, k-1, path+[i])
        
        backtrack(1, n, k, [])
        return ans
```
