import requests
import threading

url = 'https://site.com'

data = {
    '_username': '',
    '_password': '',
    '_submit': 'true',
}



def do_request():
    while True:
        response = requests.post(url, data=data).text

        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
