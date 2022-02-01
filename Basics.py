#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Autor: Torres Miranda Christian


# In[28]:


#Score for the education in U.S.A.

#Libraries section
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

#Define the Score and Frequency in a numpy array
Score=np.array(['A','B','C','D'])
Frequency=np.array([35,260,93,12])

#Calculate the variable 'n' as Total
Total=sum(Frequency)

#Relative Frequence
RelFreq=Frequency/Total

#Percentage
Perc=RelFreq * 100

#Angle of each pie chart piece
Angle= RelFreq * 360

#We join the data in a pandas Data Frame
data= {
    "Score": Score,
    "Frequency": Frequency,
    "Relative Frequency":RelFreq,
    "Percentage": Perc,
    "Angle":Angle
}
df = pd.DataFrame(data)

#Set index as 'Score' column
df=df.set_index('Score')

#Print the table
print(df)

#Define the axes
x_axis=Score
y_axis=Frequency

#Put some description
plt.ylabel('Frequency')
plt.xlabel('Score')
plt.title('Score for the education in a school')

#Plot the bar chart
plt.bar(x_axis, y_axis)
plt.show()

#Define the colors or the pie chart
normdata = colors.Normalize(min(Perc), max(Perc))
colormap = cm.get_cmap("Blues")
colores =colormap(normdata(Perc))

#Plot the pie chart
plt.pie(Perc, labels=Score, autopct="%0.1f %%", colors=colores)
plt.axis("equal")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




