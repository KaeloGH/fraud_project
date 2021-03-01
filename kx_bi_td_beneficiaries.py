#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pyodbc as p


# In[2]:


from datetime import date
today = date.today()


# In[3]:


d1 = today.strftime("%Y%d%m")
print("d1 =", d1)


# This is the raw data script:

# In[4]:


sql_query="""SELECT * from mipbi_dbo.td_beneficiary;"""


# Here we connect to the __kx_bi__ postgres database and execute the above query to generate the EAP raw data set:

# In[5]:


conn_str = (
    "DRIVER={PostgreSQL ODBC Driver(UNICODE)};"
    "DATABASE=kx_bi;"
    "UID=postgres;"
    "PWD=postgres;"
    "SERVER=172.31.244.44;"
    "PORT=5432;"
    )

conn = p.connect(conn_str)
# cursor = conn.cursor()


# In[6]:


td_beneficiaries_df = pd.read_sql(sql_query,conn)


# In[7]:


file_name='td_beneficiaries_df_{d1}.csv'.format(d1=d1)
file_path='\\home\\christo\\github_repos\\fraud_project\\data\\'
file=file_path+file_name


td_beneficiaries_df.to_csv(file, index=False)

