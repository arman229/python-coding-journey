
import myfun
def sum(x:int, y:int)->int:
    return x+y
def mult(x:int,y:int)->int:
    return x*y
print(sum(3,3))
print(mult(3,4))
# Note that when we call MyName function it call all the functions in the myfun but we only want to 
# call the MyName function this can be achive my using the __name__=__main__ 


#. If the script is directly executed by Python, the value of __name__ is set to "__main__". However, 
# if the script is imported as a module into another script, the value of 
# __name__ will be the name of the module instead of "__main__"
print(myfun.MyName('armna'))