#!/usr/bin/env python
# coding: utf-8

# In[23]:


# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(text,n):
    return [text[i:i+n] for i in range (len(text))]

text = "I am an NLPer"

print(n_gram(text,1))
# ['I', ' ', 'a', 'm', ' ', 'a', 'n', ' ', 'N', 'L', 'P', 'e', 'r']
print(n_gram(text,2))
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er', 'r']
print(n_gram(text,3))
# ['I a', ' am', 'am ', 'm a', ' an', 'an ', 'n N', ' NL', 'NLP', 'LPe', 'Per', 'er', 'r']

