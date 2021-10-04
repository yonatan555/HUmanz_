#read csv
import requests
import time
data =[]


url = 'http://localhost:3000/api/client/add'
for jsn in data:
    requests.post(url, json=jsn)
    time.sleep(3)







