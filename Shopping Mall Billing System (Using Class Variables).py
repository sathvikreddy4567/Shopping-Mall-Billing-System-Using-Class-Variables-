#creating a class name shopping mall
class shoppingmall:
    #displaying the customers
    total_customers=0  #net customers is 0
    #made a function 
    def __init__(self,name):
        self.name=name
        self.items=[]
        self.total_amount=0
        
        shoppingmall.total_customers+=1
     #function to add item details    
    def add_item(self,item,price):
        self.items.append(item)
        self.total_amount+=price
        #function to generate the bill to the user 
    def print_bill(self):
        print(f"\nCustomer: {self.name}")
        print("Items Purchased:", self.items)
        print("Total Amount:", self.total_amount)
        
#created customers history    
c1=shoppingmall('sathvikreddy')
c1.add_item('Blazzer',5000)
c2=shoppingmall('Mahesh')
c2.add_item('Shirt linen',5000)
c2.add_item('Linen trouser',3000)
c2.add_item('Bellavita perfume',699)
#print statements to perform operations 
c1.print_bill()
print(c2.items)
print("Total customers visited :",shoppingmall.total_customers)