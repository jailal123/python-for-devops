# Dictionaries

## Overview:
A dictionary in Python is a data structure that allows you to store and retrieve values using keys. It is also known as a hashmap or associative array in other programming languages. Dictionaries are implemented as hash tables, providing fast access to values based on their keys.

## Creating a Dictionary:
```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

## Accessing Values:
```python
print(my_dict['name'])  # Output: John
```

## Modifying and Adding Elements:
```python
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
```

## Removing Elements:
```python
del my_dict['city']  # Removing a key-value pair
```

## Checking Key Existence:
```python
if 'age' in my_dict:
    print('Age is present in the dictionary')
```
Let’s go step by step.

---

### ✅ **1. Dictionary Syntax in Python**

A **dictionary** is a collection of **key-value pairs**. The syntax:

```python
my_dict = {
    "name": "Abhi",
    "age": 25,
    "city": "Bhopal"
}
```

* **Keys** → `"name"`, `"age"`, `"city"`
* **Values** → `"Abhi"`, `25`, `"Bhopal"`

You can also create an empty dictionary:

```python
my_dict = {}  # empty dictionary
```

Or using the `dict()` function:

```python
my_dict = dict(name="Abhi", age=25)
```

---

#### ✅ **Accessing Values**

```python
print(my_dict["name"])  # Output: Abhi
```

#### ✅ **Adding a New Key-Value Pair**

```python
my_dict["country"] = "India"
```

#### ✅ **Changing a Value**

```python
my_dict["age"] = 26
```

#### ✅ **Removing a Key-Value Pair**

```python
my_dict.pop("city")
```

---

### ✅ **2. Example:**

```python
person = {
    "name": "Abhi",
    "age": 25,
    "profession": "Engineer"
}

print(person["name"])  # Abhi
```

---

### ✅ **3. Difference Between List and Dictionary**

| Feature        | **List**                         | **Dictionary**                          |
| -------------- | -------------------------------- | --------------------------------------- |
| **Definition** | Ordered collection of **values** | Collection of **key-value pairs**       |
| **Syntax**     | `my_list = [10, 20, 30]`         | `my_dict = {"name": "Abhi", "age": 25}` |
| **Access**     | By **index** → `my_list[0]`      | By **key** → `my_dict["name"]`          |
| **Order**      | Preserves insertion order        | Preserves insertion order (Python 3.7+) |
| **Duplicates** | Allows duplicate values          | Keys must be **unique**                 |
| **Mutability** | Mutable                          | Mutable                                 |

---

### ✅ **Quick Example Comparing Both:**

```python
# List
colors = ["red", "blue", "green"]
print(colors[1])  # blue (index-based)

# Dictionary
person = {"name": "Abhi", "age": 25}
print(person["name"])  # Abhi (key-based)

for key, value in my_dict.items():
    print(key, value)
```
