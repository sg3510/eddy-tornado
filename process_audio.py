import sys, zipfile
from time import gmtime, strftime

print zipfile.is_zipfile(sys.argv[1])
f = open('process_audio.out', 'w+')
f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
f.write(str(zipfile.is_zipfile(sys.argv[1])))
f.close()