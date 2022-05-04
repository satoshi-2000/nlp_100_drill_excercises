#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．

def print_temp(x,y,z):
    print(str(x) + '時の' + y + 'は' + str(z))

print_temp(12,"気温",22.4)
# 12時の気温は22.4

