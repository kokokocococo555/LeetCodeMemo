# LeetCode別解勉強

- LeetCodeの別解の勉強記録
- Solutionに投稿されている内容等を参照し、自分でも実装してみる
- 使用言語は`Python`

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
        while cnt<len(s)-1:
            if s[cnt:cnt+2] in roman_ex_dict:
                ans += roman_ex_dict[s[cnt:cnt+2]]
                cnt += 2
            else:
                ans += roman_dict[s[cnt]]
                cnt += 1
            
        if cnt==len(s)-1:
            ans += roman_dict[s[cnt]]

        return ans
```

### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

- 愚直に比較していく
    - 遅め（全solutionの50%くらいの速さ）
- 公式の別解アルゴリズムはまだ理解が追いついていない
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
                        if strs[i][cnt]==ans[cnt]:
                            tmp += strs[i][cnt]
                            cnt += 1
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
