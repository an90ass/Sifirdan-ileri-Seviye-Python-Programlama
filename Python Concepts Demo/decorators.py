def my_decorator(func):
    def wrapper(name):
        print('fonksiyondan once islemler')
        func(name)
        print('fonksiyondan sonra islemler')
    return wrapper
@my_decorator
def say_hello(name):# Asagidaki islemler ayni
    print("Hello",name)
def say_greeting():
    print("Greeting")
# say_hello = my_decorator(say_hello)
# say_greeting = my_decorator(say_greeting)
say_hello("Anas")
# # say_greeting()
########################################################################################################################

import math 
import time 
def calculate_time(func):
    def inner(*args,**kwargs):
     start = time.time()
     time.sleep(1)
     func(*args,**kwargs)
     finish = time.time()
     print("fonksiyon "+func.__name__+" "+str(finish-start)+" saniye sürdü.")
    return inner 
@calculate_time
def uslama(a,b):    
     print(math.pow(a,b)) 
@calculate_time
def factorial(num):
  print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

uslama(2,3)
factorial(5)
toplama(1,2)

