# Method Resolution Order (MRO) in Python
# MRO is the order in which base classes are searched when executing a method.

class A:
    label = "Class A Label"

class B(A):
    label = "Class B Label"

class C(A):
    label = "Class C Label"

class D(B, C):
    pass

obj = D()
print(obj.label)  # Output: Class B Label

# Why B's label?
# Python uses C3 Linearization algorithm to determine the MRO.
# In simple terms, it follows the order of inheritance from left to right.
# So, when looking for 'label', it first checks class D, then B, then C, and finally A.

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# Explains the order in which classes are checked for attributes/methods.