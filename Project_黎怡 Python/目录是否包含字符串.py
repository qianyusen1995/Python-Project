import os

def search_directory_for_string(directory, target_string):
    result = []
    
    # 递归遍历目录及其子目录下的文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if target_string in content:
                        result.append(file_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {str(e)}")
    
    return result

if __name__ == "__main__":
    search_directory = input("请输入要搜索的目录路径：")
    search_string = input("请输入要查找的字符串：")
    
    found_files = search_directory_for_string(search_directory, search_string)
    
    if found_files:
        print("包含字符串的文件：")
        for file_path in found_files:
            print(file_path)
    else:
        print("未找到包含字符串的文件。")
