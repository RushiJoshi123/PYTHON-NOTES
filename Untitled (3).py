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
    d={'user':1234}
    ch=input('login or signup')
    if ch=="L":
        try:
            uname=input('username : ')
            pwd=input('password')
            if d[uname]!=pwd:
                raise Exception("")
        except Exception as e :
            print(e)
        else: 
            print('Login Successfull')
    elif ch=='s':
        try:
            uanme=input('Username')
            pwd=input('password')
            cpwd=input('confirm password')
            if pwd != cpwd:
                raise Exception('passwrod missing')
            else:
                d[uname]=pwd
        except Exception as e :
            print(e)
        else:
            print('registration Succesffull')
    else:
        raise Exception('invalid choice ')
        except Exception as e :
             print(e)
        else:
            print('good bye')
        
            
            


# In[ ]:


class A: 
    #Constructor : 
    def __init__(self):
        print('object is created')
    #Destructor : 
    def __del__(self):
        print('object is deleted')
    def demo(self):
        a=5
        b=10
        c=a+b
        yield a
        yield b 
        yield c
        print('yield : ',c)
        def demo2(self):
            print('inner method')

ob=A()
t=ob.demo()
print(type(t))
for i in t : 
    print(i)
del ob


# In[ ]:


#572
import math
class SQ: 

    def __init__(self,l):
        self.l=l

    def shift(self):
        try:
            if len(self.l)==0:
                raise Exception('empty list ')
            else:
                l=self.l
                a=l[0]
                l.remove(a)
                print(a, ' is removed from the list ')
                print('the current list is : ',l)
                return a
        except Exception as e :
            print(e)
    def unshift(self,n):
        l=self.l
        nl=[]
        nl.append(n)
        l=nl+l
        return l
    def push(self,n):
        l=self.l
        l.append(n)
        return l
    def pop(self):
        l=self.l
        return l[len(l)-1]
    def remove(self):
        l=self.l
        a=max(l)
        l.remove(a)
        return a

ob=SQ([2,5,8,4,9])
print(ob.shift())
print(ob.unshift(0))
print(ob.push(10))
print(ob.pop())
print(ob.remove())
    


# In[ ]:


class ATM:
    def __init__(self):
        self.pin = None  # Initially, no pin is set.
        self.balance = 0

    def create_pin(self):
        self.pin = input('Enter the pin: ')
        print("PIN has been set successfully!")

    def change_pin(self, np):
        self.pin = np
        print('Pin changed successfully!')

    def check_balance(self):
        if self.pin is None:
            print('You must set a PIN first.')
            return
        
        p = input('Enter the pin: ')
        if p != self.pin:
            print('Invalid pin.')
            return
        else:
            print('The current balance is:', self.balance)

    def withdraw(self, amount):
        if self.pin is None:
            print('You must set a PIN first.')
            return
        
        p = input('Enter the pin: ')
        if p != self.pin:
            print('Invalid pin.')
            return
        else:
            if self.balance >= amount:
                self.balance -= amount
                print('The amount has been debited!')
                print('The current balance is:', self.balance)
            else:
                print('Insufficient balance!')

    def deposit(self, amount):
        if self.pin is None:
            print('You must set a PIN first.')
            return
        
        p = input('Enter the pin: ')
        if p != self.pin:
            print('Invalid pin.')
            return
        else:
            self.balance += amount
            print('The balance has been updated!')
            print('The current balance is:', self.balance)

    def menu(self):
        while True:
            print('1. Create pin')
            print('2. Change pin')
            print('3. Check balance')
            print('4. Withdraw money')
            print('5. Deposit money')
            print('6. Exit')
            n = int(input('Enter your choice: '))
            
            if n == 6:
                print("Exiting...")
                break
            
            if n == 1:
                self.create_pin()
            elif n == 2:
                np = input('Enter the new pin: ')
                self.change_pin(np)
            elif n == 3:
                self.check_balance()
            elif n == 4:
                amount = int(input('Enter the amount: '))
                self.withdraw(amount)
            elif n == 5:
                a2 = int(input('Enter the amount: '))
                self.deposit(a2)

atm = ATM()
atm.menu()


# In[ ]:


f=open('demo1.txt')
avg=0
sum=0
count=0
for line in f: 
    if line.startswith('X-DSPAM-Confidence'):
        for i in line : 
                sum+=1
                count+=1
        
print('avg is ',sum/count)
    


# In[ ]:


f, l = open('demo1.txt'), []
for i in f:
    s = i.split()
    for j in s:
        if j not in l:
            l.append(j)
f.close()
print(sorted(l))


# In[ ]:


f=open('mail.txt','w')
for i in range(15):
    f.write('from student_'+str(i)+'_@lju.edu.in\n')


# In[21]:


f, l = open('mail.txt'), []
d={}
count=0
for i in f:
    if (i.startswith('from ') and not 'from:' in i ):
        s = i.split()
        for j in s:
            if j.endswith('_@lju.edu.in'):
                l.append(j)
                count+=1
print(count)

for i in l :
    d[i]=l.count(i)
print(d)
m=max(d.values())
print(m)
for i in d :
    if d[i]==m:
        print(i,d[i])


# In[20]:


f, l,d= open('mail.txt'), [],{}
for i in f:
    if (i.startswith('from ') and not 'from:' in i ):
        s=i.split()
        for j in s :
            s2=j.split(':')
            if(s2[0].isdigit()):
                l.append(s2[0])
for i in l :
    d[i]=l.count(i)
d2=sorted(d.items())
for i in d2:
    print(i[0],i[1])


# In[ ]:




