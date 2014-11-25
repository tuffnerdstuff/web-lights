from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import ola_color
import time

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

        # execute action
        rP = params.get(C_RED)
        gP = params.get(C_GREEN)
        bP = params.get(C_BLUE)
        r = int(rP[0]) if rP else 0
        g = int(gP[0]) if gP else 0
        b = int(bP[0]) if bP else 0
        self.set_color(r,g,b)
            
        # write html
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

	html = """
	<html>
	<head>
	<script type="text/javascript" 
	src="https://github.com/DavidDurman/FlexiColorPicker/raw/master/colorpicker.min.js"></script>
	<style type="text/css">
        #picker { width: 200px; height: 200px }
        #slide { width: 30px; height: 200px }
	</style>
	</head>
	<body>
	<div id="picker"></div>
	<div id="slide"></div>
	<script type="text/javascript">
	ColorPicker(
			document.getElementById('slide'),
			document.getElementById('picker'),
			function(hex, hsv, rgb) {
			window.location.href = "?r=" + rgb.r + "&g=" + rgb.g + "&b=" + rgb.b;
			});
        </script>
        </body>
        </html>
	"""
        self.wfile.write(html)


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
