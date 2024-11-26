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


# In[ ]:


#Valid parenthesis : 
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
#print(t3+t4)

#taking tuple as in input: 
# n=eval(input())
# print(type(n[2]))


#Comparison:
#first element compares to first element , compares to next if both are equal 
#type of elements in both the tuples should be equal(or it should be at last )
#its an interpreted language 
t1=(10,2,30)
t2=(10,20,'a')
print(t1>t2)

#min and max of tuple : 
t1=('apple','b','Cat') 
print(min(t1))
#internal elements are compared (first chraracter is compared )capital values are always small (acaii values)
print(max(t1))


#Sorted method: 
t1=(9,5,1,2,4,7)
print(sorted(t1))
#t1.sort methods would not work in tuple
t2=sorted(t1,reverse=True) # returns list 
t3=reversed(t1) #returns tuple address 
print(t2)
print(tuple(t3))

tt1=(343,'abc',)
print(tuple(reversed(tt1)))



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


# In[ ]:


s,n=input("Enter the string : "),int(input('Enter the index:'))
if n>len(s):print(s[::-1])
else:print(s[n::]+s[0:n])  


# In[ ]:


#331
s1,s2,sum1,sum2=input('Enter the s1 string : '),input('enter the s2 string : '),0,0
for i in s1:sum1+=ord(i)
for i in s2:sum2+=ord(i)
if(sum1==sum2 and len(s1)==len(s2)):print('balanced')
else :print('not balanced')


# In[ ]:


#330
s,fs,n=input('Enter the string : '),'',int(input('enter the shift number : '))
for i in s:
    if(ord(i)>=90 and ord(i)<97):
        n2=ord(i)-23   
        fs+=chr(n2)
    elif(ord(i)>=65 and ord(i)<=90):fs+=chr(ord(i)+n)
    elif(ord(i)>=97 and ord(i)<=122):fs+=chr(ord(i)+n)
    else:fs+=i
print(fs)


# # Mutable data structures
# 

# In[ ]:


#List : 

l1=['a','b',[1,2,3,4,5],2,3,4,5]
#reverse
rev=l1[::-1]
print(rev)
#multiplication : 
l2=l1*2
print(l2)
l2=['x','y']
print(l1<l2) #elements are compared
 
#Methods:
#append and extend
l1.append(53) 
print(l1)
l1[3]=4 #elements can be changes by assigning new value 
l1.extend([2,3,4,5])
print(l1)

#insert : to insert at particular index : 
l1.insert(1,'h')
print(l1)
print(l1[3][3])

#remove: 
del l1[2:4]
print(l1)
##deletes data inside the list 
print(type(l1[1]))
# # deletes whole list 
print(l1)

l3=[2,3,3,4,54,5,5,50] #returns the last element of the list when not parametrised ! 
print(l3.pop())
#index based remove : pop 
# value based remove : remove
l3.remove(54)
print(l3)


# In[ ]:


#Sort method : 
l=[7,5,4,3,2,2,5,43,3]
t=sorted(l)
print(t)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

l2=l.copy()
l3=l[:]
l2[1]=90
l3[2]=200
print(l,l2,l3)


# In[ ]:


n,l=int(input('enter the number of elements : ')),[]
for i in range(0,n):
    l.extend[input()]
print(l)


# In[ ]:


l1=[]
l2=[]
x=int(input())
for i in range(x):
    l1.append(input())
    l2=[len(i) for i in l1]
print(l1,l2)


# In[ ]:


l1=[]
l2=[]
x=int(input())
for i in range(x):
    l1.append(input())
    l2=[i for i in l1 if 'o' in i]
print(l1,l2)


# In[ ]:


l1=list(eval(input('enter the list of number : ')))
t=int(input('enter the number to search '))
for i in range(len(l1)):
    if t==l1[i]:
        print('index : ', i)
        break
else : 
    print('not in the list')


# In[ ]:


