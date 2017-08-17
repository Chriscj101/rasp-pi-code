import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18
           , GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

sndA = pygame.mixer.Sound(".wav")
sndB = pygame.mixer.Sound(".wav")
sndC = pygame.mixer.Sound(".wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Sampler Ready."

while True:
   try:
      if (GPIO.input(21) == True):
         soundChannelA.play(sndA)
      if (GPIO.input(16) == True):
         soundChannelB.play(sndB)
      if (GPIO.input(18) == True):
         soundChannelC.play(sndC)
      sleep(.01)
   except KeyboardInterrupt:
      exit()
