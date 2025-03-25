rom flask import Flask, render_template
from gpiozero import LED
app = Flask(__name__)
led = LED(18) # Change to match your LED!
@app.route('/')
def index():
return render_template('HTML Code.html')
@app.route('/toggle/<action>')
def LEDControl(action):
if action == 'on':
led.on()
return 'LED Turned On’
elif action == 'off':
led.off()
return 'LED Turned Off'
if __name__ == '__main__':
app.run(host='10.1.0.4', port=80)