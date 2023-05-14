# Day 4

## Ramdom module

```python
import random
```
* The random module is used to generate a randomly chosen value by the computer.

### Random module methods
```python
print(random.randint(1,100))
```
#### OUTPUT
```
56
```
* randint( a , b ) ⇾ This function returns a random number in between a and b.

```python
print(random.random())
```
#### OUTPUT
```
0.5935692004469484
```
* random( ) ⇾ This function returns a random floating point number from 0.0000.... to 0.9999....

## Python Lists

```python 
fruits = ["apple" , "mango" , "banana"]
print(fruits)
```
#### OUTPUT
```
["apple" , "mango" , "banana"]
```
* Python Lists are defined using square brackets [ ]
* Different values i.e different data types can be stored as values in Lists.
* Python Lists are mutable.

### Mutability of Lists
```python
print(fruits[0])
fruits[0] = "peach"
print(fruits)
```
#### OUTPUT
```
["peach" , "mango" , "banana"]
```
* Python lists are mutable i.e a value at a particular index can be changed.

## Nested Lists

```python
number_odd = [ 1 , 3 , 5 ]
number_even = [ 2 , 4 , 6 ]

numbers = [ number_odd , number_even ]
print(numbers)
```
#### OUTPUT
```
[ [ 1 , 3 , 5 ] , [ 2 , 4 , 6 ] ]
```
* Lists can also have another lists as values.
* These are called Nested Lists.

### Accessing nested list elements
```python
numbers = [ [ 1 , 3 , 5 ] , [ 2 , 4 , 6 ] ]
print(numbers[0][1]) 
```
#### OUTPUT
```
3
```
