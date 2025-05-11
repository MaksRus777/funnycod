
class MyClass:
    some_int = 15

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        print(self.sqr_norm(val1,val2))
    @staticmethod
    def sqr_norm(a, b):
        return a*a + b*b
    def sqr_normself(self,a, b):
        return a*a + b*b
    
print(MyClass.sqr_norm(3,3))
print(MyClass(1,2).sqr_normself(2,3))

print(MyClass.sqr_normself(2,3))



