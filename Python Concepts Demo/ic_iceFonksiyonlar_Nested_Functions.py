#encapsulation
def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1+1
    num2= inner_increment(num1) 
    print(num1,num2)
outer(10)       

#########################################
print("###################################################")
def factorial(number):
    if not isinstance(number,int):
      raise TypeError("number must be an integer")
    if not number >=0:
       raise ValueError("number must be zero or positive")
 
    def inner_factorial(number):
     if  number ==1 or number ==0:
        return 1 
     
     return number * inner_factorial(number -1)
     
    return inner_factorial(number)
try:
 factorial =  factorial(0)
 print(factorial)

except Exception as ex:
   print(ex)
               