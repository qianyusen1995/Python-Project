def get_formatted_name(first, last, middle=''): #将形参middle移到形参列表末尾，并将其默认值指定为一个空字符串。
    """生成整洁的姓名"""
    if middle: #根据是否提供了中间名相应地创建姓名：
        full_name = first + ' ' + middle + ' ' + last 
    else:
        full_name = first + ' ' + last
    return full_name.title()
    
a = get_formatted_name('janis', 'joplin')
print (a)