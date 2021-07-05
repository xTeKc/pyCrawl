import requests

url = "duckduckgo.com"
get_response = requests.get("https://" + url)
print(get_response)