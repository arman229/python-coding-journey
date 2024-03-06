class User:
    def __init__(self,first_name:str,last_name:str,age:int,height:float) -> None:
        self.firstName=first_name
        self.lastName=last_name
        self.age=age
        self.height=height
        self.login=0
    def describe_user(self)->str:
       return f'My name is {self.firstName}{self.lastName}. I am {self.age} old. and my height is {self.height} and login value is {self.login}'
    def greet_user(self)->None:
        print(f'Welcome back {self.firstName}')
    def increment_login_attempts(self)->None:
        self.login+=1
        print(self.login)   
    def reset_login_attempts(self)->None:
        self.login=0 