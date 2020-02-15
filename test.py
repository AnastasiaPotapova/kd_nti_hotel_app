import requests

d = {'is_admin': 1, 'login': 'admin', 'password': 'admin'}
a = requests.get("https://nast-hotel.herokuapp.com/api/users")
print(a.content)