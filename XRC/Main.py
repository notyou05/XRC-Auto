from simple_pid import PID
import Control
import Data
import time
# Create PID controller
pid = PID(1.0, 0.1, 0.05, setpoint=10)
pid.output_limits = (0, 100)
measurement = 0

Control.replace_after_string(r"C:\tmp\xRCsim\Controls.txt", "left_x=", "-0.5")

#while True:
    #output = pid(Data.read_value_from_json(r"C:\tmp\xRCsim\myRobot.txt", ['myrobot', 'Body', 'global rot']))
  #  time.sleep(0.5)





