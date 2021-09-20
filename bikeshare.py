#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


# # First we are going to answer the question due to Chicago city

# **loading of Chicago data** 
# 

# In[2]:


Chicago_data = pd.read_csv('chicago.csv')


# **exploration of componants of data**
# 

# In[3]:


Chicago_data.columns


# In[4]:


Chicago_data.info()


# In[5]:


Chicago_data.head(1)


# **converting [Start Time,End Time] from object to datetime**
# 

# In[6]:


Chicago_data['Start Time'] = pd.to_datetime(Chicago_data['Start Time'], format='%Y-%m-%d %H:%M:%S')


# In[9]:


Chicago_data['End Time'] = pd.to_datetime(Chicago_data['End Time'], format='%Y-%m-%d %H:%M:%S')


# **Checking data info**
# 

# In[12]:


Chicago_data.info()


# **spliting datetime**
# 

# In[14]:


Chicago_data["Start time o'clock"] = Chicago_data['Start Time'].dt.time


# In[19]:


Chicago_data.head(1)


# In[17]:


Chicago_data["End time o'clock"] = Chicago_data['End Time'].dt.time


# In[20]:


Chicago_data.head(1)


# **convering[Start time o'clock,End time o'clock] to datetime**

# In[21]:


Chicago_data["Start time o'clock"] = pd.to_datetime(Chicago_data["Start time o'clock"], format='%H:%M:%S')


# In[22]:


Chicago_data["End time o'clock"] = pd.to_datetime(Chicago_data["End time o'clock"], format='%H:%M:%S')


# In[24]:


Chicago_data.head(1)


# **splitting datetime to 'Hour' column**

# In[25]:


Chicago_data['Starting H'] = Chicago_data["Start time o'clock"].dt.strftime('%H')


# In[26]:


Chicago_data['Ending H'] = Chicago_data["End time o'clock"].dt.strftime('%H')


# In[31]:


Chicago_data.head(1)


# **Finding the most common Hour**

# In[32]:


Chicago_data['Starting H'].value_counts().head(1)
#The most common Hour equel 17 


# **Splitting date to 'Month'**
# **and finding the most common month**
# 

# In[33]:


Chicago_data['Start Time'].dt.month.value_counts().head(1)
#the most common  month in Start time is 6 'June'


# In[34]:


Chicago_data['End Time'].dt.month.value_counts().head(1)
#the most common  month in End time is 6 'June'


# **Splitting date to 'Day'**
# **and finding the most common Day**

# In[35]:


Chicago_data['Start Time'].dt.day.value_counts().head(1)
#the most common  day in Start time is 18 


# In[36]:


Chicago_data['End Time'].dt.day.value_counts().head(1)
#the most common  day in Start End is 18


# **most common start station??**

# In[38]:


Chicago_data['Start Station'].value_counts().head(1)
#'Streeter Dr & Grand Ave' is the most common start station


# **most common end station??**

# In[39]:


Chicago_data['End Station'].value_counts().head(1)
#'Streeter Dr & Grand Ave' is the most common End station


# **most common trip from start to end??**

# In[44]:


Chicago_data['Start Station'].value_counts().head(1)


# In[47]:


Chicago_data['End Station'].value_counts().head(1)
#'Streeter Dr & Grand Ave' is the most common trip from start to end


# **total travel time??**

# In[51]:


Chicago_data['Trip Duration'].sum()
#total travel time = 280871787 sec = 4681196.45 min = 78019.9 h


# **average travel time??**

# In[53]:


Chicago_data['Trip Duration'].mean()
#average travel time = 936.23929 sec = 15.6 min = 0.2 h


# **counting of each user type**

# In[56]:


Chicago_data['User Type'].value_counts()
#Subscriber = 238889
#Customer =  61110
#Dependent  = 1


# **counting of each gender**

# In[59]:


Chicago_data['Gender'].value_counts()
#Male = 181190
#Female = 57758


# **'earliest' most common year of birth**
# 

# In[75]:


Chicago_data.sort_values(by='Birth Year').head(1)


# In[77]:


Chicago_data['Birth Year'].value_counts().head(1)
#the most common year of birth is 1989


# In[78]:


Chicago_data['Birth Year'].min()
#earliest year of birth is = 1899


# In[80]:


Chicago_data['Birth Year'].max()
#most recent year of birth is = 2016


# # ..........................................................................

# # Second we are going to answer the question due to new_york_city

# In[2]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


# **loading of ny_data** 
# 

# In[3]:


ny_data = pd.read_csv('new_york_city.csv')


# **exploration of componants of data**
# 

# In[4]:


ny_data.columns


# In[5]:


ny_data.info()


# In[6]:


ny_data.head(1)


# **converting [Start Time,End Time] from object to datetime**
# 

# In[7]:


ny_data['Start Time'] = pd.to_datetime(ny_data['Start Time'], format='%Y-%m-%d %H:%M:%S')


# In[8]:


ny_data['End Time'] = pd.to_datetime(ny_data['End Time'], format='%Y-%m-%d %H:%M:%S')


# **Checking data info**
# 

# In[9]:


ny_data.info()


# **spliting datetime**
# 

# In[10]:


