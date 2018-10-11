
# 乘法表

print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format(1, 2, 3, 4, 5, 6, 7, 8, 9))
for i in range(1, 10):
    print(i, end=' ')
    for n in range(i):
        print('%d*%d=%2d' % (i, n+1, i*(n+1)), end='|')
    print('\n' + '-'*63)
