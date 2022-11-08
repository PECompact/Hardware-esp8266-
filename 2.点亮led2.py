from machine import Pin#导入machine中的Pin类
from time import sleep_ms
led1 = Pin(2,Pin.OUT)#引脚，输出
led2 = Pin(5,Pin.OUT)#引脚，输出
led3 = Pin(4,Pin.OUT)#引脚，输出
led1.value(0)
led2.value(0)
led3.value(0)
while True:
    led1.value(1)#1:高电平 0：低电平（除16号自带引脚led以外）
    sleep_ms(7000)#等待7000毫秒
    led1.value(0)
    sleep_ms(100)
    
    led2.value(1)#1:高电平 0：低电平
    sleep_ms(7000)#等待7000毫秒
    led2.value(0)
    sleep_ms(100)
    
    led3.value(1)#1:高电平 0：低电平
    sleep_ms(3000)#等待3000毫秒
    led3.value(0)
    sleep_ms(100)