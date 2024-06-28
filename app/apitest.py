import requests


x=requests.get("https://test.arkobot.ir")
print(x._content)