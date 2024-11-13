#!/usr/bin/env python
# coding: utf-8

# # Chapter 4: Immutable Data Structures : 
# 

# In[ ]:


s='hello'
s="ljk university of ahmedabad" 
#Strings are case sensitive 
# for i in s:
#     print(i ,end=" ")

print(s[6]) #starts from front
#Strings are indexable (+ve(starts from 0) as well as -ve(starts from -1))
print(s[-2]) #starts from rear

#Slicing
print(s[4:14:2]) #does not include the ending point
print(s[13:3:-1])

print(s[-1:-10:1])


# #Q. check wheter the string is palindrome or not:
# s=input('Enter the string')
# rev = string[::-1]
# if(string==rev):
#     print('The string is palindrome')
# else : 
#     print('The string is not palidrome')
print(len(s))

si = s[-11:-len(s)+1:-3]
si=s[16:3:-3]
print(si)

#Repeater
st=s*3
# print(st)







# In[ ]:


#311 
st=  'hello world'
n=2
st1 = st[0:n]
st2= st[n+1::]
stf=st1+st2
print(stf)
r=input('Enter the string to be replaced : ')
stf2 = st1+r+st2
print(stf2)


# In[ ]:


#312
s='helloworld6'
f = s[0]
mn= len(s)//2
m=s[mn:mn+1:]
l = s[len(s)-1]
string=  f+m+l
print(string)
s1=s[0].upper()+s[1::]
s1=s1.upper()
print(s1.lower())
print(s.islower())
print(s.capitalize())
print(s1)


# In[ ]:


#309
s='hello world'
count=0
for i in s: 
    if(i.isupper()):
        count+=1
print(count)
print(s.isalpha())
print(s.isdigit())
print(s.isnumeric())
print(s.isupper())
print(s.isalnum())  #false in special characters 


# In[ ]:


sum,average,count,s=0,0,0,input("Enter the string: ")
for i in s:
    if(i.isdigit()):
        sum+=int(i)
        count+=1
average=sum/count
print(sum)
print(average)

c1,c2,c3,s=0,0,0,input('Enter the string: ')
for i in s :   
    if (i=='{'):c1+=1
    if (i=='['):c2+=1
    if (i=='('):c3+=1      
    if (i=='}'):c1-=1
    if (i==']'):c2-=1
    if (i==')'):c3-=1
print('True' if(c1==c2==c3==0) else 'False')


# In[ ]:


s=input()
l=len(s)
j=-1
if l%2 !=0:
    print('invalid')
else:
    for i in range(l//2):
        if(s[i]=='(' and s[j]==')' or s[i]=='[' and s[j]==']'or s[i]=='{' and s[j]=='}'):
            pass
        else :
            print('Invalid')
            break
        j-=1
    else: 
        print('valid')


# In[ ]:


s=input()
us=s[:len(s)//2:]
uus=us.upper()
rs=s[(len(s)//2)+1::]
fs=uus+rs
print(fs)


# In[ ]:


#Tuple : 
# ordered and unchangable 
t1=(20,4,30,2,5)

#Indexing:
a=t1[-4]
#we cant change the tuple(can't assign them values)
print(a)

#Slicing: 
t2=t1[5:1:-1]
print(t2)

#Concatination : 
t2=(20,4,99)
t3=t1+t2
t4=('hello')
print(type(t4))
print(t3+t4)


# In[ ]:


#324
t=eval(input())
sumEven =0
sumOdd=0
for i in t : 
    if(i%2==0):
        sumEven+=i
    else :
        sumOdd+=i
print(sumEven,sumOdd)


# In[4]:


#taking tuple as in input: 
n=eval(input())
print(type(n[2]))


# In[13]:


#Comparison:
#first element compares to first element , compares to next if both are equal 
#type of elements in both the tuples should be equal(or it should be at last )
#its an interpreted language 
t1=(10,2,30)
t2=(10,20,'a')
print(t1>t2)


# In[ ]:




