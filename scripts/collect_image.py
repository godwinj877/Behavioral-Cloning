import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()
img_count = 0

def image_callback(msg):
    global img_count, throttle_list, steering_list
    img = bridge.imgmsg_to_cv2(msg)

    cv2.imwrite("/home/godwin/turtlebot3_ws/src/behavioral_cloning/images/img_{}.jpg".format(img_count), img)
    img_count += 1

if __name__ == "__main__":
    rclpy.init()

    node = rclpy.create_node("image_capture_node")

    node.create_subscription(Image, "/camera/image_raw", image_callback, 20)

    try:
        while rclpy.ok():
            rclpy.spin(node)
    except KeyboardInterrupt:
        pass
     
    node.destroy_node()
    rclpy.shutdown()
