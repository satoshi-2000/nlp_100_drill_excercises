#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd

features = ['name','gender','people','year']
df = pd.read_table('popular-names.txt',names=features)

print(len(df))
# 2780


# In[2]:


# 11.タブをスペースに置換
df.to_csv('popular-names_space.txt',sep=' ')


# In[10]:


# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
col1 = df['name']
col2 = df['gender']

with open('col1.txt','w') as f:
    for elem in col1:
        f.write("%s\n" % elem)    

with open('col2.txt','w') as g:
    for elem in col2:
        g.write("%s\n"% elem)    


# In[27]:


# 13. col1.txtとcol2.txtをマージ
df_col1 = pd.read_table('col1.txt',sep='\n',names=['name'])
df_col2 = pd.read_table('col2.txt',sep='\n',names=['gender'])

col1_list = df_col1['name']
col2_list = df_col2['gender']

df_merge = pd.DataFrame([col1_list,col2_list])
df_merge = df_merge.T # 転置しておく
print(df_merge)
"""
Name: gender, Length: 2780, dtype: object
           name gender
0          Mary      F
1          Anna      F
2          Emma      F
3     Elizabeth      F
4        Minnie      F
...         ...    ...
2775   Benjamin      M
2776     Elijah      M
2777      Lucas      M
2778      Mason      M
2779      Logan      M

"""

df_merge.to_csv('col_merge.txt',sep='\t',index=False) # indexはデフォルトでTrueに設定されているおり、表示しないために変更


# In[29]:


# 14. 先頭からN行を出力
# コマンドライン引数をargv[1]などで受け取ったものとする
N = 5

print(df[0:N])
print(df.head(5))

# for文でN回readlines()を行い、都度出力する方法などが想定解と思われる
"""
name gender  people  year
0       Mary      F    7065  1880
1       Anna      F    2604  1880
2       Emma      F    2003  1880
3  Elizabeth      F    1939  1880
4     Minnie      F    1746  1880
"""


# In[30]:


# 15. 末尾のN行を出力
N = 5

print(df[len(df)-N:])
print(df.tail(N))
"""
          name gender  people  year
2775  Benjamin      M   13381  2018
2776    Elijah      M   12886  2018
2777     Lucas      M   12585  2018
2778     Mason      M   12435  2018
2779     Logan      M   12352  2018
"""


# In[65]:


# 16. ファイルをN分割する
# https://www.delftstack.com/ja/howto/python-pandas/split-pandas-dataframe/ (2022/05/04参照)

N = 3

print(len(df))
print(int(len(df)/N))
"""
2780
926
"""
df_list = []

for i in range(N):    
    df_list.append(df[int(i*len(df)/N) : int((i+1)*len(df)/N)])

for elem in df_list:
    print(elem.head(3))
    
"""
   name gender  people  year
0  Mary      F    7065  1880
1  Anna      F    2604  1880
2  Emma      F    2003  1880
         name gender  people  year
926     Doris      F   16298  1926
927  Virginia      F   16162  1926
928   Mildred      F   13551  1926
        name gender  people  year
1853   David      M   46366  1972
1854    John      M   43181  1972
1855  Robert      M   43037  1972
"""

"""
# splitコマンドで行う場合、 -nオプションで5分割可能。
# 下記の場合、split/ 以下に分割されたファイルが格納される
$ split -n 5 popular-names.txt split/

"""


# In[69]:


# 17. １列目の文字列の異なり
# https://note.nkmk.me/python-list-duplicate-check/ (2022/05/04 参照)

col1 = df['name'] # 1列目
col1_list = col1.values.tolist()
col1_set = set(col1_list) # setによって重複削除
print(list(col1_set))

