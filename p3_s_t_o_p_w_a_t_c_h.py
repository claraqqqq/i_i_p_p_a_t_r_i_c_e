import simplegui

# define global variables
time = "0:00:0"
t = 0
success = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    minutes = str(t // 600)
    seconds = str((t%600)//100)+str((t%100)//10)
    oneTenthSeconds = str(t%10)
    time = minutes + ":" + seconds + ":" + oneTenthSeconds
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global startState
    startState = True
    
def stop():
    timer.stop()
    global startState, success, attempts
    if startState:
        if t%10 == 0:
            success += 1
        attempts += 1
    startState = False
    label.set_text("Success/Attempts = " + str(success) + "/" + str(attempts))
    
def reset():
    timer.stop()
    global success, attempts
    success = 0
    attempts = 0
    t = 0
    time = "0:00:0"
    format(t)
    label.set_text("Success/Attempts = " + str(success) + "/" + str(attempts))
    
# define event handler for timer with 0.1 sec interval
def tictac():
    global t
    t += 1
    format(t)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(time, [50,110], 80, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 180)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
label=frame.add_label("Success/Attempts = " + str(success) + "/" + str(attempts), 200)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tictac)

# start frame
frame.start()

# Please remember to review the grading rubric
