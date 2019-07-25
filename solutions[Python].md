# 1. LeetCode勉強記録（Python編）

- LeetCodeの勉強記録
- 自力で実装したコードの他にも、Solution, Discussionに投稿されている内容等を参照し、自分でも実装してみる
- 復習が必要な問題には▲をつけている
- 使用言語は`Python`
    - しかし`Python`遅いな…


- 以下のことができれば実装はほぼ作業化する。以下のことが重要と見た。
    - テストケースを作る。
    - 頭の中や紙の上で処理してみる。その流れをプログラムに起こすだけ。

<!-- TOC -->

- [1. LeetCode勉強記録（Python編）](#1-leetcode%E5%8B%89%E5%BC%B7%E8%A8%98%E9%8C%B2python%E7%B7%A8)
  - [1.1. Easy](#11-easy)
    - [1.1.1. 1. Two Sum](#111-1-two-sum)
    - [1.1.2. 7. Reverse Integer](#112-7-reverse-integer)
    - [1.1.3. 9. Palindrome Number](#113-9-palindrome-number)
    - [1.1.4. 13. Roman to Integer](#114-13-roman-to-integer)
    - [1.1.5. ▲14. Longest Common Prefix](#115-%E2%96%B214-longest-common-prefix)
    - [1.1.6. 20. Valid Parentheses](#116-20-valid-parentheses)
    - [1.1.7. 26. Remove Duplicates from Sorted Array](#117-26-remove-duplicates-from-sorted-array)
    - [1.1.8. 27. Remove Element](#118-27-remove-element)
    - [1.1.9. 28. Implement strStr()](#119-28-implement-strstr)
    - [1.1.10. ▲35. Search Insert Position](#1110-%E2%96%B235-search-insert-position)
    - [1.1.11. 38. Count and Say](#1111-38-count-and-say)
    - [1.1.12. ▲53. Maximum Subarray](#1112-%E2%96%B253-maximum-subarray)
    - [1.1.13. 58. Length of Last Word](#1113-58-length-of-last-word)
    - [1.1.14. 66. Plus One](#1114-66-plus-one)
    - [1.1.15. ▲67. Add Binary](#1115-%E2%96%B267-add-binary)
    - [1.1.16. 69. Sqrt(x)](#1116-69-sqrtx)
    - [1.1.17. ▲70. Climbing Stairs](#1117-%E2%96%B270-climbing-stairs)
    - [1.1.18. ▲88. Merge Sorted Array](#1118-%E2%96%B288-merge-sorted-array)
    - [1.1.19. 118. Pascal's Triangle](#1119-118-pascals-triangle)
    - [1.1.20. 119. Pascal's Triangle II](#1120-119-pascals-triangle-ii)
    - [1.1.21. 121. Best Time to Buy and Sell Stock](#1121-121-best-time-to-buy-and-sell-stock)
    - [1.1.22. ▲122. Best Time to Buy and Sell Stock II](#1122-%E2%96%B2122-best-time-to-buy-and-sell-stock-ii)
    - [1.1.23. ▲125. Valid Palindrome](#1123-%E2%96%B2125-valid-palindrome)
    - [1.1.24. ▲136. Single Number](#1124-%E2%96%B2136-single-number)
    - [1.1.25. 155. Min Stack](#1125-155-min-stack)
    - [1.1.26. ▲167. Two Sum II - Input array is sorted](#1126-%E2%96%B2167-two-sum-ii---input-array-is-sorted)
    - [1.1.27. 168. Excel Sheet Column Title](#1127-168-excel-sheet-column-title)
    - [1.1.28. ▲169. Majority Element](#1128-%E2%96%B2169-majority-element)
    - [1.1.29. 171. Excel Sheet Column Number](#1129-171-excel-sheet-column-number)
    - [1.1.30. 172. Factorial Trailing Zeroes](#1130-172-factorial-trailing-zeroes)
    - [1.1.31. ▲189. Rotate Array](#1131-%E2%96%B2189-rotate-array)
    - [1.1.32. ▲190. Reverse Bits](#1132-%E2%96%B2190-reverse-bits)
    - [1.1.33. 191. Number of 1 Bits](#1133-191-number-of-1-bits)
    - [1.1.34. ▲198. House Robber](#1134-%E2%96%B2198-house-robber)
    - [1.1.35. 202. Happy Number](#1135-202-happy-number)
    - [1.1.36. 204. Count Primes](#1136-204-count-primes)
    - [1.1.37. ▲205. Isomorphic Strings](#1137-%E2%96%B2205-isomorphic-strings)
    - [1.1.38. 217. Contains Duplicate](#1138-217-contains-duplicate)
    - [1.1.39. 219. Contains Duplicate II](#1139-219-contains-duplicate-ii)
    - [1.1.40. 225. Implement Stack using Queues](#1140-225-implement-stack-using-queues)
    - [1.1.41. ▲231. Power of Two](#1141-%E2%96%B2231-power-of-two)
    - [1.1.42. ▲232. Implement Queue using Stacks](#1142-%E2%96%B2232-implement-queue-using-stacks)
    - [1.1.43. 242. Valid Anagram](#1143-242-valid-anagram)
    - [1.1.44. ▲258. Add Digits](#1144-%E2%96%B2258-add-digits)
    - [1.1.45. 263. Ugly Number](#1145-263-ugly-number)
    - [1.1.46. 268. Missing Number](#1146-268-missing-number)
    - [1.1.47. ▲278. First Bad Version](#1147-%E2%96%B2278-first-bad-version)
    - [1.1.48. ▲283. Move Zeroes](#1148-%E2%96%B2283-move-zeroes)
    - [1.1.49. 290. Word Pattern](#1149-290-word-pattern)
    - [1.1.50. 292. Nim Game](#1150-292-nim-game)
    - [1.1.51. 303. Range Sum Query - Immutable](#1151-303-range-sum-query---immutable)
    - [1.1.52. ▲326. Power of Three](#1152-%E2%96%B2326-power-of-three)
    - [1.1.53. 342. Power of Four](#1153-342-power-of-four)
    - [1.1.54. 344. Reverse String](#1154-344-reverse-string)
    - [1.1.55. 345. Reverse Vowels of a String](#1155-345-reverse-vowels-of-a-string)
    - [1.1.56. 349. Intersection of Two Arrays](#1156-349-intersection-of-two-arrays)
    - [1.1.57. 350. Intersection of Two Arrays II](#1157-350-intersection-of-two-arrays-ii)
    - [1.1.58. ▲367. Valid Perfect Square](#1158-%E2%96%B2367-valid-perfect-square)
    - [1.1.59. ▲371. Sum of Two Integers](#1159-%E2%96%B2371-sum-of-two-integers)
    - [1.1.60. 374. Guess Number Higher or Lower](#1160-374-guess-number-higher-or-lower)
    - [1.1.61. ▲383. Ransom Note](#1161-%E2%96%B2383-ransom-note)
    - [1.1.62. 387. First Unique Character in a String](#1162-387-first-unique-character-in-a-string)
    - [1.1.63. ▲389. Find the Difference](#1163-%E2%96%B2389-find-the-difference)
    - [1.1.64. ▲400. Nth Digit](#1164-%E2%96%B2400-nth-digit)
    - [1.1.65. ▲401. Binary Watch](#1165-%E2%96%B2401-binary-watch)
    - [1.1.66. ▲405. Convert a Number to Hexadecimal](#1166-%E2%96%B2405-convert-a-number-to-hexadecimal)
    - [1.1.67. 409. Longest Palindrome](#1167-409-longest-palindrome)

<!-- /TOC -->

## 1.1. Easy
### 1.1.1. [1. Two Sum](https://leetcode.com/problems/two-sum/)

- 2重ループで解けるが遅い
- 模範解答のHash Tableという辞書を使った解法が速い
  - 2重ループ不要
  - 1度計算した結果を順次保存し、保存済みの結果と新しい計算結果を比較していく、という考え方？

```python
# 模範解答を参考に実装
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            # 保存済みの結果と新しい計算結果を比較
            if target-nums[i] in seen:
                return [seen[target-nums[i]], i]
            else:
                seen[nums[i]]=i
```

### 1.1.2. [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

- strに変換して[::-1]、intに戻せばOK
  - 負か否か、結果がoverflowするか否かをcheck
- 模範解答はpop&push
  - 負か否か、overflowするか否かをcheck
  - abs(x)をとらないと -123 -> 789 にしてしまう
  - 速さはあまり変わらなかった
  
```python
# 模範解答を参考に実装
class Solution:
    def reverse(self, x: int) -> int:
        # pop&push
        ans = 0
        ab = abs(x)
        while ab!= 0:
            pop = ab % 10
            ans = ans * 10 + pop
            ab = int(ab / 10)
        # check
        if x<0:
            ans *= -1
        if ans>=-2**31 and ans<=2**31-1:
            return ans
        else:
            return 0
```

### 1.1.3. [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

- 7.のpopの考え方を使って逆順のリストを作成した後、リストとリストの逆順が同一か否かを判定
    - 負の数の場合は何もせずにFalse
    - strに変換せずに解けるかな？という記述があったためリストを使用
    - 7.のように逆順の数値を作ればよかったのでは？ -> overflowを起こす可能性あり（solutionより）
            - であれば半分だけ逆順にすればよい、と
- 模範解答では半分だけ逆順にしている
    - 半分だけ逆順にするアイデアを元に実装
    - 最初にエッジケースを検出し、その後半分だけの逆順を作る
    - 模範解答はwhileループ部分、if判定部分がさらに最適化されている

```python
# アイデアのみで自力実装
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負の値はFalse
        if x<0:
            return False
        # 1桁はTrue
        elif x <10:
            return True
        # 1の位に0があるとFalse
        elif x%10==0:
            return False
        else:
            rev = 0
            while x != 0:
                pop = x%10
                rev = rev*10 + pop
                
                # when x's digits is 2n+1
                if rev==x:
                    return True
                
                x = int(x/10)
                
                # when x's digits is 2n
                if rev==x:
                    return True

        return False
```

```python
# 模範解答を元に実装
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負の値はFalse
        if x<0:
            return False
        # 1桁はTrue
        elif x <10:
            return True
        # 1の位に0があるとFalse
        elif x%10==0:
            return False
        else:
            rev = 0
            # revがx以上になったら逆順作成を停止
            while x > rev:
                pop = x%10
                rev = rev*10 + pop
                x = int(x/10)
                # 桁数が偶数の場合はrevそのまま
                # 桁数が奇数の場合はrevの桁数を1つ落とす
                if x==rev or x==int(rev/10):
                    return True

        return False
```

### 1.1.4. [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

- Romanと数字との対応表をdictで作成
- IV, IXなどの特殊バージョンについての対応表も別途作成
- 入力を前から調べ、2文字見たときに特殊バージョンか否かで場合分け
    - 特殊バージョンの場合はカウンタを2つ進める
- [Discussionにあった解法](https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution)には、次の数字よりも現在の数字の方が小さい場合に現在の値をansから引いておく、という解法があった
    - 場合分けが減ってスムーズ
- [Discussionにあった解法](https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.)には他にも、特殊バージョンを前もって通常バージョンに置換しておく、という解法も

```python
# 自力実装
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # 特殊バージョンも辞書化
        roman_ex_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        ans = 0
        cnt = 0
        # 特殊バージョンだと2文字分進める必要があるためforではなくwhile
        while cnt<len(s)-1:
            # 特殊バージョンに合致するかcheck
            if s[cnt:cnt+2] in roman_ex_dict:
                ans += roman_ex_dict[s[cnt:cnt+2]]
                cnt += 2  # 特殊バージョン2文字分進める
            else:
                ans += roman_dict[s[cnt]]
                cnt += 1
        # 最後の文字は2文字分checkしようとするとIndexErrorになるため別途check
        if cnt==len(s)-1:
            ans += roman_dict[s[cnt]]

        return ans
```

### 1.1.5. ▲[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

- 愚直に比較していく
    - 遅め（全solutionの50%くらいの速さ）
- ▲公式の別解アルゴリズムはまだ理解が追いついていない
- Solutionへの投稿では以下のような解法もあった
    - strsリストをソートして最初と最後の要素だけをzipで比較している解法
    - strsリストの全要素の頭から1文字ずつzipで抜き出してsetでまとめ、setの長さが1の間はprefixに追加していく解法

```python
# ゴリ押し（自力実装）
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 空リスト対策
        if not strs:
            return ""
        else:
            ans = strs[0]
            tmp = ""
            cnt = 0
            for i in range(len(strs)):
                while True:
                    if cnt<=len(ans)-1 and cnt<=len(strs[i])-1:
                        # 暫定解答と対象文字列が先頭から一致している限り、文字をtmpに追加していく
                        if strs[i][cnt]==ans[cnt]:
                            tmp += strs[i][cnt]
                            cnt += 1
                        # 一致しなくなったら暫定解答を更新
                        else:
                            ans = tmp
                            tmp = ""
                            cnt = 0
                            break
                    else:
                        ans = tmp
                        tmp = ""
                        cnt = 0
                        break

        return ans
```

### 1.1.6. [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

- 先入れ後出し(FILO)のstack方式を採用
    - 処理速度はかなり速い
    - 模範解答もstack方式
- 再帰的構造と捉えて(), {}, []のペアを削除していく方法もある
    - コード数が少ないが、stack方式よりも遅い
    - Solutionに投稿されていたものも参考に

```python
# FILOのstack方式（自力実装）
class Solution:
    def isValid(self, s: str) -> bool:
        stack = 'x'  # IndexErrorを防ぐためxを入れておく
        b_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for x in s:
            # 閉じカッコの場合はstackの最後とペアかどうかをcheck
            if x in b_dict:
                if b_dict[x]==stack[-1]:
                    stack = stack[:-1]
                else:
                    return False
            # 閉じカッコ以外の場合はstackに積む
            else:
                stack += x
        # stackがきれいになっていればうまくカッコペアがなされていたと判断
        if stack=='x':
            return True
        else:
            return False

```

```python
# 再帰的構造方式（Solutionを参考に実装）
class Solution:
    def isValid(self, s: str) -> bool:
        # カッコペアを削除し続けるループで文字列の長さの半分を得るときに面倒なので
        if len(s)%2==1:
            return False
        # 文字列の長さの半分の回数、カッコペアを削除し続ける
        # 再帰的構造なので内側のカッコペアから順に消えていく
        for _ in range(int(len(s)/2)):
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        # カッコペアを削除し続けて何も残らなければOK
        return s==""

```

### 1.1.7. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

- 入力リストを破壊的に重複削除する
    - メモリ節約問題
- リスト変更後、リストの長さを数値で返す
- リスト名に新規代入しても元のリストが参照されてしまう
    - この挙動を理解するのにまず少し時間がかかった
    - 「Clarification:」に書かれていたのを見逃していた
- list.pop()を使用して重複する値を削除した
- 模範解答はリストの前半だけ変更し、最後に変更部分の長さだけを返すという方法
    - popせず、リストの要素として代入しているだけで実現している
    - 速い

```python
# カウンタを2つ使用してpopする（自力実装）
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 空リストのケースに対処
        if nums==[]:
            return 0
        
        nums_len = len(nums)
        tmp = nums[0]
        cnt1 = 1  # 更新されるnumsの現在位置を管理するカウンタ
        cnt2 = 1  # 元のnumsの値をすべて確認したか管理するカウンタ
        while cnt2<=nums_len-1:
            if nums[cnt1]==tmp:
                nums.pop(cnt1)
            else:
                tmp = nums[cnt1]
                # popしなかった場合だけカウンタを進める
                cnt1 += 1
            
            cnt2 += 1

        return len(nums)
```

```python
# リストの前半だけ変更し、最後に変更部分の長さだけを返す（模範解答を参考に実装）
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 空リストのケースに対処
        if nums==[]:
            return 0

        cnt = 0
        for i in range(len(nums)):
            if nums[cnt]!=nums[i]:
                cnt += 1  # 下の行との順番が重要
                nums[cnt] = nums[i]
            
        return cnt+1
```

### 1.1.8. [27. Remove Element](https://leetcode.com/problems/remove-element/)

- 上の26. と似た問題
    - 与えられた値に合致する要素を削除する変更を入力リストにin-placeで行う
    - 同じくTwo pointersのやり方でいけた
    - numsの要素がvalのとき、値の置き換えもpntのカウントもスキップする
    - 26.の教訓を活かして実装できたのは嬉しい
- 別解として、valの要素をリストの後ろの方と入れ換えていく方法がある
    - valの要素が少ない場合、要素の代入回数が減る

```python
# Two pointers（自力実装）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pnt = 0
        for i in range(len(nums)):
            # numsの要素がvalのときは値の置き換えもpntのカウントもスキップ
            if nums[i]!=val:
                nums[pnt] = nums[i]
                pnt += 1
                
        return pnt
```

```python
# val要素が少ない場合（模範解答を参考に実装）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        pnt = 0
        while pnt<n:
            if nums[pnt]==val:
                nums[pnt] = nums[n-1]
                n -= 1
            else:
                pnt += 1
                
        return n
```

### 1.1.9. [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

- haystackを前から順にneedleの長さ分切り取ってneedleと比較
    - 少し遅め

```python
# 自力実装
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        
        needle_len = len(needle)
        for i in range(len(haystack)):
            # haystackを前から順にneedleの長さ分切り取ってneedleと比較
            if haystack[i:i+needle_len]==needle:
                return i
            
        return -1
```

### 1.1.10. ▲[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

- 普通に前から順に比較
    - O(n)
- Discussionではbinary searchによってO(log n)でいけるとの話が
    - binary searchの復習を
    - 実行してみても実はそんなに速くない？

```python
# O(n)（自力実装）
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
            
        return i+1
```

```python
# binary search（Discussionを参考に実装）
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = int((left+right)/2)
            if nums[middle]==target:
                return middle
            if nums[middle]<target:
                left = middle+1
            else:
                right = middle-1
        return left
```

### 1.1.11. [38. Count and Say](https://leetcode.com/problems/count-and-say/)

- ポインタを2つ、カウンタを1つ使って実装
    - ノートに動きを書いてコードに起こした
    - while内のelseを通過せずにwhileループが終了した場合、tmp_ansが更新されずにansが更新される問題があったため、対処
- Discussionでは上述の方法に加え、再帰的な方法やリスト・joinを使った方法もあった
    - リスト・joinの方が速いらしい（最初に思いついた方法だが、遅いのかなと思って避けてしまった）
    - 再帰的な方法は以前の問題でも見かけたが、よく分かっていない
        - 身につけなければ…

```python
# 自力実装
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        ans = "1"
        for _ in range(1, n):
            i = 0
            j = 0
            c = 0
            tmp_ans = ""
            while i<=len(ans)-1:
                if ans[i]==ans[j]:
                    c += 1
                    i += 1
                else:
                    tmp_ans = tmp_ans + str(c) + ans[j]
                    j = i
                    c = 0
            if c!=0:  # elseを通過せずにwhileループが終了した場合にtmp_ansを更新するため
                tmp_ans = tmp_ans + str(c) + ans[j]
            ans = tmp_ans
        return ans
```

### 1.1.12. ▲[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- ブルートフォース -> O(n^2)でTLE
- 解法が分からなかった
- DiscussionではDP（動的計画法）での実装があった
    - 足し算継続 or リセットして今の値からスタート
    - これまで見てきた中で一番大きい値を保持
    - 以下のコード読んでからこの[Youtubeムービー](https://www.youtube.com/watch?v=2MmGzdiKR9Y)観ると分かりやすかった
        - Discussionに貼られていた。7:30くらいから観ると動的計画法で解く様子が観られる
- ▲DPを勉強する必要あり

```python
# O(n^2)でTLEだった（自力実装）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n^2) -> TLE
        ans = nums[0]
        l = len(nums)
        for i in range(l):
            for j in range(i, l):
                tmp = sum(nums[i:j+1])
                if ans<tmp:
                    ans = tmp
        return ans
```

```python
# Discussionを参考に実装
# 参考：https://leetcode.com/problems/maximum-subarray/discuss/20194/A-Python-solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = -float("inf")
        for n in nums:           
            current_sum = max(current_sum+n, n)  # 足し算継続 or リセットして今の値からスタート
            max_sum = max(max_sum, current_sum)  # これまで見てきた中で一番大きい値を保持
        return max_sum
```

### 1.1.13. [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

- 前から順にアルファベットをカウントしていき、スペースに当たったらリセットする
    - スペースが連続で続く場合、特に最後に連続スペースがある場合が面倒だった
    - スペースでのリセット前にカウント数を別の変数に退避させておくことで対処
    - そこそこ速い
- Discussionでは逆順にしてから最初の文字塊の数を数えている方法（cntが非0かつスペースでbreak）や、.split()してリストの最終要素の長さを返す方法が取られている
    - Pythonの関数やメソッドはどこまで使ってよいのだろうか

```python
# 自力実装
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==1:
            if s==" ":
                return 0
            else:
                return 1
        if s[0]==" ":
            cnt = pre_cnt = 0        
        else:
            cnt = pre_cnt = 1
        for i in range(1, len(s)):
            if s[i]==" " and s[i-1]!=" ":
                pre_cnt = cnt
                cnt = 0
            elif s[i]==" ":
                continue
            else:
                cnt += 1
        if s[-1]==" ":
            return pre_cnt
        else:
            return cnt
```

### 1.1.14. [66. Plus One](https://leetcode.com/problems/plus-one/)

- 型変換に頼った方法で解いた
    - list -> str -> intに型変換して1を足す
    - int -> strに型変換してfor文に入れる
    - str -> intに型変換してlistに加えていく
- Discussionには1-lineで似たような処理をしている解法や、再帰的な解法があった
    - リスト内包表記でreturnのリストを作ればよかった

```python
# 自力実装
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for x in digits:
            s += str(x)
        n = int(s)
        n += 1
        digits_pls_1 = []
        for i in str(n):
            digits_pls_1.append(int(i))
        return digits_pls_1
```

```python
# リスト内包表記バージョン（Discussionを参考に実装）
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for x in digits:
            s += str(x)
        n = int(s) + 1
        return [int(i) for i in str(n)]
```

### 1.1.15. ▲[67. Add Binary](https://leetcode.com/problems/add-binary/)

- 次こそ再帰的な方法を使おうと試行錯誤したが、できず
- 下の桁から順に足し算を進める方法でゴリ押し実装した
    - 繰り上がりが厄介
- Discussionでも[再帰的な方法で解かれていた](https://leetcode.com/problems/add-binary/discuss/24500/An-accepted-concise-Python-recursive-solution-10-lines)ので、参考にして実装してみた
    - コードを読むだけでは分からなかった
    - ノートに書いて処理の流れを追っていくと、確かに再帰的に解けている
    - ▲現段階では同様の問題でも再帰的な実装ができる気はしない

```python
# 自力実装
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1桁同士の2進数の足し算関数を定義
        def add_binary(ae, be):
            if ae=="0" and be=="0":
                return "0"
            elif ae=="1" and be=="1":
                return "10"
            else:
                return "1"

        ans = ""
        cnt = 0
        # a, bの長さを揃えるために短い方の頭を0でpadding
        if len(a)>len(b):
            for _ in range((len(a)-len(b))):
                b = "0" + b
        elif len(a)<len(b):
            for _ in range((len(b)-len(a))):
                a = "0" + a
        # 下の桁から順に足し算
        for ae, be in zip(a[::-1], b[::-1]):
            tmp_ans = add_binary(ae, be)
            if len(ans)==cnt:
                ans = tmp_ans + ans
            else: ## 繰り上がりが発生している場合、桁数とループ回数が一致しない
                if tmp_ans=="10":  # 現在の足し算も繰り上がりがある場合
                    ans = "11" + ans[1:]
                else:
                    ans = add_binary(tmp_ans, ans[0]) + ans[1:]
            cnt += 1
        return ans
```

```python
# 再帰的な方法（Discussionの写し）
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1]=="1" and b[-1]=="1":
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        if a[-1]=="0" and b[-1]=="0":
            return self.addBinary(a[:-1], b[:-1]) + "0"
        else:
            return self.addBinary(a[:-1], b[:-1]) + "1"
```

### 1.1.16. [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

- 二分探索で解いた
    - 二分探索なのでO(log n)のはずだが、比較的遅い解法になっている
- Discussionでも二分探索で解かれている
    - もう少しきれいなコードで書かれている
    - こちらの方が速い


```python
# 自力実装
class Solution:
    def mySqrt(self, x: int) -> int:
        leftx = 1
        rightx = x
        halfx = int((leftx+rightx)/2)
        while True:
            if halfx**2<=x and (halfx+1)**2>x:
                return halfx
            if halfx**2<x:
                leftx = halfx
                halfx = int((halfx+rightx)/2)
            else:
                rightx = halfx
                halfx = int((halfx+leftx)/2)
```

```python
# リファクタリング版（Discussionを参考に実装）
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        leftx = 1
        rightx = x
        while leftx<=rightx:
            halfx = int((leftx+rightx)/2)
            if halfx*halfx<=x<(halfx+1)*(halfx+1):
                return halfx
            if halfx*halfx<x:
                leftx = halfx
            else:
                rightx = halfx
```

### 1.1.17. ▲[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

- 紙の上でも解き方が分からなかった問題
- Solutionでは再帰的な解法、動的計画法による解法
    - ▲動的計画法で考えると、iの段に行く方法はi-1の段から・i-2の段からの2通りで、これを順次足し合わせていけばOK
        - 完全にフィボナッチ数列なのでリストを使わなくても解ける。フィボナッチ数列の公式を使うなど

```python
# 動的計画法（Solutionを参考に実装）
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

### 1.1.18. ▲[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

- アルゴリズムとしての解き方は分からなかったので、list.sort()を使用した
- ▲Discussionでは後ろから埋めていく解法
    - nums1の後ろにせっかくスペースを取っているのだから、そこから埋めるという方針

```python
# 自力実装
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            pass
        else:
            nums1[m:] = nums2
            nums1.sort()
```

```python
# Discussionを参考に実装
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]<=nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        if n>0:
            nums1[:n] = nums2[:n]
```

### 1.1.19. [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

- 処理の流れを素直に実装した
- SolutionはDPで解いていた
    - 自力実装と大体同じ

```python
# 自力実装
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        ans = [[1]]
        for row in range(1, numRows):
            lis = [1]
            lis_prev = ans[-1]
            for i in range(row-1):
                lis.append(lis_prev[i]+lis_prev[i+1])
            lis.append(1)
            ans.append(lis)
        return ans
```

### 1.1.20. [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

- 試行錯誤したものの、リスト内でやりくりするのは無理だった
    - リスト内でやりくり、ではなく解答の他に余分なスペースは`O(k)`まで、ということだった？
- Discussionにシンプルな解法あり
    - https://leetcode.com/problems/pascals-triangle-ii/discuss/38467/Very-simple-Python-solution
    - これが問題の条件を満たしているのか…？

```python
# Discussionを参考に実装
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            ans = [x+y for x, y in zip([0]+ans, ans+[0])]
        return ans
```

### 1.1.21. [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

- 処理の流れをそのまま実装

```python
# 自力実装
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        min_buy = prices[0]
        profit = 0
        for buy in prices[1:]:
            if min_buy>buy:
                min_buy = buy
            else:
                profit = max(profit, buy-min_buy)
        return profit
```
### 1.1.22. ▲[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

- 処理の流れをそのまま実装
    - 前から順に値段を見ていき、極小（次の日に値段が上がる日）で購入して極大（次の日に値段が下がる日）で売る、を繰り返す
    - 「次の日に株価が上がるか下がるか」を精度高く予測できれば、このアルゴリズムを使ってうまくお金儲けが出来そう
- Solutionにはさらにシンプルな実装あり
    - ▲考え方は似ているが、より単純化されていて美しい
    - 自力実装の方が速い（無駄な計算をif文で除けているから？）

```python
# 自力実装
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        buy = prices[0]
        profit = 0
        ans = 0
        for i in range(len(prices)):
            if buy>prices[i]:
                buy = prices[i]
            else:
                profit = max(profit, prices[i]-buy)
            if prices[i]<prices[i-1]:
                ans += profit
                profit = 0
                buy = prices[i]
        if buy<prices[i]:
            ans += profit
        return ans
```

```python
# Solutionを参考に実装
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        sum_profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                sum_profit += prices[i]-prices[i-1]
        return sum_profit
```

### 1.1.23. ▲[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

- 文字列を前処理して、前からと後ろからを比較
    - リストを使用しており、リストのコピーと比較しているため使用メモリは大きい
- ▲Discussionにはリストを使わず、2つのポインタで比較を回す方法が載せられていた
    - 速度は遅いが使用メモリは少なくて済む

```python
# 自力実装
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        lis = [x for x in s.lower() if x.isalnum()]
        return lis==lis[::-1]
```

```python
# Discussionを参考に実装
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower()!=s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

### 1.1.24. ▲[136. Single Number](https://leetcode.com/problems/single-number/)

- 条件：runtime: O(n), memory: 余計なメモリは使わないこと
- list.sort()を使って実装
    - 速さ・メモリともに微妙
- Solusionには条件を満たす方法・満たさない方法が掲載されていた
    - 別リストを作成して数値が入っているかどうかをinで確認する方法, O(n^2); O(n).
    - 辞書を作成して数値が入っているかどうかを.pop()で確認する方法, O(n); O(n).
        - 辞書型の.popはO(1)なので速い
    - 計算で解く方法, O(n); O(n).
        - (a+b+c)*2-(a+a+b+b+c)
    - ▲各要素のXORを取る方法, O(n); O(1).
        - a ^ b でXORを取れる
        - a^0 -> a
        - a^a -> 0
        - a^b^a -> a^a^b -> 0^b -> b
        - Solutionのコメントでの褒め言葉多数

```python
# 自力実装
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i += 2
            else:
                if nums[i+1]==nums[i+2]:
                    return nums[i]
        return nums[i]
```

```python
# 辞書使用（Solutionを参考に実装）
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        has = {}
        for i in nums:
            try:
                has.pop(i)
            except KeyError:
                has[i] = 1
        return has.popitem()[0]
```

```python
# XOR使用（Solutionを参考に実装）
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
```

### 1.1.25. [155. Min Stack](https://leetcode.com/problems/min-stack/)

- リストを使用したが、そういうことではないのだと思う…これではただのリスト
    - 処理も遅い
- Discussionでもリストを使用していた
    - ただし、min()は使用していなかった

```python
# 自力実装
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

```python
# Solutionを参考に実装
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        current_min = self.getMin()
        if current_min==None or current_min>x:
            current_min = x
        self.stack.append((x, current_min))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]


    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
```

### 1.1.26. ▲[167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

- ▲ブルートフォースはTLE, 二分探索もどきはうまく結果を得られない, という状況でギブアップ
- Discussionではtwo pointer, dictionary, binary searchによる解法があった
    - dictionaryは[1. Two Sum](https://leetcode.com/problems/two-sum/)で見た解法と同じ

```python
# two pointer（Solutionを参考に実装）
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            sum_num = numbers[r]+numbers[l]
            if sum_num==target:
                return [l+1, r+1]
            elif sum_num<target:
                l += 1
            else:
                r -= 1
```

```python
# dictionary（Solutionを参考に実装）
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(numbers):
            if target-n in dic:
                return [dic[target-n]+1, i+1]
            dic[n] = i
```
```python
# binary search（Solutionを参考に実装）
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            # 候補の1つ{numbers[i+1]}を昇順で順番に確認していく
            # ペアの数を残りの数{numbers[i+1], numbers[len(numbers)-1]}から二分探索で探す
            l, r = i+1, len(numbers)-1
            dif = target-numbers[i]
            while l<=r:
                mid = l + (r-l)//2
                if dif==numbers[mid]:
                    return [i+1, mid+1]
                elif dif>numbers[mid]:
                    l = mid+1
                else:
                    r = mid-1
```

### 1.1.27. [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)

- 26進法として解こうとするも、Zの扱いがうまくいかなかったりしてアウト
- Discussionでも26進数として解かれていた
    - 26で割った商でnを更新していくなど、近いところまでは自分でも考えられていたが、あと一歩及ばず…
    - n%26, n//26ではなく(n-1)%26, (n-1)//26を使うのが要
    - [このDiscussionの解説](https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation)が分かりやすい

```python
# 一部ケースがうまく通らなかった自力実装
class Solution:
    def convertToTitle(self, n: int) -> str:
        dic = {}
        # upper-case A-Z
        for i in range(1, 26):
            dic[i] = chr(i+64)
        dic[0] = "Z"
        ans = dic[n%26]
        r_sum = 26 if n%26==0 else n%26
        x = 2
        while 26**x<n:
            r = 1 if (n-r_sum)%(26**x)/(26**(x-1))==0 else (n-r_sum)%(26**x)/(26**(x-1))
            ans = dic[r] + ans
            r_sum = n%(26**x)
            x += 1
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def convertToTitle(self, n: int) -> str:
        dic = {}
        # upper-case A-Z
        for i in range(26):
            dic[i] = chr(i+65)
        ans = ""
        while 0<n:
            ans = dic[(n-1)%26] + ans
            n = (n-1)//26
        return ans
```

### 1.1.28. ▲[169. Majority Element](https://leetcode.com/problems/majority-element/)

- 辞書型のオブジェクトに値の出現回数を記録していった
    - 遅い <- 不要な処理がループ内に入っていたことが原因の一つ
- ▲Solutionでは6種類もの解法が紹介されていた
    - ソートして真ん中の値を返す
        - n/2以上を占めるため、リスト内での大きさが何であれ、真ん中はmajorityの数になる
    - ランダムに値を選び、その値がリスト内でn/2以上を占めるかどうかを判定
        - ブルートフォースよりは速くなる可能性もある、といったところか
    - divide & conquer approach...左右に分割していく再帰的な解法
        - 再帰ということもあり、分かりにくい
    - ▲Boyer-Moore Voting Algorithm...候補の値を決め、候補の値ならば+1, それ以外ならば-1, 0になったら次の候補, とする方法
        - elegant!

```python
# 自力実装
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt_dic = {}
        for n in nums:
            if n in cnt_dic:
                cnt_dic[n] += 1
            else:
                cnt_dic[n] = 1
        return max(cnt_dic, key=cnt_dic.get)
```

```python
# sort（Solutionを参考に実装）
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
```

```python
# Boyer-Moore Voting Algorithm（Solutionを参考に実装）
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = None
        for num in nums:
            if cnt==0:
                candidate = num
            cnt += 1 if num==candidate else -1
        return candidate
```

### 1.1.29. [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

- 168. の逆. 26進数を実装するだけ

```python
# 自力実装
class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {}
        for i in range(1, 27):
            dic[chr(i+64)] = i
        ans = 0
        for i, a in enumerate(s[::-1]):
            ans += (dic[a])*(26**i)
        return ans
```

### 1.1.30. [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

- 階乗を計算して末尾の0の数を数えようとするとTLEになる
    - 因数5の数を数えればよいのでは？と思ってn//5を出すも、答えより小さい
    - 25, 125などの倍数がたくさんの5を因数として持っているせい
- Discussionでも因数5の数を数えている
    - 5で割った商を足して、n=n//5して、5で割って...と繰り返すことで、5a+25b+125c...を求められる

```python
# Solutionを参考に実装
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n>0:
            n = n//5
            cnt += n
        return cnt
```

### 1.1.31. ▲[189. Rotate Array](https://leetcode.com/problems/rotate-array/)

- 3種類の解法、memory=O(1)の解法が要求されている
    - スライシングで実装
    - ポインタを用いた実装にも挑戦したが、一部ケースでうまくいくのみ
- ▲Solutionでは新しいリストを作成する方法、Cyclicに置き換えていく方法、Reverseをうまく使う方法が紹介されていた

```python
# スライシングを用いた自力実装
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ver.1
        k = k%len(nums)  # numsのサイズよりも大きいkを与えられた場合
        if k!=0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
```

### 1.1.32. ▲[190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)

- 2\*\*31, 2\*\*30, ...と順に割っていって、割れた場合に2\*\*0, 2\*\*1, ...と順に足していく
- Discussionでは文字列処理を掛けるone lineの解法が分かりやすかった
    - ▲bitの処理もあったが、`>>`, `<<`といった知らない記法が使われていた
        - bit処理も学ばないと
        - 参考記事: [Python ビット演算 超入門 - Qiita](https://qiita.com/7shi/items/41d262ca11ea16d85abc)
        - 参考記事: [Pythonのビット演算子（論理積、論理和、排他的論理和、反転、シフト）](https://note.nkmk.me/python-bit-operation/)

```python
# 自力実装
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            j = 31-i
            if n//(2**(j))==1:
                ans += 2**i
                n = n%(2**(j))
        return ans
```

```python
# one line（Discussionを参考に実装）
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int("{:032b}".format(n)[::-1], 2)
```

### 1.1.33. [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

- 32bitへの文字列変換(`"{:032b}".format(n)`)を使用した解法(16ms)、10進数数値を2**xで割っていく解法(32ms)を実装した
- Solutionでは`n&(n-1)`でnを更新し続けることで1を小さい桁から1つずつ減らしていく手法が紹介されていた(20ms)


```python
# 文字列処理での解法（自力実装）(16ms)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for s in "{:032b}".format(n):
            ans += int(s)
        return ans
```

```python
# 10進数数値処理での解法（自力実装）(32ms)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            j = 31-i
            if n//(2**j)==1:
                ans += 1
            n = n%(2**j)
        return ans
```

```python
# Solutionを参考に実装(20ms)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n!=0:
            ans += 1
            n = n&(n-1)
        return ans
```

### 1.1.34. ▲[198. House Robber](https://leetcode.com/problems/house-robber/)

- 解法思いつかず...
- ▲Discussionで[DPによる解法](https://leetcode.com/problems/house-robber/discuss/55977/Python-DP-solution-4-line-O(n)-time-O(1)-space-easy-to-understand-with-detailed-explanation)が解説されている
    - window size = 4 として、ずらしながら計算していく
    - [1, 2, 3, 4, 5, 6]の場合、

```
[0, 0, 0, 1, 2, 3, 4, 5, 6] と先頭に3つ0をpaddingして
|0  0  0  1| |  |  |  |  |   max(0+1, 0+1) = 1
  | 0  0  1  2| |  |  |  |   max(0+2, 0+2) = 2
    |  0  1  2  4| |  |  |   max(0+3, 1+3) = 3
       |  1  2  4  6| |  |   max(1+4, 2+4) = 6
          |  2  4  6  9| |   max(2+5, 4+5) = 9
             |  4  6  9  12| max(4+6, 6+6) = 12
```
と計算していく。elegant! DPを使いこなせるようになりたい。

```python
# Discussionを参考に実装
class Solution:
    def rob(self, nums: List[int]) -> int:
        p3, p2, p1 = 0, 0, 0
        for i in range(len(nums)):
            cur = nums[i]
            p3, p2, p1 = p2, p1, max(p3+cur, p2+cur)
        return max(p2, p1)
```

### 1.1.35. [202. Happy Number](https://leetcode.com/problems/happy-number/)

- 桁数が不明なので、while文で各桁の2乗を加算していった
    - 計算結果を保存しておき、一度出た計算結果がもう一度出たらループに入ったと判断してFalseを返す
- Discussionではnを文字列変換して各文字についてfor文で2乗を取る解法も見られた

```python
# 自力実装
class Solution:
    def isHappy(self, n: int) -> bool:
        lis = []
        while True:
            new_n = 0
            while n>0:
                new_n += (n%10)**2
                n = n//10
            if new_n==1:
                return True
            n = new_n
            if n in lis:
                return False
            lis.append(n)
```

### 1.1.36. [204. Count Primes](https://leetcode.com/problems/count-primes/)

- 2からnまでの各数を、2からn-1までの数で割った余りを確認するというゴリ押し実装をしたところ、TLE
- [エラトステネスの篩](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)をPythonで実装するも、TLE
    - 最初よりは処理できる桁数が増えた
- Discussionもエラトステネスの篩を使用している
    - すべて1のリストを作成しておき、素数以外を0に変更していく
    - 実装力の問題でTLEになってしまったのか

```python
# エラトステネスの篩の説明を見て自力実装（TLE）
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        lis = [i for i in range(2, n)]
        p = lis[0]
        pn = [p]
        while p<math.sqrt(n):
            lis = [i for i in lis if i%p!=0]
            p = lis[0]
            pn.append(p)
        pn.extend(lis[1:])
        return len(pn)
```

```python
# Discussionを参考に実装
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        lis = [1]*n
        lis[0], lis[1] = 0, 0
        for i in range(2, int(n**0.5)+1):
            if lis[i]==1:  # 0になっていないインデックスを見つけたら、その倍数のインデックスを0に更新
                lis[i*i:n:i] = [0]*len(lis[i*i:n:i])
        return sum(lis)
```

### 1.1.37. ▲[205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

- まずs->t, t->sの変換辞書を作成。s, tのコピーを作成した後、s, tをそれぞれ変換。変換後のs, tとコピーしておいたt, sを比べて、両方とも一致した場合にTrueを返す
    - s, t, 両方を処理しないとs="ab", t="aa"といったケースに間違ってTrueを返してしまう
    - s, tの変換をforループで行った場合、処理が遅い
    - s, tの変換を`s.translate(str.maketrans(dic_s))`で行った場合、速さは4倍ほど改善
        - まだ遅い
- Discussionではone lineの解法あり
    - set(zip(s, t))のlen()とset(s), set(t)のlen()が全て一致するかどうかで判定
        - elegant!
        - 詳細は以下で紹介
    - `str.find()`を使った解法も
    - ▲他にも[複数の解法あり](https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).)

```python
# 自力実装
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        if len(s)<=1:
            return s==t

        # s->tの変換辞書を作成
        dic_s = {}
        for i in range(len(s)):
            dic_s[s[i]] = t[i]

        # t->sの変換辞書を作成
        dic_t = {}
        for i in range(len(t)):
            dic_t[t[i]] = s[i]

        # s->tに変換
        s2 = s
        for i in range(1, len(s)-1):
            s = s[:i]+dic_s[s[i]]+s[i+1:]
        s = dic_s[s[0]]+s[1:]
        s = s[:-1]+dic_s[s[-1]]

        # t->sに変換
        t2 = t
        for i in range(1, len(t)-1):
            t = t[:i]+dic_t[t[i]]+t[i+1:]
        t = dic_t[t[0]]+t[1:]
        t = t[:-1]+dic_t[t[-1]]
        
        return s==t2 and s2==t
```

```python
# one line解法（Discussionを参考に実装）
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t)))==len(set(s))==len(set(t))

# Discussionの解法を解説
s = "aa"
t = "ab"
print(set(zip(s, t)))
print(set(zip(t, s)))
print(set(s))
print(set(t))
# とすると、stdoutは
{('a', 'b'), ('a', 'a')}
{('b', 'a'), ('a', 'a')}
{'a'}
{'b', 'a'}
# len()は不一致

s = "egg"
t = "add"
print(set(zip(s, t)))
print(set(zip(t, s)))
print(set(s))
print(set(t))
# とすると、stdoutは
{('e', 'a'), ('g', 'd')}
{('d', 'g'), ('a', 'e')}
{'g', 'e'}
{'a', 'd'}
# len()が一致
```

```python
# `str.find()`を使った解法（Discussionを参考に実装）
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            # 各文字が文字列のどこで最初に出現するかを比較
            # 構造が同じであれば一致するはず
            if s.find(s[i])!=t.find(t[i]):
                return False
        return True
```

### 1.1.38. [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

- おそらく実装するべき解法とは異なるが、引数のnumsの長さとnumsのset()の長さを比較するだけ
- 値と値の出現回数の辞書を作成し、出現回数が2以上の値が存在するかどうかを判定しても解ける
- Solutionでは、ソートして連続した値があるかどうか判定する方法、ハッシュテーブルを使用する方法が紹介されていた

```python
# set()を使用した自力実装
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
```

```python
# 辞書型オブジェクトを使用した自力実装
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            dic[i] = dic.setdefault(i, 0) + 1
        for j in dic.values():
            if j>1:
                return True
        return False
```

### 1.1.39. [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

- 最初は途方に暮れたが、一晩寝たらできた
- ブルートフォースで書けるもののTLE
- 重複する値のインデックス差がk**以下**という条件を見逃していた
    - k以下でいいなら最も近い値同士の距離を見ればよい
    - 辞書に各値とインデックスを保存し、インデックスを更新していく
        - numsのスキャンにn, 辞書のスキャンにn/2, 処理時間はO(n**2)かかると危惧したが、通った
        - Discussionを見ると、dic.get()を使えば存在しないキーの場合に指定の値を返せる
            - 普通に辞書をスキャンした方が速い

```python
# 自力実装（辞書スキャン）
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i-dic[nums[i]]<=k:
                    return True
            dic[nums[i]] = i
        return False
```

```python
# Discussionを参考に実装（dic.get()）
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if i-dic.get(nums[i], -k-1)<=k:
                    return True
            dic[nums[i]] = i
        return False
```

### 1.1.40. [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

- リストの機能を使ってstackを実装
    - FIFOのqueueでは実現できない機能（`list[-1]`, `list[:-1]`）を使用しているため、題意には沿っていないと考えられる
- 2つのqueueを使用して実装したものの、触っていないq2もq1の動きに連動して要素が消えていくという謎の挙動があり、Acceptに至らず
- Solutionでは2つのqueueを使用した実装、1つのqueueを使用した実装が紹介されていた
    - queueを1つだけ使用する方法はpush時にLIFOとなるように並び替える
        - 他のメソッドはqueueと同様の処理をするだけでよくなる

```python
# 自力実装
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.top()
        self.stack = self.stack[:-1]
        return x


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.stack:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

```python
# queueを1つだけ使用する方法（Solutionを参考に実装）
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.pop(0))


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.pop(0)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q1:
            return False
        else:
            return True
```

### 1.1.41. ▲[231. Power of Two](https://leetcode.com/problems/power-of-two/)

- エッジケース(n=1, 0, 負の整数)に注意して2で割り続ける
- ▲Discussionではbitを利用したone lineの解法あり
    - `2**x`をビットで表すと`1=1b, 2=10b, 4=100b, 8=1000b, ......`となる
    - `2**(x-1)`をビットで表すと`0=0b, 1=01b, 3=011b, 7=0111b, ......`となる
    - `2**(x-1)`では2進数の計算ですべての桁で繰り下がりが発生するため、`2**x`と`2**(x-1)`の`&`をとると`0000b`になる

```python
# 自力実装
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n>1:
            if n%2!=0:
                return False
            n /= 2
        if n<=0:
            return False
        elif n==1:
            return True
```

### 1.1.42. ▲[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

- `pop`, `peak`時に別のstackに移す
    - `pop`では値を`return`する前に同じ処理を行い、stackを元に戻しておく
        - 別の処理時に更に逆順にしてしまうことになるため
- 225.のようにpush時に逆順にして扱おうとしたものの、queueとは処理が違ったためにうまくいかず
- Solutionを見ると、225.のようにpush時に逆順にする実装が紹介されていた
- ▲Solutionには他にも、別のstackをうまく使った処理が行われていた
    - すべての要素を別stackに移すのではなく、sが空になるたびに移す
    - sが空かどうか、別のstackが空かどうか、という状態判定をうまく使っている
    - elegant!

```python
# 自力実装
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp_s = []
        while self.s:
            tmp_s.append(self.s.pop(-1))
        self.s = tmp_s
        ans = self.s.pop(-1)

        tmp_s = []
        while self.s:
            tmp_s.append(self.s.pop(-1))
        self.s = tmp_s
        return ans


    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp_s = []
        s_copy = self.s.copy()
        while s_copy:
            tmp_s.append(s_copy.pop(-1))
        return tmp_s[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

```python
# Solutionを参考に実装
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        tmp_s = []
        while self.s:
            tmp_s.append(self.s.pop(-1))
        self.s.append(x)
        while tmp_s:
            self.s.append(tmp_s.pop(-1))
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s.pop(-1)


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s)==0
```

### 1.1.43. [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

- Pythonの組み込み関数`sorted()`で文字列をソート済みリストに変換し、比較した
- 組み込み関数を使わないのであれば、辞書を用いた方法が考えられる
- Solutionでもこれら2つの方法が紹介されていた


```python
# 自力実装
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted_list = sorted(s)
        t_sorted_list = sorted(t)
        return s_sorted_list==t_sorted_list
```

```python
# 半分自力、半分Solutionを参考に実装
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        for x in s:
            s_dic[x] = 1+s_dic.get(x, 0)
        for y in t:
            if y in s_dic:
                s_dic[y] -= 1
            else:
                return False
        for k in s_dic:
            if s_dic[k]!=0:
                return False
        return True
```

### 1.1.44. ▲[258. Add Digits](https://leetcode.com/problems/add-digits/)

- まずはwhileループを使用して普通に実装
- ▲Follow upではwhileも再帰も使用せずにruntime O(1)での実行を要求
    - 11は2になる->`11%9=2`から、9で割った余りを使用することを考える
    - `%9`だけだと`9`の答えが`0`になってしまうので、`(n-1)%9 + 1`として対応

```python
# 自力実装
class Solution:
    def addDigits(self, num: int) -> int:
        x = num
        while x/10>=1:
            num = x
            x = 0
            while num>0:
                x += num%10
                num = num//10
            x += num%10
        return x
```

```python
# Discussionを参考に実装
class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return num
        
        return (num-1)%9+1
```

### 1.1.45. [263. Ugly Number](https://leetcode.com/problems/ugly-number/)

- 2で割れるところまで割って、3で割れるところまで割って、5で割れるところまで割って、答えが1か否かをcheck
- Discussionで採られている方法も同様

```python
# 自力実装
class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0:
            return False
        if num==1:
            return True
        
        while num%2==0:
            num /= 2
        while num%3==0:
            num /= 3
        while num%5==0:
            num /= 5
        return num==1
```

### 1.1.46. [268. Missing Number](https://leetcode.com/problems/missing-number/)

- リストの長さを得て合計を出し、前から順に引いていくと消えた数字が残る
- SolutionではXORを使用した方法も紹介されていた

```python
# 自力実装
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        perfect_sum = (length*(1+length))/2
        for i in nums:
            perfect_sum -= i
        return int(perfect_sum)
```

```python
# XORを使用した方法（Solutionを参考に実装）
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i, n in enumerate(nums):
            length ^= i^n
        return length
```

### 1.1.47. ▲[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

- 二分探索で解いた
- Solutionも二分探索
    - ▲overflow bugを避けるために`(left+right)/2`ではなく`left+(right-left)/2`を使うべきと説かれていた

```python
# 自力実装

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        
        if isBadVersion(n) and not isBadVersion(n-1):
            return n
        
        l, r = 1, n
        m = int((l+r)/2)
        while True:
            if isBadVersion(m) and not isBadVersion(m-1):
                return int(m)
            
            if isBadVersion(m):
                r = m
                m = int((l+r)/2)
            else:
                l = m
                m = int((l+r)/2)
```

```python
# Solutionを参考にリファクタリング
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while True:
            m = int((l+r)/2)
            if isBadVersion(m) and not isBadVersion(m-1):
                return int(m)

            if isBadVersion(m):
                r = m
            else:
                l = m+1
```

### 1.1.48. ▲[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

- ポインタを2つ使用
- ▲Solutionもポインタを2つ使いつつ、より最適な解法になっている
    - elegant!

```python
# 自力実装
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return

        ps, pf = 0, 0
        while pf<len(nums):
            while nums[pf]==0:
                if pf>=len(nums)-1:
                    break
                pf += 1
            if pf<len(nums):
                nums[ps] = nums[pf]
            ps += 1
            pf += 1

        while ps<len(nums):
            nums[ps] = 0
            ps += 1
```

```python
# Solutionを参考にリファクタリング
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return

        ps = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ps], nums[i] = nums[i], nums[ps]
                ps += 1
```

### 1.1.49. [290. Word Pattern](https://leetcode.com/problems/word-pattern/)

- 205.の発展形といった形の問題
- ここではstrを`split()`メソッドでリスト化して205と同様の設定に落とし込んだが、`split()`を使えない場合もwhileループなどを使用して同じ状況に持ち込めばよい
- Discussionも似たような感じ

```python
# 自力実装
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s2 = str.split(" ")
        if len(s2)!=len(pattern):
            return False

        dic_s2p = {}
        for i, s in enumerate(s2):
            dic_s2p[s] = pattern[i]
        dic_p2s = {}
        for i, p in enumerate(pattern):
            dic_p2s[p] = s2[i]
        return [p for p in pattern]==[dic_s2p[s] for s in s2] and [dic_p2s[p] for p in pattern]==[s for s in s2]
```

```python
# 205.のメモを参考に実装
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s2 = str.split(" ")
        return len(set(zip(pattern, s2)))==len(set(pattern))==len(set(s2)) and len(pattern)==len(s2)
```

### 1.1.50. [292. Nim Game](https://leetcode.com/problems/nim-game/)

- 相手に4の倍数で手番を渡し続ければ勝てる
- そのためには4の倍数以外から始められると良い

```python
# 自力実装
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0
```
### 1.1.51. [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

- `sum()`で合計を求めるとぎりぎり終わる
    - Queryごとにforループを回しているとTLEになる
- Solutionでは結果を先にブルートフォースで保持しておき、Queryで結果を呼び出す方針

```python
# 自力実装
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

```python
# Solutionを参考に実装
class NumArray:

    def __init__(self, nums: List[int]):
        self.dic = {}
        for i in range(len(nums)+1):
            self.dic[i] = sum(nums[:i])

    def sumRange(self, i: int, j: int) -> int:
        return self.dic[j+1]-self.dic[i]
```

### 1.1.52. ▲[326. Power of Three](https://leetcode.com/problems/power-of-three/)

- whileループを使うと簡単だが、Follow upに「ループと再帰を使わずに解け」とある
- 3進数に変換する？
    - 変換時にループか再帰が必要だから意味ないか
- ▲Solutionではループ、3進数への変換、対数をとる、intで表現できる最大数以内の最大の3の乗数をnで割った余りが0か否かで判定

```python
# 自力実装（whileループ使用ver）
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n==1:
                return True
            if n%3!=0 or n<=0:
                return False
            n /= 3
```

### 1.1.53. [342. Power of Four](https://leetcode.com/problems/power-of-four/)

- 326を参考に実装した
    - 素数の乗数ではない点が326と比べて厄介
    - 32bitのintの2の補数で表現できる符号付き整数は −2,147,483,648 から 2,147,483,647(Wikipediaより)
    - 2147483647以下で最大の4の乗数は4**16=4294967296
    - よって、4294967296を割りきれる、かつ4で割りきれる場合にTrue, と考えたがこれでは8などもTrueになってしまう
        - 4で割り切れる、ではなく4294967296を割った商の平方根が整数（2で割り切れる）かどうかに変更したら通った
            - 4\*\*16を4\*\*xで割ると4\*\*y=2\*\*2y が商になるため、平方根をとると2の倍数になるはず
            - 8などの2**z (z=2n+1)で割ると商も2\*\*y' (y'=2n+1)になる
- discussionではbit演算が活用されていた
    - num & (num-1) == 0  # numが2の乗数であることの確認　と　32bitの1010101010101010101010101010101 (1431655765) & num = num によって、numがbinで10000...(先頭が1で0が偶数個ある=4**nであること)を確認
    - elegant!

```python
# 自力実装
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<1:
            return False
        
        if num==1:
            return True
        
        return 4294967296%num==0 and ((4294967296/num)**(1/2))%2==0
```

```python
# Discussionを参考に実装
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and num&(num-1)==0 and num&1431655765==num
```

### 1.1.54. [344. Reverse String](https://leetcode.com/problems/reverse-string/)

- memoryをO(1)に抑えろとのことだったため、先頭と最後尾から順に入れ替えて実装
- Discussionでは同じような解法、`s[::-1]`で完了としている回答が見られた
    - 本問ではreturnではなくリストそのものを変更せよ、ということで誤解法になるが、再帰的な解法もあった
        - `self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])`を活用

```python
# 自力実装
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            s[i], s[-i-1] = s[-i-1], s[i]
```

### 1.1.55. [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

- 素直に実装
    - 344問を少し改良する形
- Discussionでも2つのpointerを使用する方法が採られていた

```python
# 自力実装
class Solution:
    def reverseVowels(self, s: str) -> str:
        vset = {"a", "i", "u", "e", "o", "A", "I", "U", "E", "O"}
        l = 0
        r = len(s)
        s = "x" + s + "x"  # IndexErrorを防ぐため
        while l<r:
            if s[l] in vset and s[r] in vset:
                s = s[:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
                l += 1
                r -= 1

            while l<r and s[l] not in vset:
                l += 1

            while l<r and s[r] not in vset:
                r -= 1
                
        return s[1:-1]
```

### 1.1.56. [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

- 2つのリストを一意にしてソートし、2つのポインタを使って素直に解いた
- Solutionではよりスマートな方法が解説されていた
- 小さい方のsetを前から順に回してもう片方のsetに含まれるか否かを判定
- 他にも、setの和集合をとる演算も紹介されていた

```python
# 自力実装
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = list(set(nums1))
        snums2 = list(set(nums2))
        snums1.sort()
        snums2.sort()
        p1, p2 = 0, 0
        ans = []
        while p1<len(snums1) and p2<len(snums2):
            if snums1[p1]==snums2[p2]:
                ans.append(snums1[p1])
                p1 += 1
                p2 += 1

            while p1<len(snums1) and p2<len(snums2) and snums1[p1]<snums2[p2]:
                p1 += 1
                
            while p1<len(snums1) and p2<len(snums2) and snums2[p2]<snums1[p1]:
                p2 += 1
                    
        return ans
```

```python
# Solutionを参考に実装
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = set(nums1)
        snums2 = set(nums2)
        if len(snums1)<len(snums2):
            return [x for x in snums1 if x in snums2]
        else:
            return [x for x in snums2 if x in snums1]
```

```python
# Solutionを参考に実装
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = set(nums1)
        snums2 = set(nums2)
        return list(snums1 & snums2)
```

### 1.1.57. [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

- リストがソートされている場合、については349問とほぼ同様の方法で解いた
- Discussionでは2つのポインタを使う方法に加え、辞書型を使う方法や`collections`を使う方法が紹介されていた

```python
# 自力実装
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1 = 0
        p2 = 0
        nums1.sort()
        nums2.sort()
        ans = []
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]==nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            
            while p1<len(nums1) and p2<len(nums2) and nums1[p1]<nums2[p2]:
                p1 += 1
                
            while p1<len(nums1) and p2<len(nums2) and nums1[p1]>nums2[p2]:
                p2 += 1
                
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        ans = []
        for n1 in nums1:
            dic[n1] = dic.get(n1, 0) + 1
            
        for n2 in nums2:
            if n2 in dic and dic[n2]>0:
                ans.append(n2)
                dic[n2] -= 1
                
        return ans
```

### 1.1.58. ▲[367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

- 1から順に因数分解しようとしたものの、TLE
- Related TopicsにBinary Searchとあるのを目にして二分探索を行ったところ、Accepted
- ▲Discussionでは二分探索に加えて、n**2=1+3+5+...+(2n-1)となることを活用した方法や[ニュートン法](https://ja.wikipedia.org/wiki/%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%88%E3%83%B3%E6%B3%95)などが紹介されていた

```python
# ヒントを見て自力実装
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True

        l, r = 1, num
        while l<r:
            mid = int((l+r)/2)
            if mid**2==num:
                return True
            elif mid**2<num:
                l = mid+1
            elif mid**2>num:
                r = mid

        return False
```

```python
# Discussionを参考に実装
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        sq = 0
        while sq<=num:
            if sq==num:
                return True
            else:
                sq += i
                i += 2
                
        return False
```

```python
# Discussionを参考に実装（ニュートン法）
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = num
        while i**2>num:
                i = (i+(num/i))//2

        return i**2==num
```

### 1.1.59. ▲[371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

- +, -を使わずに加算を表現する
- 2ビットに直してAND, XORを使う
    - 負の数に対応できず、断念
- ▲途中までの実装は合っていたので負の数に関する実装を加えればOK
    - [参考](https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed)

```python
# 自力実装（途中まで）
class Solution:
    def getSum(self, a: int, b: int) -> int:
        xor_ans = a ^ b
        and_ans = int(bin((a & b) << 1), 2)
        xor_ans2 = xor_ans ^ and_ans
        and_ans2 = int(bin((xor_ans & and_ans) << 1), 2)
        while and_ans2!=0:
            xor_ans, and_ans = xor_ans2, and_ans2
            xor_ans2 = xor_ans ^ and_ans
            and_ans2 = int(bin((xor_ans & and_ans) << 1), 2)
            
        return xor_ans2
```

### 1.1.60. [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

- 二分探索で解けた
- SolutionではTernary Searchという3分割での探索方法も紹介されていた
    - ただし、一般的に使われるのは二分探索、その理由はworstなケースで二分探索の方が速いから、らしい

```python
# 自力実装

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l<=h:
            m = int((l+h)/2)
            if guess(m)==0:
                return m
            elif guess(m)==-1:
                h = m-1
            elif guess(m)==1:
                l = m+1
```

```python
# Solutionを参考にリファクタリング
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l<=h:
            m = l + int((h-l)/2)  # オーバーフロー対策？
            res = guess(m)  # guess(m)呼び出し回数を抑える
            if res==0:
                return m
            elif res==-1:
                h = m-1
            elif res==1:
                l = m+1
```

```python
# Solutionを参考に実装
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l<=h:
            m1 = l + int((h-l)/3)
            m2 = h - int((h-l)/3)
            res1 = guess(m1)
            res2 = guess(m2)
            if res1==0:
                return m1
            elif res2==0:
                return m2
            elif res1==-1:
                h = m1-1
            elif res2==1:
                l = m2+1
            elif res1==1 and res2==-1:
                l = m1+1
                h = m2-1
```

### 1.1.61. ▲[383. Ransom Note](https://leetcode.com/problems/ransom-note/)

- 2つのポインタで実装したものの、パフォーマンスが悪い
- ▲Discussionでは文字数を数える方法で実装されていた
    - `str.count()`というメソッドが使用されていた

```python
# 自力実装
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote=="":
            return True
        if magazine=="":
            return False

        p1, p2 = 0, 0
        ran = sorted(ransomNote)
        mag = sorted(magazine)
        while p1<len(ran) and p2<len(mag):
            if ran[p1]==mag[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        if p1==len(ran):
            return True
        else:
            return False
```

```python
# Discussionを参考に実装
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rset = set(ransomNote)
        for s in rset:
            if ransomNote.count(s)>magazine.count(s):
                return False
        return True
```

### 1.1.62. [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

- 前から順にstr.count()していこうとするとTLE
- 先に出現する小文字アルファベットの数の辞書を作っておき、文字列の前から順に数を確認していくとAC
- Solutionも同様

```python
# 自力実装
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if not s[i] in dic:
                dic[s[i]] = s.count(s[i])

        for j in range(len(s)):
            if dic[s[j]]==1:
                return j
        
        return -1
```

### 1.1.63. ▲[389. Find the Difference](https://leetcode.com/problems/find-the-difference/)

- 辞書に文字の出現回数を足したり引いたりして実装した
- ▲Discussionでは辞書による方法の他、文字を数値化して足し引きし、最後に残った数字を文字化して答えを得る方法、XORを使った方法、ソートしてzipで1文字ずつ比較していく方法などがあった
    - 追加される文字が1文字、というのを見逃しており、複数文字に対応できる解法を作ってしまった

```python
# 自力実装
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        ans = ""
        for x in t:
            dic[x] = dic.get(x, 0) + 1
            
        for y in s:
            dic[y] = dic[y] - 1
            
        for k in dic:
            if dic[k]>0:
                ans += k
                
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        if s==t[:-1]:
            return t[-1]
        else:
            return [x[1] for x in zip(s, t) if x[0]!=x[1]][0]
```

### 1.1.64. ▲[400. Nth Digit](https://leetcode.com/problems/nth-digit/)

- 順に数を文字列として結合していって、文字列の長さがnを超えた段階でs[n-1]を返す
    - TLEになった
- ▲Discussionでは無駄な部分（桁数が異なる部分）をskipして処理を速くしている
    - 頭が働かなくて解法が頭に入ってこないため、こんどやる

### 1.1.65. ▲[401. Binary Watch](https://leetcode.com/problems/binary-watch/)

- 時と分を並べて10bitとみなす
    1.  考えられる2進数の組み合わせを列挙
    2.  2進数を時刻に変換
    - という2段階の処理で実装
    - 2.は実装できたものの、1.は`itertools.permutations(s)`によるsのアナグラムに時間がかかるのか、TLEに
- Discussionでは逆に12, 60までを列挙して1の数が`num`と等しいケースのみを抽出していた
    - elegant!
- ▲他にもDFSと再帰による解法もあった

```python
# 自力実装（TLE）
import itertools


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # 考えられる2進数の組み合わせを列挙
        s = "1"*num+"0"*(10-num)
        s_list = ["".join(x) for x in itertools.permutations(s)]
        # 2進数を時刻に変換
        ans = []
        for xbs in s_list:
            h = int(xbs[:4], 2)
            m = int(xbs[4:], 2)
            if h>11 or m>60:
                continue
            else:
                time = "{}:{:02}".format(h, m)
                ans.append(time)
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans =[]
        for i in range(12):
            for j in range(60):
                xbs = bin(i)+bin(j)
                if xbs.count("1")==num:
                    time = "{}:{:02}".format(i, j)
                    ans.append(time)
        return ans
```

### 1.1.66. ▲[405. Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)

- 2の補数表現、10進数->2進数への変換を活用して実装
- ▲Discussionでは[bit演算で解く方法も紹介](https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/89261/easy-10-line-python-solution-with-inline-explanation)されていた

```python
# 自力実装
class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num = 2**32+num
        lis = [str(i) for i in range(10)]
        lis.extend(["a", "b", "c", "d", "e", "f"])
        ans = ""
        while num>0:
            ans = lis[num%16]+ans
            num = num//16
        return ans
```

```python
# Discussionのコードにコメントを付与して理解
class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        mp = '0123456789abcdef'
        ans = ''
        # 32bitなので32/4=8回処理を実行
        for i in range(8):
            # 2進数の下4桁を抽出
            n = num & 15
            c = mp[n]
            ans = c + ans
            # ansに転記済の2進数下4桁を削除
            num = num >> 4
        # 8回処理を行う際に先頭に付与される0をlstrip()で削除
        return ans.lstrip('0')
```

### 1.1.67. [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

- 回文は「偶数の文字+奇数の文字1種類」で構成されていることを元に実装
    - 最初、奇数の文字も-1すれば回文に組み込めることを見逃していた
- Solutionでは貪欲法での解法が解説されていた
    - 考え方は同じ
    - どこらへんが貪欲法なのだろうか...

```python
# 自力実装
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 文字の数を辞書化
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0)+1
        # 偶数の文字を任意の数と2以上の奇数の文字-1の合計を答えとする
        ans = 0
        odd = 0
        for k in dic:
            if dic[k]%2==0:
                ans += dic[k]
            elif 1<dic[k]:  # 奇数-1も回文に使える
                ans += dic[k]-1
                odd = 1
            else:  # 奇数が1つでもあれば+1しなければならない
                odd = 1
        return ans+odd
```

```python
# Solution参考に実装
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 文字の数を辞書化
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0)+1
        # 偶数の文字を任意の数と2以上の奇数の文字-1の合計を答えとする
        ans = 0
        for k in dic:
            ans += dic[k]//2*2
            if ans%2==0 and dic[k]%2==1:  # 奇数が1つでもあれば+1しなければならない(1度だけ)
                ans += 1
        return ans
```