class Mamal :
    def walk(self):
        print("I walk ")

class Cat(Mamal):
    def anyoning(self):
        print("I am anyoning")

class Dog(Mamal):
    def park(self):
        print("I am Park ")


dog1=Dog()
dog1.walk()
dog1.park()