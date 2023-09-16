import os
import hashlib

def find_duplicates(directory):   
    files_by_content = {'E:\Picture图片\#2009-\2019'}
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            with open(path, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()
                if file_hash not in files_by_content:
                    files_by_content[file_hash] = []
                files_by_content[file_hash].append(path)

    for file_hash in files_by_content:
        if len(files_by_content[file_hash]) > 1:
            delete_files(files_by_content[file_hash])

def delete_files(file_list):
    for path in file_list:
        os.remove(path)

if __name__ == '__main__':
    find_duplicates('E:\Picture图片\#2009-\2019')
