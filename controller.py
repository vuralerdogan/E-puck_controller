"""mycontrollerauto controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import DifferentialWheels, LED, DistanceSensor, Camera, LightSensor

# create the Robot instance.
robot = DifferentialWheels()
print("Vural's Robot is running")
timestep = 40


def searchred(leftspeed, rightspeed):
    # searching for red


    print
    'searching red'
    # We specified the probability of situations. Belove statemens explain the black line and obstacle avoiding.
    if (right0 >= 100 and left7 >= 100 and gRight < 750 or (left7 >= 100 and gRight < 750)):
        rightspeed += 1000
        leftspeed -= 1000
    elif (right0 >= 100 and left7 >= 100 and gLeft < 750 or (left7 >= 100 and gLeft < 750)):
        rightspeed -= 1000
        leftspeed += 1000
    elif (right0 >= 100 and left7 >= 100):
        rightspeed += 1000
        leftspeed -= 1000
    # if an obstacle is on the right side, the right wheels' speed increases.
    elif (right0 >= 100 or right1 >= 100 or right2 >= 100):
        rightspeed += 1000
        leftspeed -= 1000

    # if an obstacle is on the right side, the left wheels' speed increases.
    elif (left7 >= 100 or left6 >= 100 or left5 >= 100):
        rightspeed -= 1000
        leftspeed += 1000
    # these ground sensors increase speed when they detect a black line.
    # we determined it as four states. Speed should be maximum of the e-puck.
    # we chose some speed limits 1500 instead of 1000 that contribute us avoiding from the line
    elif (gLeft < 600):
        rightspeed -= 1500
        leftspeed += 1500
    elif (gRight < 600):
        rightspeed += 1500
        leftspeed -= 1500
    elif (gLeft < 750 and gCentre < 600):
        rightspeed -= 1500
        leftspeed += 1500
    elif (gRight < 750 and gCentre < 600):

        rightspeed += 1500
        leftspeed -= 1500

    robot.setSpeed(leftspeed, rightspeed)


def searchyellow(leftspeed, rightspeed):
    print
    'searching yellow'
    # the searching methods are similar the only thing is that this time, it searches for yellow.
    if (right0 >= 100 and left7 >= 100 and gRight < 750 or (left7 >= 100 and gRight < 750)):
        rightspeed += 1000
        leftspeed -= 1000
    elif (right0 >= 100 and left7 >= 100 and gLeft < 750 or (left7 >= 100 and gLeft < 750)):
        rightspeed -= 1000
        leftspeed += 1000
    elif (right0 >= 100 and left7 >= 100):
        rightspeed += 1000
        leftspeed -= 1000
    # if an obstacle is on the right side, the right wheels' speed increases.
    elif (right0 >= 100 or right1 >= 100 or right2 >= 100):
        rightspeed += 1000
        leftspeed -= 1000

    # if an obstacle is on the right side, the left wheels' speed increases.
    elif (left7 >= 100 or left6 >= 100 or left5 >= 100):
        rightspeed -= 1000
        leftspeed += 1000
    # these ground sensors increase speed when they detect a black line.
    # we determined it as four states.
    elif (gLeft < 600):
        rightspeed -= 1500
        leftspeed += 1500
    elif (gRight < 600):
        rightspeed += 1500
        leftspeed -= 1500
    elif (gLeft < 750 and gCentre < 600):
        rightspeed -= 1500
        leftspeed += 1500
    elif (gRight < 750 and gCentre < 600):
        # we chose some speed limits 1500 instead of 1000 that contribute us avoiding from the line
        rightspeed += 1500
        leftspeed -= 1500

    robot.setSpeed(leftspeed, rightspeed)


# "found functions" lead to focus on target and the epuck only goes the target slowly untill
# untill it is being close the target.
def foundtrash(k, l):
    print("trash is detected")

    robot.setSpeed(k, l)
    # the belove condition contributes to achieve target.
    # k and l is not obligatory just making sure condition is proven.
    # When it come closes, it needs to detect its existence in order to run next step
    # Therefore, left7 and righ0 help e-puck to understand it is near the target.
    # And the target colours should be confirmed as well.

    if ((k >= 190 and l >= 190) and (left7 >= 140 or right0 >= 140) and (
                        red[20] >= 100 and green[20] >= 100 and blue[20] <= 10)):
        robot.setSpeed(0, 0)
        led[0].set(1)
        print("I am next to trash")


# this function same as above function. It focuses the bin.
def foundbin(k, l):
    print("bin is detected")
    robot.setSpeed(k, l)
    # same as "foundtrash" method.
    if ((k >= 190 and l >= 190) and (left7 >= 140 or right0 >= 140) and (
                        red[20] >= 100 and green[20] <= 10 and blue[20] <= 10)):
        led[0].set(0)
        print(" I am next to bin")


# enable camera.
camera = Camera("camera")
camera.enable(timestep * 2)
print("Camera width = ", camera.getWidth(), "Camera height =", camera.getHeight())

# enable LEDs
led = [0] * 8
count = 0
for i in range(8):
    name = "led" + str(i)
    led[i] = LED(name)

robot.enableEncoders(timestep)
# enable distance and ground sensors
irLeft7 = DistanceSensor("ps7")
irLeft6 = DistanceSensor("ps6")
irLeft5 = DistanceSensor("ps5")
irRight0 = DistanceSensor("ps0")
irRight1 = DistanceSensor("ps1")
irRight2 = DistanceSensor("ps2")
irLeft7.enable(timestep)
irLeft6.enable(timestep)
irLeft5.enable(timestep)
irRight0.enable(timestep)
irRight1.enable(timestep)
irRight2.enable(timestep)
gsLeft = DistanceSensor("gs0")
gsCentre = DistanceSensor("gs1")
gsRight = DistanceSensor("gs2")
gsLeft.enable(timestep)
gsCentre.enable(timestep)
gsRight.enable(timestep)

# Create an array that includes camera pixel's value
red = [0] * 40
blue = [0] * 40
green = [0] * 40

while robot.step(timestep) != -1:

    # get and set value for parameters.
    left7 = irLeft7.getValue()
    left6 = irLeft6.getValue()
    left5 = irLeft5.getValue()

    right0 = irRight0.getValue()
    right1 = irRight1.getValue()
    right2 = irRight2.getValue()

    gRight = gsRight.getValue()
    gLeft = gsLeft.getValue()
    gCentre = gsCentre.getValue()

    # display the components of each pixel
    image = camera.getImageArray()

    # get the colour component of the pixel x (0,40) y(5,6)
    for x in range(0, camera.getWidth()):
        for y in range(5, 6):
            # we fill our arrays with the colour values.
            red[x] = image[x][y][0]
            green[x] = image[x][y][1]
            blue[x] = image[x][y][2]

            # that illustrates arrays in the text field.
    print
    'r=' + str(red)
    print
    'g=' + str(green)
    print
    'b=' + str(blue)

    print("Left Encoder=", robot.getLeftEncoder(),
          "Right Encoder=", robot.getRightEncoder())
    print("IR Distances: Left=", irLeft7.getValue(),
          " Right =", irRight0.getValue())
    print("Line sensors: Left=", gsLeft.getValue(), "Centre = ",
          gsCentre.getValue(), "Right=", gsRight.getValue())
    # we create 2 parameters for encoders that contribute us to random search in different periods.
    tick1 = robot.getLeftEncoder()
    tick2 = robot.getRightEncoder()
    # get value from first LED
    ledx = led[0].get()
    print("led", ledx)
    # this is a random search method. It first scans the environment then searches. Also,
    # It scans every each 20000 encounter values.
    if (tick1 <= 700 and tick2 >= -700) or abs(tick1) % 20000 >= 19000:
        robot.setSpeed(100.5, -100.5)

        # The states according to LED situation.
        if (ledx == 0):

            # We only look for middle of screen's value "20"; therefore, we compared it [20]
            if (100 <= green[20] and red[20] >= 100 and blue[20] <= 10):
                robot.setSpeed(0, 0)
                robot.setEncoders(0, 0)
                # it resets encoders to scan again after detecting.
                k = 200
                l = 200
                foundtrash(k, l)

        if (ledx == 1):
            if (green[20] <= 10 and red[20] >= 100 and blue[20] <= 10):
                robot.setSpeed(0, 0)
                robot.setEncoders(0, 0)
                # it resets encoders to scan again after detecting.
                k = 200
                l = 200
                foundbin(k, l)
                # if scannning cannot find anything, the epuck starts to search by checking the LED
                # If the first Led is deactive, search for trash.
                # If the first led is active, search for bin.
    else:
        if (ledx == 0):

            rightspeed = 400
            leftspeed = 400
            searchyellow(leftspeed, rightspeed)
            # if led[0] is deactive, colours in the pixel of width 20 are compared with belove conditions.
            # For height value we only chose one value such as 20x5.
            # If it detects, it lockes to the yellow ball.
            # That means the desired item has been found and run the "found function"

            if (green[20] >= 120 and red[20] >= 120 and blue[20] <= 30):
                # k and l determines initial speed of locking to target.
                k = 200
                l = 200
                foundtrash(k, l)

        if (ledx == 1):

            rightspeed = 400
            leftspeed = 400
            searchred(leftspeed, rightspeed)

            if (green[20] <= 10 and red[20] >= 120 and blue[20] <= 10):
                # if Led[0] is active and red is detected, it uses same way above but calls "foundbin" instead of "found yellow"
                # and it lockes to the red ball (trash-can).
                k = 200
                l = 200
                foundbin(k, l)
