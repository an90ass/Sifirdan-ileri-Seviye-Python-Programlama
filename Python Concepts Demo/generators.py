def cube():
    for i in range(5):
        yield i**3

# genarator = cube() 
# iterator = iter(genarator)
# while True:
#    try:
#       result =next(iterator)
#       print(result)
#    except StopIteration:
#         print("Hata")

# print(next(iterator))  
# print(next(iterator))    
# print(next(iterator)) 
# print(next(iterator))   
for i in cube():
    print(i)
       
  