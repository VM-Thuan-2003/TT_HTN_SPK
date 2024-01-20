from http.server import HTTPServer, BaseHTTPRequestHandler

import RPi.GPIO as GPIO

led_1  = 2
led_2  = 3

PORT = 8080

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)
GPIO.output(led_1, 0)
GPIO.output(led_2, 0)

def control_light_inv():
    if(GPIO.input(led_1) == 1):
        GPIO.output(led_1, 0)
    else:
        GPIO.output(led_1, 1)

    if(GPIO.input(led_2) == 1):
        GPIO.output(led_2, 0)
    else:
        GPIO.output(led_2, 1)

class Sever(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        if self.path == '/led/1/on':
            print("led 1 on")
            GPIO.output(led_1, 1)
            self.path = '/index.html'
        if self.path == '/led/1/off':
            print("led 1 off")
            GPIO.output(led_1, 0)
            self.path = '/index.html'
        if self.path == '/led/2/on':
            print("led 2 on")
            GPIO.output(led_2, 1)
            self.path = '/index.html'
        if self.path == '/led/2/off':
            print("led 2 off")
            GPIO.output(led_2, 0)
            self.path = '/index.html'
        if self.path == '/led/inv':
            print("led inv")
            control_light_inv()
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

def main():
    try:
        server = HTTPServer(('127.0.0.1', PORT), Sever)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        GPIO.cleanup()
        
if __name__ == __name__:
    print("__start__")
    main()
