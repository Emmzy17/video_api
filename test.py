import requests

BASE = 'http://127.0.0.1:5000/'
data = [{'name' : 'Tips on Ejaculation','likes':1000, 'views' : 2000},
        {'name' : 'Health Pro Tips','likes':8000, 'views' : 200},
        {'name' : 'Dark Alpha traits ','likes':6500, 'views' : 7000} 
            ]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + 'video/0')
print(response)
input()
response = requests.get(BASE + 'video/1')
print(response.json())