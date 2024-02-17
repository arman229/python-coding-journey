# Using as to Give a Module an Alias
import multiplymodule as mult # Using as to Give a Module an Alias
from multiplymodule import * # Importing All Functions in a Module
# import summodule # all the funtion are imported
from summodule import max_fun# we can import module specfic
# If the name of a function you’re importing might conflict with an existing name
# in your program, or if the function name is long, you can use a
# short, unique alias—an alternate name similar to a nickname for the function.
from summodule import this_function_find_the_minimum_value_in_the_list as minfun
# sum_result=summodule.sum_fun(9,2,3,4,5)
# print(f'Import module for sum calculate {sum_result}')
max_result=max_fun(2,3,4,5)
print(f'Import module for max calculate {max_result}')
min_result=minfun(2,3,4,5)
print(f'Import module for min calculate {min_result}')
multiply=mult.mult_fun(5,2)
print(f'Multiply of two number {multiply}')
   
   
  


