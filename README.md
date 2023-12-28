sudo apt install python3-rpi-lgpio

In project folder:
python3 -m venv --system-site-packages venv

pip install -r requirements.txt

In .py file:
import RPi.GPIO as GPIO
...
...

To test:
python motor_api_server.py

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/speed -H "Content-Type: application/json" -d '{"speed": 50}'

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/stop

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/direction -H "Content-Type: application/json" -d '{"direction": true}'

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/direction -H "Content-Type: application/json" -d '{"direction": false}'




