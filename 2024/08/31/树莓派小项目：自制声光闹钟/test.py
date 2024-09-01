import gpiozero
import time
import threading as thr
import smbus
import LCD1602 as lcd


lcd.init_lcd()
with open("minute", "r") as minute_file:
    minutes = int(minute_file.read())
print(minutes)
lcd.print_lcd(0, 1, format(minutes))

with open("hour", "r") as hour_file:
    hours = int(hour_file.read())
print(hours)
lcd.print_lcd(0, 0, format(hours))
