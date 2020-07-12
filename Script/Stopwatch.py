# template for "Stopwatch: The Game"

import simplegui

# define global variables
count = 0

# define helper function format that converts time


# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
   timer.stop()
def reset():
    global count 
    count = 0
    
# define event handler for timer with 0.1 sec interval
def tick():

# define draw handler
def draw(canvas):
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
button = frame.add_button("Start", start, 100)
button = frame.add_button("Stop", stop, 100)
button = frame.add_button("Reset", reset, 100)


# start frame
frame.start()

# Please remember to review the grading rubric