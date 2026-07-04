from machine import Pin
import utime,time
buz = Pin(14,Pin.OUT)
trigger = Pin(20, Pin.OUT)
echo = Pin(21,Pin.IN)
ldr_pin = machine.ADC(27)
motor1=Pin(10,Pin.OUT)
motor2=Pin(11,Pin.OUT)
motor3=Pin(12,Pin.OUT)
motor4=Pin(13,Pin.OUT)
led_pin = machine.PWM(machine.Pin(6))
def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance
while True:
    dist=ultra()
    lval = ldr_pin.read_u16()/655
    print(lval)
    print(dist)
    utime.sleep(1)
    if(dist<30) and lval < 100:
        led_pin.duty_u16(6553)
        motor1.low()
        motor2.low()
        motor3.low()
        motor4.low()
    else:
        led_pin.duty_u16(0)
        motor1.low()
        motor2.high()
        motor3.low()
        motor4.high()