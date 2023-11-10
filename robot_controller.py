"""robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, Motion

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()
wave = Motion('../../motions/wave.motion')
# get the time step of the current world.
timestep = 32

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    
    if key == Keyboard.UP:
        wave.play()
    pass

# Enter here exit cleanup code.
