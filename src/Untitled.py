# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
ans = 0
for i in range(1, 8):
    ans += i*i
    print(i, ans)
    
print(ans)
# -

A

-1%7


# +
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        og = obstacleGrid
        r = len(og)
        c = len(og[0])
        for i in range(r):
            for j in range(c):
                if og[i][j]==1:
                    og[i][j] = 0
                else:
                    og[i][j] = 1

        print(og)
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
                    
        print(og)
        return og[-1][-1]
    
ins = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
ins.uniquePathsWithObstacles(obstacleGrid)
# -











class Solution:
    def isValidSudoku(self, board):
        # columns
        col_board = [[] for _ in range(9)]
        # 9*9
        nine_board = [[] for _ in range(9)]
        for i in range(len(board)):
            lis = board[i]
            print(lis)
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
            print(col)
            if not self.isValid(col):
                return False
        # 9*9
        for nine in nine_board:
            print(nine)
            if not self.isValid(nine):
                return False
            
        return True


    def isValid(self, lis):
        dic = {}
        for i in lis:
            if i!=".":
                dic[i] = dic.get(i, 0)+1
                print(dic[i])
                if dic[i]==2:
                    return False
        return True

ins = Solution()
inp = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ins.isValidSudoku(inp)


# https://leetcode.com/problems/combination-sum/discuss/16506/8-line-Python-solution-dynamic-programming-beats-86.77
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[[]]]+[[] for _ in range(target)]
        for i in range(1, target+1):
            for n in candidates:
                if n>i:
                    break
                for lis in dp[i-n]:
                    if not lis:
                        dp[i] += lis+[n]
                    elif n>=lis:
                        dp[i] += [lis]+[n]
        print(dp)
        return dp[target]


ins = Solution()
candidates = [2,3,6,7]
target = 7
ins.combinationSum(candidates, target)

# %debug

dp = []

dp + [2]

dp = [2, 3, 4]

dp

dp += [2]+[3]

dp


# +
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
            tmp = nums
            print(tmp, i)
            x = tmp.pop(i)
            self.backtracking(tmp, path+[x], ans)
            
            
ins = Solution()
nums = [1,2,3]
ins.permute(nums)
# -



# +
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything][modify matrix in-place instead.
        """
        # i...j
        # j...n-i
        ni = len(matrix)
        nj = len(matrix[0])
        for i in range(ni//2+1):
            for j in range(i, nj-i-1):
                matrix[i][j], matrix[j][nj-i-1], matrix[ni-i-1][nj-i-1], matrix[ni-j-1][i] = \
                matrix[ni-j-1][i], matrix[i][j], matrix[j][nj-i-1], matrix[ni-i-1][nj-i-1]
                    
ins = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
ins.rotate(matrix)
# -

matrix


# %debug

# +
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
                print("if", n, x)
            x *= x
            print("x:", x)
            n >>= 1
            print("n:", n)
        return pow
    
    
ins = Solution()
ins.myPow(2, 10)


# +
class Solution:
    def spiralOrder(self, matrix):
        ans = []
        while matrix:
            # 先頭行をpop（順方向）
            tmp = matrix.pop(0)
            ans.extend(tmp)
            if not matrix[0]:
                return ans

            # 最終列をpop（順方向）
            for i in range(len(matrix)):
                tmp = matrix[i].pop(-1)
                ans += [tmp]
            if not matrix[0]:
                return ans

            # 最終行をpop（逆方向）
            tmp = matrix.pop(-1)
            tmp.reverse()
            ans.extend(tmp)
            if not matrix[0]:
                return ans

            # 先頭列をpop（逆方向）
            tmp = []
            for i in range(len(matrix)):
                print(matrix[i], i, tmp)
                tmp.append(matrix[i].pop(0))
            tmp.reverse()
            ans.extend(tmp)
        return ans

ins = Solution()
matrix = [[7],[9],[6]]
ins.spiralOrder(matrix)


# +
matrix = []

not matrix
# -

min([1])

# +
# https://atcoder.jp/contests/abc138/submissions/6992193
from collections import deque
 
N, Q = 4, 3
to = [[] for _ in range(N)]

ab = [
    [1,2],
    [2,3],
    [2,4]
]
px = [
    [2,10],
    [1,100],
    [3,1]
]

# to: つながっているノード番号を保持
for i in range(N - 1):
    a, b = ab[i]
    to[a - 1].append(b - 1)
    to[b - 1].append(a - 1)

# P: 各ノード番号にxの和を保持（後に累積和をとる準備）
P = [0] * N
for j in range(Q):
    p, x = px[j]
    P[p - 1] += x

# cnt: 累積和の計算用    
cnt = [0] * N

# rootから順に累積和をとっていく
q = deque()
q.append((0, 0, -1))  # ダミーの値
while len(q):
    p, x, prev = q.pop()  # スタックとして使用
    x += P[p]
    cnt[p] = x
    for b in to[p]:  # つながっているノードにもxを加算
        if b != prev:
            print(b, x, p, prev, q, cnt)
            q.append((b, x, p))  # b: xを加算するノード, p: xが親（本ループですでに加算したノード）に波及して来ないようにするための制御用の値
print(*cnt)
# -

to

P

cnt


