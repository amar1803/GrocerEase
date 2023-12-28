#gs_ms - Grocery Store Management System

prdt =[]                                        #list storing the name of products customer bought
amnt = []                                       #list storing the quantity of products customer bought
prce =[]                                        #list storing the price of products customer bought
class gs_ms:
    def __init__(self,available,quantity,items):   #intiation function
      self.available = available                   #declaring class dict. available
      self.quantity = quantity                     #declaring class list quantity
      self.items = items                           #declaring class variable items
  
    def purchase(self,j):                         # function checking the availablity of item and computing total cost
        print(j+1,"PRODUCT")                      #displaying the sr. no of product
        pro = input("Enter the name of product u want to buy ") #asking for name of product to be bought
        price = 0                                 #intialising price variable
        flag1 = 0                                 #intialising flag1 variable
        flag2 = 0                                 #intialising flag2 variable
        for i in range(self.items):
           if pro == self.available[i+1][0] :     #comparing the product enetred by costumer in the available list
                flag1 = 1                         #updating flag1 as product is found
                amount = eval(input("Enter the quantity of product ")) #asking for quantity of product
                if amount <= self.quantity[i]:                   #checking the quantity
                    flag2 = 1                                    #updating flag2 as quantity can be provided 
                    self.quantity[i] = self.quantity[i] - amount #decreasing the quantity after sale
                    price = (price + self.available[i+1][1])*amount #calculating cost 
                    prdt.append(pro)                #adding name of bought product to prdt list 
                    amnt.append(amount)             #adding quantity of bought product to amnt list 
                    prce.append(price)              #adding price of bought product to prce list 
                              
        if(flag1!=1):                               #checking whether name is found in the list or not
           print("Entered Product is not available ")
        if(flag2!=1):                               #checking whether asked quantity is provided or not
           print("This quantity is not available ")
        print("Cost = ",price,"\n")
       
    def remaining(self):                             # display the remaining quantities
        print("Now Available Quantities are")
        print("PRODUCTS",'PRICE','QUANTITY',sep=' ') #print column name as product price quantity
        for i in range(self.items):
             print(self.available[i+1][0],self.available[i+1][1],self.quantity[i],sep='  ')#displaying data in tabular form
        print("\n")                                     
    def bill(self,prdt,amnt,prce):                   # display the bill 
        total = 0                                    # intialising the total cost to be paid = 0
        print("Sr No.","Product","Quantity","Price",sep='  ')  #print column name as srno product quantity price
        for i in range (len(prdt)):
            print(i+1,prdt[i],amnt[i],prce[i],sep='      ')     #displaying data in tabular form   
        for ele in range(len(prce)):                            #for calculatig total bill
            total = total + prce[ele]                           #adding the elements of list prce
        print("Total Amount to be paid = ",total)               #displaying total bill
    
class owner:                                                    #class only for user
    def __init__(self,available,quantity,items):                #intiation function
      self.available = available                                #declaring class dict. available
      self.quantity = quantity                                  #declaring class list quantity
      self.items = items                                        #declaring class variable items
    def add(self):                                              #will add the product in list and dict.
        key = input("Enter the name of product u want to add ") #name of new product
        value = eval(input("Enter the price of product "))      #price of new product
        number = eval(input('Enter the quantity of product '))  #available quantity of product
        q = len(available)
        check = 0
        for i in range (self.items):
            if self.available[i+1][0] == key:
                check=1
                self.available[i+1][1] = value
                self.quantity[i] = self.quantity[i] + number
        if check == 0:
            self.available[q+1] = [key,value]                       #appending items
            self.quantity.append(number)                            #appending quantity
            self.items = self.items + 1 
                                    #increasing number of items by 1
    def display(self):                                          #will display available products in tabular form
         print("PRODUCTS",'PRICE','QUANTITY',sep=' ')
         for i in range(self.items):
             print(self.available[i+1][0],self.available[i+1][1],self.quantity[i],sep='  ')
         print("\n")
         
def show():                                                     #will display available products in tabular form                         
     print("PRODUCTS",'PRICE','QUANTITY',sep=' ')
     for i in range(items):
        print(available[i+1][0],available[i+1][1],quantity[i],sep='  ')
     print("\n")

print("Welcome to our grocery \n")             #welcome quote
available = {1: ['Salt',50], 2: ['Sugar',60], 3:['Tea_leaves',40], 4: ['Detergent',100],
             5:['Cereal',150],6:['Bread',35], 7:['Oil',65]} #dict. of available items
quantity = [5,7,3,2,8,1,4]                     # list storing quantity related to available items
items = len(available)                         #storing total number of items available

ask = input('Are you a customer or owner ');   #asking about the entity owner or customer
if ask[:] == "owner":                          #In the case of owner we proceed as follow
    pswd = eval(input("Enter the password "))  #the owner can set the  password default taken as 1234
    if pswd == 1234:                           #if the correct password is entered then infomation can be proceed further
       show()                                  #show() displaying the available items present in the store      
       o = owner(available,quantity,items)     #o object is created of class owner
                                               #we are providing two functionality to the owner

       o.add()                                 # 1st is to add the item
       o.display()                             # 2nd is to display the items
elif ask[:] == "customer":                     #In the case of owner we proceed as follow
    show()                                     #show() displaying the available items present in the store
    g = gs_ms(available,quantity,items)         #g object is created of class gs_ms
    n = eval(input('Enter the number of products u want to buy ')) #asking user total product customer want to buy
    for i in range(n):                          # loop for the number of products customers buys
        g.purchase(i)                           # function for all the necessery steps of purchasing product
        g.remaining()                           #function display the remaining quantity left after purchasing a item
    g.bill(prdt,amnt,prce)                      #will display the final bill of customer
else:
    print("Wrong Input")                       #In case user entered anything except owner and customer
    
