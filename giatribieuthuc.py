# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:33:50 2024

@author: ASUS
"""

import math
a = float(input('Nhập giá trị a = '))
b = float(input('Nhập giá trị b = '))
m = ((math.sqrt(a)-math.sqrt(b))/(pow(a,1/4)-pow(b,1/4))) - ((math.sqrt(a)+pow((a*b),1/4))/(pow(a,1/4)+pow(b,1/4)))
print('Kết quả là: ',m) 