#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

      def backtrack(board: list, row: int):
        '''
        路径：board 中小于 row 的行都已经放置皇后
        选择列表：第 row 行的所有列都是放置皇后的选择
        结束条件：row 超过 board 的最后一行
        '''
        # 结束条件
        if row == len(board):
          result.append(board[:])
          return

        n = len(board[row]) # 列数
        for col in range(n):
          # 排除不合法选择
          if not isValid(board, row, col):
            continue
          # 做选择
          # board[row][col] = 'Q' # TypeError: 'str' object does not support item assignment
          board[row] = replacer(board[row], 'Q', col)
          # 进入下一轮决策
          backtrack(board, row+1)
          # 撤销选择
          board[row] = replacer(board[row], '.', col)

      def isValid(board: list, row: int, col: int):
        '''
        是否可以在[row][col]放置皇后
        '''
        n = len(board) # 行数
        # 检查上方列是否有皇后冲突
        for i in range(n):
          if board[i][col] == 'Q':
            return False

        # 检查右上方是否有皇后冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
          if board[i][j] == 'Q':
            return False
          i -= 1
          j += 1

        # 检查左上方是否有皇后冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
          if board[i][j] == 'Q':
            return False
          i -= 1
          j -= 1

        return True

      def replacer(s, newstring, index, nofail=False):
        # raise an error if index is outside of the string
        if not nofail and index not in range(len(s)):
            raise ValueError("index outside given string")

        # if not erroring, but the index is still not in the correct range..
        if index < 0:  # add it to the beginning
            return newstring + s
        if index > len(s):  # add it to the end
            return s + newstring

        # insert the new string between "slices" of the original
        return s[:index] + newstring + s[index + 1:]

      # 初始化键盘，n行n列  '.'表示空位 'Q'表示皇后
      board = ['.'*n for _ in range(n)]

      result = []
      backtrack(board, 0)
      return result


# @lc code=end
