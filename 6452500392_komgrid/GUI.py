#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
import os

frame = Tk()
frame.title("GUI")
frame.geometry("450x200")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

def fw():
	print("FW")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def bw():
	print("BW")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def sl():
	print("SL")
	cmd = Twist()
	cmd.linear.y = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def sr():
	print("SR")
	cmd = Twist()
	cmd.linear.y = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def rr():
	print("RR")
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= -1.0
	pub.publish(cmd)
	
def rl():
	print("RL")
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= 1.0
	pub.publish(cmd)
	
def rst():
	print("RST")
	os.system('rosservice call /reset')
	
B1 = Button(text = "Forward",bg='green',fg='white', command=fw)
B1.place(x=93, y=30)

B2 = Button(text = "Backward",bg='green',fg='white', command=bw)
B2.place(x=93, y=130)

B3 = Button(text = "Rotate_Left",bg='green',fg='white', command=rl)
B3.place(x=20, y=80)

B4 = Button(text = "Rotate_Right",bg='green',fg='white', command=rr)
B4.place(x=153, y=80)

B5 = Button(text = "Slide_Left",bg='skyblue', command=sl)
B5.place(x=338, y=80)

B6 = Button(text = "Slide_Right",bg='skyblue', command=sr)
B6.place(x=248, y=80)

B7 = Button(text = "RESET",bg='brown',fg='white', command=rst)
B7.place(x=100, y=80)

frame.mainloop()

