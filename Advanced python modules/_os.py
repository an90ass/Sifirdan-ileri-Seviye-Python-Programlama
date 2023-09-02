import os
import datetime
# Get the operating system name
operating_system_name = os.name
print("Operating System:", operating_system_name)

# Get the current directory path before changing
before_change = os.getcwd()
print("Current directory before change:", before_change)

# Change the current directory
# os.chdir('C:\\Users\\anass\\Desktop')

# Get the current directory path after changing
after_change = os.getcwd()
print("Current directory after change:", after_change)

# Create a new folder
# os.mkdir("new folder")

# os.makedirs("bb/aa")
print("Folder created successfully.")
result = os.listdir()
print(result)


for folder in os.listdir():
    if folder.endswith('.py'):
       print(folder) 

result = os.stat('_datetime.py')
file_size = result.st_size  # BYTE
# file_size_kb = result.st_size / 1024  # KB
print(file_size)  # Size in bytes
# print(file_size_kb)  # Size in kilobytes

file_creation_time = datetime.datetime.fromtimestamp(result.st_ctime) # Creation date
file_creation_time = datetime.datetime.fromtimestamp(result.st_atime) # Last access date
file_creation_time = datetime.datetime.fromtimestamp(result.st_mtime) # modification date


print(file_creation_time)
# os.system("notepad.exe")

result1 = os.path.abspath("_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
print(result1)
print(result)

result = os.path.exists("_os.py") # True
result = os.path.isdir("_os.py") # False
result = os.path.isfile("_os.py") # True

print(result)