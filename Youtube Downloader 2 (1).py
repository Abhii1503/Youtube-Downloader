#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pytube')


# In[2]:


from pytube import YouTube


# In[ ]:


YouTube('Youtube Link').streams.first().download()


# In[ ]:




