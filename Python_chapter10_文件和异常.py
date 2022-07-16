#   10.1　从文件中读取数据
#   10.1.1　读取整个文件 'file_reader.py'
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
#   10.1.2　文件路径
##相对文件路径：让Python到指定的、相对于 当前程序 所在目录Python_KT的位置去查找
with open('chapter_10/filename.txt') as file_object: #文件路径中用正斜杠"/"
    contents = file_object.read()
    print(contents.rstrip())
##绝对文件路径: 在相对路径行不通时，可使用绝对路径
file_path = 'C:/Users/QianYus/OneDrive/#Python 0726/Python_Learning/Python_KT/chapter_10/filename.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#   10.1.3 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object: #将一个表示文件及其内容的对象存储到了变量file_object中
    for line in file_object:
        print(line)
#   10.1.4　创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #方法readlines() 从文件中读取每一行，并将其存储在一个列表中
for line in lines:
    print(line.rstrip())
#   10.1.5 使用文件的内容
##使用圆周率的值
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
"""变量pi_string用于存储圆周率的值"""
pi_string = ''
"""我们使用一个循环将各行都加入pi_string"""
for line in lines: 
    """strip() rstrip()删除每行末尾的换行符"""
    pi_string += line.rstrip()
"""打印这个字符串及其长度"""
print(pi_string)
print(len(pi_string))
#   10.1.6 包含一百万位的大型文件
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
"""只打印到小数点后50位,以免终端为显示全部1 000 000位而不断地翻滚"""
print(pi_string[:52] + "...")
print(len(pi_string))
#   10.1.7　圆周率值中包含你的生日吗
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
"""将生日表示为一个由数字组成的字符串: birthday"""
birthday = input("Enter your birthday, in the form mmddyy: ")
"""检查birthday是否包含在pi_string中"""
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
#10-1 Python学习笔记 ：在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。将这个文件命名为learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。
#编写一个程序，它读取这个文件，并将你所写的内容打印三次：
#第一次打印时读取整个文件；
filename = 'chapter_10\learning_python.txt'
with open (filename) as file_object:
    contents = file_object.read()
    print(contents)
# 第二次打印时遍历文件对象；
filename = 'chapter_10\learning_python.txt'
with open (filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#第三次打印时将各行存储在一个列表中，再在with代码块外打印它们。
filename = 'chapter_10\learning_python.txt'
with open (filename) as file_object:
    lines = file_object.readlines()
learning_python = ''
for line in lines:
    learning_python += line
print(learning_python)
# 10-2 C语言学习笔记 ：可使用方法replace() 将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的'dog' 替换为'cat'：
message = "I really like dogs."
message.replace('dog', 'cat') #'I really like cats.'
# 读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。
filename = "chapter_10\learning_python.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python', 'GoLang'))



#   10.2　写入文件
##  10.2.1　写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object: #第一个实参也是要打开的文件的名称；第二个实参（'w' ）告诉Python，我们要以写入模式 打开这个文件。
    file_object.write("I love programming.")
##  10.2.2　写入多行

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n") ##要让每个字符串都单独占一行，需要在write() 语句中包含换行符：\n
    file_object.write("I love creating new games.\n")
##  10.2.3　附加到文件
filename = 'programming.txt'
with open(filename, 'a') as file_object: #通过实参'a' 将内容附加到文件末尾
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
#10-3 访客 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
file = "chapter_10/10-3.txt"
with open (file, "a") as file_object: #记得实参"a"
    name = input("Please type your name:")
    file_object.write(name)
#10-4 访客名单 ：编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
file = "chapter_10/10-4.txt"

while True:
    name = input("Please type your name:")   
    if name == "quit":
        break
    else:
        with open(file, "a") as file_object:
            file_object.write(name+'\n')
            file_object.write('hello ' + name+'\n')
#10-5 关于编程的调查 ：编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
##我的答案
file = "chapter_10/10-5.txt"
while True:
    query = input("Why do you like programming? ")
    if query == "quit":
        break
    else:
        with open(file, "a") as file_object:
            file_object.write(query.title() + "\n")
##CSDN的答案
filename = 'guest_book.txt'
responses = []

while True:
    answer = input("你为何爱编程")
    responses.append(answer)
    
    poll = input("Would you like to let someone else respond? (y/n)")
    if poll != 'y':
        break
with open(filename,'a') as f:
    for answer in responses:
        f.write(answer +'\n' )



#   10.3　异常
#   10.3.1　处理ZeroDivisionError 异常
print(5/0)
#   10.3.2　使用try-except 代码块
#编写一个try-except 代码块来处理可能引发的异常
try:
    print(5/0)
except ZeroDivisionError: #try 代码块中的代码引发了ZeroDivisionError异常
    print("You can't divide by zero!")
#   10.3.3　使用异常避免崩溃
##这个程序没有采取任何处理错误的措施，因此让它执行除数为0的除法运算时，它将崩溃traceback
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'quit':
        break
    second_number = input("Second number: ")
    if second_number == 'quit':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
#   10.3.4　else 代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'quit':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: #处理用户无效输入
        print("You can't divide by 0!") #提示用户提供有效输入
    else: #依赖于try 代码块成功执行的代码都应放到else 代码块
        print(answer)
#   10.3.5　处理FileNotFoundError 异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
#   10.3.6　分析文本
filename = 'alice.txt' #童话 Alice in Wonderland
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
#10.3.7　使用多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
    # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] #将要分析的文件的名称存储在一个列表
count_words(filename)
#   10.3.8　失败时一声不吭
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass #pass语句 可在代码块中使用它来让Python什么都不要做
    else:
    # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
#   10.3.9　决定报告哪些错误
##编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只要程序依赖于外部因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常

#10-6 加法运算 ：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发TypeError 异常。
# 编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
try:
    a = int(input("Please input first numbers: "))
    b = int(input("Please input second numbers: "))
    
except ValueError:
    print("Please enter the vaild number!")
else:
    sum = a + b
    print(sum)
#10-7 加法计算器 ：将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
while True:
    try:
        a = input("Please input first numbers: ")
        if a == "q":
            break
        else:
            a = int(a)
        b = input("Please input second numbers: ")
        if a == "q":
            break
        else:
            b = int(b)
    except ValueError:
        print("Please enter the vaild number!")
    else:
        sum = a + b
        print(sum)
#10-8 猫和狗 ：创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地方，并确认except 代码块中的代码将正确地执行。
#10-9 沉默的猫和狗 ：修改你在练习10-8中编写的except 代码块，让程序在文件不存在时一言不发。
file_cat = "chapter_10/cats.txt"
file_dog = "chapter_10/dogs.txt"

# with open (file_cat, "w") as file_object:
#     three_cats = file_object.write("Miao, Piao, Giao")
try:
    with open(file_cat, "r") as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    print("The file is not found!")

# with open (file_dog, "w") as file_object:
#     three_dogs = file_object.write("Beibei, Lele, Xixi")
try:
    with open(file_dog, "r") as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    pass
    #print("The file is not found!")

#10-10 常见单词 ：访问项目Gutenberg（http://gutenberg.org/），并找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。你可以使用方法count() 来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row' 在一个字符串中出现了多少次：
# line = "Row, row, row your boat"
# line.count('row')
# line.lower().count('row')
#请注意，通过使用lower() 将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。
# 编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the' 在每个文件中分别出现了多少次。
with open ("chapter_10/The Kobzar of the Ukraine.txt", "r", encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents[:100]+"...")
    print(contents.lower().count('the'))

#   10.4　存储数据
#   10.4.1　使用json.dump() 和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'chapter_10/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj) #要存储的数据以及可用于存储数据的文件对象

import json
filename = 'chapter_10/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
#   10.4.2　保存和读取用户生成的数据
import json
"""我们提示输入用户名"""
username = input("What is your name? ")
"""并将其存储在变量filename中"""
filename = 'username.json'
"""调用json.dump() ，并将用户名和一个文件对象传递给它，从而将用户名存储到文件中"""
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    """打印一条消息，指出我们存储了他输入的信息"""
    print("We'll remember you when you come back, " + username + "!")
"""向其名字被存储的用户发出问候"""
with open(filename) as f_obj:
    """将存储在username.json中的信息读取到变量username 中"""
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

#尝试从文件username.json中获取用户名: 因此我们首先编写一个尝试恢复用户名的try-except代码块。如果username.json不存在，我们就在except代码块中提示用户输入用户名，并将其存储在username.json中
import json
# 如果以前存储了用户名，就加载它否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj) #将用户名读取到内存中
except FileNotFoundError: #用户首次运行这个程序时，文件username.json不存在，将引发FileNotFoundError 异常
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:#提示用户输入其用户名
        json.dump(username, f_obj)#再使用json.dump() 存储该用户名
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!") #打印一条欢迎用户回来的消息
#10.4.3　重构： 将代码划分为一系列完成具体工作的函数
##源代码：
import json
def greet_user(): 
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
greet_user()
##重构greet_user() ，让它不执行这么多任务。
import json
def get_stored_username(): #为此，我们首先将获取存储的用户名的代码移到另一个函数中：
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    """问候用户，并指出其名字"""
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")     
greet_user()
##重构greet_user()，将 没有存储用户名时提示用户输入的代码 放在一个独立的函数get_new_username()中：(要编写出清晰而易于维护和扩展的代码，这种划分工作必不可少)
import json
def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username() 
    if username:
        print("Welcome back, " + username + "!") #欢迎老用户回来
    else: #get_stored_username() 返回None
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")  #问候新用户
def get_stored_username(): #这个函数只负责获取存储的用户名（如果存储了的话）
    """如果存储了用户名，就获取它"""
    filename = 'chapter_10/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():  #这个函数只负责获取并存储新用户的用户名
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'chapter_10/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
greet_user()
#10-11 喜欢的数字 ：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”。
import json
filename = "chapter_10/10-11.json"
likednumber = input("Please type in your favourite number: ")
with open(filename, "w") as file_obj:      
    json.dump(int(likednumber), file_obj)
    print("Liked number saved!")
with open(filename, "r") as file_obj:
    json.load(file_obj)
    print("I know your favorite number! It's " + likednumber + ".")
#10-12 记住喜欢的数字 ：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
import json
filename = "chapter_10/10-11.json"
try:
    with open(filename, "r") as file_obj:
        likednumber = json.load(file_obj)       
except FileNotFoundError:
    with open(filename, "w") as file_obj:
        likednumber = input("Please type in your favourite number: ")      
        json.dump(int(likednumber), file_obj)
        print("Liked number saved!")
else:
    print("I know your favorite number! It's " + str(likednumber) + ".")
#10-13 验证用户 ：最后一个remember_me.py版本假设用户要么已输入其用户名，要么是首次运行该程序。我们应修改这个程序，以应对这样的情形：当前和最后一次运行该程序的用户并非同一个人。
#为此，在greet_user() 中打印欢迎用户回来的消息前，先询问他用户名是否是对的。如果不对，就调用get_new_username() 让用户输入正确的用户名。
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
        return username

def get_new_username():  #这个函数只负责获取并存储新用户的用户名
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'chapter_10/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user(): 
    """在greet_user() 中打印欢迎用户回来的消息前，先询问他用户名是否是对的"""
    username = get_stored_username() 
    if username: #确认是否有username
        ask = input(username + " is your name?(y/n)")
        if ask == 'y':
            print("Welcome back," + username + " !")#欢迎老用户回来
        else:
            username = get_new_username()#用户名不对，调用get_new_username() 让用户输入正确的用户名
            print("We'll remember you, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")  #问候新用户
greet_user()