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


# In[ ]:


from mode1 import firstWord as fw; print(fw(input()))


# In[ ]:


#OS module :


# 

# In[ ]:


import os 
print(os.getcwd())
os.chdir(r"C:\Users\LJENG\Desktop") # does not return any thing 
print(os.getcwd())
print(os.mkdir("C4")) #FileExistError is the file already exists ! 


# In[ ]:


os.mkdir(r"C:\Users\LJENG\.ipynb_checkpoints\C4")


# In[ ]:


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

# In[ ]:


#write method: 
fh = open("demo.txt",'w')
fh.write("python\n")
fh.write('123')
fh.writelines(['java\n','programming','language'])
fh.close()


# In[ ]:


#append method : 
fh = open("demo.txt",'a')
fh.write("python\n")
fh.write('123')
fh.writelines(['java\n','programming','language']) #only string as an input under the list 
fh.close()


# In[ ]:





# In[ ]:


fh=open('demo.txt','r')
print(fh.readline())
# readline -> will read first line 
# readlines -> will return whole file in form of list 


# In[ ]:


#reading from one file and pasting it to other file : 
fh=open('demo.txt','r')
fw=open('demo2.txt','w')
fw.writelines(fh.readlines())
fh.close()
fw.close()


# In[ ]:


fh=open('demo.txt','r')
data=fh.readlines()
newdata=fh.readline()
print(data)
fh.close()


# In[ ]:


fh=open('demo.txt','r')
print(fh.tell()) # not in syllabus !!!!!
print(fh.readlines())
print(fh.tell())
fh.close()


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # seek method : 
# * fh.seek() -> resets the pointer 
# * open 
# * cloae
# * write
# * writelines
# * read
# * readline(hint)
# * readlines
# * tell
# * seek(offset

# In[ ]:


fr=open('demo.txt','r')
sum=0
l=[]
fr.seek(0)
while True:
    n=fr.readline()
    if(n.isdigit):
        for i in n:
            if(i.isdigit()):
                sum=int(i)
    if(sum!=0):
        l.append(sum)
    if(n==''):
        break
print(l)


# In[ ]:


f=open('demo.txt')
# data=f.read(5)
print(f.readlines(10))
f.close()


# In[ ]:


#r+ mode : can read and write too ! the pointer is at starting 
#overrides character by character 
f=open('demo.txt','r+')
f.read()
f.write('html')
f.seek(0)
print(f.read())
f.close()


# In[ ]:


# 192.168.101.51
# W+ and A+
f=open('demo.txt','a+')
f.write('hello')
f.seek(0)
print(f.read())
f.close()


# In[ ]:


ans={}
f=open('demo.txt')
data=f.read().split(' ')
ds=set(data)
for i in ds:
    ans[i]=data.count(i)
print(d)
    


# In[ ]:


#507 If they are different, give the line and column numbers in the files where the 
# first difference occurs.
f1,f2=open('demo1.txt'),open('demo2.txt')
d1,d2=f1.readlines(),f2.readlines()
for i in range(len(d1)):
    for j in range(len(d1[i])-1):
        if(d1[i][j]!= d2[i][j]):
            print('row number: ', (i+1))
            print('col number : ' ,(j+1))
            break
      
f1.close()
f2.close()
    
        


# In[ ]:


f,l=open('demo1.txt','w+'),[]
while True: 
    s=input('Enter Something (for quit enter END):')
    f.write(s+'\n')
    if(s[0].isupper()):l.append(s)
    if(s=='end'):print(str(l))
        break


# In[ ]:


# 505
f1=open('demo1.txt','w+')
f2=open('demo2.txt','w+')
n=f1.readline()
while True:
    if(n == ''):
        break
    if(not n[0]=='#'):
        f2.write(n)
    n=f1.readline()
        


# In[ ]:


f1,f2=open('demo1.txt','r+'),open('demo3.txt','w+')
l=f1.readlines()
for i in l : 
    a=i.split('#',1)[0]
    f2.write(a)


# 1. open
# 2. close
# 3. read
# 4. realine
# 5. readlines
# 6. write 
# 7. wrtielines
# 8. trell
# 9. seek 
# 10. readable
# 11. writable
# 12. closed 

# In[ ]:


