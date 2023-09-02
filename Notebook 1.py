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
     .parquet('abfss://0b3da212-4fe1-4e3e-bcc3-ebbe0aaf84b3@onelake.dfs.fabric.microsoft.com/08c0f6c4-d3ae-4898-92f7-1021ecf9ff33/Files/raw/data/address')
    )


# In[ ]:


df.show(5,truncate=False)


# In[ ]:


df.printSchema()


# In[ ]:




