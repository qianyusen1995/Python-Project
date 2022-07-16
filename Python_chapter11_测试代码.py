#   11.1　测试函数
#   11.1.1　单元测试和测试用例
# Python标准库中的模块unittest 提供了代码测试工具。单元测试 用于核实函数的某个方面没有问题；测试用例 是一组单元测试，这些单元测试一起核实函数在各种情形下的
# 行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。全覆盖式测试 用例包含一整套单元测试，涵盖了各种可能的函数使用方
# 式。对于大型项目，要实现全覆盖可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。
#   11.1.2　可通过的测试
import unittest
from chapter_11.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #用于包含一系列针对get_formatted_name() 的单元测试
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
unittest.main()

#   11.1.3　不能通过的测试
import unittest
from chapter_11.name_function2 import get_formatted_name

class NamesTestCase(unittest.TestCase): #用于包含一系列针对get_formatted_name() 的单元测试
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
unittest.main()
#   11.1.4　测试未通过时怎么办
import unittest
from chapter_11.name_function3 import get_formatted_name

class NamesTestCase(unittest.TestCase): #用于包含一系列针对get_formatted_name() 的单元测试
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')     
unittest.main()
#   11.1.5　添加新测试
import unittest
from chapter_11.name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function.py """
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
    unittest.main()
#11-1 城市和国家 ：编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City, Country 的字符串，如Santiago, Chile。将这个函数存储在一个名为city_functions.py的模块中。
def city_functions(cityname, countryname):
    formatted_name = cityname + " " + countryname
    return formatted_name.title()
#创建一个名为test_cities.py的程序，对刚编写的函数进行测试（别忘了，你需要导入模块unittest以及要测试的函数）。编写一个名为test_city_country() 的方法，核实使用类似于'santiago' 和'chile' 这样的值来调用前述函数时，得到的字符串是正确的。运行test_cities.py ，确认测试test_city_country() 通过了。
import unittest
from chapter_11.city_functions import city_functions

class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        formattedname = city_functions("santiago", "chile")
        self.assertEqual(formattedname, "Santiago Chile")
unittest.main()
#11-2 人口数量 ：修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为City, Country - population xxx 的字符串，如Santiago, Chile - population 5000000 。运行test_cities.py，确认测试test_city_country() 未通过。
#修改上述函数，将形参population设置为可选的。再次运行test_cities.py，
def city_functions(cityname, countryname, population = ""):
    if population:#population不为空字符串
        formatted_name = cityname + " " + countryname + " - population " + population
    else:#population为空字符串
        formatted_name = cityname + " " + countryname
    return formatted_name.title()
#确认测试test_city_country()又通过了。
import unittest
from chapter_11.city_functions2 import city_functions
class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        formattedname = city_functions("santiago", "chile")
        self.assertEqual(formattedname, "Santiago Chile")
    def test_city_country_population(self):
        """#再编写一个名为test_city_country_population() 的测试，核实可以使用类似于'santiago' 、'chile' 和'population=5000000' 这样的值来调用这个函数。再次运行test_cities.py, 确认测试test_city_country_population() 通过了。"""
        formattedname = city_functions("santiago", "chile", "5,000,000")
        self.assertEqual(formattedname, "Santiago Chile - population 5,000,000")
unittest.main()



#   11.2　测试类
##针对类的测试
#   11.2.1　各种断言方法
#   11.2.2　一个要测试的类
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
##为证明AnonymousSurvey 类能够正确地工作，我们来编写一个使用它的程序：
from chapter_11.survey import AnonymousSurvey
###定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
###显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
###显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

#   11.2.3　测试AnonymousSurvey 类
import unittest
from chapter_11.survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):#如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self): #核实用户提供三个答案时，它们也将被妥善地存储。为此，我们在TestAnonymousSurvey 中再添加一个方法：
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
unittest.main()

#   11.2.4　方法setUp()
import unittest
from chapter_11.survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

# 11-3 雇员 ：编写一个名为Employee 的类，其方法__init__() 接受名、姓和年薪，并将它们都存储在属性中。编写一个名为give_raise() 的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
class Employee:
    def __init__(self, fullname, surname, annualsalary):
        self.fullname = fullname
        self.surname = surname
        #self.name = self.fullname + "" + self.surname
        self.annualsalary = annualsalary
    
    def give_raise(self, raise_annualsalary=5000):
        return raise_annualsalary
#为Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和test_give_custom_raise() 。
#使用方法setUp() ，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.qian_yu_sen = Employee("Yusen", "Qian", 132000)
        self.qys_raises = [6000,7000]
        #self.qian_yu_sen_raised = Employee.give_raise(self.qys_raise)

    def test_give_default_raise(self):
        self.qian_yu_sen.give_raise()
        self.assertEqual(5000, self.qian_yu_sen.give_raise())

    def test_give_custom_raise(self):
        for qys_raise in self.qys_raises:
            self.qian_yu_sen.give_raise(self.qys_raises[0])
        for qys_raise in self.qys_raises:
            self.assertEqual(qys_raise, self.qian_yu_sen.give_raise(qys_raise))
            
unittest.main()