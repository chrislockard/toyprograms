# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
c =  0.005 # friction constant
thrust_sensitivity = 0.095
rotation_sensitivity = 0.055
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_thrust_info = ImageInfo([135, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if self.thrust == False:
            # Draw the ship without thrusters
            canvas.draw_image(ship_image, ship_info.get_center(), 
                              ship_info.get_size(), [self.pos[0], self.pos[1]],
                              [90, 90], self.angle)
        else:
            # Draw the ship with thrusters
            canvas.draw_image(ship_image, ship_thrust_info.get_center(), 
                              ship_thrust_info.get_size(), [self.pos[0], self.pos[1]],
                              [90, 90], self.angle)
        
    def update(self):
        """ Update the various parameters of the ship. """
        # Acceleration
        # Update position, with bounds checking: wrap the ship around the screen
        self.pos[0] += self.vel[0]
        if self.pos[0] >= WIDTH:  # ship went off the right side of the screen
            self.pos[0] = 0			# wrap the ship around to the left
        elif self.pos[0] < 0:		# ship went off the left side of the screen
            self.pos[0] = WIDTH		# wrap the ship around to the right
            
        self.pos[1] += self.vel[1]
        if self.pos[1] >= HEIGHT:	# ship went off the bottom of the screen
            self.pos[1] = 0			# wrap ship around to the top
        elif self.pos[1] < 0:		# ship went off the top of the screen
            self.pos[1] = HEIGHT	# wrap ship around to the bottom
        
        # Update angle based on the ship's angular velocity
        self.angle += self.angle_vel
        
        # Friction update
        self.vel[0] *= (1 - c)
        self.vel[1] *= (1 - c)
        
        # Update velocity
        forward = [math.cos(self.angle), math.sin(self.angle)]
        
        if self.thrust:
            # multiply the forward vector by a constant
            # replace .09 with a thrusting_sensitivity variable
            self.vel[0] += forward[0] * thrust_sensitivity
            self.vel[1] += forward[1] * thrust_sensitivity

    def rotate_left(self, vel):
        """ Rotate the ship to the left """
        self.angle_vel -= vel	# decrement the ship's angular velocity (counter-clockwise rotation)
        
    def rotate_right(self, vel):
        """ Rotate the ship to the right """
        self.angle_vel += vel	# increment the ship's angular velocity (clockwise rotation)
        
    def thrusting(self, thrusting):
        """ The ship's thrusters engage """
        if thrusting:
            self.thrust = True
            ship_thrust_sound.play()		# whooooosh
        else:
            self.thrust = False
            ship_thrust_sound.rewind()
            
    def shoot(self):
        """ The ship shoots a missile """
        global a_missile
        # calculate the tip of the ship
        forward = angle_to_vector(self.angle)
        a_missile = Sprite([self.pos[0] + (self.radius * forward[0]), self.pos[1] + (self.radius * forward[1])], 
                           [self.vel[0] + (5 * forward[0]), self.vel[1] + (5 *forward[1])], 
                           self.angle, 0, 
                           missile_image, missile_info, missile_sound)
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
                          self.pos, self.image_size, self.angle)
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        if self.pos[0] >= WIDTH:	# sprite went off the right side of the screen
            self.pos[0] = 0			# wrap the sprite around to the left
        elif self.pos[0] < 0:		# sprite went off the left side of the screen
            self.pos[0] = WIDTH		# wrap the sprite around to the right
            
        self.pos[1] += self.vel[1]
        if self.pos[1] >= WIDTH:	# sprite went off the right side of the screen
            self.pos[1] = 0			# wrap the sprite around to the left
        elif self.pos[1] < 0:		# sprite went off the left side of the screen
            self.pos[1] = WIDTH		# wrap the sprite around to the right
     
        
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    # draw the score and number of player lives
    canvas.draw_text("Lives:", (50, 50), 20, "White")
    canvas.draw_text(str(lives), (150, 50), 20, "White")
    canvas.draw_text("Score:", (WIDTH - 150, 50), 20, "White")
    canvas.draw_text(str(score), (WIDTH - 50, 50), 20, "White")
    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    # Sprite(pos, vel, ang, ang_vel, image, info, sound = None)
    a_rock = Sprite([random.randrange(0, WIDTH), random.randrange(0, HEIGHT)], 
                    [random.randrange(-4, 4), random.randrange(-4, 4)], 
                    random.random() + random.randrange(0,2), 
                    random.random() - random.random(), 	# a better way?
                    asteroid_image, asteroid_info)

# Keydown Handler
def keydown(key):
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrusting(True)
        
    elif key==simplegui.KEY_MAP["left"]:
        my_ship.rotate_left(rotation_sensitivity)
        
    elif key==simplegui.KEY_MAP["right"]:
        my_ship.rotate_right(rotation_sensitivity)
        
    elif key==simplegui.KEY_MAP["space"]:
        my_ship.shoot()	# Fire ze missile!

# Keyup Hnadler
def keyup(key):
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrusting(False)
        
    elif key==simplegui.KEY_MAP["left"]:
        my_ship.rotate_left(-rotation_sensitivity)
        
    elif key==simplegui.KEY_MAP["right"]:
        my_ship.rotate_right(-rotation_sensitivity)

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [random.randrange(240//60), random.randrange(180//60)], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [random.randrange(240//60), random.randrange(180//60)], 0, 0.1, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# start the soundtrack
soundtrack.play()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
