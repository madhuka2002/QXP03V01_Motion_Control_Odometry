from controller import Robot

TIME_STEP = 32
FOEWARD_SPEED = 3.0
MOVE_DURATION = 3.0

robot = Robot()

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(flot("inf"))
right_motor.setPosition(flot("inf"))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

start_time = robot.getTime()

while robot.step(TIME_STEP) != -1:
    
    elapsed_time = robot.getTime() - start_time

    if elapsed_time < MOVE_DURATION:
        left_motor.setVelocity(FORWARD_SPEED)
        right_motor.setVelocity(FORWARD_SPEED)
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        print("Forward movement completed.")
        break
