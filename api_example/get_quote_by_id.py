import requests


# DlQmGRzNGo3i
url = "https://api.quotable.io"


quote_id = input("Quote ID: ")

response = requests.get(url + f"/quotes/{quote_id}")

if response.status_code == 200:
    response_dict = response.json()
    print("\n" + response_dict["content"])
    print(response_dict['author'])
elif response.status_code > 400:
    print("Failed!")
    print("Reason: " + response.text)
else:
    print("Failed! Unknown reason!")