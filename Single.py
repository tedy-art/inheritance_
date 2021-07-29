class Parent:
    def func1(self):
        print('This function is in parent class.')

class Child(Parent):
    def func2(self):
        print('This function is in child class.')

ob=Child()
ob.func1()
ob.func2()