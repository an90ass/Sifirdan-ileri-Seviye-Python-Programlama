import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text) #from string to list (dict)
print(type(result))#list
print(result[0]["title"]) 
for i in result:
    print(i["title"])
