# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:48:45 2024

@author: ASUS
"""

N = int(input('Số nguyên dương N có 2 chữ số: '))
a = N % 10
b = N // 10
if 10 <= N <= 99:
    print('Tổng các chữ số của N là: ',a + b)
else: print('Hãy nhập lại số nguyên dương có 2 chữ số')



