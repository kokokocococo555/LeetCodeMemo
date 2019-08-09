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