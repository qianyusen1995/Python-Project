class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def  increment_login_attempts(self):
        self.login_attempts += 1
        print (self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print (self.login_attempts)

    def describe_user(self):
        print ("The name of the user is " + self.first_name.title() + " " + self.last_name.title() + ".")

    def greet_user(self):
        print ("Welcome to Shanghai! " + self.last_name.title()+ ".")

class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print (self.privileges)