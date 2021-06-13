class Vehicle :
    licenseCode = ""
    serialCose = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Car(Vehicle) :
    # ฟังก์ชันที่สร้างใหม่ จะไม่เกี่ยวกับฟังก์ชันในคลาสหลัก
    def sayHello(self):
        print("Hello World")
class Pickup(Vehicle):
    def say(self):
        print("I'm Pickup")
class Van(Vehicle):
    def say(self):
        print("I'm van")

car1 = Car()
# ฟังก์ชันที่อยู่ในคลาสหลัก
car1.turnOnAirConditioner()
# ฟังก์ชันที่อยู่ในคลาสย่อย
car1.sayHello()

pickup = Pickup()
pickup.turnOnAirConditioner()
pickup.say()

van = Van()
van.turnOnAirConditioner()
van.say()
