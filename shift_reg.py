import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

data = 3
latch = 5
clock = 7
clear = 11
speed = .00000000000000000000001

on = True
off = False

GPIO.setup(data, GPIO.OUT)
GPIO.setup(latch, GPIO.OUT)
GPIO.setup(clock, GPIO.OUT)
GPIO.setup(clear, GPIO.OUT)


def light(pin, isOn):
	GPIO.output(pin, isOn)

def sleep(_time):
	time.sleep(_time)

light(clear, off)
sleep(.5)
light(clear, on)

def addValue(input):
	light(data, input)
	sleep(speed)
	light(clock, on)
	sleep(speed)
	light(clock, off)
	sleep(speed)
	light(data, off)

def display():
	sleep(speed)
	light(latch, on)
	sleep(speed)
	light(latch, off)

def clearDis():
	light(clear, off)
	sleep(speed)
	light(clear, on)
	i = 0
	while(i < 64):
		addValue(off)
		#display()
		i=i+1
	display()

def disNums(num1, num2, num3, num4, num5, num6):
	clearDis()
	#clearDis()
	num1 = 9 - num1
	num2 = 9 - num2
	num3 = 9 - num3
	num4 = 9 - num4
	num5 = 9 - num5
	num6 = 9 - num6
	i = 0
	while(i < 10):
		if(i == num6):
			addValue(on)
		else:
			addValue(off)
		i = 1 + i
	i = 0
	while(i < 10):
		if(i == num5):
			addValue(on)
		else:
			addValue(off)
		i = 1 + i
	i = 0
	while(i < 10):
		if(i == num4):
			addValue(on)
		else:
			addValue(off)
		i = i + 1

	i = 0
	while(i < 10):
		if(i == num3):
			addValue(on)
		else:
			addValue(off)
		i = i + 1

	i = 0
	while(i < 10):
		if(i == num2):
			addValue(on)
		else:
			addValue(off)
		i= i + 1
	i = 0
	while(i < 10):
		if(i == num1):
			addValue(on)
		else:
			addValue(off)
		i = i + 1
	display()


def getTime():
	t = time.localtime()
	hour = str(time.strftime("%H"))
	min = str(time.strftime("%M"))
	sec = str(time.strftime("%S"))
	return(hour, min, sec)

def getTimeNice():
	hour, min, sec = getTime()
	#print(hour+":",min,":"+sec)
	#hour = str(int(hour) + 1 )
	if(int(hour) > 12):
		hour = str(int(hour) - 12)
	if(int(hour) == 0):
		hour == 12

	hour1 = -1
	hour2 = 0
	min1 = 0
	min2 = 0
	sec1 = 0
	sec2 = 0


	if(len(hour) == 2):
		hour1 = hour[:1]
	hour2 = hour[-1:]
	if(len(min) == 2):
		min1 = min[:1]
	min2 = min[-1:]
	if(len(sec) == 2):
		sec1 = sec[:1]
	sec2 = sec[-1:]
	return(hour1, hour2, min1, min2, sec1, sec2)



#disNums(6,9)
sleep(1)

i = 0

hour, min, sec = getTime()
passT = sec
passH = min

while(i < 100000000):
	hour1, hour2, min1, min2, sec1, sec2 = getTimeNice()
	curH = int(min2)
	curT = sec2

	if(curH != passH):
		j = 0
		rand = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]
		for j in range(50):
			for num in range(0,len(rand)):
				rand[num] = 1 + rand[num]
				if rand[num] > 9:
					rand[num] = 0
			disNums(rand[0], rand[1], rand[2], rand[3], rand[4], rand[5])
			sleep(.01)

	passH = curH

	if(passT != curT):
		disNums(int(hour1), int(hour2), int(min1), int(min2), int(sec1), int(sec2) )
		#print("The time is "+str(hour)+":"+str(min)+":"+str(sec))

	passT = curT

	sleep(.1)
	i=1+i
