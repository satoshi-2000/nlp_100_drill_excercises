#!/usr/bin/env python
# coding: utf-8

# In[4]:


# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# '.'は単語ではないので置換しておく
text = text.replace('.','')

split_text = text.split()

len_word_list = []
for word in split_text:
    len_word_list.append(len(word))

print(len_word_list)
# [3, 1, 4, 1, 6, 9, 2, 7, 5, 3, 5, 8, 9, 7, 9]

