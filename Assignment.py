#Programs on selection and iteration
print("Program to find odd or even if it is odd find the factorial otherwise check whether it is palindrome or not")
num=int(input("Enter the number:"))
fact=1
if(num%2==1):
    for i in range(1,num+1):
        fact=fact*i
    fact_str=str(fact)        
    num_digits=len(fact_str)
    print("The factorial of a given number is ",fact)
    print("The number of digits in factorial number :",num_digits)

        
else:
    num_str=str(num)
    reversed_str=num_str[::-1]
    if(num_str==reversed_str):
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")

#Strings and its operations
print("Substring or not")
str1=input("Enter the string1:")
str2=input("Enter the string2:")
if(len(str1)<len(str2)):
    print("No")
else: 
    i=0
    j=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            j+=1
        i+=1

    if(j==len(str2)):
        print("Yes")
    else:
        print("No")

#Lists and its operations
#(a)
print("Positive and negative indexing")
lst=list(input("Enter the list elements:").split())
print(lst)
print("Positive indexing")
for i in range(0,len(lst)):
    print("list[",i,"]:",lst[i])
print("Negative indexing")
for i in range(-len(lst),0):
    print("list[",i,"]:",lst[i])

#(b)
print("Ascending order or not")
lst=list(input("Enter the list elements:").split())
print(lst)
lst1=lst[:]
lst1.sort()
if lst==lst1:
    print("Yes,it is a ascending order")
else:
    print("No,it is not a ascending order")

#Tuples and its operations
#(a)
print("To convert tuple into string")
tupl=tuple(input("Enter the input:").split())
print(tupl)
str1=''
for i in tupl:
    str1+=i
print("String is",str1)

#(b)
print("To reverse a tuple")
tupl=tuple(input("Enter the input:").split())
print("The orginal tuple :",tupl)
print("The reversed tuple :",tupl[::-1])

#Sets and its operations
print("to check subset or not")
set1=set(input("Enter the elements:").split())
set2=set(input("Enter the elements:").split())
print("Set 1:",set1)
print("Set 2:",set2)
ans=set2.issubset(set1)
if ans==True:
    print("Yes,it is a subset")
else:
    print("No,it is not a subset")

#Dictionaries and its operations
print("To iterate over dictionaries using for loop")
my_dict = {
    'apple': 2,
    'banana': 3,
    'orange': 1,
    'grape': 4
}

for key in my_dict:
    value = my_dict[key]
    print(f"{key}: {value}")

#computaions using numpy functions
#(a)
import numpy as np

lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(arr)

#(b)
import numpy as np

lst = [1, 2, 3, 4, 5]
tupl = (6, 7, 8, 9, 10)

array_from_list = np.array(lst)
array_from_tuple = np.array(tupl)

print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)

#data manipulations using pandas
#(a)
import numpy as np
import pandas as pd

arr= np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
series_1 = pd.Series([10, 11, 12, 13, 14])

df_from_array = pd.DataFrame(arr, columns=['A', 'B', 'C'])

df_from_series = pd.DataFrame(series_1, columns=['Values'])

print("DataFrame from NumPy array:")
print(df_from_array)

print("DataFrame from Pandas Series:")
print(df_from_series)


#(b)
import pandas as pd

series_1 = pd.Series([10, 20, 30, 40, 50])
series_2 = pd.Series([5, 10, 15, 20, 25])

# Additiom
addition_result = series_1 + series_2

# Subtraction
subtraction_result = series_1 - series_2

# Multiplication
multiplication_result = series_1 * series_2

# Division
division_result = series_1 / series_2

print("Addition Result:")
print(addition_result)

print("Subtraction Result:")
print(subtraction_result)

print("Multiplication Result:")
print(multiplication_result)

print("Division Result:")
print(division_result)


#(c)
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 24],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 52000],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT']
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Rows where age is greater than 25:")
filtered_df = df[df['Age'] > 25]
print(filtered_df)

print("Selecting Name and Salary columns:")
selected_columns = df[['Name', 'Salary']]
print(selected_columns)

df['Bonus'] = df['Salary'] * 0.05
print("DataFrame with the Bonus column:")
print(df)

grouped_df = df.groupby('Department')['Salary'].mean()
print("Average salary by department:")
print(grouped_df)

sorted_df = df.sort_values(by='Salary', ascending=False)
print("DataFrame sorted by Salary:")
print(sorted_df)