l1=eval(input('enter the list of number : '))
m=min([len(i) for i in l1])
s=""
for i in range(m):
    ch=l1[0][i]
    f=True
    for j in l1 :
        if ch!=j[i]:
            f=False
            break
    if f:
        s+=ch
    else: 
        break
if(len(s)>0):
    print(s)
else:
    print(-1)
    
        


# In[ ]:


l1=list(eval(input('enter the list of number : ')))
m=([len(i) for i in l1])
print(m)


# In[ ]:


l=eval(input())
def stCount(l):
    c=0
    for i in l:
        if len(i)>=3 and i[0]==i[-1]:
            c+=1
        return c
print(c)
        


# In[ ]:


print(type('enter'))


# In[ ]:


l['3434','hello']
a=type(l[1])
print(a)


# In[ ]:


# from the list return the majority element the majority element is the element that appers more than 
# half of the time in the array 
l1=eval(input())
l=len(l1)//2
print(l)
l2=[]

for i in l1:
    if(l1.count(i)>=l):
        l2[i]=i
print(l2)
        



# In[ ]:


l1,sum,i = eval(input()),0,0
while i < len(l1):
    if l1[i] == 13:i += 2  
    else:
        sum += l1[i]     
        i += 1
print(sum)


# In[ ]:


l1,sum1 = eval(input()),0
for i in range(len(l1)):
    if(l1[i]==13):i+=2
    else:
        sum1+=l1[i]
        i-=1
print(sum1)


# In[ ]:


l1,l2,n=list(eval(input())),[],int(input())
print(l1[n:]+l1[:n])


# In[ ]:


#Set : 
s1={1,2,3,4,5,65,2,2,2,2,6}
s2={8,7,99,5,5}
#set methods: 
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2^{2,3})


# In[ ]:


s3=frozenset(s1)
print(s3)


# In[ ]:


# given an array of integers return the index i and j such that list of i + list of j == target and i!=j 
a,t=[1,2,3,4,54,5],int(input())
for i in a: 
    for j in a:
        if(i+j==t and i!=j):print(a.index(i),a.index(j))


# In[ ]:


l1,l2,i=[0,1,2,3,4,5,6],[],0
j=len(l1)-1
while (i<=len(l1)//2 or j>len(l1)//2)  :
    l2.append(l1[i])
    i+=1
    if(len(l2)>=len(l1)):
        break
    l2.append(l1[j])
    j-=1
    if(len(l2)>=len(l1)):
        break
print(l2)
    


# In[ ]:


# lambda
x=lambda n: n*n
print(x(5))


# In[ ]:


n=[1,2,3,4,5]
n2=[]
for i in n:
    n2.append(i*i)
print(n2)    


# In[ ]:


n=[1,2,3,4,5]
n2=[]
for i in n:
    n2.append(i*i)
print(n2)    


# In[ ]:


# map
a=map(lambda n:n*n,[1,2,3,4,5])
print(list(a))


# In[ ]:


def square(x):
    return x*x
a=map(square,[1,2,3,4,5])
print(list(a))


# In[ ]:


n=input('enter the digit')
a=list(map(int,n))
print(a)


# In[ ]:


# filter
# a=int(input())
x=lambda n:True if n%2==0 else False
ans=list(filter(x,[5,6,7,8,9]))
print(ans)


# In[ ]:


a=['hello','o']
x=lambda n:True if 'o' in n else False
ans=list(filter(x,a))
print(ans)


# In[ ]:


from functools import *
# n1=1
# n2=2
x=lambda n1,n2:n1+n2
print(reduce(x,[1,2,3,4,5,6]))


# In[ ]:


print(list(filter(lambda n: n % 2 == 0, map(int, input().split()))))


# In[ ]:


print(list(filter(lambda n:True if n%2==0 else False,list(map(int,input())))))


# In[ ]:


print(reduce(lambda a,b:a+b,list(filter(lambda n:True if n%2==0 else False,list(map(int,input()))))))


# In[ ]:


l,es,os=eval(input('enter the list')),0,0
es=reduce(lambda n,m:m+n,l[::2])
os=reduce(lambda n,m:m+n,l[1::2])
if(es==os):print('balanced')
elif(es>os):l.remove(es-os)
elif(os>es):l.remove(os-es)
print(l)    


# In[ ]:


# es=reduce(lambda n,m:n 
# os=reduce(lambda n,m:n+m,list(filter(lambda n: True if n%2==1 else False,l)))


# # Dictionary : 
# 

# In[ ]:


# Dictionary : 

# unorddered 
# changable 
d={'a':1,'b':2,'x':10}
# if both keys are same the last assign value will count : 
# no duplication is allowed : 
d['y'] = 100
print(d['y'])
# print(d*2) not possible 
# print(d+d) not possible 
d.clear() #elemets remove thay dictionary rahe 
print(d)

d1=d.copy() #stores at different address 
del d1
print(d is d)
print(d1)


# In[ ]:


#Methods : 
# clear
# copy
# keys
# values
# items
# get 
# pop
# popitem 
d={'a':1,'b':2,'x':10}
print(d.copy())
print(d.keys())
print(d.values())
print(d.items())
print(d.get(100,'python'))
print(d.setdefault(30,'pop'))
print(d)
print(d.pop('a'))
print(d.pop('a',3))
d.update({'b':25,'c':28})
print(d)
d1=dict.fromkeys(['k1','k2','k3'],[1,2,3])
print(d1)


# In[ ]:


#457
l,d = list(eval(input())),{}
for i in l : d[i] = [i]*l.count(i)
print(sorted(d.items(),reverse=True,key=lambda x:len(x[1])))


# In[ ]:


#469 (c):
s,d = input(),{}
l=s.split()
for i in l : 
    f=i[0].lower()
    if f in  d:
        d[f]+=[i]
    else:
        d[f]=[i]
print(d)
        


# In[ ]:


from collections import Counter; print(dict(Counter(input().lower().split())))


# In[ ]:


l=[10,20,30,40]
x=enumerate(l,50) #index starting with 50
print(dict(x))


# In[ ]:


s,k,ns,=input('enter the message : '),int(input('enter the key : ')),''
for i in range(k):   ns+=s[i::k]
print(ns)
print('enter the encrypted message : ')
e=input()
print('the message decrypted message is : ',s)


# In[ ]:


#decreption message 
st=input()
k=int(input('key: '))
msg=''
l=len(st)
part=l//k
extra=l%k
p1=st[0:(part+1)*extra]
p2=st[(part+1)*extra:]
for i in range(part+1):
    if i<part:
        msg+=p1[i::part+1]+p2[i::part]
    else:
        msg+=p1[i::part+1]
print(msg)


# In[4]:


from functools import *
l=list(eval(input('enter the numbers : ')))
s={}
for a in range(len(l)):
    for b in range(len(l)):
        for c in range(len(l)):
            # s.add([l[a],l`[b],l[c]])
            print(s)
   


# In[1]:


s="hello"
s-=3
print(s)


# In[10]:


str1="save paper,save trees"
str1.find("save")


# In[9]:


print('new' 'line')


# In[25]:


s='Vishv,Aryan,Devarsh'
#slicing index would not give error , 

s1=s[1:50]
print(len(s1))
print(s[-9:-14:-1]) 


# In[28]:


print('abcd1@234'.isalnum())


# In[30]:


print('hello''world')


# In[33]:


aTuple = ("Orange",)
print (type(aTuple))


# In[35]:


def practice(tup):
 a, b, c = tup
 return b
aTuple = "Orange", 30, "White"
print(practice(aTuple))


# In[36]

my_tuple = (1, 2, 3, 4)
my_tuple.append( (1,2,3) )
# print len(my_tuple)

