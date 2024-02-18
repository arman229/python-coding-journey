def sum_find(x:int,y:int,oper:str,sign:str)->str:
    result = eval(f'{x} {sign} {y}')
    return f'{oper} of {x} and {y} is {result}'
calculater:str=sum_find(2,3,'sum','+')
print(calculater)
calculater2:str=sum_find(2,3,'multiplication','*')
print(calculater2)
calculater3:str=sum_find(2,3,'modulus','%')
print(calculater3)