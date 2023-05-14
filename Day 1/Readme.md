# Day 1

## The print() statement
```python
print("Hello World!")
```
OUTPUT
```
Hello World!
```
* This code snippet prints the string inside the parenthesis ().

### 1. The sep parameter
```python
print("Hello","World",sep="$")
```
OUTPUT
```
Hello$World
```
* The sep parameter prints the given string with the separator defined.
* The default value of sep is space " ".

### 2. The end parameter
```python
print("Hello World",end="abcd")
```
OUTPUT
```
Hello Worldabcd
```
* The end parameter prints the given string and then the ending value defined by this parameter.
* The default value of end is "\n".

## String Concatenation
```python
print("Hello " + "World " + "Bye")
```
OUTPUT
```
Hello World Bye
```
* For string concatenation, the plus "+" operator is used.

## The input() statement
```python
print("Hello " + input("What is your name? "))
```
OUTPUT
```
What is your name? Atharva
Hello Atharva
```
* The input() method prompts the user for an input & halts the execution of the code until the input is given.

## Python Variables
```python
personname = input("Enter a name: ")
print("Hello " + personname + "\nNice to meet you!")
```
OUTPUT
```
Enter a name: Atharva
Hello Atharva
Nice to meet you!
```
* Variables can be used to store values of different datatypes.
* They can be overwritten.
