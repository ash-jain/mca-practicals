import sys

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def solution(self):
        if not self.helper(0):
            raise ValueError("Enter a positive integer greater than 3.")

        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == -1:
                    self.board[i][j] = 'Q'
                else:
                    self.board[i][j] = '-'

        for row in self.board:
            print(row)

    def helper(self, count):
        if count == self.n:
            return True

        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    self.toggler(i, j, 1)
                    self.board[i][j] = -1
                    if self.helper(count + 1):
                        return True
                    self.toggler(i, j, -1)
                    self.board[i][j] = 0
        return False

    def toggler(self, row, column, val):
        for k in range(self.n):
            if self.board[k][column] != -1:
                self.board[k][column] += val
            if self.board[row][k] != -1:
                self.board[row][k] += val

        a, b = row + 1, column + 1
        while a < self.n and b < self.n:
            if self.board[a][b] != -1:
                self.board[a][b] += val
            a += 1
            b += 1

        a, b = row - 1, column - 1
        while a >= 0 and b >= 0:
            if self.board[a][b] != -1:
                self.board[a][b] += val
            a -= 1
            b -= 1

        a, b = row + 1, column - 1
        while a < self.n and b >= 0:
            if self.board[a][b] != -1:
                self.board[a][b] += val
            a += 1
            b -= 1

        a, b = row - 1, column + 1
        while a >= 0 and b < self.n:
            if self.board[a][b] != -1:
                self.board[a][b] += val
            a -= 1
            b += 1


NQueens(int(sys.argv[1])).solution()
