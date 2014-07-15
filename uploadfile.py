import requests, sys


file_name = sys.argv
print file_name[1]
url = 'http://localhost:8888/upload'
files = {'filearg': open(file_name[1], 'rb')}

r = requests.post(url, files=files)
r.text