ny_data["Start time o'clock"] = ny_data['Start Time'].dt.time


# In[11]:


ny_data.head(1)


# **convering[Start time o'clock,End time o'clock] to datetime**

# In[12]:


ny_data["Start time o'clock"] = pd.to_datetime(ny_data["Start time o'clock"], format='%H:%M:%S')


# In[13]:


ny_data.head(1)


# **splitting datetime to 'Hour' column**

# In[14]:


ny_data['Starting H'] = ny_data["Start time o'clock"].dt.strftime('%H')


# In[15]:


ny_data.head(1)


# **Finding the most common Hour**

# In[16]:


ny_data['Starting H'].value_counts().head(1)
#The most common Hour equel 17 


# **Splitting date to 'Month'**
# **and finding the most common month**

# In[17]:


ny_data['Start Time'].dt.month.value_counts().head(1)
#the most common  month in Start time is 6 'June'


# **Splitting date to 'Day'**
# **and finding the most common Day**

# In[18]:


ny_data['Start Time'].dt.day.value_counts().head(1)
#the most common  day in Start time is 28 


# **most common start station??**

# In[19]:


ny_data['Start Station'].value_counts().head(1)
#'Pershing Square North' is the most common start station


# **most common end station??**

# In[20]:


ny_data['End Station'].value_counts().head(1)
#'Pershing Square North' is the most common End station


# **most common trip from start to end??**

# In[21]:


ny_data['Start Station'].value_counts().head(1)


# **total travel time??**

# In[22]:


ny_data['Trip Duration'].sum()
#total travel time = 269905248 sec = 4498420.8 min = 74973.68 h


# **average travel time??**

# In[23]:


ny_data['Trip Duration'].mean()
#average travel time = 899.68416 sec = 14.99 min = 0.25 h


# **counting of each user type**

# In[24]:


ny_data['User Type'].value_counts()
#Subscriber    269149
#Customer       30159


# **counting of each gender**

# In[30]:


ny_data['Gender'].value_counts()
#Male      204008
#Female     66783


# **'earliest' most common year of birth**
# 

# In[31]:


ny_data.sort_values(by='Birth Year').head(1)


# In[32]:


ny_data['Birth Year'].value_counts().head(1)
#the most common year of birth is 1989


# In[33]:


ny_data['Birth Year'].min()
#earliest year of birth is = 1885


# In[34]:


ny_data['Birth Year'].max()
#most recent year of birth is =2001


# # ...................................

# # Third we are going to answer the question due to new_york_city

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


# **loading of Chicago data** 
# 

# In[3]:


wash_data = pd.read_csv('washington.csv')


# **exploration of componants of data**
# 

# In[4]:


wash_data.columns


# In[5]:


wash_data.info()


# In[6]:


wash_data.head(1)


# **converting [Start Time,End Time] from object to datetime**
# 

# In[7]:


wash_data['Start Time'] = pd.to_datetime(wash_data['Start Time'], format='%Y-%m-%d %H:%M:%S')


# **Checking data info**
# 

# In[9]:


wash_data.info()


# **spliting datetime**
# 

# In[10]:


wash_data["Start time o'clock"] = wash_data['Start Time'].dt.time


# In[11]:


wash_data.head(1)


# **convering[Start time o'clock,End time o'clock] to datetime**

# In[12]:


wash_data["Start time o'clock"] = pd.to_datetime(wash_data["Start time o'clock"], format='%H:%M:%S')


# In[14]:


wash_data.head(1)


# **splitting datetime to 'Hour' column**

# In[15]:


wash_data['Starting H'] = wash_data["Start time o'clock"].dt.strftime('%H')


# In[16]:


wash_data.head(1)


# **Finding the most common Hour**

# In[18]:


wash_data['Starting H'].value_counts().head(1)
#The most common Hour equel 08 


# **Splitting date to 'Month'**
# **and finding the most common month**

# In[19]:


wash_data['Start Time'].dt.month.value_counts().head(1)
#the most common  month in Start time is 6 'June'


# **Splitting date to 'Day'**
# **and finding the most common Day**

# In[22]:


wash_data['Start Time'].dt.day.value_counts().head(1)
#the most common  day in Start time is 21


# **most common start station??**

# In[24]:


wash_data['Start Station'].value_counts().head(1)
#'Columbus Circle / Union Station' is the most common start station


# **most common end station??**

# In[26]:


wash_data['End Station'].value_counts().head(1)
#'Columbus Circle / Union Station' is the most common End station


# **most common trip from start to end??**

# In[28]:


wash_data['Start Station'].value_counts().head(1)


# In[30]:


wash_data['End Station'].value_counts().head(1)
#'Columbus Circle / Union Station' is the most common trip from start to end


# **total travel time??**

# In[31]:


wash_data['Trip Duration'].sum()
#total travel time = 371183985.484 sec = 6186399.7 min = 103106.66 h


# **average travel time??**

# In[33]:


wash_data['Trip Duration'].mean()
#average travel time = 1237.2799516133446 sec = 20.87 min = 0.34 h


# **counting of each user type**

# In[35]:


wash_data['User Type'].value_counts()
#Subscriber    220786
#Customer       79214


# # End of project !

# In[ ]:





# In[ ]:




