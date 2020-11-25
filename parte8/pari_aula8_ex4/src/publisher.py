#!/usr/bin/env python
# license removed for brevity
import rospy
import argparse
from colorama import Fore
from std_msgs.msg import String
from dog_lib import Dog
from pari_aula8_ex4.msg import dog

def main():
    parser =argparse.ArgumentParser(description='test')
    parser.add_argument('-tn','--topic_name',type=str, default='chatter', help='Noth')
    parser.add_argument('-m','--message_content', type=str, default='nothing to say',help='content fo message to publish.')
    parser.add_argument('-f', '--frequency', type=float, default=10, help='content of message to publish.')
    args =vars(parser.parse_args())

    pub = rospy.Publisher(args['topic_name'], dog, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(args['frequency']) # 10hz

    # dog= Dog(nome='bobby', age=17, color='Black')
    # dog.addBrother('Lassie')

    dog_message = dog()
    dog_message.name='Bobby'
    dog_message.age= '?'
    dog_message.color = 'Black'
    dog_message.brother.append('Lassie')

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing message: "+Fore.RED + str(dog_message)+ Fore.RESET+ ' on topic ' + args['topic_name'])
        pub.publish(dog_message)
        rate.sleep()

if __name__ == '__main__':
    main()