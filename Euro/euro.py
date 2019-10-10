
# coding: utf-8

# In[12]:


import numpy as np 
from pandas import DataFrame
import pandas as pd

df=pd.read_csv('euro12.csv')
print(df)



# In[14]:


"""first=df["Goals"]
print(first)


# In[18]:


second=len(df['Team'])
print(second)


# In[21]:


# 3rd question=View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline=df[['Team','Yellow Cards','Red Cards']]
print(discipline)


# In[32]:


#5th question=Calculate the mean Yellow Cards given per Team
df["Yellow Cards"].mean()


# In[33]:


#7.Select the first 7 columns
df[df.columns[:7]]


# In[36]:


#8.Select all columns except the last 3.
df.iloc [:, :32]


# In[37]:


#6.Select the teams that start with G
ans=df["Team"].str.startswith("G")
ans==True
df[ans]


# In[38]:


#4.Sort the teams by Red Cards, then to Yellow Cards
print(df.sort_values(['Red Cards','Yellow Cards'],ascending=False))


# In[45]:


#9.Select the country with good defense
df[df['Goals conceded']==df['Goals conceded'].min()]


# In[46]:


#10.Country with poor goal saving skill
df[df['Saves-to-shots ratio']==df['Saves-to-shots ratio'].min()]"""


