class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to ",self.name,self.lastname,"'s cart")
    
customer1 = Customer()
customer1.name = "Artitaya "
customer1.lastname = "Yaemjaraen"
# เรียกใช้ ฟังก์ชันผ่านตัวแปร customer1
customer1.addCart()

customer2 = Customer()
customer2.name = "B"
customer2.lastname = "C"
customer2.addCart()

customer3 = Customer()
customer3.name = "D"
customer3.lastname = "E"
customer3.addCart()
