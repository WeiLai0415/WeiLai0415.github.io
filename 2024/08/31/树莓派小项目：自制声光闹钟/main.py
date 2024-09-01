import gpiozero
import time
import threading as thr
import smbus
import LCD1602 as lcd

led1 = gpiozero.LED(4)
led2 = gpiozero.LED(27)
button = gpiozero.Button(23)
buttonH = gpiozero.Button(22)
buttonM = gpiozero.Button(15)
buzzer = gpiozero.Buzzer(26)

def screening():
    while True:
        t = time.localtime()
        hour = t.tm_hour
        minute = t.tm_min
        lcd.print_lcd(0, 1, "NOW:")
        lcd.print_lcd(0, 0, "ALARM AT:")
        lcd.print_lcd(9, 1, format(hour) + ":" + format(minute))
        with open("minute", "r") as minute_file:
            minutes = int(minute_file.read())
        print(minutes)
        lcd.print_lcd(12, 0, format(minutes))
        with open("hour", "r") as hour_file:
            hours = int(hour_file.read())
        print(hours)
        lcd.print_lcd(9, 0, format(hours) + ":")
        time.sleep(0.1)

def format(num):
	if num >= 10:
		return str(num)
	if num < 10:
		return "0" + str(num)

def toggle(led):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
def toggle1():
    toggle(led1)
    
def toggle2():
    toggle(led2)
    
def buzzing():
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    time.sleep(0.5)
   
   
def alarming():
    while True:
        # print(button.is_pressed)
        threads = []
        t1 = thr.Thread(target=toggle1)
        t2 = thr.Thread(target=toggle2)
        t3 = thr.Thread(target=buzzing)

        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
    
        for i in threads:
            i.start()
        for i in threads:
            i.join()
            
        if button.is_pressed:
            break
            time.sleep(60)

def main():
    while True:
        with open("hour", "r") as hour_file:
            hours = int(hour_file.read())
        with open("minute", "r") as minute_file:
            minutes = int(minute_file.read())
        time.sleep(0.1)
        t = time.localtime()
        hour = t.tm_hour
        minute = t.tm_min
        second = t.tm_sec
        # print(hour, minute, second)
        # lcd.print_lcd(0, 1, "NOW:")
        # lcd.print_lcd(4, 1, format(hour) + ":" + format(minute))
        # mylcd.lcd_display_string("NOW: ", 2, 0)
        # mylcd.lcd_display_string(str(hour) + ":" + str(minute), 2, 4)
        if hour == hours and minute == minutes and second == 0:
            alarming()
        time.sleep(0.1)

def setMin():
    with open("minute", "r") as minute_file:
        minutes = int(minute_file.read())
    print(minutes)
    # lcd.print_lcd(0, 1, format(minutes))
    while True:
        # if buttonMD.is_pressed:
            # mintues += 1
            # with open("minute", "w") as minute_file:
                # minute_file.write(str(minutes))
            # print(minutes)
        if buttonM.is_pressed:
            if minutes - 60 >= -1:
                minutes = minutes - 59
            else:
                minutes += 1
            with open("minute", "w") as minute_file:
                minute_file.write(str(minutes))
            print(minutes)
            # lcd.print_lcd(0, 1, format(minutes))
            # mylcd.lcd_display_string(str(minutes), 1, 3)
        time.sleep(0.2)


def setHour():
    with open("hour", "r") as hour_file:
        hours = int(hour_file.read())
    print(hours)
    # lcd.print_lcd(0, 0, format(hours))
    # lcd.print_lcd(1, 2, ":")
    while True:
        # if buttonHU.is_pressed:
            # hours += 1
            # with open("hour", "w") as hour_file:
                # hour_file.write(str(hours))
            # print(hours)
        if buttonH.is_pressed:
            if hours - 24 >= -1:
                hours = hours - 23
            else:
                hours += 1
            with open("hour", "w") as hour_file:
                hour_file.write(str(hours))
            print(format(hours))
            # lcd.print_lcd(0, 0, format(hours))
            # mylcd.lcd_display_string(str(hours), 1, 0)
            # mylcd.lcd_display_string(":", 1, 3)            
        time.sleep(0.2)



# initialize LCD display
lcd.init_lcd()
# mylcd = lcd.lcd()


threads2 = []

t21 = thr.Thread(target=main)
t22 = thr.Thread(target=setHour)
t23 = thr.Thread(target=setMin)
t24 = thr.Thread(target=screening)

threads2.append(t21)
threads2.append(t22)
threads2.append(t23)
threads2.append(t24)

for i in threads2:
    i.start()
for i in threads2:
    i.join()
    
