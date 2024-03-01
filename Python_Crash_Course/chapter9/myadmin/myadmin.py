
class User:
    def __init__(self,first_name:str,last_name:str,age:int,height:float) -> None:
        self.firstName=first_name
        self.lastName=last_name
        self.age=age
        self.height=height
        self.login=0
    def describe_user(self):
        print(f'My name is {self.firstName}{self.lastName}. I am {self.age} old. and my height is {self.height} and login value is {self.login}') 
    def greet_user(self):
        print(f'Welcome back {self.firstName}')
    def increment_login_attempts(self):
        self.login+=1
        print(self.login)   
    def reset_login_attempts(self):
        self.login=0     
class Admin(User):
    def __init__(self,first_name:str,last_name:str,age:int,height:float)->None:
        super().__init__(first_name,last_name,age,height)
        self.privileges=Privileges()
class Privileges():
    def __init__(self,privileges=[]) -> None:
        self.privileges=privileges
    def show_privileges(self):
        if self.privileges:
            for pre in self.privileges:
                print(pre)
        else:
            print('there is no priviliges')        
