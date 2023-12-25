from flask import Flask, request
import RPi.GPIO as GPIO

# Motor Control Setup
motorSpeedPin = 18  # Adjust as per your motor driver
motorDirectionPin = 23  # Adjust as per your motor driver

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorSpeedPin, GPIO.OUT)
GPIO.setup(motorDirectionPin, GPIO.OUT)

pwm = GPIO.PWM(motorSpeedPin, 1000)  # 1000 Hz frequency
pwm.start(0)

def set_speed(speed):
    pwm.ChangeDutyCycle(speed)

def set_direction(direction):
    GPIO.output(motorDirectionPin, direction)

def cleanup():
    pwm.stop()
    GPIO.cleanup()

# Flask API Setup
app = Flask(__name__)

@app.route('/speed', methods=['POST'])
def speed():
    speed = request.json.get('speed', 0)
    set_speed(speed)
    return f"Motor speed set to {speed}%"

@app.route('/direction', methods=['POST'])
def direction():
    direction = request.json.get('direction', True)  # True for one direction, False for the other
    set_direction(direction)
    return f"Motor direction set to {'forward' if direction else 'backward'}"

@app.route('/stop', methods=['POST'])
def stop():
    set_speed(0)
    return "Motor stopped"

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)  # Runs the server
    except KeyboardInterrupt:
        cleanup()
