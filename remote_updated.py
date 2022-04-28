# importing pygame module
import pygame

# importing sys module
import sys
#! /usr/bin/python3 get open motor stuff

baudRate = 115200
port = "/dev/ttyACM0"
clawToggle = 1

sys.path.append("../src/open_motor/")
# This line points the python path to the open_motor module.
# This will need to be changed based on the location of your code.

from open_motor_serial import open_motor
import time

comms = open_motor()
comms.init_serial_port(port,baudRate,0.5)



# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))
def sprint():
    comms.send_pwm_goal(0,-200,200,0)
    print("Response" +comms.get_response())
def forward():
    comms.send_pwm_goal(0,-100,100,0)
    print("Response" +comms.get_response())
def back():
    comms.send_pwm_goal(0,100,-100,0)    
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
def openClaw():
    comms.send_pwm_goal(0,0,0,200)
    print("Response" +comms.get_response())
def closeClaw():
    comms.send_pwm_goal(0,0,0,-200)
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
			if event.key == pygame.K_x:
				stop()
			
			# checking if key "M" was pressed
			if event.key == pygame.K_d:
				right()
			if event.key == pygame.K_c:
				closeClaw()
				
			if event.key == pygame.K_v:
				openClaw()
			if event.key == pygame.K_s:
				back()
			if(event.key == pygame.K_q):
				sprint()
                
                

if __name__ == "__main__":
    main()