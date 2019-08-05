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