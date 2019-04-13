#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Problem -1)

# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the program: 8
    
import math
def fact(num):
    return math.factorial(num)
    
    


# In[17]:


fact(8)


# In[33]:


# Problem -2)

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class namedetails():
    def __init__(self, getinput):
        self.getinput=getinput
    
    def getString(self):
        return self.getinput
    
    def printString(self):
        return self.getinput.upper()

namein=namedetails('mahidul')
nameout=namein
print(namein.getString())
print(nameout.printString())

# Also please include simple test function to test the class methods.
print(namedetails.getString(namein))
print(namedetails.printString(namein))


# In[39]:


# Problem -3)
# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class Rectangle():
    def __init__(self, length, width):
        self.length=length
        self.width=width
        
    def area(self):
        return self.length * self.width
    
compute=Rectangle(8,7)
print(compute.area())
        
    


# In[114]:


# Problem-4)
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.

list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
list3=list1+list2
#list3= list1.union(list2)

print(list3)
print(set(list3))


# In[10]:


# Problem-5)

# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?


#heads=int(input('Enter heads number'))

#if (heads>=1):
#    print('Number of chicken is ', int(heads/1))
#else:
#    print('Invalid number')

#legs=int(input('Enter legs number'))
    
#    if (legs/4==0):
#    print('Number of rabbits is ', int(legs/4))
#elif (legs>=4 and legs/4!=0):
#    print("It's invalid, plz enter even number of rabbits")
#    elif (legs/4)!=0:
#    print('Invalid number for rabbits')
    

    
    
    

    


# In[18]:


# Problem-5)

# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?


def main(total, numLegs):
    for rabbits in range(total + 1):
        chickens = total - rabbits
        if 2 * chickens + 4 * rabbits == numLegs:
            return chickens, rabbits
    return None, None


# In[19]:


if __name__ == '__main__':
    try:
        numHeads = int(input("Input number of heads: "))
        numLegs = int(input("Input number of legs: "))
        result = main(numHeads, numLegs)
        print ("Number of chickens are %d and rabbits are %d." % result)
    except TypeError:
        print ('TypeError: invalid input')


# In[ ]:




