from controller import Robot

TIME_STEP = 32

WHEEL_RADIUS = 0.0205
FORWARD_SPEED = 3.0

robot = Robot()

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

left_encoder = left_motor.getPositionSensor()
right_encoder = right_motor.getPositionSensor()

left_encoder.enable(TIME_STEP)
right_encoder.enable(TIME_STEP)


def stop_motors():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)


def move_distance(target_distance, speed=FORWARD_SPEED):

    direction = 1

    if target_distance < 0:
        direction = -1
        target_distance = abs(target_distance)

    start_left = left_encoder.getValue()
    start_right = right_encoder.getValue()

    while robot.step(TIME_STEP) != -1:

        current_left = left_encoder.getValue()
        current_right = right_encoder.getValue()

        left_rotation = abs(current_left - start_left)
        right_rotation = abs(current_right - start_right)

        left_distance = left_rotation * WHEEL_RADIUS
        right_distance = right_rotation * WHEEL_RADIUS

        travelled_distance = (left_distance + right_distance) / 2

        if travelled_distance < target_distance:
            left_motor.setVelocity(speed * direction)
            right_motor.setVelocity(speed * direction)
        else:
            stop_motors()
            print(f"Moved {travelled_distance:.3f} m")
            return
    

robot.step(TIME_STEP)

move_distance(-0.50)

print("Movement completed.")