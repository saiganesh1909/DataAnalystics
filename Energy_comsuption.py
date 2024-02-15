#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#data from local stronage throgh pandas.csv method

data = pd.read_csv('C:/Users/sai ganesh/Videos/engery_consumption_project/archive (1)/Sleep_health_and_lifestyle_dataset.csv')


# In[ ]:


data.head(3)


# In[3]:


type(data)


# In[ ]:


get_ipython().system('pip install mysql.connector')


# In[ ]:


import mysql.connector


# In[ ]:


conn  = mysql.connector.connect(host='localhost',user='root',password='',database='energy_consumption')


# In[ ]:


#it will create the dataramedirectly

data_sql = pd.read_sql_query("select * from `sleep_health_and_lifestyle_dataset`",conn)


# In[ ]:


data_sql.head(3)


# In[ ]:


#getting the data from amazon s3 using boto3 library


# In[ ]:


pip install boto3 pandas


# In[ ]:


import boto3


# In[ ]:


conn = boto3.client('s3',
    aws_access_key_id='AKIAUB5VLIZDNGPJCNOB',
    aws_secret_access_key='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',
    region_name='us-east-1'
)


# In[ ]:


bucket_name = 'engeryconsumptiondata'
object_key = 'Sleep_health_and_lifestyle_dataset.csv'

# Get the object
obj = s3.get_object(Bucket=bucket_name, Key=object_key)

# Read data into Python (as a string, for example)
data = obj['Body'].read().decode('utf-8')


# In[ ]:


for bucket in conn.buckets.all():
    print(bucket.name)


# In[ ]:


#creation of bucket
response = conn.create_bucket(
Bucket = 'bucket2_aws_engery_consumption'
)


# In[ ]:


data.head(2)


# In[ ]:





# In[4]:


'usually there is theory in the science each sleep time occuress according to 0.42 cal per hour and weight and how many hours their slept'


# In[5]:


#before we have to caluclate any null values

data.isnull().sum()# so their is null values


# In[7]:


#getting count of male and fefmale data from the data

male = data.loc[data['Gender'] == 'Male'].count()['Gender']
female = data.loc[data['Gender']=='Female'].count()['Gender']


# In[8]:


#counting average sleeptime for each category

male_age = data.loc[data['Gender'] == 'Male']['Age']
female_age = data.loc[data['Gender']=='Female']['Age']


# In[9]:


male_age.mean()


# In[11]:


female_age.mean()


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


plt.hist(male_age,bins=20)
plt.hist(female_age,bins=20)


# In[14]:


male_sleep = data.loc[data['Gender'] == 'Male', 'Sleep Duration']


# In[15]:


"now we have to plot the between sleepduration and their age"

plt.scatter(male_sleep,male_age)
plt.xlabel('sleep')
plt.ylabel('age')


# In[17]:


#we dont have height of the person to caluclate a caleries burned for each person per hour so we can intialize the heights from 150 to 180 randomly
#becasue we have ages from 30 to 60 mostly


# In[16]:


import numpy as np


# In[18]:


type(data)


# In[19]:


countof_numberofrows = data['Gender'].count().sum()


# In[20]:


data['height']= np.random.randint(150, 176, size = countof_numberofrows)  


# In[21]:


type(data)


# In[22]:


data.head(6)

#so we sucessfully assign the data from the 


# In[23]:


#we have to intialize the values ramdomly of data

#i will assume like 55 to 80 kgs 

data['weights']  = np.random.randint(55,80,countof_numberofrows)


# In[24]:


data.head(5)  #we are also sucessfully done our data into weights


# # so we are using theory called bmi
# The amount of energy (or calories) burned while sleeping varies by age, weight, and sex, primarily because basal metabolic rate (BMR) differs among individuals. BMR is the rate at which your body uses energy while at rest to maintain vital functions such as breathing, circulating blood, and cell production. Generally, your body burns fewer calories when you're sleeping than when you're awake and active, but it does continue to burn calories at a rate influenced by your BMR.
# 
# Calculating the exact energy expenditure during sleep can be complex because it depends on the individual's specific characteristics. However, a rough estimate can be made using the formula for BMR and adjusting for the sleeping state.
# 
# For men: BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (y) + 5
# 
# For women: BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (y) - 161
# 
# so according to this we have to caluclate the data

# In[ ]:





# In[ ]:





# In[34]:


# we can archive this iterration of rows usinf iterrows() method


data['cal'] = 0