"""
['Patricia', 'Jason', 'Marie', 'Joshua', 'Minnie', 'Melissa', 'Susan', 'Mason', 'Lauren',
'Virginia', 'Frances', 'Alice', 'Linda', 'Liam', 'Henry', 'Megan', 'Gary', 'Angela', 
'Lisa', 'Margaret', 'Daniel', 'Jacob', 'Amy', 'Rebecca', 'Kathleen', 'Christopher', 
'Barbara', 'Ethan', 'Hannah', 'Karen', 'Lillian', 'Donald', 'John', 'Shirley',
'Heather', 'Mark', 'Joan', 'David', 'Alexander', 'Noah', 'Oliver', 'Larry', 'Sophia',
'Stephanie', 'Sarah', 'Deborah', 'Brandon', 'Carolyn', 'Tracy', 'Olivia', 'Harper', 
'Joseph', 'Lori', 'Judith', 'Justin', 'Jayden', 'Florence', 'Carol', 'Mia', 'Jessica',
'Samantha', 'Helen', 'Crystal', 'Rachel', 'Dorothy', 'Isabella', 'Julie', 'Michelle',
'Emily', 'Charles', 'Walter', 'Nicole', 'Amanda', 'Lucas', 'Richard', 'Brittany',
'Amelia', 'Mary', 'Steven', 'Bessie', 'Evelyn', 'Ida', 'Emma', 'Jennifer', 'Taylor',
'Logan', 'Ashley', 'Alexis', 'Harry', 'Nancy', 'Ronald', 'Michael', 'Sharon', 'Andrew'
, 'Abigail', 'Pamela', 'Kimberly', 'Kelly', 'Betty', 'Annie', 'Matthew', 'Elizabeth',
'Clara', 'Tammy', 'Madison', 'Thomas', 'William', 'Sandra', 'Charlotte', 'Tyler',
'Debra', 'Benjamin', 'James', 'Scott', 'Aiden', 'Robert', 'Doris', 'Frank', 'Ava', 
'Austin', 'Cynthia', 'George', 'Anna', 'Donna', 'Chloe', 'Elijah', 'Nicholas', 
'Anthony', 'Jeffrey', 'Edward', 'Bertha', 'Ruth', 'Brian', 'Mildred', 'Laura', 'Ethel']
"""


# In[70]:


# 18. 各行を3コラム目の数値の降順にソート
df_s = df.sort_values('people',ascending=False) # ascending=True : 昇順がデフォルト

print(df_s.head(5))
print(df_s.tail(5))

"""
         name gender  people  year
1340    Linda      F   99689  1947
1360    Linda      F   96211  1948
1350    James      M   94757  1947
1550  Michael      M   92704  1957
1351   Robert      M   91640  1947
      name gender  people  year
27   Annie      F    1326  1881
28  Bertha      F    1324  1881
8   Bertha      F    1320  1880
29   Alice      F    1308  1881
9    Sarah      F    1288  1880
"""


# In[85]:


# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# https://note.nkmk.me/python-collections-counter/ (2022/05/04参照)

import collections

col1 = df['name'] # 1列目
col_dict = collections.Counter(col1)
col_dict = dict(col_dict)
col_list = list(zip(col_dict.keys(),col_dict.values()))
col_keys=col_dict.keys()
print(col_list) # [('name','frequency')] が表示される
print(list(col_keys))

"""
['Mary', 'Anna', 'Emma', 'Elizabeth', 'Minnie', 'Margaret', 'Ida', 'Alice', 'Bertha',
'Sarah', 'John', 'William', 'James', 'Charles', 'George', 'Frank', 'Joseph', 'Thomas',
'Henry', 'Robert', 'Annie', 'Edward', 'Clara', 'Florence', 'Ethel', 'Bessie', 'Harry',
'Helen', 'Ruth', 'Marie', 'Lillian', 'Mildred', 'Dorothy', 'Frances', 'Walter', 
'Evelyn', 'Virginia', 'Richard', 'Betty', 'Donald', 'Doris', 'Shirley', 'Barbara', 
'Patricia', 'Joan', 'Nancy', 'Carol', 'David', 'Ronald', 'Judith', 'Linda', 'Sandra',
'Carolyn', 'Sharon', 'Michael', 'Susan', 'Donna', 'Larry', 'Kathleen', 'Deborah', 
'Gary', 'Karen', 'Debra', 'Pamela', 'Cynthia', 'Mark', 'Steven', 'Lisa', 'Jeffrey', 
'Lori', 'Kimberly', 'Tammy', 'Angela', 'Michelle', 'Jennifer', 'Melissa', 'Christopher',
'Brian', 'Amy', 'Laura', 'Tracy', 'Julie', 'Jason', 'Scott', 'Stephanie', 'Heather',
'Nicole', 'Matthew', 'Rebecca', 'Jessica', 'Amanda', 'Daniel', 'Kelly', 'Joshua', 
'Crystal', 'Ashley', 'Megan', 'Brittany', 'Andrew', 'Justin', 'Samantha', 'Lauren',
'Emily', 'Brandon', 'Tyler', 'Taylor', 'Nicholas', 'Jacob', 'Hannah', 'Austin', 
'Alexis', 'Rachel', 'Madison', 'Abigail', 'Olivia', 'Ethan', 'Anthony', 'Isabella', 
'Ava', 'Sophia', 'Chloe', 'Alexander', 'Mia', 'Jayden', 'Noah', 'Aiden', 'Mason',
'Liam', 'Charlotte', 'Harper', 'Benjamin', 'Elijah', 'Amelia', 'Logan', 'Oliver', 'Lucas']
"""

