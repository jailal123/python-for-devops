Great — you're diving into **command-line arguments**, **environment variables**, and **AWS CLI usage** — all important for scripting and secure automation. Let’s break this down clearly.

---
<img width="903" height="636" alt="image" src="https://github.com/user-attachments/assets/cafa24c4-6259-4b24-8e3a-951ece6ba9cc" />




## ✅ 1. **Command Line Arguments in Python (with `sys.argv`)**

### ✅ Example:

```python
# filename: calc.py
import sys

a = sys.argv[1]  # First argument
b = sys.argv[2]  # Second argument

# Values are strings by default
print("String addition:", a + b)

# Convert to int
print("Integer addition:", int(a) + int(b))
```

### 👇 Usage from command line:

```bash
python calc.py 5 7
```

### 🔎 Output:

```
String addition: 57
Integer addition: 12
```

> 🧠 `sys.argv[]` values are **always strings** — you must cast them to `int`, `float`, etc., as needed.

---

## ✅ 2. **Environment Variables to Store Sensitive Info**

Use `os.environ` or `os.getenv()` to **read environment variables** like tokens, keys, passwords.

### ✅ Example:


#Export apitoken=465sdkjadg
#Import os
#token = os.getenv("apitoken ")  
#print("My API Token:", token)


```python
# filename: secure_script.py
import os

token = os.getenv("APITOKEN")  # Recommended
print("My API Token:", token)
```

### 👇 Set the variable in shell (temporarily):

#### ✅ Linux / Mac / Git Bash:

```bash
export APITOKEN=mysecret123
python secure_script.py
```

#### ✅ Windows CMD:

```cmd
set APITOKEN=mysecret123
python secure_script.py
```

#### ✅ Windows PowerShell:

```powershell
$env:APITOKEN="mysecret123"
python secure_script.py
```

---

## 🔐 Why Use Environment Variables?

* Keeps secrets **out of code**
* Supports **CI/CD pipelines**, Docker, cloud configs
* Helps follow **12-factor app principles**

---

## ✅ 3. **AWS CLI with Environment Variables**

You can pass **AWS credentials** via env variables.

### Example:

```bash
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=abc123...
export AWS_DEFAULT_REGION=us-east-1

aws s3 ls
```





## 🧪 Summary

| Concept            | Key Usage                                |
| ------------------ | ---------------------------------------- |
| `sys.argv[n]`      | Read command-line argument as **string** |
| `int(sys.argv[n])` | Convert to int                           |
| `os.getenv("VAR")` | Read sensitive info from env vars        |
| `export VAR=value` | Set env var in Linux/Mac                 |
| `set VAR=value`    | Set env var in Windows CMD               |
| `$env:VAR="value"` | Set env var in PowerShell                |


