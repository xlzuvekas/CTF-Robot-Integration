#import libraries
import RPi.GPIO as GPIO
import time

#from tkinter import*
#import tkinter.font

# pin settings

PWMPin = 12 #connected enable pin
Motor1 = 16 #input 1
Motor2 = 18 #input 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)#GPIO pin location
GPIO.setup(PWMPin,GPIO.OUT)#pin mode to output
GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.output(PWMPin,GPIO.LOW)#PINS START WITH LOW
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2, GPIO.HIGH)
PwmValue = GPIO.PWM(PWMPin,2000)#PWM Frequency set
PwmValue.start(100)#value range 0-100

time.sleep(60)#do nothing after 10s

GPIO.output(PWMPin,GPIO.LOW)#PINS START WITH LOW 
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2, GPIO.LOW)
