#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().system('pip install opencv-python')


# In[8]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


# In[24]:


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



# In[10]:


img=cv2.imread(r"C:\Users\lenovo\Downloads\img2.png")
plt.imshow(img)


# In[11]:


rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb)


# In[12]:


gray=cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)
plt.imshow(gray)


# In[67]:


faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9, minSize=(30, 30))
  


# In[68]:


faces


# In[69]:


img=cv2.imread(r"C:\Users\lenovo\Downloads\img2.png")
for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
output=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
   


# In[70]:


plt.imshow(output)


# In[ ]:





# In[ ]:




