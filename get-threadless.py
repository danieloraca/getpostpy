import requests

url = 'https://www.githubstatus.com/api/v2/status.json'

def do_request():
    while True:
        response = requests.get(url).text

        print(response)

do_request()