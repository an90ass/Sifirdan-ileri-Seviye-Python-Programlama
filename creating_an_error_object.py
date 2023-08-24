def chek_password(psw):
    import re
    if len(psw)<8:
         raise Exception("password must be at least 7 characters")
    elif not re.search("[a-z]",psw):
         raise Exception("Password must contain lowercase letters")
    elif not re.search("[A-Z]",psw):
         raise Exception("Password must contain capital letters")
    elif not re.search("[0-9]",psw):
         raise Exception("Password must not contain numbers")
    elif not re.search("[_@$]",psw):
         raise Exception("Passport must contain alphanumeric")
    elif re.search("/s",psw):
                  raise Exception("password must not contain spaces")
    else:
         print ("valid password")

password = "12345678a"

try:
      chek_password(password)
except Exception as ex:
     print(ex)
else:
 print ("valid password")
finally:
     print("validation is done")
