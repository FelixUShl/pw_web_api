#"PasswordHash": "88020F057FE7287D8D57494382356F97",

import requests, hashlib

login = "admin"
passwd = "admin"
serv_addr = "localhost"
password_hash = hashlib.md5(f'{passwd}'.encode()).hexdigest().upper()
password_hash += "F593B01C562548C6B7A31B30884BDE53"
password_hash = hashlib.md5(password_hash.encode()).hexdigest().upper()
password_hash = hashlib.md5(password_hash.encode()).hexdigest().upper()
json = {
    "PasswordHash": password_hash,
    "UserName": login
}
r = requests.post(f"http://{serv_addr}:40001/json/Authenticate", json=json)
print (r.json())