f=open('demo1.txt','r+')
wc,cc,sc=0,0,0
line=f.readlines()
print(line)
for i in line : 
    wc+= len(i.split())
    sc+= i.count(' ')
    cc+= len(i)
print(wc,cc,sc)
f1.close()


# In[ ]:


f=open('demo3.txt','r+')
l=f.readlines()
for i in l : 
    if(i[0]=='i' or i[0]=='I'):
        print(i[::-1])
    else:
        print(i)


# In[ ]:


f=open('demo1.txt','r+')
l=f.read().split()
for i in l : 
    if(len(i)==4 and i[0]==i[len(i)-1]):
        print(i)
    


# In[ ]:


f1,f2,f3,c=open('demo1.txt','r'),open('demo2.txt','w+'),open('demo3.txt','w+'),0

l=f1.read().split()
for i in l:
    f2.write(i[::-1])
    
f2.seek(0)
l2=f2.read().split()
for i in l2: 
    f3.write(i.upper())
    
f3.seek(0)
l3=f3.read().split()
vowels='AEIOUaeiou'
for i in l3: 
    for j in i :
        if j in vowels : 
            c+=1
print(c)
            
    


# In[ ]:


#500 question 
f,st,s,c=open('demo1.txt','r+'),input('enter the string : '),set(),0
l=f.read().split()
for i in l : 
    for j in st : 
        if j in i : 
            if(c == len(st)-1):
                if(st.count(j) == i.count(j)):
                    s.add(i)
            c+=1
    c=0
for i in s :
    print(i) 


# In[ ]:


#500
f1=open('demo1.txt')
data=f1.read().split()
st=input()
for word in data :
    f=True
    for ch in st : 
        if st.count(ch) > word.count(ch):
            f=False
            break
        if f: 
            print(word)
    f1.close()
            


# In[ ]:


try: 
    f1=open('pb499.txt','r')
    while True: 
        s=input('continue/stop : ')
        if(s=='continue'):
             for i in range(0,25):
                n=f1.readline()
                print(n)
        else:
            print('Thank You ')
            break
        if(n==''):
            break
except Exception as e  :
    print('end of the file ')
    
    


# In[ ]:


try: 
    print('enter'
except ValueError:
    print('error handled')


# In[ ]:


print(int('ab'))


# In[ ]:


try: 
    if True: 
    a+=b
except IndentationError: 
    print('hello ')


# In[ ]:


l=[1,2,3]
l[500]


# 1. pritn(' --> syntax error 
# 2. b=5 +'ab' --> type error
# 3. print(int('ab') --> value error 
# 4. if True navi line  : 
#    a=b+c   --> indentation error
# 5. l[500] : --> index error 
# 6. l[1,2,3] 
#     l[500] : --> attribute error 
# 7. d={'a':123}
#     print(d[1])  -->  key error 
# 8. import mypython -->  module not found error
# 9. b=5/0 -->  zero division error 
# 10. import math 
#     math.exp(1000) --> overflowError : 
# 

# In[ ]:


import math 
math.exp(1000)


# In[ ]:


#Exception Handling : 
# try 
# except 
# finally 
# else 
try: 
    a=int(input())
    b=int(input())
    c=a/b
    try: 
        print(5/0)
    except Exception as ve : 
        print('error')
except Exception as e:
    print('Exception : ',e)

    


# In[ ]:


try: 
    a=5/10
except:
    print('error')
else:
    print('success')
finally: 
    print('Bye')


# In[ ]:


try: 
    balance=int(input('enter the balance : '))
    amount=int(input('enter the amount : '))
    if(amount> balance):
        raise Exception('Insufficient Balance ')
except Exception as e :
    print(e)
else :
    print('Available balance : ',balance-amount)
finally: 
    print('Transaction Complete')
    


# In[ ]:


f1=open('pb499.txt','w+')
for i in range(1,130):
    f1.write(i)


# In[ ]:


try:
    d={'name':1234}
    user=input('enter username ')
    pass=input('enter password')
    cpass=inptu('confrim password : ')
    while True:
        logsing=input('login/signup')
        if logsing==('login'):
            user=input('enter username')
            pass=input('enter passwrod')
            cpass=input('confirm passwrod')
            if(user in d.keys()):
                pass=input('enter passwrod')
                cpass=input('enter confirm passwrod')
                if(pass=cpass)


# In[ ]:




