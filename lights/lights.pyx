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
        sleep(0.1)
        GPIO.output(self.clock_pin, GPIO.LOW)
        sleep(0.1)

    # set 16 bits to parallel output on the shift register
    def latch(self):
        GPIO.output(self.latch_pin, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.latch_pin, GPIO.LOW)

    # load pattern from multi-array
    def loadPattern(self, pattern):
        cdef int subarray_count, i
        GPIO.cleanup()
        GPIO.output(25, GPIO.LOW)
        for subarray_count in range(len(pattern)):
            for i in range(16):
                GPIO.output(self.serial_pin, pattern[subarray_count][i])
                self.clock()
            self.latch()
        GPIO.cleanup()

    # turn on a single light   Ex. light(12) - Turns on light number 12
    def light(self, int lightNum):
        sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        sequence[lightNum] = 1

        self.loadPattern([sequence])
