# Day 3

## Control flow

### if-else statements

#### Code 1
```python
num = 25

if num > 20:
  print("Hello")
else:
  print("Bye")
 ```
#### OUTPUT
```
Hello
```

#### Code 2
 ```python
num2 = 20

if num2 == 15:
  print("Equals")
else:
  print("Not equals")
```
#### OUTPUT
```
Not equals
```
* ' if ' and ' else ' statements are the control flow statements in Python.
* ' if ' statement checks for a condition and if it is True, it executes the block of code under it.
*  If the condition is False, the code block under ' else ' is executed.

## Comparison Operator

|Operator| Name | Description|
|:---:|:---:|:---:|
| a == b | Equals to | Returns True if both are equal |
| a < b | Less than | Returns True if a is less than b |
| a <= b | Less than or equals to | Returns True if a is less than or equal to b |
| a > b | Greater than | Returns True if a is greater than b |
| a >= b | Greater than or equals to | Returns True if a is greater than or equal to b |

```python
print(13 == 13)   # Equals to
print(31 > 30)    # Greater than
print(20 < 19)    # Less than
print(35 >= 30)   # Greater than or equals to
print(41 <= 40)   # Less than or equals to
```
#### OUTPUT
```
True
True
False
True
False
```

## Nested if

```python
num = 20

if num > 10:
  if num > 20:
    print("Hello one")
  else:
    print("Hello two")
else:
  print("Bye")
```
#### OUTPUT
```
Hello two
```
* ' if ' statement can also be used inside another ' if ' statement block.
* They work the same as the default ' if ' statements.

## elif statement

```python
number = 100

if number == 50:
  print("Hello one")
elif number == 100:
  print("Hello one two")
else:
  print("Bye bye")
```
#### OUTPUT
```
Hello one two
```
* ' elif ' statements works after the ' if ' statement's condition is False.
* ' elif ' statement also check for a condition and if it is True, it executes the block of code under it.
* If it is False, it goes to the code block below it.

## Multiple if statement

```python
number1 = 1000
number2 = 5000

if number1 > 100:
  print("Hello one")
  
if number2 < 3000:
  print("Hello three")
else:
  print("Bye one")
```
#### OUTPUT
```
Hello one
Bye one
```
* Python code can also have multiple ' if ' statements.
* They can executes in order they are written.

## Logical Operators
    
### and

*Truth Table*

|Input 1| Input 2 | Output |
|:---:|:---:|:---:|
|True|True|True|
|True|False|False|
|False|True|False|
|False|False|False|
    

### or
*Truth Table*

|Input 1| Input 2 | Output |
|:---:|:---:|:---:|
|True|True|True|
|True|False|True|
|False|True|True|
|False|False|False|

### not
*Truth Table*

|Input | Output |
|:---:|:---:|
|True|False|
|False|True|
