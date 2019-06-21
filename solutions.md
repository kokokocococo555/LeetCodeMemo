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

### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

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

### ▲[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

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

### [20. Valid Parentheses]()

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

### ▲[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

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

### [27. Remove Element](https://leetcode.com/problems/remove-element/)

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

### [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

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

### ▲[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

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

### [38. Count and Say](https://leetcode.com/problems/count-and-say/)

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

### ▲[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

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

### [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

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

### [66. Plus One](https://leetcode.com/problems/plus-one/)

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

### ▲[67. Add Binary](https://leetcode.com/problems/add-binary/)

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

### [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

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

### ▲[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

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

### ▲[83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

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

### ▲[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

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

### [100. Same Tree](https://leetcode.com/problems/same-tree/)

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

### [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

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

### ▲[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- 再帰的な方法で解いた
    - Discussionを見ると、自分の実装は無駄なif文が多いみたい
    - ただし、自分の最初の実装の方がかなり速い（無駄な計算をif文で省けている）
- ▲Discussionにはwhile文での解法もある（max()が不要）
    - 順番に降りていってカウントしている。分かりやすく、美しい解法
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

### ▲[107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

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

### ▲[108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

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

### ▲[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

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

### [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

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

### [112. Path Sum](https://leetcode.com/problems/path-sum/)

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

### [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

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

### [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

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

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

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
### ▲[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

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

### ▲[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

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

### ▲[136. Single Number](https://leetcode.com/problems/single-number/)

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

### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

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

### [155. Min Stack](https://leetcode.com/problems/min-stack/)

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

### ▲[160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

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

### ▲[167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

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

### [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)

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

### ▲[169. Majority Element](https://leetcode.com/problems/majority-element/)

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
        - 素敵

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

### [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

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

### [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

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

### [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

- 2つのテーブルをPersonIdをキーにして左外部結合する
    - 結合するテーブル名、キーはFROM句に書く

```sql
select FirstName, LastName, City, State
from Person LEFT OUTER JOIN Address ON Person.PersonId=Address.PersonId;
```