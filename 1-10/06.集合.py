#!/usr/bin/env python
# coding: utf-8

# In[6]:


# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．


def n_gram(text,n):
    return [text[i:i+n] for i in range (len(text))]

text1 = "paraparaparadise"
text2 = "paragraph"

X = n_gram(text1,2)
print(X)
# ['pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ad', 'di', 'is', 'se', 'e']
Y = n_gram(text2,2)
print(Y)
# ['pa', 'ar', 'ra', 'ag', 'gr', 'ra', 'ap', 'ph', 'h']

# リストのままでは集合演算ができないため、set()で型変換を行う

# 和集合
union_XY = set(X) | set(Y)
print(union_XY)
# {'ad', 'ra', 'h', 'di', 'e', 'ph', 'se', 'ap', 'gr', 'ar', 'is', 'pa', 'ag'}

# 差集合
diff_XY = set(X) - set(Y)
print(diff_XY)
# {'ad', 'di', 'e', 'is', 'se'}

diff_YX = set(Y) - set(X)
print(diff_YX)
# {'h', 'ag', 'gr', 'ph'}

# 積集合
inter_XY = set(X) & set(Y)
print(inter_XY)
# {'pa', 'ap', 'ra', 'ar'}

if 'se' in X:
    print('include')
else:
    print('not include')
# inlcude
    
if 'se' in Y:
    print('include')
else:
    print('not include')
# not include

