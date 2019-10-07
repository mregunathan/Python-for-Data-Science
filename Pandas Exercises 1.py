#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


sal = pd.read_csv("Salaries.csv")


# ** Check the head of the DataFrame. **

# In[3]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[4]:


sal.info()


# **What is the average BasePay ?**

# In[6]:


sal["BasePay"].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[8]:


sal["OvertimePay"].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[9]:


sal[sal.EmployeeName == "JOSEPH DRISCOLL"]


# In[11]:


sal[sal.EmployeeName == "JOSEPH DRISCOLL"].JobTitle


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[18]:


sal[sal.EmployeeName == "JOSEPH DRISCOLL"].TotalPayBenefits


# ** What is the name of highest paid person (including benefits)?**

# In[19]:


sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()].EmployeeName


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[20]:


sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()].EmployeeName


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[23]:


sal["BasePay"].groupby(sal["Year"]).mean()


# ** How many unique job titles are there? **

# In[26]:


sal["JobTitle"].nunique()


# ** What are the top 5 most common jobs? **

# In[32]:


sal["JobTitle"].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[31]:


(sal[sal["Year"]==2013].JobTitle.value_counts() == 1).sum()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[37]:


def findChief(jobTitle):
    if "chief" in jobTitle.lower():
        return True
    else:
        return False


# In[41]:


sal["JobTitle"].apply(lambda x: findChief(x)).sum()


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[45]:


sal["title_len"] = sal["JobTitle"].apply(len)


# In[46]:


sal[["title_len","TotalPayBenefits"]].corr()


# # Great Job!
