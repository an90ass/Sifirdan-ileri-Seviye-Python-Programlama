#class
class Person:
    #class attributes
      adress = 'No information'

    #constructor
    #object attributes
      def __init__(self,name,year):
            self.name = name
            self.year= year
            # print("init metodu calisti")

    # instance methods
      def intro(self):  
            print('Hello There. I am '+self.name)
      def claculateAge(self):
            return 2023 - self.year    
#object(instance)
p1 = Person(name ='Anas',year = 2002,)
p2 = Person(name ='Eskander',year = 1999)
# updating 
p2.name = 'Mohammed'
p1.adress='Bartin'
#accessing object attributes
# print(f'p1: name : {p1.name}, year : {p1.year}, adress : {p1.adress}')
# print(f'p2: name : {p2.name}, year : {p2.year}, adress : {p2.adress}')

p1.intro()
p1_age = p1.claculateAge()

print(f'p1: Adim {p1.name} Yasim: {p1_age}')
print(f'p1: Adim {p2.name} Yasim: {p2.claculateAge()}')

################################################################################################
print('#######################################################################################')
class Circle():
      pi = 3.14

      def __init__(self,yaricap=1):
        self.yaricap = yaricap

      def cevre_hesapla(self):
           return 2 * self.pi + self.yaricap
      def alan_hesapla(self):
           return self.pi * (self.yaricap**2)
      
c1 = Circle() # yaricap = 1
c2 = Circle(5) # yaricap = 5
print(f'c1: alan = {c1.alan_hesapla()}, cevre = {c1.cevre_hesapla()}')
print(f'c2: alan = {c2.alan_hesapla()}, cevre = {c2.cevre_hesapla()}')

print('#######################################################################################')
                        # inheritance

class Person():
     def __init__(self,fname,lname):
          self.firstname = fname
          self.lastname = lname
          print('Person created')

     def who_am_i(self):
         print('I am a person')
     def eat(self):
          print('I am eating')    

class Student(Person):
        def __init__(self,fname,lname,number):
          self.studentNumber = number
          Person.__init__(self,fname,lname)
          print('Student created')
          #ovveride
        def who_am_i(self):
         print('I am a student')
         
        def say_hello(self):
             print('Hello I am a Student')

class Teacher(Person):
     def __init__(self, fname, lname,branch):
          super().__init__(fname, lname)
          self.branch = branch
     def who_am_i(self):
        print(f'I am {self.firstname} {self.lastname} a {self.branch} teacher')  

    
p1 = Person('Cinar','Hoca')
s1 = Student('Anas','AL-Maqtari',123)
t1 = Teacher('Mohammed','Thabet','Python')
print(p1.firstname,p1.lastname)
print(s1.firstname,s1.lastname,s1.studentNumber)
            
p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.say_hello()

