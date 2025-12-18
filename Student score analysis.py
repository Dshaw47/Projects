#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df=pd.read_csv("Expanded_data_with_more_features.csv")


# In[6]:


print(df.head())


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[14]:





# In[15]:


print(df.head())


# # Gender wise distribution

# In[37]:


ax=sns.countplot(data=df,x="Gender")
plt.title("Gender Distribution")
ax.bar_label(ax.containers[0])
plt.show()


# # effect of parents education on student scores 

# In[38]:


gb=df.groupby("ParentEduc").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
print(gb)
sns.heatmap(gb, annot=True)
plt.title("Relationship Between Parents Education on student scores")
plt.show()


# # effect of parents maratial status on student Scores

# In[39]:


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
print(gb1)
sns.heatmap(gb1, annot=True)
plt.title("Relationship Between Parents Maratial Status on student scores")
plt.show()


# # Detecting Outliers

# In[41]:


sns.boxplot(data=df, x="MathScore")
plt.show()


# In[42]:


sns.boxplot(data=df, x="ReadingScore")
plt.show()


# In[43]:


sns.boxplot(data=df, x="WritingScore")
plt.show()


# In[45]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Group

# In[70]:


groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
l=["group A","group B","group C","group D","group E"]
mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist,labels=l,autopct="%1.2f%%")
plt.title("Distribution via Ethenic group")
print(mlist)
plt.show()


# In[67]:


ax=sns.countplot(data=df,x="EthnicGroup")
ax.bar_label(ax.containers[0])


# In[ ]:




