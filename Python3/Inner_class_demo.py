class Outer:
    def __init__(self):
        print("Outer class Object Creation...")
    class Inner:
        def __init__(self):
            print("Inner class Object Creation...")
        def m1(self):
            print("Inner class Method")
            
o=Outer() # Outer object created, 
i=o.Inner() # Inner object creation, As it is a part of outter object we cant directly create inner object.. 
i.m1()    # calling instance method of inner class