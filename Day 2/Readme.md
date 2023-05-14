# Day 2

## Data types
### Strings
```python
firstname = "Atharva"
surname = "Tiwary"
```
* Strings are a combination of characters.
* They are defined uisng Single or Double quotes. 

### Integer
```python
age = 20
sum = 45
```
* Integers are the numbers in Python 
* Any non-decimal number is an interger in Python.

### Float
```python
pi = 3.14159
```
* Float are the decimal numbers.
* Float precision is the number of digits after the decimal point.
* The default prcision is set to 28 places.

### Boolean
```python
isTeenager = False
isSmart = True
```
* Boolean represent two values True and False.
* It can also be represented in integer: 0 as False and any other value as True. 



## Type error, Type checking, Type casting

### Type Error

```python
print("a " + 3 + " c")      
```
OUTPUT
```
TypeError: can only concatenate str (not "int") to str
```
* Type error is one of the common error messages in Python in which the datatype of the parameter does not match with the required datatype.

### Type Checking

```python
print(type("hello"))
print(type(123))
```
OUTPUT
```
<class 'str'>
<class 'int'>
```
* To check the data type of a value, type() method if used.
* It returns the data type of the value.

### Type Casting

```python
n = 35
print(type(n))

n = float(n)
print(type(n))
```
OUTPUT
```
<class 'int'>
<class 'float'>
```
* Type casting means to change from one data type to another.
* str() - It changes datatype to string.
* int() - It changes datatype to integer.

## Mathematical operators

```python
 print(2 + 5)  # Addition
 print(5 - 3)  # Subtraction 
 print(3 * 6)  # Multiplication
 print(16 / 4)  # Division
 print(4**3)  # Exponential
```
OUTPUT
```
7
2
18
4.0
64
```
* Addition ( + ) : Addition of two numbers 
* Subtraction ( - ) : Subtraction of two numbers
* Multiplication ( * ) : Multiplies two numbers
* Division ( / ) : Divides two numbers. Result is in float.
* Floor division ( // ) : Divides the two numbers. Results the quotient of the division 
* Modulus ( % ) : Divides the two numbers. Results the remainder of the division
* Exponential ( ** ) : Raised to power of the number.

### Mathematical Operators Priority

*( Highest to Lowest )*

|Operators| Symbol |
|:---------:|:--------:|
|Parenthesis| ( ) |
|Exponential|**|
|Multiplication, Division| *  /|
|Addition, Subtraction| +   - |

## f-Strings

```python
name = "Atharva"
age = 20
pi = 3.14
print(f" Your name is {name}, your age is {age} and value of pi is {pi}")
```
OUTPUT
```
Your name is Atharva, your age is 20 and value of pi is 3.14
```

* f-strings are useful when you have to display non-string variables in the print statement.
* Before the text, type ' f ' in the print statement. 
* Any variable you want to print can be defined in between the curly brackets { }.
