"""
About GPIO Mappings in Galileo..

GPIO	Digital I/O
gpio11	pin0
gpio12	pin1
gpio13	pin2
gpio14	pin3
gpio6	pin4
gpio0	pin5
gpio1	pin6
gpio38	pin7
gpio40	pin8
gpio4	pin9
gpio10	pin10
gpio5	pin11
gpio15	pin12
gpio7	pin13

"""

import os
import os.path
import time


from wiringx86 import GPIOGalileoGen2 as GPIO
gpio = GPIO(debug=False)
from flask import Flask,url_for, render_template
app = Flask(__name__)
from flask import request
from flask import json

#Our robot mappings
#For motor 1
dir1 = 5
#For motor 2
dir2 = 6

gpio.pinMode(dir1, gpio.OUTPUT)

gpio.pinMode(dir2, gpio.OUTPUT)

@app.route('/')
def hello_world():
 return render_template('Test Page.html')

@app.route('/Left')
def Left():
 #Control Code for left turn
 gpio.digitalWrite(dir2, gpio.HIGH)
 gpio.digitalWrite(dir1, gpio.LOW)
 time.sleep(0.3)
 print 'Left'
 return render_template('Test Page.html')

@app.route('/Right')
def Right():
 #Control Code for right turn
 gpio.digitalWrite(dir2, gpio.LOW)
 gpio.digitalWrite(dir1, gpio.HIGH)
 time.sleep(0.3)
 print 'Right'
 return render_template('Test Page.html')

@app.route('/Forward')
def Forward():
 #Control code for Forward
 gpio.digitalWrite(dir1, gpio.HIGH)
 gpio.digitalWrite(dir2, gpio.HIGH)
 time.sleep(0.4)
 print 'Forward'
 return render_template('Test Page.html')

@app.route('/Reverse')
def Reverse():
 #Control code for Reverse
 gpio.digitalWrite(dir1, gpio.LOW)
 gpio.digitalWrite(dir2, gpio.LOW) 
 time.sleep(0.4)
 print 'Reverse'
 return render_template('Test Page.html')

#gpio.cleanup()

if __name__ == '__main__':
 app.run(host='0.0.0.0',port = 5000, debug=True)   
 #app.run()
