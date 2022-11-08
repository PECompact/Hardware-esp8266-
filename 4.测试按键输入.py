from machine import Pin
from time import sleep_ms
#btn_pin = Pin(4,Pin.IN)
led_pin = Pin(0,Pin.OUT)
while True:
    #val = btn_pin.value()
    a = int(input("输入一个整数"))
    if a==1:
        led_pin.value(1)
    elif a==0:
        led_pin.value(0)
    else:
        for i in range(a):
            led_pin.value(0)
            sleep_ms(500)
            led_pin.value(1)
            sleep_ms(500)
    '''print(val)
    sleep_ms(500)'''
    