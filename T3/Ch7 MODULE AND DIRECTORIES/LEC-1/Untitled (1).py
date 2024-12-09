#!/usr/bin/env python
# coding: utf-8

# # Ch7 - Module & Directories

# In[ ]:


import mode1 as m
m.x=50
m.demo('python')
print(m.x)


# In[ ]:


from mode1 import demo as d
d('hello')


# In[ ]:


import mode1 as m
a,b=int(input('enter the first number : ')),int(input('enter the second number : '))
m.sum(3,4)
m.sub(5,4)
m.power(3,4)
m.div(5,4)


# In[3]:


from mode1 import firstWord as fw; print(fw(input()))


# In[7]:


#OS module :


# 

# In[1]:


import os 
print(os.getcwd())
os.chdir(r"C:\Users\LJENG\Desktop") # does not return any thing 
print(os.getcwd())
print(os.mkdir("C4")) #FileExistError is the file already exists ! 


# In[22]:


os.mkdir(r"C:\Users\LJENG\.ipynb_checkpoints\C4")


# In[17]:


import os
print(os.listdir())
os.chdir(r"C:\Users\LJENG")
os.remove(r"C:\Users\LJENG\demo.txt")


# ## file  methods : 
# 
# * getcwd
# * chdir
# * mkdir
# * rmdir
# * listdir
# * remove

# # Ch-6 Working with files 

# In[45]:


#write method: 
fh = open("demo.txt",'w')
fh.write("python\n")
fh.write('123')
fh.writelines(['java\n','programming','language'])
fh.close()


# In[47]:


#append method : 
fh = open("demo.txt",'a')
fh.write("python\n")
fh.write('123')
fh.writelines(['java\n','programming','language']) #only string as an input under the list 
fh.close()


# In[ ]:





# In[60]:


fh=open('demo.txt','r')
print(fh.readline())
# readline -> will read first line 
# readlines -> will return whole file in form of list 


# In[79]:


#reading from one file and pasting it to other file : 
fh=open('demo.txt','r')
fw=open('demo2.txt','w')
fw.writelines(fh.readlines())
fh.close()
fw.close()


# In[78]:


fh=open('demo.txt','r')
data=fh.readlines()
newdata=fh.readline()
print(data)
fh.close()


# In[87]:


fh=open('demo.txt','r')
print(fh.tell()) # not in syllabus !!!!!
print(fh.readlines())
print(fh.tell())
fh.close()


# In[98]:


n=int(input('enter the numbero f person s : '))
fw=open('demo.txt','w')
for i in range(0,n):
    name=input('enter the name : ')
    phn=input('enter the phone number : ')
    fw.write(name)
    fw.write('\n')
    fw.write(phn)
    fw.write('\n')
fw.close()


# In[145]:


fr=open('demo.txt','r')
sum=0
fr.seek(0)
while True:
    n=fr.readline()
    for i in n :
        if(i.isdigit()):
            sum+=int(i) 
    if(len(n)==0):
        break
print(sum)


# In[132]:


fr=open('demo.txt','r')
print(fr.readline())
print(fr.readline())
print(fr.readline())
print(fr.readline())
print(fr.readline())
print(fr.readline())
print(fr.readline())
print(fr.readline())
print(fr.readline()=='')


# In[ ]:


# seek method : 
fh.seek() -> resets the pointer 


# In[143]:


fr=open('demo.txt','r')
sum=0
n=fr.readline()
fr.seek(0)
while True:
    n=fr.readline()
    print(n)


# In[ ]:




