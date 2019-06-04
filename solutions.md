# LeetCode別解勉強

- LeetCodeの別解の勉強記録
- Solutionに投稿されている内容等を参照し、自分でも実装してみている

## easy
### [1. Two Sum](https://leetcode.com/problems/two-sum/solution/)

- 2重ループで解けるが、遅い
- Hash Tableという辞書を使った解法が速い
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

### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/solution/)

- strに変換して[::-1]、intに戻せばOK
  - 負か否か、結果がoverflowするか否かをcheck
- 模範解答はpop&push
  - 負か否か、overflowするか否かをcheck
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
        if ans>=-2**31 and ans<= 2**31-1:
            return ans
        else:
            return 0
```
