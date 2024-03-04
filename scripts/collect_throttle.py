import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import csv

throttle_list = []
steering_list = []

class TwistToCSV(Node):
    def __init__(self):
        super().__init__('twist_to_csv')
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.twist_callback, 20)

        with open('/home/godwin/turtlebot3_ws/src/behavioral_cloning/throttle_steering_data.csv', mode='w') as csv_file:
            fieldnames = ['linear_x', 'angular_z']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    def twist_callback(self, data):
        with open('/home/godwin/turtlebot3_ws/src/behavioral_cloning/throttle_steering_data.csv', mode = 'a') as csv_file:
            fieldnames = ['linear_x', 'angular_z']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'linear_x' : data.linear.x, 
                             'angular_z' : data.angular.z})


if __name__ == "__main__":
    rclpy.init()
    twist_to_csv = TwistToCSV()
    try:
        while rclpy.ok():
            rclpy.spin(twist_to_csv)
    except KeyboardInterrupt:
        pass
    twist_to_csv.destroy_node()
    rclpy.shutdown()
