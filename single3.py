class Parent_class(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id

    #to fetch employee details
    def Employee_detials(self):
        return self.id,self.name

    #to check employee id valid or not
    def Employee_check(self):
        if self.id>500000:
            return "Valid Employee"
        else:
            return "INvalid Employee"

#derived class or sub class
class child_class(Parent_class):
    def End(self):
        print("END OF PROGRAM")

#driver code
emp1=Parent_class("Employee1",600445)
print(emp1.Employee_detials(),emp1.Employee_check())

emp2=child_class("Employee2",198754)
print(emp2.Employee_detials(),emp2.Employee_check())