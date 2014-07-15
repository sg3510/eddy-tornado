import requests

# r = requests.post('http://localhost:8888/upload', files={'test.txt': open('test.txt', 'rb')})

url = 'http://localhost:8888/upload'
files = {'filearg': open('alert01.wav', 'rb')}

r = requests.post(url, files=files)
r.text