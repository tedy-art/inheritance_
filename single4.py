class Parent_class(object):
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2

    #Perform Addition
    def Addition(self):
        print("Addition value 1 :",self.value1)
        print("Addition value 2 :",self.value2)
        return self.value1+self.value2

    #Perform Multiplication
    def Multiplication(self):
        print("Multiplication value 1 :",self.value1)
        print("Multiplication value 2 :",self.value2)
        return  self.value1*self.value2

    #Perform substraction
    def Substraction(self):
        print("Substraction value 1 :",self.value1)
        print("Substraction value 2 :",self.value2)
        return self.value1-self.value2

#child class/Derived class/sub class
class child_class(Parent_class):
    pass

ob1=child_class(10,15)
print("Added value: ",ob1.Addition())
print(" ")

ob2=child_class(20,30)
print("Multiplied value: ",ob2.Multiplication())
print(" ")

ob3=child_class(50,30)
print("Substraction :",ob3.Substraction())