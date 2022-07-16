import json
def get_stored_username(): #这个函数只负责获取存储的用户名（如果存储了的话）
    """如果存储了用户名，就获取它"""
    filename = 'chapter_10/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        print(username)

