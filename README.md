web-lights
==========

A simple OLA web-client written in python for controlling ambient lightning.

Installation
------------

0. Install python
1. Install OLA and configure your DMX universe 
2. Configure web-lights
2.1. Universe ID can be set via UNIVERSE in ola_color.py (default = 1)
2.2. Size of RGB array can be set via SEGMENTS in ola_color.py (default = 8)
4. Install initscript
4.1. Make a symlink to web-lights.py: sudo ln -s /usr/bin/web-lights <BASE>/web-lights.py
4.2. Copy init script (located in init_script/web-lights): cp <BASE>/init_script/web-lights /etc/init.d/
4.3. Edit init script and set USER to your username
4.4. Enable auto-start: update-rc.d /etc/init.d/web-lights defaults
5. Start web-lights: /etc/init.d/web-lights start
6. Go to http://<server_ip>:9000
7. Enjoy!
