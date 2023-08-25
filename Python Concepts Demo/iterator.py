liste = [1,2,3,4,5]
iterator = iter(liste)

# print(next(iterator))#1
# print(next(iterator))#2
# print(next(iterator))#3
# print(next(iterator))#4
# print(next(iterator))#5

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
print("**********************************************************************************************************************")
class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            s = self.start
            self.start+=1
            return s
        else:
            raise StopIteration
list =MyNumbers(15,20)
myiter = iter(list)
# print(next(myiter))
# print(next(myiter))
# for i in list:
#     print(i)
while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break