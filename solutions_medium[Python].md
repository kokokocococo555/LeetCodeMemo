# 1. LeetCode勉強記録（Python編）_Medium

- LeetCodeの勉強記録
    - Medium編
- 自力で実装したコードの他にも、Solution, Discussionに投稿されている内容等を参照し、自分でも実装してみる
- 復習が必要な問題には▲をつけている
- 使用言語は`Python`

<!-- TOC -->

- [1. LeetCode勉強記録（Python編）_Medium](#1-leetcode%e5%8b%89%e5%bc%b7%e8%a8%98%e9%8c%b2python%e7%b7%a8medium)
  - [1.1. Medium](#11-medium)
    - [1.1.1. ▲3. Longest Substring Without Repeating Characters](#111-%e2%96%b23-longest-substring-without-repeating-characters)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85)
- [Solutionを参考に実装（さらに最適化）](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85%e3%81%95%e3%82%89%e3%81%ab%e6%9c%80%e9%81%a9%e5%8c%96)
    - [1.1.2. ▲5. Longest Palindromic Substring](#112-%e2%96%b25-longest-palindromic-substring)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-1)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-1)
    - [1.1.3. 6. ZigZag Conversion](#113-6-zigzag-conversion)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-2)
- [Solutionを参考にリファクタリング](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e3%83%aa%e3%83%95%e3%82%a1%e3%82%af%e3%82%bf%e3%83%aa%e3%83%b3%e3%82%b0)
    - [1.1.4. 8. String to Integer (atoi)](#114-8-string-to-integer-atoi)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-3)
    - [1.1.5. ▲11. Container With Most Water](#115-%e2%96%b211-container-with-most-water)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-2)
    - [1.1.6. 12. Integer to Roman](#116-12-integer-to-roman)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-4)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-3)
    - [1.1.7. ▲15. 3Sum](#117-%e2%96%b215-3sum)
- [自力実装（TLE）](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85tle)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85)
    - [1.1.8. 16. 3Sum Closest](#118-16-3sum-closest)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-5)
    - [1.1.9. ▲17. Letter Combinations of a Phone Number](#119-%e2%96%b217-letter-combinations-of-a-phone-number)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-6)
- [Solutionを参考に実装(backtrack)](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85backtrack)
    - [1.1.10. ▲18. 4Sum](#1110-%e2%96%b218-4sum)
- [https://leetcode.com/problems/4sum/discuss/128591/Easy-to-understand-python-Solution をコピー](#httpsleetcodecomproblems4sumdiscuss128591easy-to-understand-python-solution-%e3%82%92%e3%82%b3%e3%83%94%e3%83%bc)
    - [1.1.11. 22. Generate Parentheses](#1111-22-generate-parentheses)
- [Solutionを写経](#solution%e3%82%92%e5%86%99%e7%b5%8c)
    - [1.1.12. ▲29. Divide Two Integers](#1112-%e2%96%b229-divide-two-integers)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-4)
    - [1.1.13. 31. Next Permutation](#1113-31-next-permutation)
- [Solution(Java)を写経(Python)](#solutionjava%e3%82%92%e5%86%99%e7%b5%8cpython)
    - [1.1.14. 33. Search in Rotated Sorted Array](#1114-33-search-in-rotated-sorted-array)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-7)
    - [1.1.15. 34. Find First and Last Position of Element in Sorted Array](#1115-34-find-first-and-last-position-of-element-in-sorted-array)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-8)
    - [1.1.16. 36. Valid Sudoku](#1116-36-valid-sudoku)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-9)
    - [1.1.17. ▲39. Combination Sum](#1117-%e2%96%b239-combination-sum)
- [DFS（Discussionを写経）](#dfsdiscussion%e3%82%92%e5%86%99%e7%b5%8c)
- [https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.](#httpsleetcodecomproblemscombination-sumdiscuss16510python-dfs-solution)
    - [1.1.18. 40. Combination Sum II](#1118-40-combination-sum-ii)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-10)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-1)
    - [1.1.19. ▲43. Multiply Strings](#1119-%e2%96%b243-multiply-strings)
- [Discussionを写経](#discussion%e3%82%92%e5%86%99%e7%b5%8c)
- [https://leetcode.com/problems/multiply-strings/discuss/17615/Simple-Python-solution-18-lines](#httpsleetcodecomproblemsmultiply-stringsdiscuss17615simple-python-solution-18-lines)
    - [1.1.20. 46. Permutations](#1120-46-permutations)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-11)
    - [1.1.21. 47. Permutations II](#1121-47-permutations-ii)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-12)
    - [1.1.22. 48. Rotate Image](#1122-48-rotate-image)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-13)
    - [1.1.23. 49. Group Anagrams](#1123-49-group-anagrams)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-14)
    - [1.1.24. ▲50. Pow(x, n)](#1124-%e2%96%b250-powx-n)
- [Discussionをコピペ](#discussion%e3%82%92%e3%82%b3%e3%83%94%e3%83%9a)
- [https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed](#httpsleetcodecomproblemspowx-ndiscuss19560shortest-python-guaranteed)
    - [1.1.25. 54. Spiral Matrix](#1125-54-spiral-matrix)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-15)
    - [1.1.26. ▲55. Jump Game](#1126-%e2%96%b255-jump-game)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-16)
    - [1.1.27. 56. Merge Intervals](#1127-56-merge-intervals)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-17)
    - [1.1.28. ▲59. Spiral Matrix II](#1128-%e2%96%b259-spiral-matrix-ii)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-2)
- [https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions](#httpsleetcodecomproblemsspiral-matrix-iidiscuss222824-9-lines-python-solutions)
    - [1.1.29. 60. Permutation Sequence](#1129-60-permutation-sequence)
- [自力実装（TLE）](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85tle-1)
- [Discussionを写経](#discussion%e3%82%92%e5%86%99%e7%b5%8c-1)
- [https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation](#httpsleetcodecomproblemspermutation-sequencediscuss22512share-my-python-solution-with-detailed-explanation)
    - [1.1.30. 62. Unique Paths](#1130-62-unique-paths)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-18)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-3)
    - [1.1.31. 63. Unique Paths II](#1131-63-unique-paths-ii)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-19)
    - [1.1.32. 64. Minimum Path Sum](#1132-64-minimum-path-sum)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-4)
    - [1.1.33. 71. Simplify Path](#1133-71-simplify-path)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-20)
    - [1.1.34. 73. Set Matrix Zeroes](#1134-73-set-matrix-zeroes)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-21)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-5)
    - [1.1.35. 74. Search a 2D Matrix](#1135-74-search-a-2d-matrix)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-22)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-5)
    - [1.1.36. ▲75. Sort Colors](#1136-%e2%96%b275-sort-colors)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-23)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-6)
- [https://leetcode.com/problems/sort-colors/discuss/26479/AC-Python-in-place-one-pass-solution-O(n)-time-O(1)-space-no-swap-no-count](#httpsleetcodecomproblemssort-colorsdiscuss26479ac-python-in-place-one-pass-solution-on-time-o1-space-no-swap-no-count)
    - [1.1.37. 77. Combinations](#1137-77-combinations)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-24)
- [Discussionを参考にリファクタリング](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e3%83%aa%e3%83%95%e3%82%a1%e3%82%af%e3%82%bf%e3%83%aa%e3%83%b3%e3%82%b0)
    - [1.1.38. 78. Subsets](#1138-78-subsets)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-25)
- [Discussionを参考に改善](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e6%94%b9%e5%96%84)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-7)
    - [1.1.39. 79. Word Search](#1139-79-word-search)
- [Discussionを写経](#discussion%e3%82%92%e5%86%99%e7%b5%8c-2)
- [https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.](#httpsleetcodecomproblemsword-searchdiscuss27660python-dfs-solution-with-comments)
    - [1.1.40. 80. Remove Duplicates from Sorted Array II](#1140-80-remove-duplicates-from-sorted-array-ii)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-26)
    - [1.1.41. ▲81. Search in Rotated Sorted Array II](#1141-%e2%96%b281-search-in-rotated-sorted-array-ii)
- [Discussionを写経](#discussion%e3%82%92%e5%86%99%e7%b5%8c-3)
- [https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28195/Python-easy-to-understand-solution-(with-comments).](#httpsleetcodecomproblemssearch-in-rotated-sorted-array-iidiscuss28195python-easy-to-understand-solution-with-comments)
    - [1.1.42. 89. Gray Code](#1142-89-gray-code)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-8)
- [https://leetcode.com/problems/gray-code/discuss/29954/DP-Python-solution](#httpsleetcodecomproblemsgray-codediscuss29954dp-python-solution)
- [https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)](#httpsleetcodecomproblemsgray-codediscuss29893one-liner-python-solution-with-demo-in-comments)
    - [1.1.43. ▲90. Subsets II](#1143-%e2%96%b290-subsets-ii)
- [Discussionを写経](#discussion%e3%82%92%e5%86%99%e7%b5%8c-4)
- [https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS).](#httpsleetcodecomproblemssubsets-iidiscuss30305simple-python-solution-dfs)
    - [1.1.44. ▲91. Decode Ways](#1144-%e2%96%b291-decode-ways)
- [Discussionを参考に写経](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%86%99%e7%b5%8c)
- [https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming](#httpsleetcodecomproblemsdecode-waysdiscuss253018python3a-easy-to-understand-explanation-bottom-up-dynamic-programming)
    - [1.1.45. 93. Restore IP Addresses](#1145-93-restore-ip-addresses)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-27)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-9)
- [https://leetcode.com/problems/restore-ip-addresses/discuss/31140/Python-easy-to-understand-solution-with-comments-(backtracking).](#httpsleetcodecomproblemsrestore-ip-addressesdiscuss31140python-easy-to-understand-solution-with-comments-backtracking)
    - [1.1.46. 120. Triangle](#1146-120-triangle)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-28)
    - [1.1.47. ▲127. Word Ladder](#1147-%e2%96%b2127-word-ladder)
- [Solutionを写経](#solution%e3%82%92%e5%86%99%e7%b5%8c-1)
- [Solutionを写経](#solution%e3%82%92%e5%86%99%e7%b5%8c-2)
    - [1.1.48. 130. Surrounded Regions](#1148-130-surrounded-regions)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-29)
    - [1.1.49. ▲131. Palindrome Partitioning](#1149-%e2%96%b2131-palindrome-partitioning)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-10)
- [https://leetcode.com/problems/palindrome-partitioning/discuss/42100/Python-easy-to-understand-backtracking-solution.](#httpsleetcodecomproblemspalindrome-partitioningdiscuss42100python-easy-to-understand-backtracking-solution)
    - [1.1.50. ▲134. Gas Station](#1150-%e2%96%b2134-gas-station)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-30)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-11)
- [https://leetcode.com/problems/gas-station/discuss/42661/Possibly-the-MOST-easiest-approach-O(N)-one-variable-Python](#httpsleetcodecomproblemsgas-stationdiscuss42661possibly-the-most-easiest-approach-on-one-variable-python)
    - [1.1.51. 137. Single Number II](#1151-137-single-number-ii)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-31)
    - [1.1.52. ▲139. Word Break](#1152-%e2%96%b2139-word-break)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-12)
    - [1.1.53. 150. Evaluate Reverse Polish Notation](#1153-150-evaluate-reverse-polish-notation)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-32)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-13)
    - [1.1.54. 151. Reverse Words in a String](#1154-151-reverse-words-in-a-string)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-33)
    - [1.1.55. ▲152. Maximum Product Subarray](#1155-%e2%96%b2152-maximum-product-subarray)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-34)
- [https://leetcode.com/problems/maximum-product-subarray/discuss/48243/In-Python-can-it-be-more-concise を一部変更](#httpsleetcodecomproblemsmaximum-product-subarraydiscuss48243in-python-can-it-be-more-concise-%e3%82%92%e4%b8%80%e9%83%a8%e5%a4%89%e6%9b%b4)
    - [1.1.56. 153. Find Minimum in Rotated Sorted Array](#1156-153-find-minimum-in-rotated-sorted-array)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-35)
- [Solutionを参考に実装](#solution%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-6)
    - [1.1.57. 373. Find K Pairs with Smallest Sums](#1157-373-find-k-pairs-with-smallest-sums)
- [自力実装](#%e8%87%aa%e5%8a%9b%e5%ae%9f%e8%a3%85-36)
    - [1.1.58. 948. Bag of Tokens](#1158-948-bag-of-tokens)
    - [1.1.59. ▲1105. Filling Bookcase Shelves](#1159-%e2%96%b21105-filling-bookcase-shelves)
- [Discussionを参考に実装](#discussion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85-14)
- [https://leetcode.com/problems/filling-bookcase-shelves/discuss/323415/simple-Python-DP-solution](#httpsleetcodecomproblemsfilling-bookcase-shelvesdiscuss323415simple-python-dp-solution)
    - [1.1.60. ▲1191. K-Concatenation Maximum Sum](#1160-%e2%96%b21191-k-concatenation-maximum-sum)
- [Disucssionを参考に実装](#disucssion%e3%82%92%e5%8f%82%e8%80%83%e3%81%ab%e5%ae%9f%e8%a3%85)
- [https://leetcode.com/problems/k-concatenation-maximum-sum/discuss/382808/Python3-6-liner-Kadane](#httpsleetcodecomproblemsk-concatenation-maximum-sumdiscuss382808python3-6-liner-kadane)

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

### 1.1.38. [78. Subsets](https://leetcode.com/problems/subsets/)

- backtrackingで解いた
- Discussionでは再帰のコードが紹介されていたり、backtrackingでのコードがDFSとして紹介されていたりした

```python
# 自力実装
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtrack(nums, k, path):
            if k==0:
                ans.append(path)
                return
            
            for i in range(len(nums)):
                tmp = nums[:]
                x = tmp.pop(i)
                if not path or x>path[-1]:
                    backtrack(tmp, k-1, path+[x])
                
        for i in range(len(nums)+1):
            backtrack(nums, i, [])
            
        return ans
```

```python
# Discussionを参考に改善
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(nums, idx, path):
            ans.append(path)
            for i in range(idx, len(nums)):
                backtrack(nums, i+1, path+[nums[i]])
                
        backtrack(nums, 0, [])
        return ans
```

```python
# Discussionを参考に実装
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        for num in nums:
            ans += [item+[num] for item in ans]
        return ans
```

### 1.1.39. [79. Word Search](https://leetcode.com/problems/word-search/)

- 指定の文字列を作成するパスの発見と、一度通った道は通らないという条件づけとを同時に行う方法が思いつかず、断念
- Discussionを見ると、なんとなく思い浮かべていた方法が実装されていた
- 実装力の大切さ

```python
# Discussionを写経
# https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, r, c, word):
                    return True
        return False
    
    
    def dfs(self, board, r, c, word):
        if len(word)==0:
            return True
        if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or word[0]!=board[r][c]:
            return False
        tmp = board[r][c]
        board[r][c] = ""
        res = self.dfs(board, r+1, c, word[1:]) or \
              self.dfs(board, r-1, c, word[1:]) or \
              self.dfs(board, r, c+1, word[1:]) or \
              self.dfs(board, r, c-1, word[1:])
        board[r][c] = tmp
        return res
```

### 1.1.40. [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

- ポインタとカウンタを使用

```python
# 自力実装
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                cnt += 1
            else:
                cnt = 0
            if cnt<=1:
                nums[p] = nums[i]
                p += 1
        return p
```

### 1.1.41. ▲[81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

- 分からず
- ▲Discussionでは、探索範囲を半分に分け、順に並んでいる方に二分探索をかける、というのを繰り返していた

```python
# Discussionを写経
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28195/Python-easy-to-understand-solution-(with-comments).
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return True
            while l<m and nums[l]==nums[m]:  # ???
                l += 1
            if nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]<target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False
```

### 1.1.42. [89. Gray Code](https://leetcode.com/problems/gray-code/)

- 問題の意味がよくわからない

```python
# Discussionを参考に実装
# https://leetcode.com/problems/gray-code/discuss/29954/DP-Python-solution
# https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [0]
        for i in range(1, n + 1):
            dp = dp + [j + 2**(i - 1) for j in dp][::-1]
        return dp
```

### 1.1.43. ▲[90. Subsets II](https://leetcode.com/problems/subsets-ii/)

- backtrackingでやろうとしたらTLEになった
- ▲Discussionではイテレータのようなbacktracking(DFS)で解いていた

```python
# Discussionを写経
# https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS).
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtrack(nums, idx, path):
            ans.append(path)
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                backtrack(nums, i + 1, path + [nums[i]])
                
        backtrack(nums, 0, [])
        return ans
```

### 1.1.44. ▲[91. Decode Ways](https://leetcode.com/problems/decode-ways/)

- backtrackで解こうとしたらTLEになった
- ▲Discussionを見るとDPで解かれていたが、その理屈がいまいち納得いかないのと、思いつく気がしない

```python
# Discussionを参考に写経
# https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1): 
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
```

### 1.1.45. [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

- 強引な処理がところどころ見られる
- Discussionではbacktrackingで解いていた

```python
# 自力実装
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if 12 < n or n < 4:
            return []

        cuts = []
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    cut = [0, i, j, k, n]
                    cuts.append(cut)
        ips = []
        for cut in cuts:
            ip = []
            for i in range(4):
                ip.append(int(s[cut[i]:cut[i+1]]))
            ips.append(ip)

        ans = []
        for ip in ips:
            if 0 <= ip[0] <= 255 and\
               0 <= ip[1] <= 255 and\
               0 <= ip[2] <= 255 and\
               0 <= ip[3] <= 255:
                tmp = ".".join([str(x) for x in ip])
                if len(tmp) == n + 3:  # `000`といった部分でバグらないようにしている（強引）
                    ans.append(tmp)

        return ans
```

```python
# Discussionを参考に実装
# https://leetcode.com/problems/restore-ip-addresses/discuss/31140/Python-easy-to-understand-solution-with-comments-(backtracking).
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, 0, "", ans)
        return ans
    
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], index+1, path + s[:i] + ".", res)
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index+1, path + s[:i] + ".", res)
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path + s[:i] + ".", res)
```

### 1.1.46. [120. Triangle](https://leetcode.com/problems/triangle/)

- 漸化式にできる -> 漸化式にできるならDPをやってみる　というのを思い出して解いた
- Discussionではさらに効率化された解放も
  - https://leetcode.com/problems/triangle/discuss/38741/Python-Bottom-up-DP-O(n)%2BO(n)-solution-(-5-lines-)

```python
# 自力実装
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for s in range(1, len(triangle)):
            for i in range(len(triangle[s])):
                if i == 0:
                    triangle[s][i] += triangle[s-1][i]
                elif i == len(triangle[s]) - 1:
                    triangle[s][i] += triangle[s-1][i-1]
                else:
                    triangle[s][i] += min(triangle[s-1][i-1], triangle[s-1][i])
        return min(triangle[-1])
```

### 1.1.47. ▲[127. Word Ladder](https://leetcode.com/problems/word-ladder/)

- backtrackingで解こうとしたものの、TLE
- ▲Solutionでは最短経路グラフ問題として扱い、BFSを使用
  - BFSの練習にも、グラフ問題の練習にもGood
  - タプルをqueueに入れて全部回して次に行く、という流れはBFSでよく見る
  - elegant!

```python
# Solutionを写経
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or not endWord in wordList:
            return 0
        
        L = len(beginWord)
        
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        print(all_combo_dict)
        
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                    all_combo_dict[intermediate_word] = []
        return 0
```

```python
# Solutionを写経
from collections import defaultdict

class Solution:
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)
        
    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            for word in self.all_combo_dict[intermediate_word]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or not endWord in wordList:
            return 0
        
        self.length = len(beginWord)
        
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        queue_begin = collections.deque([(beginWord, 1)])
        queue_end = collections.deque([(endWord, 1)])
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans

            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0
```

### 1.1.48. [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

- 四辺からOを辿っていく
- 実装に手間取った
- DiscussionではBFSで解いていた
  - やっていることは同じ

```python
# 自力実装
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []

        rn = len(board)
        cn = len(board[0])
        
        def change(r, c, rc, cc):
            if board[r+rc][c+cc] == "O":
                board[r+rc][c+cc] = "@"
                if r + 1 > 0 and r + 1 < rn - 1:
                    change(r+rc, c+cc, 1, 0,)
                if r - 1 > 0 and r - 1 < rn - 1:
                    change(r+rc, c+cc, -1, 0)
                if c + 1 > 0 and c + 1 < cn - 1:
                    change(r+rc, c+cc, 0, 1)
                if c - 1 > 0 and c - 1 < cn - 1:
                    change(r+rc, c+cc, 0, -1)
            
        for j in range(cn):
            change(0, j, 0, 0)
            change(rn - 1, j, 0, 0)

        for i in range(rn):
            change(i, 0, 0, 0)
            change(i, cn - 1, 0, 0)
            
        
        for i in range(rn):
            for j in range(cn):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "@":
                    board[i][j] = "O"
```

### 1.1.49. ▲[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

- 回文か否かを判定するメソッドは作れそうだったが、それを上手に問題に当てはめる方法が分からなかった
- ▲Discussionを見るとDFS(backtracking)の典型的な問題という印象だった

```python
# Discussionを参考に実装
# https://leetcode.com/problems/palindrome-partitioning/discuss/42100/Python-easy-to-understand-backtracking-solution.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        
        def backtrack(s, path, ans):
            if not s:
                ans.append(path)
                return
            
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    backtrack(s[i:], path + [s[:i]], ans)
                    
        backtrack(s, [], ans)
        return ans
```

### 1.1.50. ▲[134. Gas Station](https://leetcode.com/problems/gas-station/)

- 普通に実装するとTLE
- すでにチェックが終わった部分をスキップするとAC
- ▲Discussionではさらに最適化され、最初にgasとcostの合計を比較してから、前から順番に確認するだけで実現できている
  - elegant!

```python
# 自力実装
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sums_gas = [g - c for g, c in zip(gas, cost)]
            
        p = 0
        while p < len(gas):
            tmp, flg = self.check_gas(p, gas, cost, sums_gas)
            if flg:
                return p
            if tmp < p:
                return -1
            p = tmp + 1
            
        return -1

    def check_gas(self, j, gas, cost, sums_gas):
        tmp_sum = 0
        for k in range(len(gas)):
            idx = (j + k) % len(gas)
            tmp_sum += sums_gas[idx]
            if tmp_sum < 0:
                return idx, False
            
        return idx, True
```

```python
# Discussionを参考に実装
# https://leetcode.com/problems/gas-station/discuss/42661/Possibly-the-MOST-easiest-approach-O(N)-one-variable-Python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        p, tank = 0, 0
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                p = i + 1
        return p
```

### 1.1.51. [137. Single Number II](https://leetcode.com/problems/single-number-ii/)

- 線形時間で解け、メモリを使用するな、という条件だったが、ひとまず無視して実装
- Discussionではどうやらビット処理を行っているようだが、保留

```python
# 自力実装
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
            if dic[i] == 3:
                _ = dic.pop(i)
               
        k, _ = dic.popitem()
        return k
```

### 1.1.52. ▲[139. Word Break](https://leetcode.com/problems/word-break/)

- 再帰的な方法で実装したものの、TLE
- ▲DiscussionではDPで実装されていた

```python
# Discussionを参考に実装
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i:i + len(w)] and (dp[i - 1] or i == 0):
                    dp[i + len(w) - 1] = True
        return dp[-1]
```

### 1.1.53. [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

- Reverse Polish Notation (RPN: 逆ポーランド表記)の実装
- stackで実装した
- [Wikipedia](https://ja.wikipedia.org/wiki/%E9%80%86%E3%83%9D%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E8%A8%98%E6%B3%95)にもスタックで実装する、という旨が記載されていた
- Discussionでもstackを使用していた
- 加えて、ラムダ式を使用してさらにすっきりとしたコードを実現

```python
# 自力実装
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lis = ["+", "-", "/", "*"]
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if stack[-1] in lis:
                op = stack.pop()
                x2 = stack.pop()
                x2 = int(x2)
                x1 = stack.pop()
                x1 = int(x1)
                if op == "+":
                    tmp = x1 + x2
                elif op == "-":
                    tmp = x1 - x2
                elif op == "*":
                    tmp = x1 * x2
                elif op == "/":
                    tmp = int(x1 / x2)
                stack.append(tmp)
        return int(stack[-1])
```

```python
# Discussionを参考に実装
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+": lambda x1, x2: x1 + x2,
            "-": lambda x1, x2: x1 - x2,
            "*": lambda x1, x2: x1 * x2,
            "/": lambda x1, x2: int(x1 / x2),
        }
        for t in tokens:
            if t in op:
                x2 = stack.pop()
                x2 = int(x2)
                x1 = stack.pop()
                x1 = int(x1)
                stack.append(op[t](x1, x2))
            else:
                stack.append(t)
        return int(stack[-1])
```

### 1.1.54. [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

- 標準メソッドを使えば簡単に実装できた
- 想定解はおそらく異なるのだろうが

```python
# 自力実装
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s)
```

### 1.1.55. ▲[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

- 素直に実装した後、引っかかったケースを地道に潰していった
- テストケースが完備されているからこそ為せる技
- ▲Discussionでは、正負の値の情報をうまく保持しながら前から順に計算していくという方法が取られていた。すごい！
- https://leetcode.com/problems/maximum-product-subarray/discuss/48243/In-Python-can-it-be-more-concise
  - このコードは一部変更が必要
  - elegant!!!

```python
# 自力実装
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p0, p1 = 0, 0
        ns = len(nums)
        negidx = []
        ans = nums[0]
        while p1 < ns:
            if p0 > 0:
                ans = max(ans, 0)
            if nums[p1] < 0:
                negidx.append(p1)
            if nums[p1] == 0 or p1 == ns - 1:
                if nums[p1] != 0:
                    p1 = p1 + 1
                if len(negidx) % 2 == 0:
                    tmp = 1
                    for i in range(p0, p1):
                        tmp *= nums[i]
                        ans = max(ans, tmp)
                elif len(negidx) > 1:
                    tmp1 = 1
                    for i in range(p0, negidx[-1]):
                        tmp1 *= nums[i]
                        ans = max(ans, tmp1)
                    tmp2 = 1
                    for i in range(negidx[0] + 1, p1):
                        tmp2 *= nums[i]
                        ans = max(ans, tmp2)
                else:
                    tmp1 = 1
                    for i in range(p0, negidx[0]):
                        tmp1 *= nums[i]
                        ans = max(ans, tmp1)
                    tmp2 = 1
                    for i in range(negidx[0] + 1, p1):
                        tmp2 *= nums[i]
                        ans = max(ans, tmp2)
                negidx = []
                p0 = p1 + 1
            p1 += 1
        return ans
```

```python
# https://leetcode.com/problems/maximum-product-subarray/discuss/48243/In-Python-can-it-be-more-concise を一部変更
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = big = small = nums[0]
        for n in nums[1:]:
            tmp = small
            small = min(n, n*big, n*tmp)
            big = max(n, n*big, n*tmp)
            ans = max(ans, big)
        return ans
```

### 1.1.56. [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- 単純に実装するだけ
- Solutionでは二分探索がなされていた

```python
# 自力実装
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]
```

```python
# Solutionを参考に実装
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if r == 0:
            return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        
        while l <= r:
            m = (l + r) // 2
            if nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
```

以下、ランダムに問題を取り出して解く

### 1.1.57. [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

- k * k のsumと組を作成し、上から順にk個取り出す実装
- 処理が遅い
- Discussionではheapqでの実装やBFSでの実装が見られた（https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84629/BFS-Python-104ms-with-comments）
- heapqの要素にリストやタプルを入れた場合、そのlist[0]やtuple[0]をキーとして値がpopされる

```python
# 自力実装
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if k >= len(nums1) * len(nums2):
            return [[n1, n2] for n1 in nums1 for n2 in nums2]

        dic = {}
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                sm = nums1[i] + nums2[j]
                tmp = dic.get(sm, [])
                tmp.append([nums1[i], nums2[j]])
                dic[sm] = tmp
        keys = sorted(dic.keys())
        ans = []
        for m in keys:
            ls = dic[m]
            ans.extend(ls)
            if len(ans) >= k:
                return ans[:k]
        return ans
```

### 1.1.58. [948. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

- 小さい方から取り続ける
- 取れなくなったら最大のものでチャージ
- 細かい条件に注意しつつ、繰り返す
- 貪欲法

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens:
            return 0

        tokens.sort()
        ans = 0

        while len(tokens) > 0:
            while tokens and P >= tokens[0]:
                P -= tokens.pop(0)
                ans += 1
                if len(tokens) == 0:
                    return ans

            if len(tokens) > 1 and tokens[-1] > tokens[0] and ans > 0:
                P += tokens.pop()
                ans -= 1
            else:
                return ans
```

### 1.1.59. ▲[1105. Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/)

- 実装方針が思いつかない
- DiscussionではDPで解かれていた
- ▲DP配列が何を表しているのか、いまいちピンとこない…

```python
# Discussionを参考に実装
# https://leetcode.com/problems/filling-bookcase-shelves/discuss/323415/simple-Python-DP-solution
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            maxw = shelf_width
            maxh = 0
            j = i - 1
            while j >= 0 and maxw >= books[j][0]:
                maxw -= books[j][0]
                maxh = max(maxh, books[j][1])
                dp[i] = min(dp[i], dp[j] + maxh)
                j -= 1
        return dp[n]
```

### 1.1.60. ▲[1191. K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)

- ▲Discussionを見ると`Kadane's Algorithm`というのを使用していた
  - subarrayの合計の中で最大のものを得るアルゴリズム

```python
for num in arr:
    cur = max(num, num + cur)
    res = max(res, cur)
```

```python
# Disucssionを参考に実装
# https://leetcode.com/problems/k-concatenation-maximum-sum/discuss/382808/Python3-6-liner-Kadane
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def Kadane(arr, res = 0, cur = 0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        mod = 10 ** 9 + 7
        if k > 1:
            ans = ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod  # ここの証明が分からない
        else:
            ans = Kadane(arr) % mod
        return ans
```