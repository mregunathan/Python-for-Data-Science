#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Extra Exercises 
# 
# 

# Get all items of the below dictionary

# In[1]:


d = {'key1':'item1','key2':'item2'}


# In[2]:


d.items()


# Write a function to get the student resident type and print the tuition fees of the student. If the student is resident, fees is 500 and if the student is non resident, fee is 1000

# In[3]:


def studentFees(student_type):
    if student_type == "Resident":
        return 500
    else:
        return 1000


# In[4]:


studentFees("Resident")


# In[5]:


studentFees("Non Resident")


# Get a decimal number with multiple digits and format it to 2 digits.

# In[8]:


def formatDecimal(d):
    return format(d, ".2f")


# In[9]:


print(formatDecimal(3.4567))


# Print numbers from 0 till a given number

# In[12]:


def printNum(n):
    while n >= 0:
        print(n)
        n -=1
    print("All numbers are printed")


# In[13]:


printNum(10)


# ** Print the input var n times **

# In[16]:


def timesn(var, n):
    return var*n


# In[17]:


print(timesn("mahima", 5))


# Find how many numbers between 1 and 100 are lesser than a variable

# In[18]:


var = 50
count = 0
for i in range(100):
    if var > i+1:
        count +=1
print(count)


# Given a list of strings, convert them to a list of numeric values

# In[1]:


# Task 1
list1 = ["10.5", "30", "18.5"]
list2 = []

# Method 1
for l in list1:
    list2.append(float(l))
print(list2)

# Method 2
result = map(lambda x: float(x), list1)
print(list(result))

# Method 3
list1 = [float(l) for l in list1]
print(list1)


# Here is a list of some state names that we have pulled in from the web. But as you can see, they need to be cleaned up.

# In[2]:


import re
states = ["Utah$$", "   New! York", "alabama    ","Wyoming,,"]
new_states = []
for state in states:
    new_state = re.sub("[^A-Za-z ]+", "", state) # Removes special characters
    new_state = new_state.strip() # Removes the leading ad trailing spcaces
    new_state = new_state.title() # Capitalize the first character of each word
    new_states.append(new_state)
print(new_states)


# Count the number of occurrences of words starting with the letter ‘b’ in the following list, and store the word and count in a dict

# In[3]:


list_words = ['bear', 'deer', 'fish', 'bee', 'boar', 'horse', 'cat', 'dog', 'bee', 'bear', 'bee']
count = 0
dict_b_words = {}
for word in list_words:
    if word.startswith("b"):
        if word in dict_b_words:
            dict_b_words[word] += 1
        else:
            dict_b_words[word] = 1
            
print(dict_b_words)


# In[ ]:




