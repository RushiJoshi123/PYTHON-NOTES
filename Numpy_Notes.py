#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class staff:
    def __init__(self):
        self.name=input('enter the name')
        self.sal=float(input('enter the salary'))
    def display(self):
        print(self.name)
        print(self.sal)
class teaching(staff):
        def __init__(self):
            super().__init__()
            self.sub=input('enter the subject')
        def display(self):
            super.display()
            print(self.sub)
class nonteaching(staff):
        def __init__(self):
            super().__init__()
            self.dep=input('enter the dep')
        def display(self):
            super().display()
            print(self.dep)
s=teaching()
p=nonteaching()
s.display()
p.display

    


# In[ ]:


class staff:
    def __init__(self):
        self.name = input('Enter the name: ')
        self.sal = (input('Enter the salary: '))
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.sal)

class teaching(staff):
    def __init__(self):
        super().__init__()
        self.sub = input('Enter the subject: ')
    def display(self):
        super().display()
        print("Subject:", self.sub)

class nonteaching(staff):
    def __init__(self):
        super().__init__()
        self.dep = input('Enter the department: ')
    def display(self):
        super().display()
        print("Department:", self.dep)


s = teaching()
p = nonteaching()
s.display()
p.display()


# In[ ]:


class matrix:
    def __init__(self):
        self.row=0
        self.col=0
        self.mat=[]
    def get_row(self):
        self.row=int(input())
    def get_col(self):
        self.col=int(input())
    def get_matrix(self):
        def __add__(self,other):
        
        for i in range (self.row):
            row=[]
            for j in range (self.col):
                   row.append(int(input()))
            self.mat.append(row)
            print(self.mat)
        
m=matrix()
m.get_row()
m.get_col()
m.get_matrix()


# In[ ]:


class matrix:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.mat = []

    def get_row(self):
        self.row = int(input("Enter the number of rows: "))

    def get_col(self):
        self.col = int(input("Enter the number of columns: "))

    def get_matrix(self):
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append(int(input()))
            self.mat.append(row)

    def display_matrix(self):
        for row in self.mat:
            print(" ".join(map(str, row)))


m = matrix()
m.get_row()
m.get_col()
m.get_matrix()
m.display_matrix()


# In[ ]:


class matrix:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.mat = []

    def get_row(self):
        self.row = int(input("Enter the number of rows: "))

    def get_col(self):
        self.col = int(input("Enter the number of columns: "))

    def get_matrix(self):
        print("Enter matrix elements row by row:")
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append(int(input(f"Enter element at ({i+1}, {j+1}): ")))
            self.mat.append(row)

    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            print("Matrix dimensions must match for addition.")
            return None
        
        result = matrix()
        result.row, result.col = self.row, self.col
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append(self.mat[i][j] + other.mat[i][j])
            result.mat.append(row)
        return result

    def __mul__(self, other):
        if self.col != other.row:
            print("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
            return None
        
        result = matrix()
        result.row, result.col = self.row, other.col
        for i in range(self.row):
            row = []
            for j in range(other.col):
                sum_product = 0
                for k in range(self.col):
                    sum_product += self.mat[i][k] * other.mat[k][j]
                row.append(sum_product)
            result.mat.append(row)
        return result

    def display_matrix(self):
        print("The matrix is:")
        for row in self.mat:
            print(" ".join(map(str, row)))


print("Matrix 1:")
m1 = matrix()
m1.get_row()
m1.get_col()
m1.get_matrix()

print("\nMatrix 2:")
m2 = matrix()
m2.get_row()
m2.get_col()
m2.get_matrix()

m3 = m1 + m2
if m3 is not None:
    print("\nResultant Matrix after Addition:")
    m3.display_matrix()

m4 = m1 * m2
if m4 is not None:
    print("\nResultant Matrix after Multiplication:")
    m4.display_matrix()


# In[ ]:


# Abstraction : 
from abc import ABC,abstractmethod
class DemoAbClass(ABC):
    @abstractmethod
    def demo(self):
        print('demo method of parent class')
class baseclass(DemoAbClass):
    def display(self):
        print('base class')
    def demo(self):
        print('demo method of base class')
ob = baseclass()
ob.demo()
ob.display()


# In[ ]:


from abc import ABC,abstractmethod
import math
class shape: 
    x=10
    @abstractmethod 
    def calculate_area() :
        pass
class rectangle(shape):
    def calculate_area(self,l,b):
        return l*b
    def __gt__(self,other):
        return self.area>other.area
class circle(shape):
    def calculate_area(self,r):
        self.area = math.pi*r*r
        return self.area
ob1 = rectangle()
ob2 = circle()
print(ob1.calculate_area(3,4))
print(ob2.calculate_area(3))


# In[ ]:


from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def recieve_call(self):
        pass
    @abstractmethod
    def end_call(self):
        pass
    @abstractmethod
    def is_free(self):
        pass
    @abstractmethod
    def get_rank(self):
        pass
class Respondent(Employee):
    def __init__(self):
        self.id = int(input('enter the id : '))
        self.name = input('enter the name ')
        self.b=True
        self.rank=3
    def recieve_call(self):
        print(f'call received by {self.name}')
        self.b=False
    def end_call(self):
        print('call ended')
        self.b=True
    def is_free(self):
        return self.b
    def get_rank(self):
        return self.b
    
        
class Manager(Employee):
    def __init__(self):
        self.id = int(input('enter the id: '))
        self.name = input('enter the name : ')   
        self.b=True
        self.rank=2
    def recieve_call(self):
        print(f'call received by {self.name}')
        self.b=False
    def end_call(self):
        print('call ended')
        self.b=True
    def is_free(self):
        return self.b
    def get_rank(self):
        return self.rank
    
    
class Director(Employee):
    def __init__(self):
        self.id = int(input('enter the id: '))
        self.name = input('enter the name : ')
        self.rank=1
        self.b=True
    def recieve_call(self):
        print(f'call received by {self.name}')
        b=False
    def end_call(self):
        print('call ended')
        b=True
    def is_free(self):
        return self.b
    def get_rank(self):
        return self.rank
class call :
    def __init__(self):
        self.name=input('enter the name : ')
        self.id=int(input('enter the id : '))
        self.assign=False
class callHand:
    res=[]
    manager=[]
    direc=[]   
    def add_emp(self,ob):
        if ob.rank==3:
            callHand.res.append(ob)
        if ob.rank==2:
            callHand.manager.append(ob)
        if ob.rank==1:
            callHand.direc.append(ob)
    def dispatch_call(self,cob):
        for i in  callHand.res:
            if i.b : 
                i.recieve_call()
                cob.assign = True
                break
        if(cob.assign==False):
            for i in  callHand.manager:
                    if i.b : 
                        i.recieve_call()
                        cob.assign = True
                        break
        if(cob.assign==False):
             for i in  callHand.direc:
                    if i.b : 
                        i.recieve_call()
                        cob.assign = True
                        break
        else:
            print('all are busy...')
            
                          
r1 = Respondent()
m1 = Manager()
d1 = Director()
ch=  callHand()
ch.add_emp(r1)
ch.add_emp(m1)
ch.add_emp(d1)
c1= call()
ch.dispatch_call(c1)
c2= call()
ch.dispatch_call(c2)
c3= call()
ch.dispatch_call(c3)
c4= call()
ch.dispatch_call(c4)


# In[ ]:


class Employee : 
    def set(self):
        self.name=
    def __init__(self):
        self.id = int(input('enter your id : '))
        self.name=input('enter your name : ')
        self.salary=int(input('enter your salary : '))     


# # Numpy
# 

# In[23]:


import numpy as np 

l=[]
for i in range(1,211):
    l.append(i)
arr = np.array(l)
print("dimension : ",arr.ndim)
print("shape : ", arr.shape) # returns tuple 
# print(arr) # vector 
print()
arr = arr.reshape(5,6,7)
print('first')
print(arr[0:3,4:5:,-2:2:-1])
print()
print(arr)


# In[28]:


import numpy as np
l=[]
for i in range(18):
    l.append(i+1)
sum=0
arr= np.array(l)
arr= arr.reshape(3,2,3)
print(arr)
for i in arr:
    for j in i: 
        sum+=j[1]
print('the sums is '+sum)
    


# In[47]:


#Concatenate : 
import numpy as np 
a1 = np.array(range(1,13)).reshape(2,2,3)
a2 = np.array(range(13,25)).reshape(2,2,3)
print(a1.shape,a2.shape)
c=np.concatenate((a1,a2)).reshape(2,3,4)
print(c.ndim)
print(c.shape)
print(c)


# In[ ]:


c = np.concatenate


# In[58]:


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
c= arr.reshape(1,1,12)
print(c)


# In[ ]:





# In[ ]:




