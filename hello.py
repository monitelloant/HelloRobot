from gopigo import *
import time

def shimmy():
    for x in range(2):
        right()
        time.sleep(.5)
        left()
        time.sleep(.5)

def twirl():
    right_rot()
    time.sleep(2)
def eyes():
    led_on(LED_L)
    led_on(LED_R)

def eyesoff():
    led_off(LED_L)
    led_off(LED_R)

shimmy()
twirl()
eyes()
eyesoff()
stop()
