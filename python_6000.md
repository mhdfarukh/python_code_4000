# Python Variables Practice

- [Variable](#variables-1-50)
- [Multiple Assignment](#multiple-assignment-21-35)
- [Practice Problems](#Practice-Problems-36-50)
- [2.Data Types](#Data-Types-51-100)
- [3.Type Conversion](#Type-Conversion-101-150)
- [4.Type Casting & Input Problems](#Type-Casting-&-Input-Problems-151-200)
- [Python Comparison Operators Practice Questions](#Python-Comparison-Operators-Practice-Questions)

---

## Variable

### 01. Create a variable named `name` and store your name
```python
name = "farukh"
print(name)
```

### 02. Create a variable `age` and store your age
```python
age = 23
print(age)
```

### 03. Print the value of a variable
```python
a = 12
print(a)
```

### 04. Create two variables and print both
```python
a = 12
b = 8
print(a, b)
```

### 05. Store a decimal number in a variable
```python
a = 22.04
print(a)
```

### 06. Store a boolean value
```python
a = True
b = False
print(a, b)
```

### 07. Store today's temperature
```python
x = 35.5
print(x)
```

### 08. Store a city name
```python
a = "Varanasi"
print(a)
```

### 09. Store another city name
```python
a = "Varanasi"
print(a)
```

### 10. Print a variable multiple times
```python
a = "hello"
print(a * 3)
```

### 11. Store two numbers and print their sum
```python
a = 5
b = 3
print(a + b)
```

### 12. Store two numbers and print their difference
```python
a = 20
b = 15
print(a - b)
```

### 13. Store two numbers and print their product (multiply `*`)
```python
a = 8
b = 5
print(a * b)
```

### 14. Store two numbers and print their quotient (division `/`)
```python
a = 10
b = 5
quotient = a / b
print(quotient)
```

### 15. Store three numbers and calculate their sum
```python
a = 12
b = 3
c = 5
print(a + b + c)
```

### 16. Store your first and last name separately
```python
first_name = "farukh"
last_name = "khan"
print(first_name)
print(last_name)
```

### 17. Print your full name using a variable
```python
name = "farukh khan"
print(name)
```

### 18. Store your school or company name
```python
school = "K M V M"
company = "KGN"
print(school)
print(company)
```

### 19. Store your country
```python
country = "India"
print(country)
```

### 20. Print all variables together
```python
name = "farukh"
surname = "khan"
age = 23
print(name)
print(surname)
print(age)
```

---

## Multiple Assignment (21-35)

### 21. Assign three variables in one line
```python
a, b, c = 1, 2, 3
print(a, b, c)
```
### 22. Assign the same value to three variables.
```python
a, b, c = 10, 10, 10
print(a, b, c)
```
## 23. Swap two variable.
```python
a = 20
b = 30
a, b = b, a
print("a", a)
print("b", b)
```

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

# 27. Create variables using meaningful name.
```python
age  = 22
name = "rahul"
city = "Varanasi"
print(age)
print(name)
print(city)
```
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

