#!/usr/bin/env python

from os import curdir, sep, path
import time, json, sys, re, logging

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from urlparse import urlparse, parse_qs
from plugin_system import ServerPluginManager as PM


HOST = ""
PORT = 9000
PARAM_ACTION = "action"

ROOT = path.dirname(path.realpath(sys.argv[0]))
pm = None
logging.basicConfig()

class WebLightsServer(ThreadingMixIn, HTTPServer):
    pass

class WebLightsRequestHandler(BaseHTTPRequestHandler):
        

    def do_GET(self):
        
        # parse params
        url = self.path
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)
        path = parsed_url.path
        print("PATH %s"%path)
    
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
            elif url.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            elif url.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            elif url.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            elif url.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            elif url.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            elif url.endswith(".hello"):
                mimetype='text/html'
                sendReply = False
                plugin_name = self.parse_plugin_name(url,'hello')
                plugin = pm.get_plugin(plugin_name)
                replyString=plugin.hello()
                
            elif path.endswith(".set"):
                mimetype='text/html'
                sendReply = False
                plugin_name = self.parse_plugin_name(url,'set')
                plugin = pm.get_plugin(plugin_name)
                plugin.do(params)
                replyString="%s.set: OK"%plugin_name
                
            elif path.endswith(".get"):
                mimetype='application/json'
                plugin_name = self.parse_plugin_name(url,'get')
                plugin = pm.get_plugin(plugin_name)
                replyString=json.dumps(plugin.get_state())
                sendReply = False

            else: # Unsupported Media Type
                self.send_error(415,'File has unsopported media type: %s' % self.path)
                return

            # Supported Media Type
            self.send_response(200)
            
            if sendReply == True:
                #Open the static file requested and send it
                file_path = ROOT + sep + url
                print("Serving static file: %s" % file_path)
                f = open(file_path, 'rb') 
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            else:
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(replyString)


        except IOError:
            self.send_error(404,'File Not Found: %s (Root: %s)' % (self.path,ROOT))
    
    def parse_plugin_name(self,url,mode):
        return re.match(("/(.*?)\.%s"%mode),url).group(1)


if len(sys.argv) == 2:
    ROOT = sys.argv[1]
else:
    ROOT = path.dirname(path.realpath(sys.argv[0]))
myServer = WebLightsServer((HOST, PORT), WebLightsRequestHandler)
pm = PM()
print(time.asctime(), "Server Starts - %s:%s" % (HOST, PORT))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOST, PORT))
