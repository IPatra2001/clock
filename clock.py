import tkinter as tk
import time
import math

window = tk.Tk()
window.geometry("400x400")

def update_clock():
    hours = int(time.strftime("%I"))
    minutes =int(time.strftime("%M")) 
    seconds = int(time.strftime("%S"))

# 360/60 = 6 tradius/sec
# cos(radians(t))=adjacent/hypotenuse = y/r => y = r*(cos(radians(t)))
# sin(radians(t)) = opposite/hypotenuse = x/r => x = r*(sin(radians(t)))
    # seconds hand per second
    seconds_x =  seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len *  math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # minutes hand per minutes
    minutes_x =  minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len *  math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # hourss hand per hourss
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len *  math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock)
   
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand = True, fill = 'both')

#create background
bg = tk.PhotoImage(file="img_clock.png")
canvas.create_image(200, 200, image=bg)

# create clock hands
center_x = 200
center_y = 200
seconds_hand_len = 70
minutes_hand_len = 50
hours_hand_len = 30

# Drawing hands
# seconds hand
seconds_hand = canvas.create_line(200,200,200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5,fill="black")

#minutes hand
minutes_hand = canvas.create_line(200,200,200 + minutes_hand_len, 200 + minutes_hand_len, width=3,fill="black")

# hours hand
hours_hand = canvas.create_line(200,200,200 + hours_hand_len, 200 + hours_hand_len, width=5,fill="black")


update_clock()
window.mainloop()




