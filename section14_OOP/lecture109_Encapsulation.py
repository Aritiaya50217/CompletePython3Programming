from typing import Text


class Animal():
    def eat(self):
        print("Eating Eating !!")

class Cat(Animal):
    name = ""
    def setName(self,text):
        # Getter ฟังก์ชันที่จะดึงออกมาตรงๆ
        # setter ฟังก์ชันในการกำหนดค่า
        self.name = text
        print("Setting New Cat Name :",self.name)
    def eat(self):
        print("Meowwww",self.name)
    
cat1 = Cat()
cat1.name = "TT"

cat1.eat()

