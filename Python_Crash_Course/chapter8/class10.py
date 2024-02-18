# Lambda Function
# from typing import Callable
# add:Callable[[int,int],int] = lambda x,y:x+y
# result=add(2,3)
# print(result)
from typing import Dict
# Using Arbitrary Keyword Arguments
def my_decorator(func):
    def wrapper(num):
        print("Adding 10 to the number...")
        func(num)
        print("Finished adding 10.")
    return wrapper

@my_decorator
def add_ten(num):
    result = num + 10
    print("Result:", result)
add_ten(5)

 