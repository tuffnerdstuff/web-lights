from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import ola_color_dummy as ola_color
import time
from os import curdir, sep

hostName = ""
hostPort = 9000
PARAM_ACTION = "action"
C_RED = "r"
C_GREEN = "g"
C_BLUE = "b"
ACTION_COLOR = "color"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        # parse params
        url = self.path
        params = parse_qs(urlparse(url).query)
    
        # show webinterface
        if url == "/":
            url = "/index.html"
    
        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if url.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if url.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if url.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if url.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            if url.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if url.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if url.startswith("/color.do"):
                sendReply = False
                rP = params.get(C_RED)
                gP = params.get(C_GREEN)
                bP = params.get(C_BLUE)
                r = int(rP[0]) if rP else 0
                g = int(gP[0]) if gP else 0
                b = int(bP[0]) if bP else 0
                self.set_color(r,g,b)

                
            self.send_response(200)
            
            if sendReply == True:
                #Open the static file requested and send it
                file_path = curdir + sep + url
                print("Serving static file: %s" % file_path)
                f = open(file_path, 'rb') 
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            else:
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write("<html><body>OK</body></html>")


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
        


    def set_color(self,r,g,b):
        print("Setting color to: (%i,%i,%i)" % (r, g, b))
        ola_color.SendDMXFrame(r,g,b)

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
