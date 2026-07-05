s = 'PAYPALISHIRING'
numRows = 5
if numRows == 1 or numRows >= len(s):
    print(s)

rows = [''] * numRows
going_down = False
cur_row = 0

for ch in s:
    rows[cur_row] += ch
    if cur_row == 0 or cur_row == numRows - 1:
        going_down = not going_down
    cur_row += 1 if going_down else -1
    print(rows)
print(''.join(rows))