# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:07:26 2024

@author: ASUS
"""

hour = int(input('Nhập giờ: '))
min = int(input('Nhập phút: '))
sec = int(input('Nhập giây: '))
x = hour*3600 + min*60 + sec
print('Đổi ra giây là: ',x)
