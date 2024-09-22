class Addition():
    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2

    def addition(self, addition1, addition2):
        self.variable1 += addition1
        self.variable2 += addition2

class Multiplication():
    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2

    def multiplication(self, multiplication1, multiplication2):
        self.variable1 *= multiplication1
        self.variable2 *= multiplication2

x = 2

if x == 1:
    x = Addition(2,2)
    x.addition(2,2)
    print(x.variable1, x.variable2)
else:
    x = Multiplication(4,4)
    x.multiplication(2,2)
    print(x.variable1, x.variable2)

print('\n')

def currency(a,b):
    result = a * b
    return result

print(
    currency(20,4.50)
)