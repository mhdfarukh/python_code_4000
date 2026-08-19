# a = 1 # a is (integer)
# b = 5.12 # b is a (flooting) point number
# C = "Farukh" # c is a (string)
# d = False # d is a (boolean) variable (True & False)
# jab kisi variable me koi value nahi hoti h 
# e = None # e is a none variable

# ' *********************************** '

# 51. Store an intrger.
# An integer is a number without a decimal point.
x = 1 
print(x)

# 52. Store a float.
a = 22.0
print(a)

# 53. Store a boolean.
a = 2
b = 5
smaller = a < b # True
big  = a > b # False

print(smaller)
print(big)

# 54. Store a string
a = "String"
print(a)

# 55. print the type of each variable.
name = "farukh"
age = 22
marks = 52.2

print(type(name))
print(type(age))
print(type(marks))

# 56.Create a list.
list1 = [10, 20, 30, 40]
print(list1)

# 57.Create tuple.
tuple_list = (50, 60, 70, 80,)
print(tuple_list)

# 58.Create a set.
group_set = {1,2,3,4,4,3,2,5} 
print(group_set) 

# 59.Create a dictionary.
my_dictionary = {"name": "Farukh", "age": 22}
print(my_dictionary)

# 60.print each data type.
my_list = [10,20,30,]
my_tuple = (10,20,30,40)
my_set = {10,20,30,40}
my_dictionary = {"name": "farukh", "age": 22}

print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dictionary))

# 61.Store multiple integers in a list.
mulitiple_list = [10, 20, 30, 40, 50]
print("mulitiple_list", mulitiple_list)

# 62.Store namas in a list.
name_list = ["Rahul", "Roshan", "Farukh"]
print("name_list", name_list)

# 63.Store cities in a tuple.
cities_name = ("varanasi", "Lucknow", "Allahabad", "Delhi")

print("cities_name", cities_name)

# 64.Store unique numbers in a set.
unique_numbers = {1, 2, 3, 4, 5, 6, 6}
print("unique_numbers", unique_numbers)

# 65.Create a student dictionary.
student = {"name":"Farukh",
           "age": 23,
           "course": "computer aplication",
             }
print(student)

# 66. Check the type of every variable.
namee = "Farukh"
agee = 23
i_student = True
markss = 25.5

print (type(name))
print(type(age))
print(type(student))
print(type(marks))

# 67. Compare int and float.
my_int = 10
my_float = 10.2

print("int:", my_int)
print("float:", my_float)


# 68. Compare list and tuple.
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print("list:", my_list)
print("tuple:", my_tuple)

# 69. Compare set and dictionary. 
my_sett = {10, 20, 30, 30, 40, 40 }
my_dictionaryy = {10, 20, 30, 40, 40,}


# 70. Compare bool and int.
a = True
b = 20

print(type(a))
print(type(b))


# 71. Create a nested list.
number = [
    ["Farukh", 50],
    ["Roshan", 80],
    ["Rahul", 40]
] # nested list h.
print(number)

# 72. Create nested dictionary.
nest_dict = {
         "nest_dic1":{
             "name": "Farukh",
             "age": 70,
             "course": "python"
               }
              }
print(nest_dict)


# 73. Create a tuple inside a list.
inside_tuple = [10, 20, 30, (40, 50, 60, 70)]
                # tupel () ke andar list []
print(inside_tuple)

# 74.Create a list inside dictionary.
inside_list = {
        "marks":[ 11, 12, 13, 14, 15]
    }
print(inside_list)

# 75. Store mixed data type in a list.
mixed_datalist = [
    10, 15.23, "hello", True & False, (12,46)
]
print(type(mixed_datalist))

# 76. Find list length.
my_listt = ["apple","banana", "data"]
# get the lenght 
list_lenght = len(my_list)

print("lenght:",list_lenght)

# 77. Find tuple lenght.
my_tuplee = (25, 45, 65, 80 , 90)
   # get the lenght.
tuplee = len(my_tuplee)

print("lenght:", tuplee)

# 78. Find dictionary lenght.
my_dicti = { "name:","farukh"}
    # get the lenth.
le_dictionar = len(my_dicti)

print("lenght:",le_dictionar)


# 79. Find set lenght.
num = {1, 2 , 3 , 4, 5, 5, 5, 6, 7}
lenght_set = len(num)

print("lenght:",lenght_set)

# 80. print all data type together.
mame = "farukh" #string
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
print(type(student))

# 81. Identify mutable data type.



# 82. Identify immutable data type.




# 83. Create empty list.



# 84. Create empty tupel.



# 85. Create empty set.




# 86. Create empty dictionary.




# 87. print memory type.




                                  # Section 3 : Type Conversion
                                  
# 101. Convert string to integer.
a = "1000"
a = int(a)
print(a)
print(type(a))

# 102. Convert integer to string.

aa = 120  # int
aa = str(aa)
print(aa)
print(type(aa))

# 103. Convert float to integer.
bb = 15.4  # float
bb = int(bb)
print(bb)
print(type(bb))

# 104. Convert integer to float.
c = 140   # int
c = float(c)
print(c)
print(type(c))

# 105. Convert string to float.
cc = "hello" # str
cc = float(c)
print(cc)
print(type(cc))

# 106. Convert float to string.
d = 120.00
d = str(b)
print(d)
print(type(d))

# 107. Convert Boolean to integer.
dd = True # Boolean
dd = int(dd)
print(dd)
print(type(dd))

# 108. Convert Integer to Boolean.
y = 14
y = bool(y)
print(y)
print(type(y))

#109. Convert string to list
s = "farukh"
s = list(s)
print(s)
print(type(s))

# 110. Convert list to tuple.
f = [21, 22, 33, 44,]
f = tuple(f)
print(f)
print(type(f))

# 111. Convert tuple to list.
w = (77, 88, 99, 55)
w = list(w)
print(w)
print(type(w))

# 112. Convert list to set.
ww = [11, 22, 33, 44]
ww = set(ww)
print(ww)
print(type(ww))

# 113. Convert set to list. 
Q = {45, 78, 94, 61}
Q = list(Q)
print(Q)
print(type(Q))

# 114. Convert dictionary keys to list.
E = {"name": "dllipe", "age": 25}
E = list(E)
print(E)
print(type(E))

# 115. Convert dictionary values to set.
EE = {"aam": "Mangeo", "Kela": 15}
EE = set(EE)
print(EE)
print(type(EE))

# 116. Convert String to tuple.



# 117. Convert String to Set.



# 118. Convert tuple to set.



# 119. Convert Set to Tuple.



# 120. Convert list to String.






