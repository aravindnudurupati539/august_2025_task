#syntax
# def functioname():
    #function block of code
# functionname()

# def greet():#function definition
#     print("welcome to pythonlife")#function body
#     num_1 = 10 #function body
#     num_2 = 20 #function body
#     print(num_1+num_2) #function body
# greet()    



# def add():#function definition
#     num_1 = 10 #function body
#     num_2 = 5
#     print(num_1+num_2)
# add()#function definition


# def looping():
#     for i in range(10):
#         print(i)
# looping()

# for i in range(10):
#     print(i)


# def add(num_1,num_2): #function definition
#     print(num_1+num_2)
# add(40,20)#function calling , here 40 and 20 are the arguments(values)
# add(10,20)
# add(10,800)
# add(70,20)
# add(80,20)
# add(10,80)


# def add(num_1,num_2):
#     print(num_1+num_2)
# num_1 = int(input("enter the number: "))
# num_2 = int(input("enter the number2: "))
# add(num_1,num_2)
# add(num_1,num_2)




# def details(user=None,dept=None,id=None):
#     print(user,dept,id)
# details("vasu","fullstack",1234)
# details("raju","frontend",25849)
# details("srinu",)
# details()


# def discount(price,discount=10):
#     discount_amount = (price * discount )/100
#     final_price = price - discount_amount
#     print(final_price)
# discount(10000)
# discount(5000)
# discount(20000,20)


#arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)
# def sample(*a):#* --> all 
#     print(a)
# sample("pythonlife",5.7,25)

#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing

#**
# def sample(**a):
#     print(a)
# sample(a=10,b=20,c=30)

# * --> tuple
# ** --> dict


#variables ---> two types -->local variables ---> global variables
#1. local variables --> funtion (inside the function )
#2. global variables --> outside the function 


# def sample():
#     user = "rajesh"#local variables
#     id = 1234#local variables
#     print(user,id)
# sample()


# def add(num_3):
#     num_1 = 10
#     num_2 = 20
#     result = num_1 +num_2
#     print(result)
#     print(num_1*num_3)
#     num_1+=num_3
#     print(num_1)
# add(25)



# balance = 1000#global variable
# def credit(amount):
#     user = "vasu" #local variable
#     print(user)
#     print(amount)
#     print("inside funtion",balance)
# credit(5000)
# print(balance)

# balance = 1000#global variable
# def credit(amount):
#     global balance
#     print(f"amount credited {amount}")
#     balance += amount
#     print(f"total balance {balance}")
# credit(5000)

# print(balance)


# def add(n1,n2):
#     return n1+n2
# obj = add(25,25)

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)
# sub(10,5)
# sub(20,50)
# add(5,25)


# area = 40



# new changes done
age = 35
def voter():
    return age
voter()