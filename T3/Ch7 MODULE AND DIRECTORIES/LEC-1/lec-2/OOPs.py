#!/usr/bin/env python
# coding: utf-8

# # Ch-8 OOps
# 

# 1. encapsulation - data binding 
# 2. inheritance
# 3. abstraction
# 4. polymorphism 

# In[23]:


#Class object and function calling : 
class demo():
    def m1(self,x,y):
        self.name=x
        self.age=y
    def display(self):
        print(self.name,end=' : ')
        print(self.age)
ob1=demo()
ob2=demo()

ob1.m1('x',10)
ob2.m1('y',20)
ob1.display()
ob2.display()  


# In[25]:


#Constructors : 
class demo():
    def __init__(self,x,y):
        self.name=x
        self.age=y
    def display(self):
        print(self.name)
        print(self.age)
ob1=demo('x',10)
ob2=demo('y',20)
ob1.display()


# In[30]:


class NumberSet : 
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
t=NumberSet(6,10)
print(t)


# In[46]:


class Animal : 
    totalAnimals=0 # class variable 
    def __init__(self,n1,n2):
        self.arms=n1   #instance variable 
        self.legs=n2
        Animal.totalAnimals+=1
    def limbs(self):
        return self.arms+self.legs
spider=Animal(4,5)
print(spider.arms)
print('total limbs of spider : ',spider.limbs())

monkey=Animal(2,2)
octopus=Animal(8,0)
print(monkey.limbs())
print(octopus.legs)
print('total animals: ',Animal.totalAnimals)
#class variable is refers to class not any object 


# In[57]:


class Student: 
    def __init__(self,x,y):
        self.studentName=x
        self.marks=y
    def change(self,newm):
        print('old marks: ', self.marks)
        self.marks=newm
        print('new marks: ',self.marks)
    
ob1=Student('dhulo',0)
print(ob1.studentName)
ob1.change(2)
        
        


# In[77]:


class WordPlay: 
    def __init__(self,l):
        self.l=l
    def wlength(self,length):
        nl=[]
        for i in self.l:
            if(len(i)==length):
                nl.append(i)
        return nl 
    def startsWith(self,char1):
        nl=[]
        for i in self.l:
            if(i.startswith(char1)):
                nl.append(i)
        return nl
    def endsWith(self,char2):
        nl=[]
        for i in self.l:
            if(i.endswith(char2)):
                nl.append(i)
        return nl
    def palindrome(self):
        nl=[]
        for i in self.l:
            if(i==i[::-1]):
                nl.append(i)
        return nl
    def only(self,str):
        nl=[]
        for i in self.l:
            if(word for char in i ):
                nl.append(i)
        return nl
    def avoids(self,str2):
        nl=[]
        for i in self.l:
            if(not all(word for char in i)):
                nl.append(i)
        return nl 
f=open('f1.txt','r')
l=f.read().split()
ob1=WordPlay(l)   
print(ob1.wlength(5))
print(ob1.startsWith('a'))
print(ob1.endsWith('e'))
print(ob1.palindrome())
print(ob1.only('hel'))
print(ob1.avoids('nayan'))

               
               
        


# In[58]:


print('hello'.startsWith('h'))


# In[96]:


l = ['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot']
nl = []
str = 'ap'
for i in l:
    if all(char in str for char in i):
        nl.append(i)  
print(nl)  


# In[ ]:




