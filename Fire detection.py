
# coding: utf-8

# In[7]:


import cv2#for multiple faces
import numpy as np
#import serial
import time

v=cv2.VideoCapture(0)
time.sleep(2)
fdc=cv2.CascadeClassifier(r'fire_detection.xml')
while(1):
        d,i=v.read()
        #print(i.shape)
        fire=fdc.detectMultiScale(i,2.3,5)

        if(len(fire)>=1):
         for x,y,w,h in fire:
              font=cv2.FONT_HERSHEY_SIMPLEX
              cv2.putText(i,'Fire Detected',(x-w,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)
              cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),2)
            # roi_gray = gray[y:y+h, x:x+w]
        cv2.imshow('image',i)

        if(len(fire)==1):
           
           print('fire is detected')
        k=cv2.waitKey(5)
        if(k==ord('q')):
                cv2.destroyAllWindows()
                break
                


# In[3]:


help('detectMultiScale')


# In[1]:


import statistics


# In[2]:


x= [1,5,7,8,9]
p=statistics.variance(x)


# In[3]:


p

