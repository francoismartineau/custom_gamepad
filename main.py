import time
import vgamepad as vg
# vgamepad
# https://pypi.org/project/vgamepad/#getting-started

# Reading sensor with python
# https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.04-Reading-a-Sensor-with-Python/

def accelerate(gamepad, value):
	gamepad.right_trigger(value=value)
	gamepad.update()

if __name__ == "__main__":
	gamepad = vg.VX360Gamepad()
	while (True):
		accelerate(gamepad, 255)
		time.sleep(1)
		accelerate(gamepad, 0)
		time.sleep(1)