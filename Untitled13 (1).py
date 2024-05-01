#!/usr/bin/env python
# coding: utf-8

# In[21]:


s1 = "abcde"
s2 = ''
for i in range(len(s1)):
    s2 += s1[(i + 1) % len(s1)]

print(s2)


# In[ ]:





# In[ ]:




