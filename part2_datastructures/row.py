row = ['_']*3
board =[]
for i in range(3):
  board.append(row)
board[0][0] = 'a'
print(board)
print('L'*10)
a = '{:4d}'.format(42)
b = '{:4}'.format('aa')
print(a)
print(b)
print('{:=-5d}'.format(23))