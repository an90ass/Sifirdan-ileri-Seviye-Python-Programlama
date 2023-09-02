# UserAuthenticationManager
import json
import os 
class User():
      def __init__(self,username,password,email):
          self.username = username
          self.password = password
          self.email = email
          
class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoogedIn = False
        self.currentUser = {}
        #load users form .josn file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file) 
                for user in users:
                 user = json.loads(user)# json string bilgiden python objesine donusturme عشان نقدر نوصل للمعلومات لأنها الان عباره عن json
                 newUser = User(username=user['username'],password=user['password'],email=user['email'])
                 self.users.append(newUser)
                #  print(user['email'])  
            print(self.users)

    def register(self,user:User):
        self.users.append(user) # yada .append(self)
        self.savTofile()
        print('User created')
        
    def login(self,username,password):
          for user in self.users:
            if user.username == username and user.password == password:
                self.isLoogedIn = True
                self.currentUser = user
                print('Logged in sucssesfuly')
                break
    def logout(self):
        self.isLoogedIn = False
        self.currentUser={}
        print('Logout done successfully')


    def  identity(self):
        if self.isLoogedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print("Could not login")
        
    def savTofile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list,file)

repository = UserRepository()

while True:
    print('Menu'.center(50,'*'))
    choise = input('1- Register\n2- Login\n3- LogOut\n4-Identity\n5- Exit\nYour choice : ') 
    if choise =='5':
        break
    else:
        if choise =='1': # register 
            username = input('Username:')
            password = input('Password:')
            email = input('email:')
            user = User(username=username,password=password,email=email)
            repository.register(user)
            # print(repository.users)

        elif choise == '2':# login
          if repository.isLoogedIn:
            print('You are already logged in')
          else: 
            user_name = input('User name:')
            user_password = input('Password:')
            repository.login(user_name,user_password)

        elif choise == '3': # logout
            repository.logout()
        elif choise == '4':#Identity
            repository.identity()
        else:
           print ('You entered wrong number')
           