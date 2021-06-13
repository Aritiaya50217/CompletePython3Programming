class Animal():
    def eat(self):
        print("Eating Eating !! ")

class Cat(Animal):
    # การใช้ overriding
    def eat(self):
        print("Meowwww")

cat1 = Cat()
cat1.eat()

animal1 = Animal()
animal1.eat()

