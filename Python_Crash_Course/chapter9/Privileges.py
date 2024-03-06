class Privileges():
    def __init__(self,privileges=[]) -> None:
        self.privileges=privileges
    def show_privileges(self):
        if self.privileges:
            for pre in self.privileges:
                print(pre)
        else:
            print('there is no priviliges') 