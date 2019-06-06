# LeetCode別解勉強

- LeetCodeの別解の勉強記録
- Solutionに投稿されている内容等を参照し、自分でも実装してみる
- 復習が必要な問題には▲をつけている
- 使用言語は`Python`
    - しかし`Python`遅いな…


- 以下のことができれば実装はほぼ作業化する。以下のことが重要と見た。
    - テストケースを作る。
    - 頭の中や紙の上で処理してみる。その流れをプログラムに起こすだけ。

## Easy
### [1. Two Sum](https://leetcode.com/problems/two-sum/)

- 2重ループで解けるが遅い
- 模範解答のHash Tableという辞書を使った解法が速い
  - 2重ループ不要
  - 1度計算した結果を順次保存し、保存済みの結果と新しい計算結果を比較していく、という考え方？

```python
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

### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

- strに変換して[::-1]、intに戻せばOK
  - 負か否か、結果がoverflowするか否かをcheck
- 模範解答はpop&push
  - 負か否か、overflowするか否かをcheck
  - abs(x)をとらないと -123 -> 789 にしてしまう
  - 速さはあまり変わらなかった
  
```python
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

### [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

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

### [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

- Romanと数字との対応表をdictで作成
- IV, IXなどの特殊バージョンについての対応表も別途作成
- 入力を前から調べ、2文字見たときに特殊バージョンか否かで場合分け
    - 特殊バージョンの場合はカウンタを2つ進める
- [discussionにあった解法](https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution)には、次の数字よりも現在の数字の方が小さい場合に現在の値をansから引いておく、という解法があった
    - 場合分けが減ってスムーズ
- [discussionにあった解法](https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.)には他にも、特殊バージョンを前もって通常バージョンに置換しておく、という解法も

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

### ▲[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

- 愚直に比較していく
    - 遅め（全solutionの50%くらいの速さ）
- ▲公式の別解アルゴリズムはまだ理解が追いついていない
- Solutionへの投稿では以下のような解法もあった
    - strsリストをソートして最初と最後の要素だけをzipで比較している解法
    - strsリストの全要素の頭から1文字ずつzipで抜き出してsetでまとめ、setの長さが1の間はprefixに追加していく解法

```python
# 自力実装（ゴリ押し）
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

### [20. Valid Parentheses]()

- 先入れ後出し(FILO)のstack方式を採用
    - 処理速度はかなり速い
    - 模範解答もstack方式
- 再帰的構造と捉えて(), {}, []のペアを削除していく方法もある
    - コード数が少ないが、stack方式よりも遅い
    - Solutionに投稿されていたものも参考に

```python
# FILOのstack方式
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
# 再帰的構造方式
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

### ▲[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

- リストであれば
    - 両方のリストから先頭から順に数をpop
    - 数同士を比較し、小さい方を新しいリストに追加
    - 大きい方は残したまま小さかった方のリストから次の数をpop
    - どちらかのリストが空になるまで繰り返す
    - 残ったリストの要素を新しいリストに結合
    - この機能を2つのcntを使用することで実現
- しかしリストではなくListNodeというClassを使用しているため、len()やスライシングが使えない
- ▲discussionを見ると再帰的なコードが書けるっぽい（要復習）
- 再帰ではなく、上述の元アイデアをListNodeに落とし込んだ解法が上がっていたため、ListNodeの挙動を参考にして実装
  - [python3 24ms beats 100%
  ](https://leetcode.com/problems/merge-two-sorted-lists/discuss/200801/python3-24ms-beats-100)

```python
# リストならうまく動きそうなバージョン
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
# ListNodeで動いたバージョン

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

### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

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
# カウンタを2つ使用してpopする
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
# 模範解答を参照してリストの前半だけ変更し、最後に変更部分の長さだけを返す
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

### [27. Remove Element](https://leetcode.com/problems/remove-element/)

- 上の26. と似た問題
    - 与えられた値に合致する要素を削除する変更を入力リストにin-placeで行う
    - 同じくTwo pointersのやり方でいけた
    - numsの要素がvalのとき、値の置き換えもpntのカウントもスキップする
    - 26.の教訓を活かして実装できたのは嬉しい
- 別解として、valの要素をリストの後ろの方と入れ換えていく方法がある
    - valの要素が少ない場合、要素の代入回数が減る

```python
# Two pointers
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
# val要素が少ない場合
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

### [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

- haystackを前から順にneedleの長さ分切り取ってneedleと比較
    - 少し遅め

```python
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

### ▲[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

- 普通に前から順に比較
    - O(n)
- discussionではbinary searchによってO(log n)でいけるとの話が
    - binary searchの復習を
    - 実行してみても実はそんなに速くない？

```python
# O(n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
            
        return i+1
```

```python
# binary search
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