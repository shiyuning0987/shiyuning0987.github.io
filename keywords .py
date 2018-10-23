#!/usr/bin/env python
# coding: utf-8

# In[1]:


all_txt_file = ['trade-wars-news1.txt',
               'trade-wars-news2.txt',
               'trade-wars-news3.txt',
               'trade-wars-news4.txt',
               'trade-wars-news5.txt']

read_all_txt_file = []
for file in all_txt_file:
   f=open (file,'r')
   content= f.read()
   read_all_txt_file.append(content)


# In[2]:


all_words = ''.join(read_all_txt_file)


# In[3]:


import re
punctuation='[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?:【】“”‘’！，。？、~@#￥%……&*（）]+'
string = re.sub(punctuation,' ',all_words)
string=string.lower()
string


# In[4]:


string.split()


# In[5]:


List=string.split()


# In[6]:


import collections
from collections import Counter


# In[7]:


print (Counter(List))


# In[8]:


b = Counter(List).most_common(15)
print(b)


# In[9]:


import csv


# In[10]:


with open('result.csv','w') as f:
    mywriter=csv.writer(f)
    mywriter.writerow(["keyword","frequency"])
    mywriter.writerows(b)


# In[ ]:





# In[ ]:




