class Test:
    def __init__(self):

        self.a =10
        self.b =20

    def print_name(self):
        print("hello from print name function")
   # declaring the instance variable inside the instance method

    def m1(self):
        self.c = 30

t = Test()
print(t.__dict__) # {'a': 10, 'b': 20}

print("--------------------------------------------")

t.m1()

print(t.__dict__) # {'a': 10, 'b': 20, 'c': 30}
print("========================================")
t.d = 40



print(t.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}, new instance variable d will be added to the object
