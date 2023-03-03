def elif_to_dict(elif_data):  
    """Convert an if-elif block into a python dictionary\n
    Argument (elif_data) is the full text of the if-elif-else block"""
    
    main_list = elif_data.split("==")
    dic = dict()
    for i in range(1,len(main_list)):
        kv = main_list[i].split(":")
        key = kv[0].strip("'").strip('"')
        value = kv[1].split()[1].strip("'").strip('"')
        dic[key] = value
    
    return dic

def main():
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
