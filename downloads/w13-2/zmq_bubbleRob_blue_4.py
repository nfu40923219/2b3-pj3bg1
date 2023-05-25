# pip install pyzmq cbor keyboard
from zmqRemoteApi import RemoteAPIClient
import keyboard

client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')

# start
sim.startSimulation()
print('Simulation started')

def setBubbleRobVelocity(leftWheelVelocity, rightWheelVelocity):
    leftMotor = sim.getObject('/leftMotor4')
    rightMotor = sim.getObject('/rightMotor4')
    sim.setJointTargetVelocity(leftMotor, leftWheelVelocity)
    sim.setJointTargetVelocity(rightMotor, rightWheelVelocity)

'''
# Example usage 1:
setBubbleRobVelocity(1.0, 1.0)
time.sleep(2)
setBubbleRobVelocity(0.0, 0.0)
'''
# use keyborad to move BubbleRob

while True:
    if keyboard.is_pressed('i'):
        setBubbleRobVelocity(5.0, 5.0)
    elif keyboard.is_pressed('k'):
        setBubbleRobVelocity(-3.0, -3.0)
    elif keyboard.is_pressed('j'):
        setBubbleRobVelocity(-2.0, 2.0)
    elif keyboard.is_pressed('l'):
        setBubbleRobVelocity(2.0, -2.0)
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setBubbleRobVelocity(0.0, 0.0)




