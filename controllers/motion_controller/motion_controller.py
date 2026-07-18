from controller import Robot
import math

TIME_STEP = 32

WHEEL_RADIUS = 0.0205
FORWARD_SPEED = 3.0
AXLE_LENGTH = 0.052  # distance between e-puck wheels in metres
TURN_SPEED = 2.0

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
    

def rotate(angle_degrees, speed=TURN_SPEED):
    direction = 1

    if angle_degrees < 0:
        direction = -1

    target_angle = abs(math.radians(angle_degrees))

    wheel_target_distance = (AXLE_LENGTH / 2.0) * target_angle

    start_left = left_encoder.getValue()
    start_right = right_encoder.getValue()

    while robot.step(TIME_STEP) != -1:
        current_left = left_encoder.getValue()
        current_right = right_encoder.getValue()

        left_rotation = abs(current_left - start_left)
        right_rotation = abs(current_right - start_right)

        left_distance = left_rotation * WHEEL_RADIUS
        right_distance = right_rotation * WHEEL_RADIUS

        average_wheel_distance = (left_distance + right_distance) / 2.0

        if average_wheel_distance < wheel_target_distance:
            left_motor.setVelocity(-speed * direction)
            right_motor.setVelocity(speed * direction)
        else:
            stop_motors()
            print(f"Rotated: {angle_degrees} degrees")
            return
            
            
robot.step(TIME_STEP)

rotate(90)
move_distance(0.30)

rotate(-90)
move_distance(0.30)

rotate(180)

print("Rotation test completed.")