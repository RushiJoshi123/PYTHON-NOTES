#!/usr/bin/env python
# coding: utf-8

# In[23]:


#683
import numpy as np
arr = np.array([[1,2],[3,4],[5,6]])
x=np.array_split(arr,1,axis=2)
print(x)
for i in x : 
    print(i)
a1 = np.array(range(1,25)).reshape(3,2,4)
print(a1)


# In[41]:


l = np.array(range(1,25)).reshape(3,2,4)
print(x)
print('next: ')
x1 = np.array_split(l,2,axis=2)
x2 = np.array_split(l,3,axis=2)
x3 = np.array_split(l,4,axis=1)
print('split 2')
print(x1)
print('split 3')
print(x2)
print('split 4')
print(x3)


# In[35]:


# dimension
# ndim
# shape
# indexing
# slicing
# reshape
# concatenate 
# array_split
# sort 
# where
# opeartions


# In[43]:


l = np.array(range(1,161)).reshape(4,3,5)
s = l.array_split(l,3,axis=1)


# In[50]:


import numpy as np 
arr = np.array([[[9,1],[5,3]],[[7,20],[4,2]]])
x=np.sort(arr,axis=0)
print(x) # Acending
print(x[::-1]) #Decending 


# In[56]:


arr = np.array([[2,3,9,5],[1,4,10,8]])
print(arr)
x=np.where(arr%2==0)
print(x)


# In[63]:


# Operations : 
import numpy as np 
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[3,2,1],[7,4,5]])
print(type(a1)) 
print(a1*a2)


# In[65]:


import numpy as np
a=np.array([[5],[7],[8]])
b=np.array([[5,7,8]])
print(b+a)


# In[67]:


import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[6,5,3],[4,2,1]]])
x=arr[0:2,::2,::2]
print(x)
print(x.shape)


# In[ ]:




