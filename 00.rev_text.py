#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 00.文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
text = "stressed"

rev_text = text[::-1] # スライスを利用
print(rev_text)
# desserts


# In[3]:


# https://note.nkmk.me/python-reverse-reversed/ 参照(2022/05/04)
rev_text_list = list(reversed(text))
print(rev_text_list)
# ['d', 'e', 's', 's', 'e', 'r', 't', 's']

rev_text2 = ''.join(text_list)
print(rev_text2)
# desserts


# In[6]:





# In[ ]:




