from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time

hostName = "localhost"
hostPort = 9000
PARAM_ACTION = "action"
PARAM_COLOR = "color"
ACTION_COLOR = "color"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        # parse params
        url = self.path
        params = parse_qs(urlparse(url).query)

        # execute action
        action = params.get(PARAM_ACTION)
        if action and action[0] == ACTION_COLOR:
            print ("ACTION: COLOR")
            color = params.get(PARAM_COLOR)
            if color:
                self.set_color(color[0])
        else:
            print ("ACTION: none")
            
        # write html
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % url, "utf-8"))
        self.wfile.write(bytes("<p>Parameters: %s</p>" % params, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def set_color(self,color):
        print("Setting color to: %s" % color)

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
