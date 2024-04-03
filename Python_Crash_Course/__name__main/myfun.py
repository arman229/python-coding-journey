def MyName(name:str)->str:
    return name.capitalize()
def Age(age:int)->str:
    return f'my age is {age} years old'
print(f'Please note that the value of the name is {__name__} in myfun.py and index.py when we run these scripts')
def main():
    print(MyName('james'))
    print(Age(20))
if __name__ == '__main__':
    main()