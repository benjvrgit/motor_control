sudo apt install python3-rpi-lgpio

python3 -m venv --system-site-packages venv

pip3 install rpi-lgpio

import RPi.GPIO as GPIO

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/speed -H "Content-Type: application/json" -d '{"speed": 50}'

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/stop

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/direction -H "Content-Type: application/json" -d '{"direction": true}'
curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/direction -H "Content-Type: application/json" -d '{"direction": false}'




