
# coding: utf-8

# In[545]:


import pandas as pd
import numpy as np


# In[546]:


pl0 = pd.read_csv("Kraftwerksliste_CSV.csv", error_bad_lines=False, engine="python", encoding="latin1", sep=";", skiprows=9)
bm = pd.read_csv("block_plant_mapper.csv", error_bad_lines=False, engine="python", sep=";")


# In[547]:


pl0.rename(columns={ pl0.columns[10]: "Energieträger_old", pl0.columns[13]: "Energieträger"}, inplace=True)


# In[548]:


#bm
pl1 = pl0.loc[np.logical_or(pl0.Energieträger == "Kernenergie", np.logical_or(pl0.Energieträger == "Erdgas", np.logical_or(pl0.Energieträger == "Steinkohle", pl0.Energieträger == "Braunkohle"))), :]


# In[549]:


# pl1


# In[550]:


pl2 = pl1.rename(columns={ pl1.columns[0]: "BlockID", pl1.columns[3]: "PLZ", pl1.columns[4]: "Ort", pl1.columns[8]: "Inbetriebnahme", pl1.columns[9]: "Status", pl1.columns[15]: "KWK", pl1.columns[16]: "Nettoleistung"})
#pl3 = pl2.rename(columns={ pl1.columns[1]: "BlockID" })


# In[551]:


pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace('.','')
pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace(',','.')
#pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace('\n','')
#pl2['Nettoleistung'] = pl2[pd.to_numeric(pl2["Nettoleistung"])]
#pl2['Nettoleistung'] = pl2['Nettoleistung'].str.replace(';','.')


# In[552]:


#pl2[] = pl2[pd.to_numeric(pl2["Nettoleistung"])]
pl2['Nettoleistung'] = pl2['Nettoleistung'].apply(pd.to_numeric)


# In[553]:


# pl2


# In[554]:


cols = [10, 11,12,14,17,18,19]
pl3 = pl2.drop(pl2.columns[cols],axis=1)


# In[555]:


# pl3


# In[556]:


atest = pl3.groupby(["Status"]).count()


# In[557]:


# atest


# In[558]:


# Status: endgültig stillgelegt, vorläufig stillgelegt, in Betrieb, Sicherheitsbereitschaft, Sonderfall, 
# Stillegung: [Jahreszahl]
# StA: ja/ nein


# In[559]:


newdf = pd.DataFrame()


# In[560]:


def generate_decom_tuple(state):
    if state == "In Betrieb":
        return("in Betrieb", 0)
    elif "Endgültig Stillgelegt" in state:
        a = "stillgelegt"
        b = int(state[22:26])
        return (a, b)
    elif "Vorläufig Stillgelegt" in state:
        a = "vorläufig stillgelegt"
        return (a, 0)
    else:
        return(state, 0)
    return (0, 0)


# In[561]:


def fix_company(company):
    cmp = company
    company_prefix, _ = company.split(" " , 1)
    company_dict = {"RWE": "RWE AG", "Vattenfall": "Vattenfall GmbH", "Uniper": "Uniper SE", "EnBW": "EnBW AG", "Steag": "Steag GmbH"}
    try:
        cmp = company_dict[company_prefix]
    except KeyError:
        return company
    return cmp


# In[562]:


for index, row in pl3.iterrows():
    #if row['Status'] == "Endgültig Stillgelegt 2016 (mit StA)":
    # print(row)
    status, stilllegung = generate_decom_tuple(row['Status'])
    cmp = fix_company(row['Unternehmen'])
    row['Unternehmen'] = cmp
    row['Status'] = status
    row['Stilllegung'] = stilllegung
    newdf = newdf.append(row)
    


# In[563]:


newdf['Stilllegung'] = newdf['Stilllegung'].astype(int)


# In[564]:


pl3 = newdf


# In[565]:


atest = newdf.groupby(["Unternehmen"]).count()
atest.sort_values("BlockID", inplace=True, ascending=False)


# In[566]:


# pl3


# In[567]:


#atest


# In[568]:


# pl3.rename(columns={ pl3.columns[10]: "Energieträger"}, inplace=True)


# In[569]:


pl4 = bm.merge(pl3, how="outer", on="BlockID")


# In[570]:


pl5 = pl4[pd.notnull(pl4['BlockID'])]
#pl5 = pl4
pl6 = pl5[pd.notnull(pl5['Nettoleistung'])]


# In[571]:


# pl6


# In[572]:


blocks = pl6.copy()
stammdaten = pl6.copy()


# In[573]:


blocks.sort_values("Nettoleistung", inplace=True, ascending=False)
# blocks


# In[574]:


plants = blocks.loc[:]
plants = plants.dropna(subset=["KraftwerkID"])


# In[575]:


plants_d = plants.loc[plants.duplicated("KraftwerkID", keep=False)]
# plants_d


# In[576]:


plants_c = plants_d.groupby(["KraftwerkID"]).sum()
plants_count = plants_d.groupby(["KraftwerkID"]).count()


# In[577]:


plants_f = plants_c.reset_index()


# In[578]:


plants_count = plants_count.loc[:, ["BlockID"]]


# In[579]:


plants_count = plants_count.reset_index()
# plants_count 


# In[580]:


plants_f = plants_f.merge(plants_count, on="KraftwerkID", how="inner")
# plants_f


# In[581]:


plants_a = plants.drop_duplicates(subset="KraftwerkID")


# In[582]:


plants_b = plants_d.loc[:]


# In[583]:


plants_f = plants_f.rename(columns={ "Nettoleistung": "Gesamtleistung", "BlockID": "Blockzahl"})


# In[584]:


plants_f = plants_f.merge(plants_a, on="KraftwerkID", how="left")
# plants_f


# In[585]:


#cols = [4,5,6,8]
#blocks.drop(blocks.columns[cols],axis=1, inplace=True)
#test_blocks = blocks.drop(blocks.columns[cols],axis=1)


# In[586]:


blocks.drop(['Ort', 'PLZ', 'Straße und Hausnummer (Standort Kraftwerk)', 'Kraftwerksname'], axis=1, inplace=True)


# In[587]:


# blocks


# In[588]:


# test_blocks


# In[589]:


#blocks.loc[blocks.Energieträger == 'Erdgas',]


# In[590]:


plants_2 = plants.rename(columns={plants.columns[6]: "Anschrift"})
# plants_2


# In[591]:


# plants_2


# In[592]:


cols = [2, 3, 8, 9, 10, 11, 12]
plants_3 = plants_2.drop(plants_2.columns[cols],axis=1, )
# plants_3


# In[593]:


# stammdaten


# In[594]:


# cols = [0,2,3,9,10,11,12]
drop_list = ['KraftwerkID', 'Blockname', 'Energieträger', 'Inbetriebnahme', 'KWK', 'Kraftwerksname', 'Nettoleistung', 'Status', 'Stilllegung', 'Unternehmen']
stammdaten.drop(drop_list, axis=1, inplace=True)


# In[595]:


# stammdaten


# In[596]:


stammdaten.to_csv("stammdaten.csv", index=False)


# In[597]:


blocks.to_csv("blocks_3.csv", index=False)


# In[598]:


stammdaten.to_csv("stammdaten_nh.csv", index=False, header=False)
blocks.to_csv("blocks_nh.csv", index=False, header=False)

