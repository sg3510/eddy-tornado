import requests, sys, os, zipfile

#file_name = sys.argv[1]
#=file_name

def upload_file(file_name):

  fname = os.path.splitext(file_name)[0]

  file = zipfile.ZipFile(fname+".zip", "w")
  file.write(file_name, os.path.basename(file_name), zipfile.ZIP_DEFLATED)
  file.close()

  url = 'http://localhost:8888/upload'
  files = {'filearg': open(fname+".zip", 'rb')}

  os.remove(fname+".zip")

  r = requests.post(url, files=files)
  r.text