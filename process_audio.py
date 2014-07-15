import sys, zipfile, os
from time import gmtime, strftime

filename = sys.argv[1]
fname = os.path.splitext(filename)[0]
print zipfile.is_zipfile(sys.argv[1])
f = open('process_audio.out', 'w+')
f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
f.write(str(zipfile.is_zipfile(sys.argv[1])))


# Let's unzip the file
zf = zipfile.ZipFile(filename)
for index, info in enumerate(zf.infolist()):
	extn = os.path.splitext(info.filename)[1]
	zf.extract(info.filename, 'temp/')
	os.rename('temp/' + info.filename, fname + extn)
	if index >= 2:
		f.write("Unexpected input! More than one file!")

f.close()