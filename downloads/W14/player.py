# pip install pyzmq cbor keyboard
from zmqRemoteApi import RemoteAPIClient
import keyboard

client = RemoteAPIClient('localhost', 23000)

sim = client.getObject('sim')


def setBubbleRobVelocity(leftWheelVelocity, rightWheelVelocity):
    leftMotor = sim.getObject('/leftMotor')
    rightMotor = sim.getObject('/rightMotor')
    sim.setJointTargetVelocity(leftMotor, leftWheelVelocity)
    sim.setJointTargetVelocity(rightMotor, rightWheelVelocity)
def KickingSpeed(kickingVelocity):
    kicking_joint = sim.getObject('/kicking_joint')
    sim.setJointTargetVelocity(kicking_joint, kickingVelocity)

# use keyborad to move BubbleRob

while True:
    if keyboard.is_pressed('up'):
        setBubbleRobVelocity(5.0, 5.0)
    elif keyboard.is_pressed('down'):
        setBubbleRobVelocity(-3.0, -3.0)
    elif keyboard.is_pressed('left'):
        setBubbleRobVelocity(-2.0, 2.0)
    elif keyboard.is_pressed('right'):
        setBubbleRobVelocity(2.0, -2.0)    
    elif keyboard.is_pressed('0'):
        KickingSpeed(5.0)
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setBubbleRobVelocity(0.0, 0.0)
