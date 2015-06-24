__author__ = 'Evan Seils'

import RPi.GPIO as GPIO
from time import sleep


class Lights():
    # GPIO pins
    serial_pin = 23
    clock_pin = 24
    latch_pin = 25


    # cleanup and init GPIO pins when class is created
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.serial_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)

    # clock bit
    def clock(self):
        GPIO.output(self.clock_pin, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(self.clock_pin, GPIO.LOW)
        sleep(0.01)

    # set 16 bits to parallel output on the shift register
    def latch(self):
        GPIO.output(self.latch_pin, GPIO.HIGH)
        GPIO.output(self.latch_pin, GPIO.LOW)

    # load pattern from multi-array
    def loadPattern(self, pattern, delay):
        GPIO.output(self.latch_pin, GPIO.LOW)
        for subarray_count in range(len(pattern)):
            for i in range(24):
                GPIO.output(self.serial_pin, pattern[subarray_count][i])
                self.clock()
            print "\033[92mShifted In: " + str(pattern[subarray_count]) + "\033[0m"
            sleep(delay)
            self.latch()

    # turn on a single light   Ex. light(12) - Turns on light number 12
    def light(self, lightNum):
        sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        sequence[lightNum] = 1

        self.loadPattern([sequence], 0)

    def __del__(self):
	GPIO.cleanup()