for i, row in data.iterrows():
    var1 = row['Gender']
    if var1 == 'Male':
        BMR = 10 * row['weights'] + 6.25 * row['height'] - 5 * row['Age'] + 5
    elif var1 == 'Female':
        BMR = 10 * row['weights'] + 6.25 * row['height'] - 5 * row['Age'] - 161
    else:
        print('Gender not specified')
        continue  # Skip this iteration if Gender is neither 'Male' nor 'Female'
    
    var = (BMR / 24)
    data.at[i, 'cal'] = var


# In[38]:


data['cal'] =data['cal']*data['Sleep Duration']


# In[39]:


#converting into 

data['cal'] = data['cal'].astype(int)


# In[41]:


data.head(4)#we sucessfully done the data


# In[42]:


#our next task is to calucalte the how many calaries we will get after taking certain amount of breakfast


# In[47]:


Country= ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada']


# In[48]:


TOP_1Breakfast= [
        'Pancakes with syrup',  # United States
        'Congee with pickled vegetables',  # China
        'Miso soup with rice',  # Japan
        'Bread with sausage and cheese',  # Germany
        'Masala dosa with sambar',  # India
        'Full English breakfast',  # United Kingdom
        'Croissant with coffee',  # France
        'Pão de queijo with coffee',  # Brazil
        'Cappuccino with cornetto',  # Italy
        'Maple syrup on pancakes',  # Canada
    ]


# In[52]:


type(TOP_1Breakfast)


# In[97]:


data['Country'] = np.random.choice(Country, size=len(data), replace=True)


# In[98]:


data.head(2)


# In[66]:


person = {'UnitedStates':'Pancakes with syrup', 
              'China':'Congee with pickled vegetables',
              'Japan':'Miso soup with rice', 
              'Germany':'Bread with sausage and cheese',
              'India':'Masala dosa with sambar',
              'United Kingdom':'Full English breakfast',
              'France':'Croissant with coffee',
              'Brazil':'Pão de queijo with coffee',
              'Italy':'Cappuccino with cornetto',
              'Canada':'Maple syrup on pancakes'}


# In[128]:





# In[113]:


df =data.iloc[:,0:8]


# Pancakes with syrup (United States): About 520 calories for three medium pancakes with 2 tablespoons of maple syrup.
# Congee with pickled vegetables (China): Approximately 200-250 calories for a medium bowl of congee and a small serving of pickled vegetables.
# Miso soup with rice (Japan): Around 200 calories for one medium bowl of miso soup and a half-cup of cooked rice.
# Bread with sausage and cheese (Germany): Approximately 500-600 calories for a medium serving, depending on the amount of cheese and sausage.
# Masala dosa with sambar (India): About 400 calories for one medium masala dosa and a serving of sambar.
# Full English breakfast (United Kingdom): Around 800-1000 calories for a medium serving including eggs, bacon, sausages, beans, toast, and tomatoes.
# Croissant with coffee (France): Approximately 300 calories for a medium butter croissant, not including the coffee. If you add sugar or cream to the coffee, remember to add those calories as well.
# Pão de queijo with coffee (Brazil): Around 300 calories for three medium-sized pão de queijo and a black coffee without sugar.
# Cappuccino with cornetto (Italy): About 250-300 calories for a medium cappuccino and a medium cornetto (Italian croissant).
# Maple syrup on pancakes (Canada): This is similar to the first item, but if considering just the maple syrup, about 52 calories per tablespoon. For three pancakes, it's about 520 calories plus the syrup.

# In[ ]:





# In[115]:


df['breakfast'] = df['Country'].map(person)


# In[116]:


df


# In[118]:


breakfat_cal= {'UnitedStates':520,
              'China':220,
              'Japan':200,
              'Germany':550,
              'India':400,
              'United Kingdom':700,
              'France':300,
              'Brazil':300,
              'Italy':250,
              'Canada':520}


# In[119]:


df['breakfast_cal'] = df['Country'].map(breakfat_cal)


# In[120]:


df.head(4)


# In[123]:


df.rename(columns={'cal':'sleeping_calburn'}, inplace=True)


# In[124]:


df.head(2)


# In[125]:


df['remain_cal'] = df['breakfast_cal']-df['sleeping_calburn']


# In[126]:


df.head(4)


# In[127]:


#converting into data
df.to_csv('engery_consum.csv', index=False)


# In[129]:


get_ipython().system('pip install skimpy')
from skimpy import skim


# In[ ]:




