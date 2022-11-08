from machine import Pin
from time import sleep_ms
btn_pin = Pin(10,Pin.IN)
btn1_pin = Pin(9,Pin.IN)
led_pin = Pin(16,Pin.OUT)
led1_pin = Pin(9,Pin.OUT)
a = False
a1 = False
while True:
    val1 = btn1_pin.value()
    if val1==1:
        sleep_ms(500)
        a = not a
    if a1==True:
        led1_pin.value(0)
        val = btn_pin.value()#读取按键引脚的状态
        if val==1:
            sleep_ms(500)
            a = not a
        if a==True:
            led_pin.value(0)
        else:
            led_pin.value(1)
    else:
        led1_pin.value(1)
