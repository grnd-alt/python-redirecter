import requests
print(requests.post("http://10.0.0.149/index.php",data = {"login":"test","password":"1234"}).content)