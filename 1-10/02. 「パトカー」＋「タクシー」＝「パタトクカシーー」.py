#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

police = "パトカー"
taxi = "タクシー"

pol_list = list(police)
tax_list = list(taxi)

link_text = ""
for i in range(len(police)):
    link_text = link_text + pol_list[i] + tax_list[i]

print(link_text)
# パタトクカシーー    

