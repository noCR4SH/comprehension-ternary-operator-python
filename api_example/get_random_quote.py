import requests

url = "https://api.quotable.io"

response = requests.get(url + "/random")

print(response.text)
response_dict = response.json()


print(response_dict["content"])
print(response_dict["author"])