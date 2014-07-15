import requests

# r = requests.post('http://localhost:8888/upload', files={'test.txt': open('test.txt', 'rb')})

url = 'http://localhost:8888/upload'
files = {'filearg': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

r = requests.post(url, files=files)
r.text