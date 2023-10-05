import os

# SQL Injection vulnerability
user_input = input("Enter a username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "'"

# Command Injection vulnerability
command = input("Enter a command: ")
os.system(command)

# Insecure use of eval
expression = input("Enter an expression: ")
result = eval(expression)

# Insecure file handling (no validation or sanitization)
file_name = input("Enter a filename: ")
with open(file_name, "r") as f:
    content = f.read()

# Insecure use of pickle (serialization)
import pickle
data = {"username": "admin", "password": "password123"}
serialized_data = pickle.dumps(data)

# Insecure use of base64 encoding/decoding
import base64
encoded_data = base64.b64encode(b"Sensitive data")
decoded_data = base64.b64decode(encoded_data)

# Insecure use of hashlib (unsalted hashing)
import hashlib
password = input("Enter a password: ")
hashed_password = hashlib.md5(password.encode()).hexdigest()

# Insecure use of regular expressions
import re
user_input = input("Enter an email address: ")
if not re.match(r"[^@]+@[^@]+\.[^@]+", user_input):
    print("Invalid email address")

# Insecure use of string concatenation
name = input("Enter your name: ")
greeting = "Hello, " + name

# Insecure use of string interpolation
name = input("Enter your name: ")
greeting = "Hello, %s" % name

# Insecure use of f-strings
name = input("Enter your name: ")
greeting = f"Hello, {name}"

# Insecure use of string concatenation in a loop
items = ["item1", "item2", "item3"]
result = ""
for item in items:
    result += item

# Insecure use of string.format() method
name = input("Enter your name: ")
greeting = "Hello, {}".format(name)

# Insecure use of string.Template
from string import Template
template = Template("Hello, $name")
name = input("Enter your name: ")
message = template.substitute(name=name)

# Insecure use of raw SQL queries (SQL injection)
user_input = input("Enter a username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "'"

# Insecure use of shell commands (command injection)
user_input = input("Enter a command: ")
os.system(user_input)

# Insecure use of subprocess with shell=True
command = input("Enter a command: ")
import subprocess
subprocess.call(command, shell=True)
