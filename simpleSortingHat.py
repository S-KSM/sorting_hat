
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_excel("./data/70251 113R1.xlsx",sheetname="ps-4")
df = df.reset_index()[["Select","ID","Name","Program and Plan", "Level"]]


# In[3]:

df_f = df[df["Select"]=="f"]
df_m = df[df["Select"]=="m"]


# In[4]:

class member:
    def __init__(self,name,ID,plan,level,sex):
        self.name = name
        self.ID = ID
        self.plan = plan
        self.level = level
        self.sex = sex
        
        
class groups(member):
    def __init__(self):
        self.number = 0
        self.member = []
        self.gplans = {}
        self.glevels = {}
        self.gsexs = {}
        self.maxmember = 6
        
    def num(self):
        return self.number
    
    def add_member(self,mymember):
        if self.number < self.maxmember:
            self.member.append((mymember.name,mymember.ID))
            self.number += 1
            self.ID = mymember.ID

            if mymember.plan in self.gplans:
                self.gplans[mymember.plan] += 1
            else:
                self.gplans[mymember.plan] = 1


            if mymember.level in self.glevels:
                self.glevels[mymember.level] += 1
            else:
                self.glevels[mymember.level] = 1

            if mymember.sex in self.gsexs:
                self.gsexs[mymember.sex] += 1
            else:
                self.gsexs[mymember.sex] = 1

    def get_sex(self):
        return self.gsexs
        
    def get_levels(self):
        return self.glevels
        
    def get_plans(self):
        return self.gplans
    def get_members(self):
        return [self.member[i] for i in range(self.number)]
    
        


# In[5]:

dictGroups ={}
lstMember =[]


# In[6]:

df = df.sort(["Select","Program and Plan","Level"])


# In[7]:

for row in range(df.shape[0]):
    lstMember.append(member(df.iloc[row,2],df.iloc[row,1],df.iloc[row,3],df.iloc[row,4],df.iloc[row,0]))
    
    


# In[8]:

for i in range(12):
    dictGroups[i] = groups()


# In[9]:

for i in range(len(lstMember)):
    dictGroups[i%12].add_member(lstMember[i])


# In[10]:

a = {}
for i in range(len(dictGroups)):
    a[i] = dictGroups[i].get_members()


# In[11]:

pd.DataFrame(a).to_excel("output/groups.xlsx",sheet_name="Sheet1",
                         header=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg"],index= False)


# In[ ]:




# In[ ]:




# In[ ]:



