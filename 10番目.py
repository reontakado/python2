# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:54:24 2019

@author: reon
"""

num=int(input("整数を入力してください　>"))
if 900<=num<=1100 or 1900<=num<=2100:
    print("1000または2000の100以内です")
else:
    print("1000または2000の100以内ではありません")