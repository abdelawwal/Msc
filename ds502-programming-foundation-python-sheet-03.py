#!/usr/bin/env python
# coding: utf-8

# # Sheet 3

# ############
# 
# Question 01:
# 
# Write a python program that reads a file and print the number of plandromic words that it contains.

# In[1]:


# opening the file
with open("Examples-of-Single-Word-Palindromes.txt") as fp:
    # store the every word of the file in a list
    palindromeList=fp.read().split() 
    print("The Original List of file words is : \n", palindromeList) # this line is for our understanding
    
    
    # defining a function which will check 
    # if the string is palindrome or not
    def is_palindrome(mystring):
        mystring=mystring.lower()
        reverse=mystring[::-1]
        return mystring==reverse

    
    # extracting all palindrome string
    palindromeList=list(filter(is_palindrome,palindromeList))
    palindromeNumbers = len(palindromeList)

    print("\n The List of palindrome words is : \n",palindromeList)

    print ("\n Numbers of all palindrome words in the file are : ",palindromeNumbers)


# ############ - ############ - ############ - ############
# 
# Question 02:
# 
# Write a program that prompts the user to enter a text filename and displays the number of vowels and consonants in the file.

# In[2]:


# Examples-of-Single-Word-Palindromes.txt

filename = input("Enter The file Name : ")
with open(filename) as fp:
    fileList = list(filename)
    vowelNo = 0
    consonantNo = 0

    for i in fileList:
        if i == 'a' or i=='e' or i=='i' or i =='o' or i=='u':
            vowelNo += 1
        else:
            consonantNo += 1

    print("\n The Number of Vowels Characters in the file are :",vowelNo,"\n The Number of Constants Characters in the file are :",consonantNo)


# ############ - ############ - ############ - ############
# 
# Question 03:
# 
# Write a program that prompts the user to enter a text file, reads words from the file, and displays all the non-duplicate words.

# In[3]:


with open("question3.txt") as fp:
    fileline = fp.readline()
    print('The Original Test is : \n','--------------------\n',fileline,'\n')
    originaltext = fileline.split()
    newtext = []
    for i in originaltext:

        # If condition is used to store unique string
        # in another list 'newtext'
        
        if (fileline.count(i)>=1 and (i not in newtext)):
            newtext.append(i)
            
    print('The New Text is : \n','----------------\n',' '.join(newtext))


# ############ - ############ - ############ - ############
# 
# Question 04:
# 
# Write a program to remove newline characters from a file and write the result in another file.

# In[4]:


# read file

with open("in_file.txt","r+") as infp:

    # read and store all lines into list
    lines = infp.readlines()

    # move file pointer to the beginning of a file
    infp.seek(0)

    # truncate the file
    infp.truncate()

    # open file for writing
    with open("out_file.txt", "w") as outfp:
    
    # start writing lines        
        for line in lines:
            outfp.write(line)


# ############ - ############ - ############ - ############
# 
# Question 05:
# 
# Write a program to read the first n lines of a file. Prompt the user to enter the value for n.

# In[5]:


## question5.txt

# prompte for number of lines to print
n = int(input("Enter the number of lines to display : "))

# read file
with open("question5.txt","r") as fp:
    
    lines = fp.readlines()
    print("-------------------------\n")
    
    # start writing lines
    # iterate line and line number    
    
    for number, line in enumerate(lines):
        
        if number <= n-1:
            print(line)


# ############ - ############ - ############ - ############
# 
# Question 06:
# 
# Write a program to read the last n lines of a file. Prompt the user to enter the value for n.

# In[6]:


## question5.txt

# print result
#print("\n the last ",n," lines of a file : \n" + str(res))


fname = input('Enter the File name you want to open : ')
n = int(input("Enter The number of lines you want to read from the end of the file : "))
print("-----------------------------------------------------------------------------\n")
with open(fname) as f:

    for line in (f.readlines() [-n:]):
        print(line)


# ############ - ############ - ############ - ############
# 
# Question 07:
# 
# Write a program to combine each line from the first file with the corresponding line in the second file in a tuple.

# ############ - ############ - ############ - ############
# 
# Question 08:
# 
# Write a program that reads the contents of the file and counts the occurrences of each letter. Prompt the user to enter the filename.

# In[7]:


# Sheet3.txt

# prompte for number of the last lines to print 
fp_v = input("Enter the file name to counts the occurrences of each letter : ")

all_letters = {}

# read file
with open(fp_v,"r") as fp:
    lines = fp.readlines()
    
    for i in lines:
        
        for j in i:
            if j in all_letters:
                all_letters[j] +=1
            else:
                all_letters[j] = 1
                
# print the occurrences of each letter
print ("\n Count of all the occurrences of each letter is :\n ----------------------------------------------- \n" 
       +  str(all_letters))            


# ############ - ############ - ############ - ############
# 
# Question 09:
# 
# Write a program to read and write the contents from one csv file to another.

# In[8]:


# train.csv
# new_train.csv


import csv

with open("train.csv", mode="r") as old_file:
    reader_obj = csv.reader(old_file) #read the current csv file

    with open("new_train.csv", mode="w+") as new_file:
        writer_obj = csv.writer(new_file, delimiter=",") # Writes to the new CSV file 

        for data in reader_obj:
            #loop through the read data and write each row in new_demo_csv.csv
            writer_obj.writerow(data)


# ############ - ############ - ############ - ############
# 
# Question 10:
# 
# Write the following dataset to a csv file with name “employee.csv”
# emp_name, sal, dept
# ‘a’, 100, ‘cs’
# ‘b’, 200, ‘is’
# ‘c’, 300, ‘cs’
# ‘d’, 400, ‘ds’
# ‘e’, 500, ‘cs’
# ‘f’, 600, ‘cs’

# In[9]:


import csv
  
# list of column names 
column_names = ['emp_name','sal','dept']

# list of data 
data  = [['a',100,'cs'],['b',200,'is'],['c',300,'cs'],['d',400,'ds'],['e',500,'cs'],['f',600,'cs']]

with open('employee.csv', 'w+', newline ='') as csv_file:
    #this is the writer object
    writer = csv.writer(csv_file)
    
    # this will list out the names of the columns which are always the first entrries
    writer.writerow(column_names) 
    
    for i in data:
         #this is the data
        writer.writerow(i)    


# ############ - ############ - ############ - ############
# 
# Question 11:
# 
# Using employee.csv file to find the number of employees working in cs dept

# In[10]:


import csv

count_n = 0
with open('employee.csv','r') as data:

    employee = csv.reader(data)
    
    for emp in employee:
        if emp[2] == "cs":
            count_n += 1
            
            
print ("The number of employees working in CS dept are : " , count_n)

