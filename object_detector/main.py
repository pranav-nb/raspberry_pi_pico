from machine import Pin
import utime
import machine
trigger = Pin(2, Pin.OUT) ##trigger pin to GPIO 2 as output
echo = Pin(3, Pin.IN) ##echo pin to GPIO 3 as input
signalon=0
signaloff=0
led=Pin(6, Pin.OUT) ##led pin to GPIO 6 as output
from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
DEFAULT_I2C_ADDR = 0x27 ##i2c address
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

while 1:
 trigger.low() ##keep the trigger low
 utime.sleep_us(2)
 trigger.high() ##keep the trigger high for 5 us
 utime.sleep_us(5)
 trigger.low()
 while echo.value() == 0: ## calculate for the echo values
     signaloff = utime.ticks_us()
 while echo.value() == 1:
     signalon = utime.ticks_us()
 timepassed = signalon - signaloff
 distance = (timepassed * 0.0343) / 2 ##calculate the distance
 lcd.move_to(0,0)
 if(distance<100 or distance>1):
     lcd.putstr("distance: "+str(round(distance,1)))
     print(round(distance,1))
     led.value(0)
     if(distance<10):
         led.value(1)
 else:
     led.value(0)
 utime.sleep(0.15)
 lcd.clear()
