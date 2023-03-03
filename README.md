# elif-to-dictionary
A python function that converts an if-elif-else block to a dictionary

## How to use:
- Download and import the function elif_to_dict() to your python file
- Provide the full text of your if-elif-else block as an argument to the function
- Store the dictionary in a variable
- To get a value for else:
  ```
  else_return = "Value not found"
  dic.get("val", else_return)
  ```
  
### Example:  
```
from elif_to_dict import elif_to_dict
text = """
    if mask=="255.255.255.255":
        return '/32'
    elif mask=='255.255.255.254':
        return '/31'
    elif mask=='255.128.0.0':
        return '/9'
    elif mask=='255.0.0.0':
        return '/8'
    else:
        return 'value not found'
    """

dic = elif_to_dict(text)
print(dic)
else_return = "value not found"             # value that will be returned if the key doesn't exist in the dictionary 
print(dic.get("255.128.0.0", else_return))  # prints '/9'
print(dic.get("val", else_return))          # prints 'value not found'
```

#### Dictionary output:  
`{'255.255.255.255': '/32', '255.255.255.254': '/31', '255.128.0.0': '/9', '255.0.0.0': '/8'}`
