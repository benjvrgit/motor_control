python3 -m venv --system-site-packages venv

sudo apt install python3-rpi-lgpio

pip3 install rpi-lgpio

import RPi.GPIO as GPIO

curl -X POST http://[Your_Raspberry_Pi_IP_Address]:5000/speed -H "Content-Type: application/json" -d '{"speed": 50}'


