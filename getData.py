import gpiozero
from gpiozero import LED
from time import sleep
from datetime import datetime

initTime = datetime.now().strftime("%y%M%d%h%m%s")
led = LED(17)
def getInput():
	isQuit = True
	initTime = datetime.now()
	while isQuit:
		try:
			blinkTime = input("Iteration: ")
			blinkTime = int(blinkTime)
			isQuit = False
		except:
			print("Please enter a Int")
		if((datetime.now()-initTime).seconds > 120):
			print("Timeout",(datetime.now()-initTime).seconds)
			isQuit = False
			return None

	return blinkTime

a = getInput()
for i in range(a):
	led.on()
	sleep(1)

	


