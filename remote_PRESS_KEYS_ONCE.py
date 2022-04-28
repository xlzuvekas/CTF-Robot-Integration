# importing pygame module
import picamera

import io
import pygame

# importing sys module
import sys
#! /usr/bin/python3 get open motor stuff

baudRate = 115200
port = "/dev/ttyACM0"


sys.path.append("../src/open_motor/")
# This line points the python path to the open_motor module.
# This will need to be changed based on the location of your code.

from open_motor_serial import open_motor
import time

comms = open_motor()
comms.init_serial_port(port,baudRate,0.5)



# initialising pygame

# Init pygame 
pygame.init()
screen = pygame.display.set_mode((0,0))

# Init camera
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.crop = (0.0, 0.0, 1.0, 1.0)

x = (screen.get_width() - camera.resolution[0]) / 2
y = (screen.get_height() - camera.resolution[1]) / 2

# Init buffer
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

# Main loop
exitFlag = True
while(exitFlag):
    for event in pygame.event.get():
        if(event.type is pygame.MOUSEBUTTONDOWN or 
           event.type is pygame.QUIT):
            exitFlag = False

    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:
          (camera.resolution[0] * camera.resolution[1] * 3)],
           camera.resolution, 'RGB')

    screen.fill(0)
    if img:
        screen.blit(img, (x,y))

    pygame.display.update()
    
def sprint():
    comms.send_pwm_goal(0,200,-200,0)
    print("Response" +comms.get_response())
def forward():
    comms.send_pwm_goal(0,100,-100,0)
    print("Response" +comms.get_response())
def back():
    comms.send_pwm_goal(0,-100,100,0)    
    print("Response" +comms.get_response())  
def left():
    comms.send_pwm_goal(0,100,100,0)
    print("Response" +comms.get_response())
def right():
    comms.send_pwm_goal(0,-100,-100,0)
    print("Response" +comms.get_response())
def stop():
    comms.send_pwm_goal(0,0,0,0)
    print("Response" +comms.get_response())
# creating a running loop
while True:
    
	# creating a loop to check events that
	# are occuring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# checking if keydown event happened or not
		if event.type == pygame.KEYDOWN:
			
			# checking if key "A" was pressed
			if event.key == pygame.K_w:
				forward()
			
			# checking if key "J" was pressed
			if event.key == pygame.K_a:
				left()
			
			# checking if key "P" was pressed
			if event.key == pygame.K_s:
				back()
			
			# checking if key "M" was pressed
			if event.key == pygame.K_d:
				right()
				
			if event.key == pygame.K_x:
				stop()
			if(event.key == pygame.KMOD_SHIFT):
				sprint()

if __name__ == "__main__":
    main()



camera.close()
pygame.display.quit()
