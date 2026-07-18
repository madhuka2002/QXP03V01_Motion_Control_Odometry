from controller import Robot
import math

TIME_STEP = 32

WHEEL_RADIUS = 0.0205
AXLE_LENGTH = 0.052

FORWARD_SPEED = 3.0
TURN_SPEED = 2.0

robot_x = 0.0
robot_y = 0.0
robot_theta = 0.0

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


def print_pose():
    print("--------------------------------")
    print(f"X       : {robot_x:.3f} m")
    print(f"Y       : {robot_y:.3f} m")
    print(f"Heading : {math.degrees(robot_theta):.1f}°")
    print("--------------------------------")



def update_odometry():
    global robot_x
    global robot_y
    global robot_theta
    global previous_left_encoder
    global previous_right_encoder

    current_left = left_encoder.getValue()
    current_right = right_encoder.getValue()

    delta_left = (current_left - previous_left_encoder) * WHEEL_RADIUS
    delta_right = (current_right - previous_right_encoder) * WHEEL_RADIUS

    previous_left_encoder = current_left
    previous_right_encoder = current_right

    distance = (delta_left + delta_right) / 2.0

    delta_theta = (delta_right - delta_left) / AXLE_LENGTH

    robot_theta += delta_theta

    robot_x += distance * math.cos(robot_theta)
    robot_y += distance * math.sin(robot_theta)
    
    
def move_distance(target_distance, speed=FORWARD_SPEED):
    global robot_x, robot_y

    direction = 1

    if target_distance < 0:
        direction = -1
        target_distance = abs(target_distance)

    start_left = left_encoder.getValue()
    start_right = right_encoder.getValue()

    left_motor.setVelocity(speed * direction)
    right_motor.setVelocity(speed * direction)

    while robot.step(TIME_STEP) != -1:
        update_odometry()
        current_left = left_encoder.getValue()
        current_right = right_encoder.getValue()

        left_rotation = abs(current_left - start_left)
        right_rotation = abs(current_right - start_right)

        left_distance = left_rotation * WHEEL_RADIUS
        right_distance = right_rotation * WHEEL_RADIUS

        travelled_distance = (left_distance + right_distance) / 2.0

        if travelled_distance >= target_distance:
            stop_motors()

            signed_distance = direction * travelled_distance

            print(f"Moved: {signed_distance:.3f} m")
            return


def rotate(angle_degrees, speed=TURN_SPEED):
    global robot_theta

    direction = 1

    if angle_degrees < 0:
        direction = -1

    target_angle = abs(math.radians(angle_degrees))

    wheel_target_distance = (AXLE_LENGTH / 2.0) * target_angle

    start_left = left_encoder.getValue()
    start_right = right_encoder.getValue()

    left_motor.setVelocity(-speed * direction)
    right_motor.setVelocity(speed * direction)

    while robot.step(TIME_STEP) != -1:
        update_odometry()
        current_left = left_encoder.getValue()
        current_right = right_encoder.getValue()

        left_rotation = abs(current_left - start_left)
        right_rotation = abs(current_right - start_right)

        left_distance = left_rotation * WHEEL_RADIUS
        right_distance = right_rotation * WHEEL_RADIUS

        average_wheel_distance = (
            left_distance + right_distance
        ) / 2.0

        if average_wheel_distance >= wheel_target_distance:
            stop_motors()

            robot_theta = math.atan2(
                math.sin(robot_theta),
                math.cos(robot_theta)
            )

            print(f"Rotated: {angle_degrees}°")
            return


def drive_square(side_length=0.30):
    for side in range(4):
        print(f"Side {side + 1}")

        move_distance(side_length)
        print_pose()

        rotate(-90)
        print_pose()

    stop_motors()
    print("Square completed.")



robot.step(TIME_STEP)


previous_left_encoder = left_encoder.getValue()
previous_right_encoder = right_encoder.getValue()

move_distance(1.0)

rotate(90)

move_distance(1.0)

print_pose()

print("Motion and odometry test completed.")