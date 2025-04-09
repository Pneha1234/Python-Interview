class A:
    pass
    # def show(self):
    #     print("A.show()")
    #     return self
class B(A):
    pass
    # def show(self):
    #     print("B.show()")
    #     return self
class C(A):
    pass
    # def show(self):
    #     print("C.show()")
    #     return self
class D(B, C):
    pass
    # def show(self):
    #     print("D.show()")
    #     return self
d =D()
d.show()