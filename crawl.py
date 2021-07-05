import requests

from list import subdomain_list

def request(url):
    # url to crawl 
    url = "notAwebpage.duckduckgo.com"
    try:
        get_response = requests.get("https://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        pass

