#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


import seaborn as sns


# In[3]:


student_per = pd.read_csv("StudentsPerformance.csv")


# In[4]:


student_per.head(4)


# In[5]:


student_per.drop(['lunch','test preparation course'],axis = 1)


# In[6]:


student_per['parental level of education'] = student_per['parental level of education'].fillna("default")


# In[7]:


student_per


# In[8]:


student_per['race/ethnicity'] = student_per['race/ethnicity'].map({
    'group A':'Asian Students',
    'group B':'African Students',
    'group C':'Afro-Asian Students',
    'group D':'American Students',
    'group E':'European Students’'
}
)


# In[9]:


student_per.head()


# In[19]:


ax = sns.countplot(x="test preparation course", hue="gender", palette="Set1", data=student_per)
ax.set(title="Test Preparation", xlabel="Course", ylabel="Total")
plt.show()


# In[21]:


ax = sns.countplot(x="race/ethnicity", hue="gender", palette="Set1", data=student_per)
ax.set(title="Students according to each group", xlabel="Ethnicity", ylabel="Total")
plt.show()


# In[24]:


marks_intervals = [0, 40, 50, 60, 75]
categories = ['failed', 'second class', 'first class', 'distinction']
student_per['Marks_Categories_math'] = pd.cut(student_per.mathscore, marks_intervals, labels=categories)
ax = sns.countplot(x="Marks_Categories_math", hue="gender", palette="Set1", data=student_per)
ax.set(title="Math Marks Grouping", xlabel="Marks Groups", ylabel="Total")
plt.show()


# In[33]:


student_per = student_per.rename(columns={'reading score':'readingscore'})
student_per['Marks_Categories_reading'] = pd.cut(student_per.readingscore, marks_intervals, labels=categories)
ax = sns.countplot(x="Marks_Categories_reading", hue="gender", palette="Set1", data=student_per)
ax.set(title="Reading Marks Grouping", xlabel="Marks Groups", ylabel="Total")
plt.show()


# In[34]:


student_per = student_per.rename(columns={'writing score':'writingscore'})
student_per['Marks_Categories_writing'] = pd.cut(student_per.writingscore, marks_intervals, labels=categories)
ax = sns.countplot(x="Marks_Categories_writing", hue="gender", palette="Set1", data=student_per)
ax.set(title="Writing Marks Grouping", xlabel="Marks Groups", ylabel="Total")
plt.show()
