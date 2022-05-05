#!/usr/bin/env python
# coding: utf-8

# In[32]:


# 20. JSONデータの読み込み
# https://fnwiya.hatenablog.com/entry/2016/01/07/210000 (2022/05/05参照)
# https://note.nkmk.me/python-pandas-query/ (2022/05/05参照)

import gzip
import json
import pandas as pd

obj_list = []
#df = pd.DataFrame(index=[],names=['title','text'])

# pd.read_jsonでも良い
with gzip.open('jawiki-country.json.gz','r') as f:
    for line in f:
        obj = json.loads(line) # 辞書型で格納される
        obj_list.append(obj)

df = pd.DataFrame(obj_list)
#text = df["title"] == 'イギリス'
df_eng = df.query('title == "イギリス"')
text_list = df_eng['text'].values
print(text_list)
"""
235    {{redirect|UK}}\n{{redirect|英国|春秋時代の諸侯国|英 (春秋)...
Name: text, dtype: object
"""


# In[50]:


# 21. カテゴリ名を含む行を抽出
# 行を抽出するため、カテゴリ名の宣言から始まり、改行(\n)されるまでのパターンを抽出すれば良い
# https://murashun.jp/article/programming/regular-expression.html (2022/05/05参照)
# https://note.nkmk.me/python-str-extract/ (2022/05/05参照)
import re

text2 = text_list[0]
text = str(text2)
pattern_list =re.findall(r'\[\[Category:.+\]\]', text)

for pattern in pattern_list:
    print(pattern)
"""
[[Category:イギリス|*]]
[[Category:イギリス連邦加盟国]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国|元]]
[[Category:海洋国家]]
[[Category:現存する君主国]]
[[Category:島国]]
[[Category:1801年に成立した国家・領域]]
"""


# In[51]:


# 22. カテゴリ名の抽出

text2 = text_list[0]
text = str(text2)
pattern_list =re.findall(r'\[\[Category:(.+)\]\]', text) # ()で括った

for pattern in pattern_list:
    print(pattern)

"""
イギリス|*
イギリス連邦加盟国
英連邦王国|*
G8加盟国
欧州連合加盟国|元
海洋国家
現存する君主国
島国
1801年に成立した国家・領域
"""


# In[76]:


# 23. セクション構造
# https://ja.wikipedia.org/wiki/Help:%E3%82%BB%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3 (2022/05/05参照)
# sectionを取り出す
# 今回の場合はレベルが高々3であるため逐次差分を取り出すが、
# 深い場合が想定されるならば、階層の上限を一定レベルまでに制限して、要素数が0になるまでループを回せば良い
# '='の数を2で割れば良い
# '='をreplace()で置換する

def get_sec_level(section):
    return (int(section.count('=') / 2) + 1) # 抽出した時点でレベル1以上のセクションであるため


section_list =re.findall(r'==(.+)==', text) # textからセクション一覧を抽出
for section in section_list:
    sec_level = get_sec_level(section)
    print(section.replace('=',''),sec_level)

"""
国名 1
歴史 1
地理 1
主要都市 2
気候 2

"""    


# In[99]:


# 24. ファイル参照の抽出
# https://murashun.jp/article/programming/regular-expression.html (2022/05/05参照)
# [[ファイル:Descriptio Prime Tabulae Europae.jpg 
# [[ファイル:hogehoge.<拡張子>]]となっている
# 今回はjpg,svg,pngの3種類しかないため、とりあえず{3}文字までに設定する

#media_list = re.findall(r'\[\[ファイル:(.+\.[a-z|A-Z]{3}).+\]\]',text)

#media_list = re.findall(r'\[\[ファイル:(.+[jpg|svg|png|JPG|SVG|PNG]).+\]\]',text)
media_list = re.findall(r'\[\[ファイル:(.+[jpg|svg|png|JPG|SVG|PNG])',text)

#media_list = re.match(r'\[\[ファイル:(.+\.[a-z|A-Z]{3}).+\]\]',text)
#media_list = re.findall(r'\[\[ファイル:([a-z|A-Z|0-9]+\.[a-z|A-Z]{3})',text)

#print(media_list)

for media in media_list:
    print(media)


# In[78]:


print(text)


# In[164]:


# 25. テンプレートの抽出
# https://docs.python.org/3/library/re.html (2022/05/05参照)
temp_dict = {}
text_split = text.split('\n')

for line in text_split:
    # styleを含む場合があったため、否定読み(?!hogehoge)を導入
    # [ ?](space+?)で空白があってもなくても    
    pattern = re.findall(r'^\|(?! ?style|\<!)(.+)=(.+)$',line)
    
    if len(pattern) == 1:
        temp_dict[pattern[0][0]] = pattern[0][1] # 多次元リストの要素指定で、[0][0]はkey,[0][1]はvalueに設定

print(temp_dict)    


# In[165]:


# 26. 強調マークアップの除去
# 例 : '''グレー ... 王国''' 

text_remove_empha = text.replace("'''","")
text_remove_empha = text_remove_empha.replace("''","")


temp_dict = {}
text_split = text_remove_empha.split('\n')

for line in text_split:
    # styleを含む場合があったため、否定読み(?!hogehoge)を導入
    # [ ?](space+?)で空白があってもなくても    
    pattern = re.findall(r'^\|(?! ?style|\<!)(.+)=(.+)$',line)
    
    if len(pattern) == 1:
        temp_dict[pattern[0][0]] = pattern[0][1] # 多次元リストの要素指定で、[0][0]はkey,[0][1]はvalueに設定

print(temp_dict) 


# In[173]:


# 27. 内部リンクの除去Permalink


text_remove_empha = text.replace("'''","")
text_remove_empha = text_remove_empha.replace("''","")


#text_remove_link = text_remove_empha.replace(r"\[\[.+\|.+\]]",".+.+")
text_remove_link = text_remove_empha.replace("[[","")
#text_remove_link = text_remove_link.replace(r"\{\{.+\}\}",".+")
text_remove_link = text_remove_link.replace("{{","")
text_remove_link = text_remove_link.replace("}}","")
text_remove_link = text_remove_link.replace("]]","")


temp_dict = {}
#text_split = text_remove_empha.split('\n')
text_split = text_remove_link.split('\n')

for line in text_split:
    # styleを含む場合があったため、否定読み(?!hogehoge)を導入
    # [ ?](space+?)で空白があってもなくても    
    pattern = re.findall(r'^\|(?! ?style|\<!)(.+)=(.+)$',line)
    
    if len(pattern) == 1:
        temp_dict[pattern[0][0]] = pattern[0][1] # 多次元リストの要素指定で、[0][0]はkey,[0][1]はvalueに設定

print(temp_dict) 


# In[182]:


# 28. MediaWikiマークアップの除去
# <br />などのタグ類を除去する場合は同様にstring.replace()を行えば良い


text_remove_empha = text.replace("'''","")
text_remove_empha = text_remove_empha.replace("''","")


#text_remove_link = text_remove_empha.replace(r"\[\[.+\|.+\]]",".+.+")
text_remove_link = text_remove_empha.replace("[[","")
#text_remove_link = text_remove_link.replace(r"\{\{.+\}\}",".+")
text_remove_link = text_remove_link.replace("{{","")
text_remove_link = text_remove_link.replace("}}","")
text_remove_link = text_remove_link.replace("]]","")


temp_dict = {}
#text_split = text_remove_empha.split('\n')
text_split = text_remove_link.split('\n')

for line in text_split:
    # styleを含む場合があったため、否定読み(?!hogehoge)を導入
    # [ ?](space+?)で空白があってもなくても    
    pattern = re.findall(r'^\|(?! ?style|\<!)(.+)=(.+)$',line)
    
    if len(pattern) == 1:
        # 辞書データ用の構造処理のため、この段階で'|'を除去
        #pattern[0][1] = tuple(str(pattern[0][1]).replace("|",""))
        temp_str = str(pattern[0][1])
        temp_str = temp_str.replace("|","")        
        temp_dict[pattern[0][0]] = pattern[0][1] # 多次元リストの要素指定で、[0][0]はkey,[0][1]はvalueに設定
        temp_dict[pattern[0][0]] = temp_str 

print(temp_dict) 


# In[193]:


# 29. 国旗画像のURLを取得する
# '国旗画像 ': ' Flag of the United Kingdom.svg'
# https://www.mediawiki.org/wiki/API:Imageinfo/ja#Python (2022/05/05参照)

import requests
S = requests.Session()

title = temp_dict["国旗画像 "] 

title = "File:" + title

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",    
    "titles": title
    #  Flag of the United Kingdom.svg
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"])
    
# File:Flag of the United Kingdom.svg is uploaded by User:Xaosflux

