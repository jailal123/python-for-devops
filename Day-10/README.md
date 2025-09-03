Let’s break this into pieces and explain with **clear examples**:

---

### ✅ **1. Taking Input and Splitting into a List**

You can take a string input from the user and split it into a list:

```python
# Take input and split into a list
data = input("Enter values separated by space: ")
data_list = data.split()  # splits by space
print(data_list)
```

**Example Input:**

```
apple mango orange
```

**Output:**

```
['apple', 'mango', 'orange']
```

You can also split by **comma**:

```python
data_list = data.split(",")
```




---

### ✅ **2. `os` Module to Talk to the Operating System**

The **os module** lets you interact with the OS. Example: listing files in a directory:

```python
import os

# Current directory
print("Current Directory:", os.getcwd())

# List all files and folders
files = os.listdir()
print("Files:", files)
```

You can also list a **specific folder**:

```python
print(os.listdir("C:/Windows"))
```

---

### ✅ **3. Exception Handling with `try` and `except`**

To handle errors like `PermissionError` or `FileNotFoundError`:

```python
import os

try:
    files = os.listdir("C:/RestrictedFolder")  # May cause PermissionError
    print(files)
except PermissionError:
    print("Permission Denied! You cannot access this folder.")
except FileNotFoundError:
    print("Folder does not exist.")
except Exception as e:
    print("An error occurred:", e)
```

---

### ✅ **4. Using `break` and `continue` in Loops**

* `break` → Exit the loop immediately.
* `continue` → Skip the current iteration and move to the next.

Example:

```python
for i in range(1, 10):
    if i == 5:
        print("Breaking at 5")
        break  # loop ends here
    if i % 2 == 0:
        continue  # skips even numbers
    print(i)
```

**Output:**

```
1
3
Breaking at 5
```

---

### ✅ **5. Handling `PermissionError` Specifically**

`PermissionError` happens when you try to access a folder or file without rights:

```python
import os

try:
    os.remove("C:/System32/file.txt")  # Dangerous example!
except PermissionError:
    print("You don't have permission to delete this file.")
```

---

#### 🔹 **Combine Everything in One Example:**

```python
import os

# Input: folder path
folder = input("Enter folder path: ")

try:
    files = os.listdir(folder)
    print("Files in folder:")
    for file in files:
        if file.endswith(".txt"):
            continue  # skip .txt files
        print(file)
        if file == "stop.txt":
            print("Found stop file, breaking...")
            break
except PermissionError:
    print("Permission Denied!")
except FileNotFoundError:
    print("Folder not found!")
except Exception as e:




Let's break this into clear parts and address everything step by step:

---

### ✅ **1. `print(flask[2][type])` meaning**

This looks like **Python indexing and key access**.

* `flask[2]` → means take the **third element** from the `flask` list (index starts at 0).
* `[type]` → if that element is a dictionary, it tries to get the value of the key `type`.

Example:

```python
flask = [
    {"name": "Flask", "type": "Framework"},
    {"name": "Django", "type": "Framework"},
    {"name": "FastAPI", "type": "Framework"}
]

print(flask[2]["type"])  # Output: Framework
```

---

### ✅ **2. Python to GitHub API or CLI using script**

There are **two main ways**:

* **Using GitHub CLI (`gh`)** – commands like `gh repo clone`, `gh pr create`.
* **Using GitHub API + Python `requests` module**.

---

#### **Using GitHub API with Python (`requests`)**

**Example: Create a Pull Request**

```python
import requests
import json

# GitHub token (use Personal Access Token)
TOKEN = "your_github_token"
REPO = "username/repository"
API_URL = f"https://api.github.com/repos/{REPO}/pulls"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

data = {
    "title": "My Pull Request",
    "head": "feature-branch",  # source branch
    "base": "main",            # target branch
    "body": "This is an automated PR"
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.json())  # JSON to dictionary
```

---

### ✅ **3. JSON to Dictionary in Python**

If you have a JSON string:

```python
import json

json_str = '{"name": "Flask", "type": "Framework"}'
dict_obj = json.loads(json_str)
print(dict_obj)         # {'name': 'Flask', 'type': 'Framework'}
print(dict_obj['type']) # Framework
```

---

### ✅ **4. Basic Python Data Structures**

* **Set** → `my_set = {1, 2, 3}`
* **List** → `my_list = [1, 2, 3]`
* **Tuple** → `my_tuple = (1, 2, 3)`

**Difference:**

* `[]` list → mutable (can change)
* `()` tuple → immutable (cannot change)
* `{}` set → unordered, unique elements



    print("Unexpected error:", e)
```
