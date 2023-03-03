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
    text = """if mask=="255.255.255.255":
        return '/32'
    elif mask=='255.255.255.254':
        return '/31'
    elif mask=='255.255.255.252':
        return '/30'
    elif mask=='255.255.255.248':
        return '/29'
    elif mask=='255.255.255.240':
        return '/28'
    elif mask=='255.255.255.224':
        return '/27'
    elif mask=='255.255.255.192':
        return '/26'
    elif mask=='255.255.255.128':
        return '/25'
    elif mask=='255.255.255.0':
        return '/24'
    elif mask=='255.255.254.0':
        return '/23'
    elif mask=='255.255.252.0':
        return '/22'
    elif mask=='255.255.248.0':
        return '/21'
    elif mask=='255.255.240.0':
        return '/20'
    elif mask=='255.255.224.0':
        return '/19'
    elif mask=='255.255.192.0':
        return '/18'
    elif mask=='255.255.128.0':
        return '/17'
    elif mask=='255.255.0.0':
        return '/16'
    elif mask=='255.254.0.0':
        return '/15'
    elif mask=='255.252.0.0':
        return '/14'
    elif mask=='255.248.0.0':
        return '/13'
    elif mask=='255.240.0.0':
        return '/12'
    elif mask=='255.224.0.0':
        return '/11'
    elif mask=='255.192.0.0':
        return '/10'
    elif mask=='255.128.0.0':
        return '/9'
    elif mask=='255.0.0.0':
        return '/8'
    else:
        return '**ERROR**'"""

    dic = elif_to_dict(text)
    print(dic)
    else_return = "**ERROR**" # value that will be returned if the key doesn't exist in the dictionary 
    print(dic.get("255.192.0.0", else_return)) # returns '/10'
    print(dic.get("val", else_return))  # returns '**ERROR**'

if __name__=="__main__":
    main()
