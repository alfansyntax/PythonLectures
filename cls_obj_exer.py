# Create an online store for products like phones,laptops where name and price will taken
# Track total products being created
# Create a static method to calculate discount
class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1
    def get_info(self):
        print(f"{self.name} has a price of {self.price}")
    @classmethod
    def get_track(cls):
        print(f"Total products in store is {cls.count}")
    @staticmethod
    def cal_disc(price,off):
        offer_price=price-(off*price/100)
        print(f"The offer price for is {offer_price}")
p1=Product("Laptop",75_000)
p2=Product("Phone",30_000)
p3=Product("Computer",100_000)
p1.get_info()
p2.get_info()
p1.cal_disc(p1.price,10)
Product.get_track()    
print("--------------------------------------------------------------------------------------------------")

# Create a bank account with name,acc number,balance.Add methods to withdraw,deposit and check balance.
class Bank:
    def __init__(self,name,acc,bal):
        self.name=name
        self.acc=acc
        self.bal=bal
    def deposit(self,deposit):
        self.bal=self.bal+deposit
        print(f"New balance of {self.name} after depositing is {self.bal}")
    def withdraw(self,withdraw):
        if(withdraw>self.bal):
            print("Insufficient Balance.")
        else:
         self.bal=self.bal-withdraw
         print(f"New balance of {self.name} after withdrawing is {self.bal}")
    def get_info(self):
        print(f"Account Name   : {self.name}")
        print(f"Account Number : {self.acc}")
        print(f"Account Balance: {self.bal}")

b1=Bank("Alfan",2422,30_000)
b1.deposit(10_000)
b1.withdraw(50_000)
b1.withdraw(5000)
b1.get_info()
        

