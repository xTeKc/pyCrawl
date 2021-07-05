import requests

url = "duckduckgo.com"
try:
    get_response = requests.get("https://" + url)
    print(get_response)
except requests.exceptions.ConnectionError:
    pass