#Parent class
class Above:
    i=5
    def fun1(self):
        print('hey there, you are in the parent class.')

#sub class
class Below(Above):
    i=10
    def fun2(self):
        print('Hey there, you are in the child class')

temp1=Below()
temp2=Above()
temp1.fun1()
temp1.fun2()
temp2.fun1()

print(temp1.i)
print(temp2.i)