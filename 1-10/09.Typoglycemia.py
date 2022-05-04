#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば
”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）
を与え，その実行結果を確認せよ．
"""

import random

text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

split_text = text.split()
typo_list = []
for word in split_text:    
    if len(word) >= 5:
        # 文字列の分割
        pre_char = word[0]
        suf_char = word[len(word)-1]
        mid_char = word[1:(len(word)-1)]        
        mid_list = [mid_char[i:i+1] for i in range (len(mid_char))] # 単語を1文字ずつに区切る                
        rand_mid = ''.join(random.sample(mid_list,len(mid_list)))
        typo_list.append(pre_char + rand_mid + suf_char) # 単語の合成
    else:
        typo_list.append(word)

typo_text = ' '.join([word for word in typo_list])

print(typo_text)
"""
I c’lodnut beilvee that I cloud aalltucy unterasdnd what I was reiandg :
the poemnahnel power of the hmuan mind .
"""

