print(" \n read all the code below and look at the outputs to undrestand how data is being handled in python and then u can have better underestanding of the python language \n")

# varibales in python 

x = 2 
y = "hello world"
print("1- ",x)
print("2- ",y)

# data structures in python 
# 1- lists   2- dictionary
print("================================================================")

list = [1, "hello world", 999, [22, "hello world"]]

print("3- " ,list)
print("4- " ,list[0])
print("5- ",list[1])
print("6- ",list[3])
print("7- ",list[3][1])

dictionary = { 1 : "hello world", "text": "hi how u doin", "number": 9999, 555:999,
              "list": [1, 2, 3, "hellow world"],
              "dictionary": {"text": "dict inside dict is posibale", "number": 999999999}}

print("8- ",dictionary[1])
print("9- ",dictionary["text"])
print("10- ",dictionary["number"])
print("11- ",dictionary["list"])
print("12- ",dictionary["list"][0])
print("13- ",dictionary["list"][1])
print("14- ",dictionary["dictionary"])
print("15- ",dictionary["dictionary"]["text"])
print("16- ",dictionary["dictionary"]["number"])



# types in python
print("================================================================")

string = "hello world"
number = 123
float = 123.5
boolean1 = True
boolean2 = False

print("17- ", string)
print("18- ", number)
print("19- ", float)
print("20- ", boolean1)
print("21- ", boolean2)


# if statment in python
print("================================================================")
variable = True

if variable == True:
    print("the condition is true")
    print("if that variable with the type of boolean was True this sentence will be printed if it was False it wouldnt get printed")
    
else: 
    print("the condition is False")
    print("vaiable was False")
    
    
z = 499

if z >= 500:
    print("z is higher than 500 or equal to 500")
    
else: 
    print("z is not higher than 500 or equal to 500")
    
    
    
print("================================================================")

# loops in python
print("\n var will be printed 10 times and every time will increase by 1 \n")
var = 1
for i in range(10):
    
    print(var)
    
    var = var + 1
    


print(" \n looping throw a lists variables \n")
test_list = [ 1, 2, 3, "3rd index of list", "4th index of list", "5th index of list"]
for c in test_list:
    
    print(c)
    


print("\n looping throw dict keys and values \n ")
test_dict = {1: "hello world", 2: "this is a dictionary", "number": 999, "random number": 785765765675675, "simple text": "hello how are u"}

for x,y in test_dict.items():
    
    print(x, y)
    


# while loop
print("\n loop will continue until the condition become false it means that h become more that 20 \n")
h = 0
while h < 20:
    
    print(h)
    h = h + 1
    

print("\n change while condition from inside the loop \n ")
p = True
k = 10
while p:
    print(k)
    k = k + 1
     
    if k == 30:
        p = False
    
    
# try and except    
print("=======================================================")
try:
    #int(input("enter a number: "))
    print("try is working")
    
except:
    print("try didnt work")
    
    
# functions in python 
print("======================================================")
def nameOfTheFunction(variable1, variable2 ): # functions can get infinit variables

    print("hello world")
    print(variable1)
    print(variable2)
    

nameOfTheFunction(555,"hi whats your name")


# class in python
print("======================================================")
class NameOfTheClass:
    
    x = 1
    y = 5
    text = "hello world"
    
    def __init__(self, number, list):
        self.number = number
        self.list = list
        
    
    def first(self):
        print("first")
        
    def second(self):
        print("second")
        
    def hello_world(self):
        print(self.text)
        
    def forth(self):
        print("number : ",self.number)
        print("list :" ,self.list)
        
    
    # u can have infinit functions in a class
    
    
class_var = NameOfTheClass(number=98989545652, list=[1,3,3, "hi how are u"])

class_var.first()

class_var.second()

class_var.hello_world()

class_var.forth()


print("================================================================")


    
    
