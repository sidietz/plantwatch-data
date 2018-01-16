
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pl0 = pd.read_csv("Kraftwerksliste_CSV.csv", error_bad_lines=False, engine="python", encoding="latin1", sep=";", skiprows=9)
bm = pd.read_csv("block_plant_mapper.csv", error_bad_lines=False, engine="python", sep=";")


# In[3]:


#bm
pl1 = pl0.loc[np.logical_or(pl0.Energieträger == "Kernenergie", np.logical_or(pl0.Energieträger == "Erdgas", np.logical_or(pl0.Energieträger == "Steinkohle", pl0.Energieträger == "Braunkohle"))), :]


# In[4]:


pl2 = pl1.rename(columns={ pl1.columns[0]: "BlockID", pl1.columns[3]: "PLZ", pl1.columns[4]: "Ort", pl1.columns[8]: "Inbetriebnahme", pl1.columns[9]: "Status", pl1.columns[16]: "Nettoleistung"})
#pl3 = pl2.rename(columns={ pl1.columns[1]: "BlockID" })


# In[5]:


pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace('.','')
pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace(',','.')
#pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace('\n','')
#pl2['Nettoleistung'] = pl2[pd.to_numeric(pl2["Nettoleistung"])]
#pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace(';','.')


# In[6]:


#pl2[] = pl2[pd.to_numeric(pl2["Nettoleistung"])]
pl2['Nettoleistung'] = pl2['Nettoleistung'].apply(pd.to_numeric)


# In[7]:


cols = [10, 11,12,14,15,17,18,19]
pl3 = pl2.drop(pl2.columns[cols],axis=1)


# In[8]:


pl3.rename(columns={ pl3.columns[10]: "Energieträger"}, inplace=True)


# In[9]:


pl4 = bm.merge(pl3, how="outer", on="BlockID")


# In[10]:


pl5 = pl4[pd.notnull(pl4['BlockID'])]
#pl5 = pl4
pl6 = pl5[pd.notnull(pl5['Nettoleistung'])]


# In[11]:


blocks = pl6.copy()
stammdaten = pl6.copy()


# In[12]:


blocks.sort_values("Nettoleistung", inplace=True, ascending=False)
# blocks


# In[13]:


plants = blocks.loc[:]
plants = plants.dropna(subset=["KraftwerkID"])


# In[14]:


plants_d = plants.loc[plants.duplicated("KraftwerkID", keep=False)]
# plants_d


# In[15]:


plants_c = plants_d.groupby(["KraftwerkID"]).sum()
plants_count = plants_d.groupby(["KraftwerkID"]).count()


# In[16]:


plants_f = plants_c.reset_index()


# In[17]:


plants_count = plants_count.loc[:, ["BlockID"]]


# In[18]:


plants_count = plants_count.reset_index()
# plants_count 


# In[19]:


plants_f = plants_f.merge(plants_count, on="KraftwerkID", how="inner")
# plants_f


# In[20]:


plants_a = plants.drop_duplicates(subset="KraftwerkID")


# In[21]:


plants_b = plants_d.loc[:]


# In[22]:


plants_f = plants_f.rename(columns={ "Nettoleistung": "Gesamtleistung", "BlockID": "Blockzahl"})


# In[23]:


plants_f = plants_f.merge(plants_a, on="KraftwerkID", how="left")
# plants_f


# In[24]:


cols = [4,5,6,8]
blocks.drop(blocks.columns[cols],axis=1, inplace=True)


# In[25]:


#blocks.loc[blocks.Energieträger == 'Erdgas',]


# In[26]:


plants_2 = plants.rename(columns={plants.columns[6]: "Anschrift"})
# plants_2


# In[27]:


cols = [2, 3, 8, 9, 10, 11, 12]
plants_3 = plants_2.drop(plants_2.columns[cols],axis=1, )
# plants_3


# In[28]:


cols = [0,2,3,9,10,11,12]
stammdaten.drop(stammdaten.columns[cols],axis=1, inplace=True)


# In[29]:


stammdaten.to_csv("stammdaten.csv", index=False)


# In[30]:


blocks.to_csv("blocks_3.csv", index=False)


# In[31]:


stammdaten.to_csv("stammdaten_nh.csv", index=False, header=False)
blocks.to_csv("blocks_nh.csv", index=False, header=False)

