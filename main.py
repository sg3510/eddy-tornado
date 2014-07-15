import tornado
import tornado.ioloop
import tornado.web
import os, uuid
import zipfile
import multiprocessing, subprocess, sys
from time import gmtime, strftime, sleep
 
__UPLOADS__ = "uploads/"
 
class Userform(tornado.web.RequestHandler):
    def get(self):
        self.render("fileuploadform.html")
 
 
class Upload(tornado.web.RequestHandler):
    def post(self):
        fileinfo = self.request.files['filearg'][0]
        # print self.request.files['filearg'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        # cname = str(uuid.uuid4()) + extn
        cname = strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + extn
        fh = open(__UPLOADS__ + cname, 'wb')
        fh.write(fileinfo['body'])

        self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)

        p = subprocess.Popen(['python', 'process_audio.py',__UPLOADS__ + cname], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
 
 
application = tornado.web.Application([
        (r"/", Userform),
        (r"/upload", Upload),
        ], debug=True)
 
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()