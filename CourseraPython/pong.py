# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, -1]
score1 = 0
score2 = 0
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 1.0
paddle2_vel = 1.0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = random.randrange(1, HEIGHT)
    x_dir = random.randrange(120, 240) / 60
    y_dir = random.randrange(60, 180) / 60
    
    if not right:
        ball_vel = [-x_dir,-y_dir]
    else:
        ball_vel = [x_dir, -y_dir]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    ball_init(random.choice([True, False]))
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= 0 and paddle1_pos + paddle1_vel < HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel >= 0 and paddle2_pos + paddle2_vel < HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        
    if paddle1_pos + paddle1_vel >= HEIGHT:
        paddle1_pos -= paddle1_vel
    if paddle2_pos + paddle2_vel >= HEIGHT:
        paddle2_pos += paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line( [0 + HALF_PAD_WIDTH, paddle1_pos], 
                [0 + HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT],
                PAD_WIDTH, "White")
    c.draw_line( [WIDTH - HALF_PAD_WIDTH, paddle2_pos],
                [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT],
                PAD_WIDTH, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of the top of the canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # collide and reflect off of the bottom of the canvas
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # detect if ball has collided with the left gutter
    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        # Check if the ball is between the top and bottom of the left paddle
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
        # It was, invert the ball's horizontal velocity
            ball_vel[0] = - ball_vel[0]
        else:
            # Player 2 has scored a point and the game should reset
            score2 += 1
            ball_init(True)
    
    # detect if ball has collided with the right gutter
    if ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        # Check if the ball is between the top and bottom of the opponent's paddle
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            # It was, invert the ball's horizontal velocity
            ball_vel[0] = - ball_vel[0]
        else:
            # Player 1 has scored a point and the ball should reset
            score1 += 1
            ball_init(False)
   
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score1), [2 * (WIDTH / 6), 50], 30, "Gray")
    c.draw_text(str(score2), [4 * (WIDTH / 6), 50], 30, "Gray")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 4.0
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = -4.0
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

# start frame
frame.start()
new_game()
