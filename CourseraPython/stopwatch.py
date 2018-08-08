# template for "Stopwatch: The Game"
import simplegui

# define global variables
elapsed_time = 0
running = False
good_stop = 0
total_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """ Takes elapsed_time 't' and converts it to minutes, seconds
    and tenths of seconds """
    minutes = t // 600
    
    tens_seconds = ((t//10) % 60) // 10
    
    ones_seconds = ((t//10)% 60) % 10
    
    tenths_seconds = t % 10
    
    return str(minutes) + ":" + str(tens_seconds) + str(ones_seconds) + "." + str(tenths_seconds)

def init():
    """ Initialize (or re-initialize) counters to zero """
    global elapsed_time, good_stop, total_stop
    elapsed_time = 0
    good_stop = 0
    total_stop = 0
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    """ Starts the timer """
    global running
    running = True
    timer.start()
    
def stop():
    """ Stops the timer and calculates number of stops """
    global elapsed_time, running, good_stop, total_stop
    if running == True:
        total_stop += 1
        if elapsed_time % 10 == 0:
            good_stop += 1
    running = False    
    timer.stop()
    
def reset():
    """ Restarts the timer and re-initializes counters """
    global running
    running = False
    timer.stop()
    init()

# define event handler for timer with 0.1 sec interval
def timer_engine():
    """ Timer engine """
    global elapsed_time
    elapsed_time += 1
    
# define draw handler
def draw(canvas):
    """ Draw text to canvas """
    canvas.draw_text( format(elapsed_time), [105, 150], 36, "White" )
    canvas.draw_text( "Good Stops:", [40, 25], 20, "White" )
    canvas.draw_text( str(good_stop), [75, 50], 26, "Green" )
    canvas.draw_text( "Total Stops:", [175, 25], 20, "White" )
    canvas.draw_text( str(total_stop), [210, 50], 26, "Gray" )

#create frame
frame = simplegui.create_frame("Stopwatch, the game!", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_engine)
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()

# Please remember to review the grading rubric
