#!/usr/bin/env python
# coding: utf-8

# In[37]:


# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(text):
    return ''.join([chr(219-ord(char)) if (char.islower()) else (char) for char in text]) 

text = "You Say Hello And I Say Hello."
cipher_text2 = cipher(text)

print(cipher_text2)
print("-------------")
decry_text = cipher(cipher_text2)
print(decry_text)
"""
Ylf Szb Hvool Amw I Szb Hvool.
-------------
You Say Hello And I Say Hello.
"""

