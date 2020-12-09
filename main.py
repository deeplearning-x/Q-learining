import numpy as np


row = 5
col = 5
r = 0.8
Q_show = np.zeros((col, row), dtype=np.str)
for i in range(row):
    for j in range(col):
        Q_show[i, j] = 'O'
Q_show[1, 1] = 'X'
Q_show[1, 3] = 'X'
Q_show[3, 1] = 'X'
Q_show[3, 3] = 'X'
Q_show[4, 4] = '$'

Q_table = np.zeros((col*row, 4), dtype=float)
Q_data = np.zeros((col*row, 4), dtype=float)
Q_data[0] = [-1, 0, -1, 0]
Q_data[1] = [-1, -100, 0, 0]
Q_data[2] = [-1, 0, 0, 0]
Q_data[3] = [-1, -100, 0, 0]
Q_data[4] = [-1, 0, 0, -1]
Q_data[5] = [0, 0, -1, -100]
Q_data[6] = [0, 0, 0, 0]
Q_data[7] = [0, 0, -100, -100]
Q_data[8] = [0, 0, 0, 0]
Q_data[9] = [0, 0, 0, -1]
Q_data[10] = [0, 0, -1, 0]
Q_data[11] = [-100, -100, 0, 0]
Q_data[12] = [0, 0, 0, 0]
Q_data[13] = [-100, -100, 0, 0]
Q_data[14] = [0, 0, 0, -1]
Q_data[15] = [0, 0, -1, -100]
Q_data[16] = [0, 0, 0, 0]
Q_data[17] = [0, 0, -100, -100]
Q_data[18] = [0, 0, 0, 0]
Q_data[19] = [0, 100, 0, -1]
Q_data[20] = [0, -1, -1, 0]
Q_data[21] = [-100, -1, 0, 0]
Q_data[22] = [0, 0, -1, 0]
Q_data[23] = [-100, -1, 0, 100]
Q_data[24] = [0, -1, 0, -1]
i = 1000
while i != 0:
    i = i-1
    row = np.random.randint(0, 5)
    col = np.random.randint(0, 5)
    while True:
        j = np.random.randint(0, 4)
        if j == 0:
            if row == 0:
                continue
            Q_table[row*5 + col, 0] = Q_data[row*5 + col, 0] + r * max(Q_table[(row-1)*5 + col, 0],
                                                                       Q_table[(row-1)*5 + col, 1],
                                                                       Q_table[(row-1)*5 + col, 2],
                                                                       Q_table[(row-1)*5 + col, 3])
            if Q_table[row*5 + col, 0] > 100 or Q_table[row*5 + col, 0] <= -100:
                break
            row -= 1
        if j == 1:
            if row == 4:
                continue
            Q_table[row*5 + col, 1] = Q_data[row*5 + col, 1] + r * max(Q_table[(row+1) * 5 + col, 0],
                                                                       Q_table[(row+1) * 5 + col, 1],
                                                                       Q_table[(row+1) * 5 + col, 2],
                                                                       Q_table[(row+1) * 5 + col, 3])
            if Q_table[row*5 + col, 1] > 100 or Q_table[row*5 + col, 1] <= -100:
                break
            row += 1
        if j == 2:
            if col == 0:
                continue
            Q_table[row*5 + col, 2] = Q_data[row*5 + col, 2] + r * max(Q_table[row * 5 + (col-1), 0],
                                                                       Q_table[row * 5 + (col-1), 1],
                                                                       Q_table[row * 5 + (col-1), 2],
                                                                       Q_table[row * 5 + (col-1), 3])
            if Q_table[row*5 + col, 2] > 100 or Q_table[row*5 + col, 2] <= -100:
                break
            col -= 1
        if j == 3:
            if col == 4:
                continue
            Q_table[row*5 + col, 3] = Q_data[row*5 + col, 3] + r * max(Q_table[row *5+ (col+1), 0],
                                                                       Q_table[row *5+ (col+1), 1],
                                                                       Q_table[row *5+ (col+1), 2],
                                                                       Q_table[row *5+ (col+1), 3])
            if Q_table[row*5 + col, 3] >= 50 or Q_table[row*5 + col, 3] <= -50:
                break
            col += 1
print(Q_table)


def fun(a: int, b: int):
    Q_show[a, b] = 'P'
    print(Q_show)
    while a * b != 16:
        print()
        Q_show[a, b] = 'O'
        arrkey = 0
        tmax = Q_table[a * 5 + b, 0]
        for k in range(4):
            if Q_table[a * 5 + b, k] >= tmax:
                tmax = Q_table[a * 5 + b, k]
                arrkey = k
        if arrkey == 0:
            a -= 1
        if arrkey == 1:
            a += 1
        if arrkey == 2:
            b -= 1
        if arrkey == 3:
            b += 1
        Q_show[a, b] = 'P'
        print(Q_show)


fun(0, 0)