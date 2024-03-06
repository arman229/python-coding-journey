from user_class import User
from Privileges import Privileges
class Admin(User):
    def __init__(self,first_name:str,last_name:str,age:int,height:float)->None:
        super().__init__(first_name,last_name,age,height)
        self.privileges=Privileges()