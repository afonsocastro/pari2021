#!/usr/bin/env python
# license removed for brevity
import rospy
import argparse
from colorama import Fore
from std_msgs.msg import String
from dog_lib import Dog

def main():
    parser =argparse.ArgumentParser(description='test')
    parser.add_argument('-tn','--topic_name',type=str, default='chatter', help='Noth')
    parser.add_argument('-m','--message_content', type=str, default='nothing to say',help='content fo message to publish.')
    parser.add_argument('-f', '--frequency', type=float, default=10, help='content of message to publish.')
    args =vars(parser.parse_args())

    pub = rospy.Publisher(args['topic_name'], String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(args['frequency']) # 10hz

    dog= Dog(nome='bobby', age=17, color='Black')
    dog.addBrother('Lassie')
    while not rospy.is_shutdown():
        rospy.loginfo("Publishing message: "+Fore.RED + args['message_content']+' on topic ' + args['topic_name'])
        pub.publish(args['message_content'])
        rate.sleep()

if __name__ == '__main__':
    main()