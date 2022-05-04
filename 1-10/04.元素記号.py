#!/usr/bin/env python
# coding: utf-8

# In[3]:


# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）
# への連想配列（辞書型もしくはマップ型）を作成せよ．

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
text = text.replace('.','')

split_list = text.split()
# 開始番号を0ではなく1に設定する場合、numpy配列やpandasのdataFrameに格納して-1処理をするか、for文の内包表記でリストの各要素を-1すれば良い
one_index_list = [0,4,5,6,7,8,14,15,18]

dict_word = {}
for i in range(len(split_list)):
    if i in one_index_list:
        pre_char = split_list[i][0] # 先頭1文字
    else:
        pre_char = split_list[i][0:2] # 先頭2文字
    
    dict_word[pre_char] = i
    
print(dict_word)
"""
{'H': 0, 'He': 1, 'Li': 2, 'Be': 3, 'B': 4, 'C': 5, 'N': 6, 'O': 7, 
'F': 8, 'Ne': 9, 'Na': 10, 'Mi': 11, 'Al': 12, 'Si': 13, 'P': 14,
'S': 15, 'Cl': 16, 'Ar': 17, 'K': 18, 'Ca': 19}

"""

