#!/usr/bin/env python
# coding: utf-8

# ## Notebook 1
# 
# 
# 

# In[ ]:


# Welcome to your new notebook
# Type here in the cell editor to add code!

df=( spark.\
     read.\
     options(inferSchema='True',
             header='True',
             delimiter=',',
             encoding='UTF-8',
             ignoreLeadingWhiteSpace='True',
             ignoreTrailingWhiteSpace='True')\
     .parquet('abfss://Files/raw/data/address')
    )


# In[ ]:


df.show(5,truncate=False)


# In[ ]:


df.printSchema()


# In[ ]:




