class Test:
    a = 10

    def __init__(self):
        Test.d = 80

    def m1(self):
        Test.e = 90

    @classmethod
    def m2(cls):
        cls.g = 55
        Test.h = 14

    @staticmethod
    def m3():
        Test.kk =11


t = Test()
print(t.__dict__)  # {}
print("------------------------")
print(
    Test.__dict__)  # {'__module__': '__main__', 'a': 10, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
t.m1()
print("***********************************")
print(Test.__dict__)

print("***********class method ************************")
Test.m2()
print(Test.__dict__)

print("************static method***********************")
Test.m3()
print(Test.__dict__)
Test.j = 10
print("************outside of the class***********************")
print(Test.__dict__)
