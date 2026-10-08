# 🐍 Python Programming – Complete Practice

Welcome to my Python programming practice repository.

This repository contains Python concepts, examples,
and practice problems from beginner to intermediate level.

## 👨‍💻 Author
**MHD FARUKH**

🎓 BCA Student
📍 Varanasi, India
---
## 📚 Table of Contents

-1. [Variable](#variables-1-50)
-2. [Multiple Assignment](#multiple-assignment-21-35)
-3. [Practice Problems](#Practice-Problems-36-50)
-4. [2.Data Types](#Data-Types-51-100)
-5. [3.Type Conversion](#Type-Conversion-101-150)
-6. [4.Type Casting & Input Problems](#Type-Casting-&-Input-Problems-151-200)
-7. [Python Comparison Operators Practice Questions](#Python-Comparison-Operators-Practice-Questions)
---

# 1. Variables

## 📌 Introduction.
A variable is name used to store data in python. 

### Examples 💻 01: Create a Variable

**Question:** 
# 01: Create a variable named `name` and store your name
```python
name = "farukh"
print(name)
```
**Output 🖥️:**
```text
Farukh
```
### Examples 💻 02: Store Age

**Question:**
# 02: Create a variable `age` and store your age
```python
age = 23
print(age)
```

**Output 🖥️:**
```text
23
```
### Examples 💻 03: Print a Value

**Question:**
# 03: Print the value of a variable
```python
a = 12
print(a)
```
### Examples 💻 04: Create Two variables print

**Question:**
# 04: Create two variables and print both
```python
a = 12
b = 8
print(a, b)
```
### Examples 💻 05: Store Decimal Number 

**Question:**
# 05: Store a decimal number in a variable
```python
a = 22.04
print(a)
```
### Examples 💻 06: Boolean value

**Question:**
# 06: Store a boolean Value.
```python
a = True
b = False
print(a, b)
```
### Examples 💻 07: Print temperature

**Question:**
# 07: Store today's temperature
```python
x = 35.5
print(x)
```
### Examples 💻 08: print a City

**Question:**
# 08: Store a city name
```python
a = "Varanasi"
print(a)
```
### Examples 💻 09: Another City name

**Question:**
# 09: Store another city name
```python
a = "Allahabad"
print(a)
```
### Examples 💻 10: Multiple times varibal

**Question:**
# 10: Print a variable multiple times
```python
a = "hello"
print(a * 3)
```
### Examples 💻

# 11: Store two numbers and print their sum
```python
a = 5
b = 3
print(a + b)
```
### Examples 💻

# 12: Store two numbers and print their difference
```python
a = 20
b = 15
print(a - b)
```
### Examples 💻

# 13: Store two numbers and print their product (multiply `*`)
```python
a = 8
b = 5
print(a * b)
```
### Examples 💻

# 14: Store two numbers and print their quotient (division `/`)
```python
a = 10
b = 5
quotient = a / b
print(quotient)
```
### Examples 💻

# 15: Store three numbers and calculate their sum
```python
a = 12
b = 3
c = 5
print(a + b + c)
```
### Examples 💻

# 16: Store your first and last name separately
```python
first_name = "farukh"
last_name = "khan"
print(first_name)
print(last_name)
```
### Examples 💻

# 17: Print your full name using a variable
```python
name = "farukh khan"
print(name)
```
### Examples 💻

# 18: Store your school or company name
```python
school = "K M V M"
company = "KGN"
print(school)
print(company)
```
### Examples 💻

# 19: Store your country
```python
country = "India"
print(country)
```
### Examples 💻

# 20: Print all variables together
```python
name = "farukh"
surname = "khan"
age = 23
print(name)
print(surname)
print(age)
```
---
# 2. Multiple Assignment

## 📌 Introduction

Multiple assignment allows us to assign values to multiple variables
in a single line of Python code.

### Example 1: Assign Multiple Values.(21-35)

### **Questions** 📝.

# 21. Assign three variables in one line
```python
a, b, c = 1, 2, 3
print(a, b, c)
```
### **Questions** 📝.

# 22. Assign the same value to three variables.
```python
a, b, c = 10, 10, 10
print(a, b, c)
```
## **Questions** 📝.

# 23. Swap two variable.
```python
a = 20
b = 30
a, b = b, a
print("a", a)
print("b", b)
```

# **Questions** 📝.

# 24. Swap three variable.
```python
a = 10
b = 20
c = 30
a, b, c = c, b, a
print("a", a)
print("b", b)
print("c", c)
```
# **Questions** 📝.

# 25.  print variables before swapping.
```python
a = 10
b = 20
a = a + b # 30

b = a - b # 20
a = a - b # 10

print("a =", a)
print("b =", b)
```

# **Questions** 📝.

# 26. print vaeriables after swapping.
```python
a = 10
b = 20
# swapping logic 
a = a + b  # 30
b = a - b  # 10 
a = a - b  # 20

# print variable after swpping
print("a =", a)
print("b =", b)
```

# **Questions** 📝.

# 27. Create variables using meaningful name.
```python
age  = 22
name = "rahul"
city = "Varanasi"
print(age)
print(name)
print(city)
```
# **Questions** 📝.

# 28. Create variable using snake_case.
```python
first_name = "farukh"
last_name = "khan"
student_age = 23
college_name = "J N M college"

print(first_name)
print(last_name)
print(student_age)
print(college_name)
```
# **Questions** 📝.

# 29. Craate variables with uppercase names.
```Python
NAME = "farukh"
AGE = 23
COLLEGE ="JNM College"
     # Uppercase Wale me Variables CAPIATAL me hata h 
print(NAME)
print(AGE)
print(COLLEGE)
```
# **Questions** 📝.

# 30. Store different data type in diffrerent variable.
```Python
name = "farukh"  # string
age =  22        # int
height = 5.3     # float
is_student = True # booolean
cities = ("varanasi", "delihi")  # tupel
number = {1, 2, 3}   # set

print(name)
print(age)
print(height)
print(is_student)
print(cities)
print(number)
```
# **Questions** 📝.

# 31. Store marks of five subjects.
```python
sub1 = 52
sub2 = 85
sub3 = 74
sub4 = 68
sub5 = 82
print(sub1, sub2, sub3, sub4, sub5)
```
# **Questions** 📝.

# 32. Store salary and bonus.
```python
salary = 25000
bonus = 5000

print("salary", salary)
print("bonus", bonus)
```
# **Questions** 📝.

# 33. Store width and height.
```python
width = 25
height = 35
print("width",width, )
print("height",height)
```
**Questions** 📝.

# 34. Store length and breadth.
```python
lenght = 20
breadth = 35
print("length",lenght, )
print("breadth",breadth)
```
**Questions** 📝.

# 35. Store principal, rete and time.
```python
principal = 1000
rate = 50
time = 5.00
print("pricipal Amount", principal)
print("rate interest", rate, "%")
print("time period", time, "years")
```
# (3). Practice Problems (36–50)

**Questions** 📝.

# 3. Calculate rectangle area.
```python
length = 10
width  = 20
print("area", length*width)
```
**Questions** 📝.

# 37. Calculate rectangle perimeter.
```python
length = 5
width  = 10
print("perimeter", 2*(length+width))
```
**Questions** 📝.

# 38. Calculate circle area.
```python
# circle ka area nikalne k formula pi r square (pi * r * r)
# pi = 3.14 hota h.
radius = 10
# r = 10 ( pi * r * r)
area = 3.14 * radius * radius
print(area)
```
**Questions** 📝.

# 39. Calculate circle circumference.
```python
# circle (chakr)center se kinare tak duri.
circle = 5
# formula ( c = 2pi.r) 
# pi ka maan 3.14 hota h 
# r = 5 h 

circumference = 2 * 3.14 * circle
print(circumference)
```
**Questions** 📝.

# 40. Calculate simple interest.
```python
# Formula = P * R * T (Principal, Reat, Time in years)
principal = 2000
interst_rate = 20
time = 26
```
**Questions** 📝.

# 41. Calculate total marks.
```python
marks1 = 20
marks2 = 50
marks3 = 60
print("marks1 =", marks1 + marks2 + marks3)
```
**Questions** 📝.

# 42. Calculate average marks.
```python
marks1 = 50
marks2 = 80
marks3 = 60

print("Average marks =", marks1 / marks2 / marks3)
```
# 43. Calculate annual salary.
```python
salary_monthly =1000
annual_salary = 12
print("Annual salary =", salary_monthly * annual_salary)
```
**Questions** 📝.

# 44. Calculate spped.
```python
car_speed = 150
pahucne_ka_time = 3 

print("speed =",  car_speed / pahucne_ka_time )
```
**Questions** 📝.

# 45. Calculate BMI.
```python
weight = 70
height = 1.60

bmi = weight / (height ** 2)
print("BMI:",round(bmi, 2))
```
**Questions** 📝.

# 47. Convert hours into minutes.
```python
h = 2 
mm = h * 60
print(mm)
```
**Questions** 📝.

# 48. Convert minutes into seconds.
```python
mm = 2
seconds = mm * 60
print (seconds)
```
**Questions** 📝.

# 49. Convert kilometers into meters.
```python
km = 2
meters = km * 1000
print(meters)
```
**Questions** 📝.

# 50. Calculate profit or loss.
```python
# (cp) cost price & (sp) selling price
cp = 300
sp = 150
profit = sp - cp
loss = cp - sp 

print (profit)
print(loss)
```
---
# (4). Data Types (51–100)

## 📌 Introduction.

A data type defines the kind of value a variable can store.

Python has several built-in data types that are used
to store different types of data, such as numbers, text,
collections, and logical values.

### 🔹 Common Python Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| int | Integer numbers | 23 |
| float | Decimal numbers | 10.5 |
| str | Text or string | "Farukh" |
| bool | True or False values | True |
| list | Ordered, changeable collection | [1, 2, 3] |
| tuple | Ordered, unchangeable collection | (1, 2, 3) |
| set | Unordered collection of unique values | {1, 2, 3} |
| dict | Key-value pairs | {"name": "Farukh"} |

### 💡 Important Note

Python is dynamically typed, which means
you do not need to declare the data type of a variable
explicitly. Python automatically identifies the data type
based on the assigned value.
---


### 1. Integer (int)

An integer is a whole number without a decimal point. 

### Examples 💻 

**Question** 📝.
# 51. Store an intrger.
```python
x = 22 
print(x)
```
**Output:**
```text
22
```
### 2. Float (float)
A float is a number that contains a decimal point.

### Examples 💻

# **Question** 📝.
# 52. Store a float.
```python
a = 22.0
print(a)
```
**Output:**
```text
22.0
```
## 3. Boolean Data Type (bool)
The Boolean data type represents Ture of False values.

### Examples 💻.

# **Question** 📝.
# 53. Store a boolean.
```python
a = 2
b = 5
smaller = a < b # True
big  = a > b # False

print(smaller)
print(big)
```
## 4. String (text) Data type (str).
A String is a sequence of characters enclosed in
single quotes, double quotes, or triple quotes.
 
### Examples 💻.

# **Question** 📝.
# 54. Store a string
```python
a = "String"
print(a)
```
# **Question** 📝.

# 55. print the type of each variable.
```python
name = "farukh"
age = 22
marks = 52.2
print(type(age))
print(type(marks))
```
# **Question** 📝.

# 56.Create a list.
```python
list1 = [10, 20, 30, 40]
print(list1)
```
# **Question** 📝.

# 57.Create tuple.
```python
tuple_list = (50, 60, 70, 80,)
print(tuple_list)
```
# **Question** 📝.

# 58.Create a set.
```python
group_set = {1,2,3,4,4,3,2,5} 
print(group_set) 
```
# **Question** 📝.

# 59.Create a dictionary.
```python
my_dictionary = {"name": "Farukh", "age": 22}
print(my_dictionary)
```
# **Question** 📝.

# 60.print each data type.
```python
my_list = [10,20,30,]
my_tuple = (10,20,30,40)
my_set = {10,20,30,40}
my_dictionary = {"name": "farukh", "age": 22}

print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dictionary))
```
# **Question** 📝.

# 61.Store multiple integers in a list.
```python
mulitiple_list = [10, 20, 30, 40, 50]
print("Mulitiple Integers", mulitiple_list)
```
# **Question** 📝.

# 62.Store namas in a list.
```python
name_list = ["Rahul", "Roshan", "Farukh"]
print("name List", name_list)
```
# **Question** 📝.

# 63.Store cities in a tuple.
```python
cities_name = ("varanasi", "Lucknow", "Allahabad", "Delhi")

print("Cities_name", cities_name)
```
# **Question** 📝.

# 64.Store unique numbers in a set.
```python
unique_numbers = {1, 2, 3, 4, 5, 6, 6}
print("Unique Numbers", unique_numbers)
```
# **Question** 📝.

# 65.Create a student dictionary.
```python
student = {"name":"Farukh",
           "age": 23,
           "course": "computer aplication",
             }
print(student)
```
# **Question** 📝.

# 66. Check the type of every variable.
```python
name = "Farukh"
age = 23
i_student = True
marks = 25.5

print (type(name))
print(type(age))
print(type(i_student))
print(type(marks))
```
# **Question** 📝.

# 67. Compare int and float.
```python
my_int = 10
my_float = 10.2

print("int:", my_int)
print("float:", my_float)
```
# **Question** 📝.

# 68. Compare list and tuple.
```python
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print("list:", my_list)
print("tuple:", my_tuple)
```
# **Question** 📝.

# 69. Compare set and dictionary. 
```python
my_sett = {10, 20, 30, 30, 40, 40 }
my_dictionaryy = {"name":"farukh"}
print(my_sett)
print(my_dictionaryy)
```
# **Question** 📝.

# 70. Compare bool and int.
```python
a = True
b = 20

print(type(a))
print(type(b))
```
# **Question** 📝.

# 71. Create a nested list.
```python
number = [
    ["Farukh", 50],
    ["Roshan", 80],
    ["Rahul", 40]
] # nested list h.
print(number)
```
# **Question** 📝.

# 72. Create nested dictionary.
```python
nest_dict = {
         "nest_dic1":{
             "name": "Farukh",
             "age": 70,
             "course": "python"
               }
              }
print(nest_dict)
```
# **Question** 📝.

# 73. Create a tuple inside a list.
```python
inside_tuple = (10, 20, 30, [40, 50, 60, 70])
                # tupel () ke andar list []
print(inside_tuple)
```
# **Question** 📝.

# 74.Create a list inside dictionary.
```python
inside_list = {
        "marks":[ 11, 12, 13, 14, 15]
    }
print(inside_list)
```
# **Question** 📝.

# 75. Store mixed data type in a list.
```python
mixed_datalist = [
    10, 15.23, "hello", True & False, (12,46)
]
print(type(mixed_datalist))
```
# **Question** 📝.

# 76. Find list length.
```python
my_listt = ["apple","banana", "data"]
# get the lenght 
list_lenght = len(my_listt)

print("lenght:",list_lenght)
```
# **Question** 📝.

# 77. Find tuple lenght.
```python
my_tuplee = (25, 45, 65, 80 , 90)
   # get the lenght.
tuplee = len(my_tuplee)

print("lenght:", tuplee)
```
# **Question** 📝.

# 79. Find set lenght.
```python
num = {1, 2 , 3 , 4, 5, 5, 5, 6, 7}
lenght_set = len(num)

print("lenght:",lenght_set)
```
# **Question** 📝.

# 80. print all data type together.
```python
name = "farukh" #string
age = 23
# integer
hight = 5.3
# float
a_student = True
# boolean
marks = [22, 56, 64, 67]
# list
subjects = ("python", "c++")
# tuple
numbers = {10, 20, 30}
# set  
n_studentt = {"name": "Farukh", "age": "23"}  # Dictionary

print(type(name))
print(type(age))
print(type(hight))
print(type(a_student))
print(type(marks))
print(type(subjects))
print(type(numbers))
print(type(n_studentt))
```
# **Question** 📝.

# 81. Identify mutable data type.
```python
mutable = [ 2, 4, 6, 8,]
print(type(mutable))
```
# **Question** 📝.

# 82. Identify immutable data type.
```python
imutable = ( 2, 4, 6, 8, 10,)
print(type(imutable))
```
# **Question** 📝.

# 83. Create empty list.
```python
empty_list = [ ]
print(empty_list)
```
# **Question** 📝.

# 85. Create empty set.
```python
empty_set = set()
print(type(empty_set))
```
# **Question** 📝.

# 86. Create empty dictionary.
```python
empty_dictionary = { }
print(type(empty_dictionary))
```
# **Question** 📝.

# 87. print memory type.
```python
my_tuple = ()
print(type(my_tuple))
```
# **Question** 📝.

# 88. Check if value is integer.
```python
a = 25
print(type(a))
```
# **Question** 📝.

# 89. Check if value is string.
```python
a = "value"
print(type(a)==str)
```
# **Question** 📝.

# 90. Check if value is Boolean.
```python
a = True
print(type(a) == bool)
```
