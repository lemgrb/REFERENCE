# Hello world
print("Hello World")

## 1. Variables
```python
# Variables = just assign a value. No data type 
# First character cannot be a digit
x = 7
y = "I"
z = "am"
print(x)
print(y)
print(y + z)
```

## 2. Data Types

### 2.0 Classes
+ Classes are blueprints for creating instances or objects

```python
class TestCase:
    count = 0
    # instance variable & attributes
    def __init__(self, name):
        self.name = name
    # methods are part of the class. First argument usu. is 'self'
    def print_name(self):
        return self.name

instance = TestCase("TC001")
print(instance.count)
print(TestCase.count)
print(instance.print_name())
print(instance.name)
```

### 2.1 String
- Concatenate STRINGS with `+`
- Strings cannot be added to numeric values
- Use double or single quotes

#### Substring
```python
price='USD500'
price_number = price[3:]
print(price_number) # 500
```
#### Replace
```python
price='5,000'
print(price.replace(',','')) # 5000
```
### 2.2 Number
#### 2.2.1 Integer
#### 2.2.2 Floating point
- Of course, with decimal point
#### 2.2.3 Complex
### 2.3 Sequence : `list(), tuple(), range()`
range: mura rag sa lodash, generate number from 0 to n-1
```python
x = range(3)
for y in x:
  print(y) # --> 0,1,2
```
### 2.4 Mapping : `dict()`
### 2.5 Set types: `set(), frozenset()`
### 2.6 Boolean : `bool`
e.g. `is_hot = True` or `is_true = 1>0`
### 2.7 Binary types `(bytes, bytesarray, memoryview)`

## Type Conversion
- float to int: `int(73.1)`
- int to float: `float(73)`
- int to str `str(123)`
- string to tuple (collection of immutable items in order) 
  - `tuple('I am')` --> ("I"," ","a","m")
- string to list  (collection of mutable items in order) 
  - `list("I am") `  --> ["I"," ","a","m"]

## Basic Operators, Maths
+ `*/+-`
+ `%` modulo
+ `**` exponent
+ `//` floor
+ PRECEDENCE: `(),**,*,/,//,%,+,-`

## Comparisons and logical
+ `==` Equal
+ `!=` Not equal
+ `>,<,>=,<=`
+ `and`,`or`,`not`

## Conditional
`if, else, elif`

## Loops
`for` and `while`

Loop through a string
```python
for s in "string":
  print(s)
```

Loop through a list
```python
fruits = ["apple","orange"]
for s in fruits:
  print(s)
```

+ break
+ continue

while/else:
```python
i=1
while(i<15):
  print(i)
  i += 1
else:
  print("i is no longer less than 15")
```

### Loop

Print all keys
```python
for key in my_json.keys():
  print(key)
```

Enumerate index
```python
for index,product_container in enumerate(product_containers)
    driver.find_element(By.XPATH('//div[%s]'%(index+1)))
```

Access value from dictionary: `my_json['message']`

## Functions
Define function: `def function_name():`

```python
def divisible_by_3_or_2(num):
    if(num%2==0 and num%3==0):
        return "Divisible by both 2 and 3"
    elif(num%2==0):
        return "Divisible by 2"
    elif (num%3==0):
        return "Divisible by 3"
    else:
        return "Not divisible by 2 or 3"

print("6 is " + divisible_by_3_or_2(6))
print("12 is " + divisible_by_3_or_2(12))
print("1 is " + divisible_by_3_or_2(1))
print("3 is " + divisible_by_3_or_2(3))
print("2 is " + divisible_by_3_or_2(2))
```

## Data Structures

### List
```python
url_list = [] # Create 
for photo in json_data:
    url_list.append(photo['url'])
```

#### Sort a list
```python
numlist=[3,1,2]
print(sorted(numlist)) # [1, 2, 3]
```

### Set
Convert List to Set:
```python
url_set = set(url_list)
print(len(url_set))
```
