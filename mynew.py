import naoqi
from naoqi import ALProxy
import time
import math
textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)  # Include your IP and port here
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)  # Include your IP and port here

# Which parts of the robot arm should we move
shoulderJoint = "LShoulderPitch"
wristJoint = "LWristYaw"

useSen = 0
useSen_1 = 0

# Below we define "Hello" function and export here keyframes from Choregraphe
def Hello():
	# Choregraphe bezier export in Python.
	from naoqi import ALProxy
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.96, 1.36, 1.76, 2.16, 2.56, 2.96, 3.36, 4.36])
	keys.append([[-0.698132, [3, -0.333333, 0], [3, 0.133333, 0]], [-1.0472, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.349066, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.0472, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.349066, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.0472, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.349066, [3, -0.133333, 0], [3, 0.333333, 0]], [-0.418879, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.96, 1.36, 1.76, 2.16, 2.56, 2.96, 3.36, 4.36])
	keys.append([[-0.151844, [3, -0.333333, 0], [3, 0.133333, 0]], [-0.151844, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.151844, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.151844, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.151844, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.151844, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.151844, [3, -0.133333, 0], [3, 0.333333, 0]], [-1.20079, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.96, 1.36, 1.76, 2.16, 2.56, 2.96, 3.36, 4.36])
	keys.append([[0.75, [3, -0.333333, 0], [3, 0.133333, 0]], [0.75, [3, -0.133333, 0], [3, 0.133333, 0]], [0.75, [3, -0.133333, 0], [3, 0.133333, 0]], [0.75, [3, -0.133333, 0], [3, 0.133333, 0]], [0.75, [3, -0.133333, 0], [3, 0.133333, 0]], [0.75, [3, -0.133333, 0], [3, 0.133333, 0]], [0.75, [3, -0.133333, 0], [3, 0.333333, 0]], [0.3, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.96, 1.36, 1.76, 2.16, 2.96, 3.36, 4.36])
	keys.append([[-1.09956, [3, -0.333333, 0], [3, 0.133333, 0]], [-1.09956, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.09956, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.09956, [3, -0.133333, 0], [3, 0.266667, 0]], [-1.09956, [3, -0.266667, 0], [3, 0.133333, 0]], [-1.09956, [3, -0.133333, 0], [3, 0.333333, 0]], [1.44339, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.96, 1.36, 1.76, 2.16, 2.56, 2.96, 3.36, 4.36])
	keys.append([[0.738274, [3, -0.333333, 0], [3, 0.133333, 0]], [0.738274, [3, -0.133333, 0], [3, 0.133333, 0]], [0.738274, [3, -0.133333, 0], [3, 0.133333, 0]], [0.738274, [3, -0.133333, 0], [3, 0.133333, 0]], [0.738274, [3, -0.133333, 0], [3, 0.133333, 0]], [0.738274, [3, -0.133333, 0], [3, 0.133333, 0]], [0.738274, [3, -0.133333, 0], [3, 0.333333, 0]], [0.214676, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.96, 1.36, 1.76, 2.16, 2.56, 2.96, 3.36, 4.36])
	keys.append([[0.165806, [3, -0.333333, 0], [3, 0.133333, 0]], [0.165806, [3, -0.133333, 0], [3, 0.133333, 0]], [0.165806, [3, -0.133333, 0], [3, 0.133333, 0]], [0.165806, [3, -0.133333, 0], [3, 0.133333, 0]], [0.165806, [3, -0.133333, 0], [3, 0.133333, 0]], [0.165806, [3, -0.133333, 0], [3, 0.133333, 0]], [0.165806, [3, -0.133333, 0], [3, 0.333333, 0]], [0.10821, [3, -0.333333, 0], [3, 0, 0]]])

	try:
	  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
	  motion = ALProxy("ALMotion", "127.0.0.1", 9559)
	  # motion = ALProxy("ALMotion")
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err

# Here we call our "Hello" function to make appropriate movement. After that NAO should say "hi" to user.
Hello()
textSpeakProxy.say("Hi! I want to play with you!")

# Below we define new function "RiseLeftArm". It's needed in order to rise NAO's left arm after "hi" command.
def RiseLeftArm():
	# Choregraphe bezier export in Python.
	from naoqi import ALProxy
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.96])
	keys.append([[-0.79587, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.96])
	keys.append([[-0.226893, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.96])
	keys.append([[0.73, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.96])
	keys.append([[-1.09956, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.96])
	keys.append([[0.738274, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.96])
	keys.append([[-1.42593, [3, -0.333333, 0], [3, 0, 0]]])

	try:
	  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
	  motion = ALProxy("ALMotion", "127.0.0.1", 9559)
	  # motion = ALProxy("ALMotion")
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err

# Here we call our "RiseLeftArm" function
RiseLeftArm()

# Disables left arm motions during a move
leftArmEnable  = False
rightArmEnable = True
motionProxy.setMoveArmsEnabled(leftArmEnable, rightArmEnable)

while(1):
	speed = motionProxy.getAngles(shoulderJoint, useSen)  # Takes radians from shoulderJoint
	speed_angle = (2 * 90 * speed[0]) / math.pi  # Converts radians to angles

	rotation = motionProxy.getAngles(wristJoint, useSen_1)  # Takes radians from wristJoint
	rotation_angle = (2 * 90 * rotation[0]) / math.pi  # Converts radians to angles
	rotation_rate = (-rotation_angle - 90) / 90  # Computes rotation_rate of wristJoint

	if((speed_angle > -73) & (speed_angle < 6.5)):  # Here we set the condition that if the hand is raised or about 90 degrees, then the robot moves quickly
		print("We are going forward faster")
		motionProxy.move(2, 0.0, 0.0)
	elif((speed_angle > 6.5) & (speed_angle < 55)):  # Here we set the condition that if the hand is about 90 degree or almost dropped, then the robot moves slowly
		print("We are going forward slower")
		motionProxy.move(1, 0.0, 0.0)
	else:  # Otherwise it should stop if the arm is too bent or dropped
		print("I need to stop")
		motionProxy.move(0.0, 0.0, 0.0)

    # Angle of wristJoint after "RiseLeftArm" is called is -81.7. So here we should calculate rotations considering this fact. I give additional 10 degree to avoid some unwanted turn
	if(rotation_angle < -91.7):
			print("We are going to right")
			motionProxy.move(0.0, 0.0, -8 * (rotation_rate))

	elif(rotation_angle > 16.3):
			print("We are going to left")
			motionProxy.move(0.0, 0.0, -rotation_rate)

	time.sleep(0.100)
