import machine
import time as t
#方法一：
led = machine.Pin(2,machine.Pin.OUT)#引脚，输出（16号自带引脚led）
while True:
    led.value(0)#0:高电平 1：低电平
    t.sleep(1)
    led.value(1)
    t.sleep(1)
'''方法二：
from machine import Pin#导入machine中的Pin类
led = Pin(2,Pin.OUT)#引脚，输出
from time import sleep_ms
sleep_ms(1000)#等待1000毫秒'''